import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # створення обʼєкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(
            r"/Users/dima/Documents/Python_basics/GitHub/QA_Auto_23" + "chromedriver")
    )

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # знаходимо поле, в яке будемо вводити неправильне імʼя користувача або поштову адресу
    login_elem = driver.find_element(By.ID, 'login_field')

    # вводимо неправильне імʼя або поштову адресу
    login_elem.send_keys('sergiibutenko@mistakeinemail.com')

    # знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, 'password')

    # вводимо неправильний пароль
    pass_elem.send_keys('12345678')

    # знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, 'commit')

    # емулюємо клік лівою кнопкою миші
    btn_elem.click()

    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == 'Sign in to GitHub · GitHub'

    # закриваємо браузер
    driver.close()
