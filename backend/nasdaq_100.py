import pandas as pd
from sources import DB_PATH, NASDAQ


class Nasdaq100:

    @staticmethod
    def load_nasdaq_100_data():
        return pd.read_csv(DB_PATH + NASDAQ, index_col=0)


if __name__ == '__main__':
    n = Nasdaq100()
    df = n.load_nasdaq_100_data()
    print('debug breakpoint')
