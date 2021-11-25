import pandas as pd
from sources import *


class DataScraper:

    @staticmethod
    def prepare_trading_view_data(scraped_trading_view_df):
        return scraped_trading_view_df.set_axis(['TICKER', 'PRICE', 'CHG', 'PRICE_CHANGE', 'RATING', 'VOLUME',
                                                'VOLUME*PRICE', 'MARKET CAP', 'P/E', 'EPS', 'NUMBER OF EMPLOYEES',
                                                 'SECTOR'], axis=1, inplace=True)

    @staticmethod
    def get_raw_nasdaq_data():
        return pd.read_html(NASDAQ)[0]


if __name__ == '__main__':
    d = DataScraper()
    df = d.prepare_trading_view_data(d.get_raw_nasdaq_data())
    print('debug breakpoint')
