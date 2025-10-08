from api_requests.delete_offer import DeleteOffer
from data import TextMessage
import allure


class TestDeleteOffer:

    @allure.title('Проверка возвращения кода ответа 200 и текса ответа об успешном удалении офера в теле ответа при удалении офера с корректными данными')
    def test_delete_offer(self, create_offer):
        delete = DeleteOffer()
        text = TextMessage()

        dele = delete.delete_offer(create_offer[1].get('id'), create_offer[3])

        assert dele[0] == 200 and dele[1]['message'] == text.delete_true, \
            'Офер не удален'