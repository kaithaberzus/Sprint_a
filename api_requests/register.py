import requests
import config
import allure


class CreateUser:

    @allure.step('Отправка запроса на регистрацию пользователя')
    def create_user(self, data):
        registr = requests.post(f"{config.MAIN_URL}{config.REGISTRATE}",
                      data = data
                      )

        return registr.status_code, registr.json()
