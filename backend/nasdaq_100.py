import pandas as pd
from sources import DB_PATH, NASDAQ


class Nasdaq100:

    @staticmethod
    def load_nasdaq_100_data():
        return pd.read_csv(DB_PATH + NASDAQ, index_col=0)

    def get_nasdaq_100_sectors_df(self):
        nasdaq_100_df = self.load_nasdaq_100_data()
        sector_list = self.get_sector_list(nasdaq_100_df)
        nasdaq_100_obj = self.get_nasdaq_sectors_obj(nasdaq_100_df)
        sector_df_list = []
        for sector in sector_list:
            sector_df = self.get_df_for_sector(nasdaq_100_obj, sector)
            sector_df_list.append(sector_df)
        return sector_df_list

    @staticmethod
    def get_df_for_sector(obj, sector_name):
        return obj.get_group(sector_name)

    @staticmethod
    def get_nasdaq_sectors_obj(df):
        df_obj = df.groupby('SECTOR')
        return df_obj

    @staticmethod
    def get_sector_list(df):
        return df['SECTOR'].unique()


if __name__ == '__main__':
    n = Nasdaq100()
    sectors_df_list = n.get_nasdaq_100_sectors_df()
    print('debug breakpoint')
