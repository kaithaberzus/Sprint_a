import requests
import config
from data import Data
import allure


class DeleteOffer:

    @allure.step('Отправка запроса на удаление офера')
    def delete_offer(self, listing_id, token):
        delete = requests.delete(f'{config.MAIN_URL}{config.DELETE_LISTING}/{listing_id}',
                                 headers = Data.auth_token_without_ctype(token)
                                 )
        print(delete.status_code, delete.json())
        return delete.status_code, delete.json()