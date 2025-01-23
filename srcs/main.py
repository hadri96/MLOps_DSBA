from data.DSBA_dataloader import data_loader, preprocess_data

if __name__ == "__main__":
	data = data_loader("diabetes.tab.txt", delimiter="\t", extension="txt")
	X,y = preprocess_data(data)
	print(X.head())
	print(y.head())
