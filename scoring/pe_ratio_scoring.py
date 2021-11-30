import pandas as pd
from backend.nasdaq_100 import Nasdaq100Sectors


class PERatioScoring:
    def __init__(self, series):
        self.series = series

    def get_series_mean(self):
        return self.series.mean()

    def get_series_standard_score(self):
        return (self.series - self.series.mean())/self.series.std()

    def get_score_rating(self):
        init_ratings = 5 - (self.get_series_standard_score() * 5)
        init_ratings[init_ratings > 10] = 10
        init_ratings[init_ratings < 0] = 0
        score_ratings = init_ratings.round()
        return score_ratings


if __name__ == '__main__':
    p = PERatioScoring(Nasdaq100Sectors('Electronic Technology').get_numeric_col('P/E'))
    pe_mean = p.get_series_mean()
    pe_standard_score = p.get_series_standard_score()
    pe_score_rating = p.get_score_rating()
    print('debug breakpoint')
