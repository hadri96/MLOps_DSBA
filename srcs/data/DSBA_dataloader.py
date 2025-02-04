import pandas as pd
import numpy as np
import os
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def load_data(file_path, extension="csv", data_dir="data", delimiter=","):
    """
    Load data from a file with the specified extension and path.
    
    Args:
        extension (str): File extension, can be "csv", "xlsx", "txt". Defaults to "csv".
        file_path (str): The name of the data file. 
        data_dir (str): Path to the data file. Defaults to "data".
        delimiter (str): Delimiter to split the data.
    
    Returns:
        pandas.DataFrame: The loaded data.
    
    Raises:
        ValueError: If the file extension is not supported or the file does not exist.
    """
    current_dir = os.getcwd()
    path = os.path.join(current_dir, data_dir, file_path)
    if not os.path.exists(path):
        raise ValueError(f"Path {path} does not exist")
    elif not os.path.isfile(path):
        raise ValueError(f"Path {path} is not a file")
    if extension == "csv" or extension == "txt":
        data = pd.read_csv(path, delimiter=delimiter)
    elif extension == "xlsx":
        data = pd.read_excel(path)
    else:
        raise ValueError(f"Unsupported file extension: {extension}")
    
    return data

def preprocess_data(data, target_column="Y"):
    """
    Preprocess data from a DataFrame, presumably containing only two kinds of data types, numerical and categorical.

    Args:
        data (DataFrame): DataFrame to be preprocessed.
        target_column (str): The name of the target column.

    Return:
        clean_X (DataFrame): DataFrame of features after preprocessed. 
        y : label.

    """
	# extract the numerical feature and string features
    numeric_features = data.dtypes.index[data.dtypes=="int64"].tolist()
    numeric_features = [f for f in numeric_features if f != target_column]
    numeric_transformer = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )
    
    categorical_features = data.dtypes.index[data.dtypes=="float64"].tolist()
    categorical_transformer = Pipeline(
        steps=[
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ]
    )
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )
    print(data)
    y = data[target_column].values
    X = data.drop(columns=[target_column])
    clean_X= preprocessor.fit_transform(X)

    return clean_X, y

def data_loader(file_path:str, extension:str="csv",  data_dir:str="data", delimiter=","):
	"""
	Load and preprocess data from a file with the specified extension and path.

	Args:
		file_path: Name of the file to load.
		extension: File extension, either "csv" or "xlsx". Defaults to "csv".
		delimiter (str): Delimiter to split the data.
		data_dir: Directory containing the data file. Defaults to "data".

	Returns:
		X : The preprocessed and cleaned data.
		y (ndarray) : 1-d numpy array.
	"""
	data = load_data(file_path, extension, data_dir,delimiter)
	X, y = preprocess_data(data)
	return X, y 

if __name__ == "__main__":
	pass
