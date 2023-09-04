import show_menu as sh
import work_atm as atm

successful_operation = 0   # Количество успешных операций
user_cash = 0   # Баланс на счете
percent_of_cashback = 3   # процент кэшбэка
rich_account = 5_000_000   # Богатый счет
wealth_tax_percent = 10   # налог на богатство
off_list = []

while True:

    # проверка на богатство перед каждой операцией
    user_cash = atm.wealth_check(user_cash, wealth_tax_percent, rich_account)
    print(f'Ваш баланс после налога на богатство: {round(user_cash, 2)}')
    
    menu_item = sh.show_menu()

    # пополнение денег
    if menu_item == 1:
        user_cash, successful_operation = atm.refill(user_cash, int(input('Введите сумму для пополнения: ')), successful_operation)

    # снятие денег
    elif menu_item == 2:
        user_cash, successful_operation = atm.withdrawal(user_cash, int(input('Введите сумму для снятия: ')),successful_operation)
    
    # Выход
    elif menu_item == 3:
        print('До скорых встреч!')
        break
    else: 
        print('Такого числа нет в меню. До скорых встреч.')
        break

    print(f'Ваш баланс после операции : {round(user_cash, 2)}')

    # кэшбэк после 3ьей операции снятия или пополнения
    if successful_operation % 3 == 0:
            user_cash = atm.cashback(user_cash, percent_of_cashback)
            print(f'Ваш баланс после начисления кэшбэка: {round(user_cash, 2)}')
    
    # вывод списка операций
    if successful_operation > 0 and (off_list == [] or successful_operation != list(off_list[-1])[0]):
        off_list.append((successful_operation, user_cash))
        print(off_list)







