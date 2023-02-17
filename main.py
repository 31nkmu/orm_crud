from applications.account.views import UserView

user = UserView()


def main():
    while True:
        print('Выбери один из вариантов. Введи число')
        try:
            choice = int(input('1: войти в аккаунт\n2: зарегистрироваться\nТвой выбор: '))
            if choice not in [1, 2]:
                raise AttributeError()
            if choice == 1:
                email = input('Введи свой email')
                password = input('Введи свой пароль')
                data = {
                    'data'
                }
                user.get()


        except ValueError:
            print('!!!!!!!!!!!!!Нужно ввести только чило')
        except AttributeError:
            print('!!!!!!!!!!!!!Нет такого варианта')


if __name__ == '__main__':
    main()
