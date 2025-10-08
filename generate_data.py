from faker import Faker


class GenerateData:

    fake = Faker()

    #Генерация пароля
    def create_password(self):
        return self.fake.password()

    #Генерация почты
    def create_email(self):
        return self.fake.email()