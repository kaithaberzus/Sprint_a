from api_requests.auth import Auth
import allure


class TestAuth:

    @allure.title('Проверка возвращения кода ответа 201 и и токена авторизации в теле ответа при отправке запроса с корректными данными на авторизацию пользователя')
    def test_auth_user_true(self, reg):
        auth = Auth()

        response_auth = auth.auth_user(reg[4])

        assert response_auth[0] == 201 and 'token' in response_auth[1], \
            'Авторизация не успешна'