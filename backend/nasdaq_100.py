import pandas as pd
from sources import DB_PATH, NASDAQ


class Nasdaq100:
    def __init__(self):
        self.sector_list = self.get_sector_list()
        self.sectors_df_dict = self.get_nasdaq_100_sectors_dict()

    def get_nasdaq_100_sectors_dict(self):
        nasdaq_100_df = self.load_nasdaq_100_data()
        sector_list = self.get_sector_list()
        nasdaq_100_obj = self.get_nasdaq_sectors_obj(nasdaq_100_df)
        sectors_df_dict = {sector: self.get_df_for_sector(nasdaq_100_obj, sector) for sector in sector_list}
        return sectors_df_dict

    @staticmethod
    def load_nasdaq_100_data():
        # return pd.read_csv('nasdaq_100.csv', index_col=0) #for Heroku deployment version
        return pd.read_csv(DB_PATH + NASDAQ)

    @staticmethod
    def get_df_for_sector(obj, sector_name):
        return obj.get_group(sector_name)

    @staticmethod
    def get_nasdaq_sectors_obj(df):
        df_obj = df.groupby('SECTOR')
        return df_obj

    def get_sector_list(self):
        return self.load_nasdaq_100_data()['SECTOR'].unique()


class Nasdaq100Sectors:
    def __init__(self, sector_name):
        self.sector_name = sector_name

    def get_nasdaq100_sector_df(self):
        nasdaq100 = Nasdaq100()
        return nasdaq100.sectors_df_dict[self.sector_name]

    def get_numeric_col(self, col_name):
        sector_df = self.get_nasdaq100_sector_df()
        sector_col = sector_df[col_name]
        sector_col_series = pd.to_numeric(sector_col, errors='coerce')
        return sector_col_series

    def get_str_col(self, col_name):
        sector_df = self.get_nasdaq100_sector_df()
        sector_str_col = sector_df[col_name]
        return sector_str_col


if __name__ == '__main__':
    n = Nasdaq100()
    sector_list = n.get_sector_list()
    print(sector_list)
    print('debug breakpoint')
