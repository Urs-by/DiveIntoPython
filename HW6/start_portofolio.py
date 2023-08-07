from portofolio import get_most_profitable_stock, calculate_portfolio_value, _first_prices

stocks = {"APL": 10, "GOOGL": 5, "MSFT": 8}

prices = {"APL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
current_prices = {"APL": 130.25, "GOOGL": 1600.75, "MSFT": 200.50}

print(f'Общая стоимость портфеля: {calculate_portfolio_value(stocks, prices)} ')

#print(_first_prices)

print(f'Наибольшая прибыль в компании: {get_most_profitable_stock(stocks, current_prices)}')

