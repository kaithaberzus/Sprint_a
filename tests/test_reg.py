from api_requests.register import CreateUser
from data import TextMessage
import allure


class TestReg:

    @allure.title('Проверка возвращения кода ответа 201 и токена авторизации при регистрации пользователя с корректными данными')
    def test_create_user_true(self, reg):
        assert reg[0] == 201 and 'access_token' in reg[1], \
            'Пользователь не создан'

    @allure.title('Проверка возвращения кода ответа 400 и текста тела ответа о существовании пользователя с такими данными при регистрации пользователя с данными уже зарегистрированного пользователя')
    def test_create_user_with_existing_user_data(self, reg):
        create_user = CreateUser()
        text = TextMessage()

        user_data = reg[3]
        create_user.create_user(reg[3])
        double_creation_user = create_user.create_user(user_data)

        assert double_creation_user[0] == 400 and double_creation_user[1]['message'] == text.mail_existing, \
            'Пользователь зарегистрирован'
