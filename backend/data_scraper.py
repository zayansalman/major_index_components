import pandas as pd
from sources import *


class DataScraper:

    def prepare_nasdaq_data(self):
        raw_nasdaq_data_df = self.get_raw_nasdaq_data()
        raw_nasdaq_data_df.set_axis(['TICKER', 'PRICE', 'CHG', 'PRICE_CHANGE', 'RATING', 'VOLUME', 'VOLUME*PRICE',
                                     'MARKET CAP', 'P/E', 'EPS', 'NUMBER OF EMPLOYEES', 'SECTOR'], axis=1,
                                    inplace=True)
        return raw_nasdaq_data_df

    @staticmethod
    def get_raw_nasdaq_data():
        return pd.read_html(NASDAQ)[0]


if __name__ == '__main__':
    d = DataScraper()
    df = d.prepare_nasdaq_data()
    print('debug breakpoint')
