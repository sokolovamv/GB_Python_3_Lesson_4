# пополнение денег
def refill(balance, cash, operation):
    # проверка на кратность 50 и подсчет удачных попыток снятия и пополнения
    if cash % 50 == 0:
        return balance + cash, operation + 1
    else:
        print('Нельзя пополнить на данное количество денег')
        return balance, operation


# Снятие денег
def withdrawal(balance, cash, operation):
    # проверка на кратность 50 по условию
    if cash % 50 == 0:
        # вычет комиссии за снятие с учетом баланса на счете 

        if 30 <= cash * 0.015 <= 600 and cash * 1.015 < balance:
            return balance - cash * 1.015, operation + 1
        
        elif cash * 0.015 < 30 and cash + 30 < balance:
            return balance - cash + 30, operation + 1

        elif cash * 0.015 > 600 and cash + 600 < balance:
            return balance - cash + 600, operation + 1

        else:
            print('На балансе не хватает денег')

    else:
        print('Нельзя снять данное количество денег')
    return balance, operation


# Кэшбэк после 3 операции
def cashback(balance, per_cashback):
    balance *= (1 + per_cashback / 100)
    return balance


# налог на богатство 
def wealth_check(balance, tax, rich_):
    if balance >= rich_:
        balance *= (1 - tax / 100)
    return balance
