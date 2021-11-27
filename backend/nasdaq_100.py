import pandas as pd


class Nasdaq100:
    def __init__(self):
        nasdaq100_df = self.load_nasdaq_100_data()
        self.sector_list = self.get_sector_list(nasdaq100_df)
        self.sectors_df_dict = self.get_nasdaq_100_sectors_dict()

    def get_nasdaq_100_sectors_dict(self):
        nasdaq_100_df = self.load_nasdaq_100_data()
        sector_list = self.get_sector_list(nasdaq_100_df)
        nasdaq_100_obj = self.get_nasdaq_sectors_obj(nasdaq_100_df)
        sectors_df_dict = {sector: self.get_df_for_sector(nasdaq_100_obj, sector) for sector in sector_list}
        return sectors_df_dict

    @staticmethod
    def load_nasdaq_100_data():
        return pd.read_csv('nasdaq_100.csv', index_col=0)

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

# if __name__ == '__main__':
#     n = Nasdaq100()
#     sectors_dict = n.get_nasdaq_100_sectors_dict()
#     print('debug breakpoint')
