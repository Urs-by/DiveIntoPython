# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

BILL = 50
CASHBACK = 0.03
STEP_FOR_CASHBACK = 3
PERCENT = 0.015
MIN_SUM = 30
MAX_SUM = 600
WEALTH_TAX = 0.1
GOLD_SUM = 5000000


def enter_sum() -> int:
    """
    функция запрашивает сумму наличных и проверяет ее на кратность 50
    :return: bill - сумму введенных наличных
    """
    money = int(input("Введите сумму наличных средств: "))
    if money > 0 and money % 50 == 0:
        return money
    else:
        print(f"Сумма наличных средств должна быть кратна {BILL}")
        return enter_sum()


def add_cashback(cash: float) -> float:
    """
    функция добавляет проценты за количество транзакций
    :param cash: сумма на счете
    :return: cash обновленная сумма на счете
    """
    print(f"Вам начислены проценты {round(cash * CASHBACK, 2)}")
    cash = cash + cash * CASHBACK
    history_cash.append(cash)
    print(f"Сумма на счете {round(cash, 2)}")
    return cash


def verification_gold_sum(cash: float) -> float:
    """
    функция проверяет сумму на богатство и при превышении порога отнимает налог на богатство
    :param cash: сумма на счете
    :return: cash обновленная сумма на счете
    """
    if cash >= GOLD_SUM:
        print(f"С Вас высчитан налог на богатство в размере {cash * WEALTH_TAX}")
        cash = cash - cash * WEALTH_TAX
        history_cash.append(cash)

    return cash

def add_sum(cash: float)-> float:
    """
    функция пополняет текущий счет
    :param cash: сумма на счете
    :return: cash обновленная сумма на счете
    """
    money = enter_sum()
    cash = cash + money
    history_cash.append(cash)

    return cash

def wihdrawal(cash: float)-> float:
    """
    функция снятия денег
    :param cash:
    :return:
    """
    money = enter_sum()

    commission = money * PERCENT

    if commission < MIN_SUM:
        commission = MIN_SUM
    elif commission > MAX_SUM:
        commission = MAX_SUM
    if cash < money + commission:
        print("на Вашей карте нет столько денег, введите меньшую сумму")
    else:
        print(f"за снятие наличных с карты с Вас удержена коммиссия в размере {round(commission, 2)}")
        cash = cash - money
        history_cash.append(cash)
        cash = cash - commission
        history_cash.append(cash)

    return cash


cash = 0
history_cash = [0]
transactions = 1

while True:

    print("""
    Доступные операции:
    1 - пополнить карту;
    2 - снять наличные;
    3 - проверить баланс;
    4 - история движения средств;
    5 - забрать карту
            """)
    option = int(input("Выберите операцию: \n"))
    if option == 1:

        cash = verification_gold_sum(cash)
        cash = add_sum(cash)
        if transactions % STEP_FOR_CASHBACK == 0:
            cash = add_cashback(cash)
        transactions += 1
    elif option == 2:
        cash = verification_gold_sum(cash)
        cash = wihdrawal(cash)
        if transactions % STEP_FOR_CASHBACK == 0:
            cash = add_cashback(cash)
        transactions += 1
    elif option == 3:
        cash = verification_gold_sum(cash)
        print(f"На Вашем счету {round(cash, 2)}")
    elif option == 4:
        print("Ваша история движения средств:")
        print(* history_cash)
    elif option == 5:
        break
    else:
        cash = verification_gold_sum(cash)
        print("Вы ввели не существующую операцию, попробуйте снова")