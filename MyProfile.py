# MyProfile app
import re

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
e_mail = ''
information = ''
# Business data
Taxpayer_Identification_number = '' #ИНН
MSRNIE = '' #ОГРНИП
bill_number = '' #расчетный счет
name_bank = '' # назнвание банка
BIK_number = ''
correspondent_bill = '' # корреспондетский счет
mail_index = '' # почтоный индекс
address = ''

def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, i_parameter, mail_index, address):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Почтовый индекс', mail_index)
    print('Адрес', address)
    if information:
        print('')
        print('Дополнительная информация:')
        print(i_parameter)

def information_about_businessman(MSRNIE, Taxpayer_Identification_number, bill_number, name_bank, BIK_number, correspondent_bill):
    print('')
    print('Информация о предпринимателе')
    print('ОГРНИП:', MSRNIE)
    print('ИНН:', Taxpayer_Identification_number)
    print('Банковские реквизиты')
    print('Р/с:', bill_number)
    print('Банк:', name_bank)
    print('БИК:', BIK_number)
    print('К/с', correspondent_bill)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')


                uphone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in uphone:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch

                e_mail = input('Введите адрес электронной почты: ')
                mail_index = input('Введите почтовый индекс: ')
                result = re.findall('[0-9]{6}', mail_index)
                mail_index = result
                address = input('Введите почтовый адрес (без индекса): ')
                information = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # ввод информации о предпринимателе
                while 1:
                    MSRNIE = int(input('Введите ОГРНИП: '))
                    if len(str(MSRNIE)) != 15:
                        print('ОГРНИП должен содержать 15 сиволов')
                        continue
                    break
                Taxpayer_Identification_number = input('Введите ИНН: ')
                while 1:
                    bill_number = int(input('Введите расчетный счет: '))
                    if len(str(bill_number)) != 20:
                        print('Расчетный счет должен состоять из 20 символов')
                        continue
                    break
                name_bank = input('Введите название банка: ')
                BIK_number = input('Введите БИК: ')
                correspondent_bill = input('Введите корреспондетский счет: ')
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, e_mail, information, mail_index, address)

            elif option2 == 2:
                general_info_user(name, age, phone, e_mail, information, mail_index, address)

                # print information about businessman
                information_about_businessman(MSRNIE, Taxpayer_Identification_number, bill_number, name_bank, BIK_number, correspondent_bill)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')