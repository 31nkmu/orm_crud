import config.services as services

user_obj = services.Account()
category_obj = services.Category()
product_obj = services.Product()


def main():
    while True:
        print('Привет 👋\nВыбери один из вариантов (введи число)')
        try:
            # меню
            choice = int(input('1: войти в аккаунт\n2: зарегистрироваться\nТвой выбор: '))
            if choice not in [1, 2]:
                raise AttributeError()
            if choice == 1:
                user = user_obj.get_user()
            elif choice == 2:
                user = user_obj.register()

            # категории
            category_obj.get_or_create_category()

            # продукты
            services.product_cycle(user)

        except ValueError:
            print('\n!!!!!!!!!!!!!Нужно ввести только чило\n')
        except AttributeError:
            print('\n!!!!!!!!!!!!!Нет такого варианта\n')


if __name__ == '__main__':
    main()
