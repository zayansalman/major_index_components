import pandas as pd
from sources import DB_PATH, NASDAQ


class Nasdaq100:

    @staticmethod
    def load_nasdaq_100_data():
        return pd.read_csv(DB_PATH + NASDAQ, index_col=0)


if __name__ == '__main__':
    n = Nasdaq100()
    nasdaq_100_df = n.load_nasdaq_100_data()
    sectors = nasdaq_100_df['SECTOR'].unique()
    nasdaq_100_sectors_obj = nasdaq_100_df.groupby('SECTOR')
    test = nasdaq_100_sectors_obj.get_group('Electronic Technology')
    print('debug breakpoint')
