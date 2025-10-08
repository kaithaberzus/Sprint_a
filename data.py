from requests_toolbelt import MultipartEncoder
from generate_data import *


class Data:

    gd = GenerateData()

    # Данные для регистраии и авторизации
    def data_for_reg_and_auth(self):
        email = self.gd.create_email()
        password = self.gd.create_password()
        reg = {"email": email,
                "password": password,
                "submitPassword": password
                }

        auth = {"email": email,
                "password": password
                }

        return reg, auth

    # Данные для редактирования и создания офера
    def data_for_create_offer(self, name):
        data = MultipartEncoder(fields =
                                {"name": name,
                                 "category": "Хобби",
                                 "condition": "Новый",
                                 "city": "Москва",
                                 "description": "Fibroblasts from brest cancer",
                                 "price": "100000"
                                 })

        return data

    # Токен для создания и редактирования офера
    @staticmethod
    def auth_token(token, data):
        return {'Authorization': f"Bearer {token}",
                "Content-Type": data.content_type
                }

    # Токен для удаления офера
    @staticmethod
    def auth_token_without_ctype(token):
        return {'Authorization': f"Bearer {token}"
                }

    # Старое название объявления
    old_name = "fibroblasts"
    # Новое название объявления
    new_name = "Fibroblasts"

    # Токен для теста на не подходящий токен
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTY1NDAsImVtYWlsIjoia2FAYnJlenVzLnJ1IiwibmFtZSI6IlVzZXIiLCJpYXQiOjE3NTk5MDE2MjksImV4cCI6MTc1OTk4ODAyOX0.f6PfAntUbbIaVstdO33ffxu0UORJT7pTcGV9QTovzaw'


# Тексты ответов
class TextMessage:

    mail_existing = 'Почта уже используется'
    no_offer = "Оффер не найден или у вас нет прав на его редактирование"
    delete_true = 'Объявление удалено успешно'