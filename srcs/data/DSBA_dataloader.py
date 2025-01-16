import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

def load_data(file_path, extension="csv", data_dir="data"):
	"""
	Load data from a file with the specified extension and path.

	Args:
		extension (str): File extension, either "csv" or "xlsx". Defaults to "csv".
		path (str): Path to the data file. Defaults to "data".

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
	if extension == "csv":
		data = pd.read_csv(path)
	elif extension == "xlsx":
		data = pd.read_excel(path)
	else:
		raise ValueError(f"Unsupported file extension: {extension}")

	return data

def preprocess_data(data):
	pass

def data_loader(file_path:str, extension:str="csv", data_dir:str="data"):
	"""
	Load and preprocess data from a file with the specified extension and path.

	Args:
		file_path: Name of the file to load.
		extension: File extension, either "csv" or "xlsx". Defaults to "csv".
		data_dir: Directory containing the data file. Defaults to "data".

	Returns:
		pandas.DataFrame: The preprocessed and cleaned data.
	"""
	data = load_data(file_path, extension, data_dir)
	#clean_data = preprocess_data(data)
	return data


if __name__ == "__main__":
	pass
