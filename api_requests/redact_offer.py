import config
from data import Data
import requests
import allure


class RedactOffer:

    @allure.step('Отправка запроса на редактирование офера')
    def redact_offer(self, id_offer, data, token):
        redact = requests.patch(f"{config.MAIN_URL}{config.UPDATE_OFFER}/{id_offer}",
                                data = data,
                                headers = Data.auth_token(token, data)
                                )

        return redact.status_code, redact.json()