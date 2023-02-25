from modules.ui.page_objects.sign_in_page import SignInTwilio
import pytest


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
