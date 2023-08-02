

def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    """
    Функция расчитывает общую стоимость портфеля акций
    :param stocks: словарь с количеством акций
    :param prices: словарь с ценой за акцию
    :return: общая стоимость портфеля акций
    """
    return sum(stocks*prices for stocks, prices in zip(stocks.values(), prices.values()))

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}

print(calculate_portfolio_value(stocks, prices))
