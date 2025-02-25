from data import Url
import pytest
from selenium import webdriver
import requests
from generators import generate_user_body
from methods.user_methods import UserMethods


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1500, 1080)
        driver.get(Url.BASE_URL)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1500, 1080)
        driver.get(Url.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture()
def user_method():
    return UserMethods

@pytest.fixture()
def generate_user_data():
    user_data = generate_user_body()
    email = user_data['email']
    password = user_data['password']
    name = user_data['name']
    yield [user_data, email, password, name]
    user_token = UserMethods().user_token_by_user_data(email, password, name)
    UserMethods().delete_user(user_token)

