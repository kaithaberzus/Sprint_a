import pytest
from api_requests.delete_offer import DeleteOffer
from data import Data
from api_requests.register import CreateUser
from api_requests.create_listing import CreateListing
from api_requests.auth import Auth


# Фикстура регистрации
@pytest.fixture
def reg():
    create_user = CreateUser()
    data = Data()
    auth = Auth()

    user_data = data.data_for_reg_and_auth()


    cr_us = create_user.create_user(user_data[0])
    token = auth.auth_user(user_data[1])[2]

    yield cr_us[0], cr_us[1], token, user_data[0], user_data[1]

# Фикстура удаления офера
@pytest.fixture
def delete_offer(reg, create_offer):
    delete = DeleteOffer()

    yield create_offer[0], create_offer[1], create_offer[2]

    delete.delete_offer(create_offer[1].get('id'), reg[2])

# Фикстура созадния офера
@pytest.fixture
def create_offer(reg):
    create_listing = CreateListing()
    data = Data()

    listing_data = data.data_for_create_offer(data.old_name)
    create_listing = create_listing.create_listing(reg[2], listing_data)

    yield create_listing[0], create_listing[1], listing_data, reg[2], reg[4], reg[3]
