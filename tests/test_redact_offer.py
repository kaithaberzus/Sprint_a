from api_requests.redact_offer import RedactOffer
from data import Data
from data import TextMessage
import allure


class TestRedactOffer:


    @allure.title('Проверка возвращения кода ответа 200 и обновления данных в теле ответа при редактировании офера с корректными токеном авторизации')
    def test_redact_offer(self, create_offer):
        redact = RedactOffer()
        data = Data()

        new_data = data.data_for_create_offer(data.new_name)
        red = redact.redact_offer(create_offer[1]['id'], data.data_for_create_offer(data.new_name), create_offer[3])

        assert red[0] == 200 and create_offer[4] != new_data, \
            'Офер не обновлен'

    @allure.title('Проверка возвращения кода ответа 401 и текста о невозможности редактирования офера при редактировании офера с некорректным токеном авторизации')
    def test_redact_offer_with_false_token(self, create_offer):
        redact = RedactOffer()
        data = Data()
        text = TextMessage()

        new_data = data.data_for_create_offer(data.new_name)
        red = redact.redact_offer(create_offer[1]['id'], data.data_for_create_offer(data.new_name), data.token)

        assert red[0] == 401 and red[1]['message'] == text.no_offer, \
            'Офер отредактирован'