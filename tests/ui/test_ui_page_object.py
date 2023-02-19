from modules.ui.page_objects.sign_in_page import SignInPage, SignInTwilio
import pytest


@pytest.mark.ui
def test_incorrect_username_page_object():
    # створення обʼєкту сторінки
    sign_in_page = SignInPage()

    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login('page_object@gmail.com', 'wrong password')

    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title('Sign in to GitHub · GitHub')

    # закриваємо браузер
    sign_in_page.close()


@pytest.mark.ui
def test_incorrect_userdata_page_object():
    # створення обʼєкту сторінки
    sign_in_twilio = SignInTwilio()

    # відкриваємо сторінку https://www.twilio.com/try-twilio
    sign_in_twilio.go_to()

    # виконуємо спробу увійти в систему Twilio
    sign_in_twilio.try_login(
        'african', 'plant', 'african_plant@gmail.com', 'incorrect_password')

    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_twilio.check_title('Twilio | Try Twilio Free')

    # закриваємо браузер
    sign_in_twilio.close()
