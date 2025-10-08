import allure


class TestCreateListing:

    @allure.title('Проверка возвращения кода ответа 201 и id офера в теле ответа при создании офера с корректными данными')
    def test_create_listing_true(self, reg, delete_offer):

        assert delete_offer[0] == 201 and 'id' in delete_offer[1], \
            'Офер не создан'