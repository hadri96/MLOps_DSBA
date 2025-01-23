from data.DSBA_dataloader import data_loader

if __name__ == "__main__":
	data = data_loader("train.csv")
	print(data.head())
