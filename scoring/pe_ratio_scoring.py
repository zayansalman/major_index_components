import pandas as pd
from backend.nasdaq_100 import Nasdaq100Sectors, Nasdaq100


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


class Nasdaq100PERatioScoring:

    @staticmethod
    def add_pe_ratio_scores_to_sectors_dict():
        nasdaq100 = Nasdaq100()
        pe = 'P/E'
        sector_list = nasdaq100.sector_list
        for sector in sector_list:
            p = PERatioScoring(Nasdaq100Sectors(sector).get_numeric_col(pe))
            pe_score_rating = p.get_score_rating()
            sector_df = nasdaq100.sectors_df_dict[sector]
            sector_df['P/E Rating'] = pe_score_rating
        return nasdaq100.sectors_df_dict


if __name__ == '__main__':
    npe = Nasdaq100PERatioScoring()
    sector_dict = npe.add_pe_ratio_scores_to_sectors_dict()
    print('debug breakpoint')
