import pandas as pd
import os
import sys


def pre_process(path_stocks, cols, path_final_data):
    '''
    This Function takes in the location of the all the data files for the stocks and
    creates new dataframes for each type of column merging all the stocks in one df
    and saves them in csv files

    for example a df named df_open will contain the time series data of open prices for each stock
    each stock will be a column

    Parameters:
            path: path of the stock price data
            cols: columns in exiting dataframes
    Output
    respective csv files for each column in the initial dataset(.txt files)
    '''
    # declaring empty dataframes
    df_Open = pd.DataFrame(list())
    df_High = pd.DataFrame(list())
    df_Low = pd.DataFrame(list())
    df_Close = pd.DataFrame(list())
    df_Volume = pd.DataFrame(list())
    df_OpenInt = pd.DataFrame(list())

    for stock in os.listdir(path_stocks):
        # check if files are empty
        filesize = os.path.getsize(path_stocks+'/'+stock)
        if filesize == 0:
            continue
        if stock.split('.')[2] != 'txt':
            continue
        path = path_stocks+'/'+stock
        for col in cols:

            if col == 'Date':
                continue
            df_temp = pd.read_csv(
                path, usecols=['Date', col], index_col='Date')
            new_col = stock.split('.')[0]+col
            if col == 'Open':
                df_Open[new_col] = df_temp[col]

            elif col == 'High':
                df_High[new_col] = df_temp[col]

            elif col == 'Low':
                df_Low[new_col] = df_temp[col]

            elif col == 'Close':
                df_Close[new_col] = df_temp[col]

            elif col == 'Volume':
                df_Volume[new_col] = df_temp[col]

            elif col == 'OpenInt':
                df_OpenInt[new_col] = df_temp[col]

    #         sys.exit(0)
            del(df_temp)

	# print("procesing")

# change index to datetime object for dataframes
    df_Open.index = pd.to_datetime(df_Open.index)
    df_High.index = pd.to_datetime(df_High.index)
    df_Low.index = pd.to_datetime(df_Low.index)
    df_Close.index = pd.to_datetime(df_Close.index)
    df_Volume.index = pd.to_datetime(df_Volume.index)
    df_OpenInt.index = pd.to_datetime(df_OpenInt.index)

    if not os.path.isdir(path_final_data):
    	os.makedirs(path_final_data)

    # save dataframes to .csv files
    df_Open.to_csv(os.path.join(path_final_data,'df_Open.csv'))
    df_High.to_csv(os.path.join(path_final_data,'df_High.csv'))
    df_Low.to_csv(os.path.join(path_final_data,'df_Low.csv'))
    df_Close.to_csv(os.path.join(path_final_data,'df_Close.csv'))
    df_Volume.to_csv(os.path.join(path_final_data,'df_Volume.csv'))
    df_OpenInt.to_csv(os.path.join(path_final_data,'df_OpenInt.csv'))


if __name__ == '__main__':
    path_stocks = '/home/rishabh/Documents/Data_Science_Projects/DS_Medium_post/stocks/Stocks'
    df = pd.read_csv(
        '/home/rishabh/Documents/Data_Science_Projects/DS_Medium_post/stocks/Stocks/cpl.us.txt')
    cols = df.columns
    path_final_data = '/home/rishabh/Documents/Data_Science_Projects/StockMarketPredictor/data/'
    pre_process(path_stocks, cols, path_final_data)
