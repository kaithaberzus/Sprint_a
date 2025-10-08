import requests
import config
import allure


class Auth:

    @allure.step('Отправка запроса на авторизацию пользователя')
    def auth_user(self, data):
        auth = requests.post(f'{config.MAIN_URL}{config.AUTH}',
                             data = data
                             )
        token = auth.json()['token']['access_token']

        return auth.status_code, auth.json(), token