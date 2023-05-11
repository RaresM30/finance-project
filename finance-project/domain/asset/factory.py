from domain.asset.asset import Asset
import yahooquery


class AssetFactory:
    def make_new(self, ticker: str) -> Asset:
        t = yahooquery.Ticker(ticker)
        profile = t.summary_profile[ticker]
        name = self.__extract_name(profile)
        country = profile["country"]
        sector = profile["sector"]
        return Asset(
            ticker=ticker,
            nr=0,
            name=name,
            country=country,
            sector=sector,
        )



    @classmethod
    def __extract_name(cls, profile: dict) -> str:
        summary = profile["longBusinessSummary"]
        words = summary.split(" ")
        first_2_words = words[0:2]
        name = " ".join(first_2_words)
        return name

    @classmethod
    def make_from_persistence(cls, info: tuple) -> Asset:
        return Asset(
            ticker=info[0],
            nr=info[1],
            name=info[2],
            country=info[3],
            sector=info[4],
        )
