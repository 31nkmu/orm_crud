from pprint import pprint

from sqlalchemy.orm.exc import UnmappedInstanceError


from applications.account.views import LoginView, UserView
from applications.product.views import CategoryView, ProductView

user_login_obj = LoginView()
user_obj_ = UserView()
category_obj_ = CategoryView()
product_obj_ = ProductView()


class Account:
    @staticmethod
    def get_user() -> dict:
        while True:
            try:
                data = {
                    'data': {
                        'email': input('Введи свой email: ').lower(),
                        'password': input('Введи свой пароль: ').lower()
                    }
                }
                user = user_login_obj.get(data)
                print('\nТы успешно залогинился 🥳\n')
                return user
            except Exception as ex_:
                print(f'\n{ex_}\n')

    @staticmethod
    def register() -> dict:
        while True:
            try:
                data = {
                    'data': {
                        'email': input('Введи email: ').lower(),
                        'password': input('Введи пароль: ').lower(),
                        'password2': input('Подтверди свой пароль: ').lower()
                    }
                }
                user = user_obj_.create(data)
                print('\nТы успешно зарегистрировался 🥳\n')
                return user
            except Exception as ex_:
                print(f'\n{ex_}\n')


class Category:
    @staticmethod
    def get_or_create_category():
        while True:
            try:
                category_list = category_obj_.list()
                print('Список доступных категорий (запомните их номера):')
                for dict_ in category_list:
                    print(f"{dict_['id']}: {dict_['title']}")
                choice = input('Добавить новую категорию? (Да/Нет): ').lower()
                if choice not in ['yes', 'no', 'да', 'нет']:
                    raise AttributeError()
                if choice in ['да', 'yes']:
                    category_obj_.create({
                        'data': {'title': input('Введи название категории: ').lower()}
                    })
                    for dict_ in category_list:
                        print(f"{dict_['id']}: {dict_['title']}")
                    print('\nКатегория успешно добавлен 🥳\n')
                elif choice in ['нет', 'no']:
                    return
            except AttributeError:
                print('\n!!!!!!!!!!!!!Неправильный ответ\n')
            except Exception as ex_:
                print(f'\n{ex_}\n')


class Product:
    @staticmethod
    def get():
        while True:
            try:
                request = {
                    'id': int(input('id продукта: '))
                }
                data = product_obj_.get(request)
                return data
            except ValueError:
                print('\n!!!!!!!!!!!!!Нужно ввести только чило\n')
            except IndexError:
                print('\n!!!!!!!!!!!!!Нет такого продукта\n')
            except Exception as ex_:
                print(f'\n{ex_}\n')

    @staticmethod
    def post(user):
        while True:
            try:
                request = {
                    'data': {
                        'title': input('Название: ').lower(),
                        'price': int(input('Цена: ')),
                        'category_id': int(input('Номер категории: ')),
                        'user_id': user.get('id')
                    }
                }
                data = product_obj_.post(request)
                print('\nПродукт успешно добвален 🥳\n')
                return data
            except ValueError:
                print('\n!!!!!!!!!!!!!Нужно ввести только чило\n')
            except Exception as ex_:
                print(f'\n{ex_}\n')

    @staticmethod
    def list():
        return product_obj_.list()

    @staticmethod
    def update(user):
        while True:
            try:
                request = {
                    'id': int(input('id продукта: ')),
                    'data': {
                        'title': input('Название: ').lower(),
                        'price': int(input('Цена: ')),
                        'category_id': int(input('Номер категории: ')),
                        'user_id': user.get('id')
                    }
                }
                data = product_obj_.update(request)
                print('\nПродукт успешно обновлен 🥳\n')
                return data
            except ValueError:
                print('\n!!!!!!!!!!!!!Нужно ввести только чило\n')
            except AttributeError:
                print('\n!!!!!!!!!!!!Нет продукта с таким id\n')
                break
            except Exception as ex_:
                print(f'\n{ex_}\n')

    @staticmethod
    def delete(user):
        while True:
            try:
                request = {
                    'id': int(input('id продукта: ')),
                    'user_id': user.get('id')
                }
                product_obj_.delete(request)
                print('\nПродукт успешно удален 🥳\n')
                return
            except ValueError:
                print('\n!!!!!!!!!!!!!Нужно ввести только чило\n')
            except IndexError:
                print('\n!!!!!!!!!!!!!Нет такого продукта\n')
            except UnmappedInstanceError:
                print('\n!!!!!!!!!!!!Нет продукта с таким id\n')
            except AttributeError:
                print('\n!!!!!!!!!!!!Нет продукта с таким id\n')
                break
            except Exception as ex_:
                print(f'\n{ex_}\n')
                break


product_obj = Product()
category_obj = Category()


def product_cycle(user):
    print('Теперь давай поработаем с продуктами')
    while True:
        try:
            # продукты

            choice = int(input(
                "1: создать\n"
                "2: изменить\n"
                "3: список продуктов\n"
                "4: один продукт\n"
                "5: удалить продукт\n"
                "6: категории\n"
                "7: выйти в меню\n"
                "Твой выбор: "
            ))
            if choice not in range(1, 8):
                raise AttributeError()
            if choice == 1:
                pprint(product_obj.post(user=user))
            elif choice == 2:
                print(product_obj.update(user=user))
            elif choice == 3:
                pprint(product_obj.list())
            elif choice == 4:
                pprint(product_obj.get())
            elif choice == 5:
                product_obj.delete(user=user)
            elif choice == 6:
                category_obj.get_or_create_category()
            elif choice == 7:
                break

        except ValueError:
            print('\n!!!!!!!!!!!!!Нужно ввести только чило\n')
        except AttributeError:
            print('\n!!!!!!!!!!!!!Нет такого варианта\n')
