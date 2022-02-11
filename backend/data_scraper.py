import pandas as pd
from sources import DB_PATH, NASDAQ_URL, NASDAQ


class DataScraper:

    @staticmethod
    def get_index_component_data_from_trading_view_as_df(link, index_name):
        index_df = pd.read_html(link)[0]
        index_df.set_axis(['TICKER', 'PRICE', 'CHG', 'PRICE_CHANGE', 'RATING', 'VOLUME',
                           'VOLUME*PRICE', 'MARKET CAP', 'P/E', 'EPS', 'NUMBER OF EMPLOYEES',
                           'SECTOR'], axis=1, inplace=True)
        index_df['PRICE'] = index_df['PRICE'].str.rstrip('USD')
        pd.to_numeric(index_df['PRICE'])
        index_df.to_csv(DB_PATH + index_name)
        return index_df


if __name__ == '__main__':
    d = DataScraper()
    df = d.get_index_component_data_from_trading_view_as_df(NASDAQ_URL, NASDAQ)
    print('debug breakpoint')
