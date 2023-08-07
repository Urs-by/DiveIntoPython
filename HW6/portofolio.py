__all__ = ['calculate_portfolio_value', 'calculate_portfolio_return', 'get_most_profitable_stock']

_first_prices = {}

def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    """
    Функция расчитывает общую стоимость портфеля акций
    :param stocks: словарь с количеством акций
    :param prices: словарь с ценой за акцию
    :return: общая стоимость портфеля акций
    """

    global _first_prices
    print(f'Первоначальная стоимость акций: {_first_prices}')
    if _first_prices == {}:
        _first_prices = prices

    # res = 0
    # for key, value in stocks.items():
    #     res = res + (value * prices[key])
    # return res

    # или следующий вариант в одну строку при условии, что в словарях одинаковая последовательность ключей
    return sum(stock * price for stock, price in zip(stocks.values(), prices.values()))


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    """
    функция возвращает процентную доходность конкретного портфеля
    :param initial_value: начальная стоимость портфеля акций
    :param current_value: текущая стоимость портфеля акций
    :return: процентная доходность портфеля
    """
    return (current_value - initial_value) / 100


def get_most_profitable_stock(stocks: dict, current_prices: dict) -> str:
    """
    Функция возвращает символ акции, которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью.
    :param initial_prices: начальная стоимость акций
    :param current_prices: текущая стоимость акций
    :param stocks: словарь с ценой за акцию
    :return: символ акции, которая имеет наибольшую прибыль
    """
    res = {stock: calculate_portfolio_return(initial_price, current_price)
           for stock, initial_price, current_price in
           zip(stocks.keys(), _first_prices.values(), current_prices.values())}

    return max(res, key=res.get)


# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
#
# prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
# current_prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 310.50}
#
# if __name__ == "__main__":
#     start = calculate_portfolio_value(stocks, prices)
#     print(start)
#
#     print(get_most_profitable_stock(stocks, current_prices))
