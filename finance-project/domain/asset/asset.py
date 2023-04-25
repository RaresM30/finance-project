import yfinance


class Asset:
    def __init__(self, ticker: str, nr: float, name: str, country: str, sector: str):
        self.__ticker = ticker
        self.__nr = nr
        self.__name = name
        self.__country = country
        self.__sector = sector
        yfin = yfinance.Ticker(ticker)
        self.__info = yfin.fast_info
        # print(self.__yfin.fast_info)

    @property
    def ticker(self) -> str:
        return self.__ticker

    @property
    def units(self) -> float:
        return self.__nr

    @property
    def name(self) -> str:
        return self.__name

    @property
    def country(self) -> str:
        return self.__country

    @property
    def current_price(self) -> float:
        price = self.__info["lastPrice"]
        return round(price, 2)

    @property
    def currency(self) -> str:
        return self.__info["currency"]

    @property
    def closed_price(self) -> float:
        return self.__info["previousClose"]

    @property
    def fifty_day_price(self) -> float:
        return self.__info["fiftyDayAverage"]

    @property
    def today_low_price(self) -> float:
        return self.__info["dayLow"]

    @property
    def today_high_price(self) -> float:
        return self.__info["dayHigh"]

    @property
    def open_price(self) -> float:
        return self.__info["open"]

    @property
    def percentage_diff(self) -> str:
        diff = self.closed_price - self.current_price
        percent_diff = (diff / self.closed_price) * 100
        if diff > 0:
            return (
                f"The closed price {self.closed_price} is {percent_diff:.2}%"
                f" higher than the current price {self.current_price}"
            )
        elif diff < 0:
            return (
                f"The closed {self.closed_price} is {abs(percent_diff):.2f}%"
                f" lower than current {self.current_price}"
            )
        return "The values are the same"
