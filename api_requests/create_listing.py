import requests
import config
from data import Data
import allure


class CreateListing:

    @allure.step('Отправка запроса на создание офера')
    def create_listing(self, token, data):
        listing = requests.post(f"{config.MAIN_URL}{config.CREATE_LISTING}",
                                data = data,
                                headers = Data.auth_token(token, data)
                                )

        return listing.status_code, listing.json()