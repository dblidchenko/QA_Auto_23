from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInTwilio(BasePage):
    URL = 'https://www.twilio.com/try-twilio'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInTwilio.URL)

    def try_login(self, firstname, lastname, email, password):
        # знаходимо поле, в яке будемо вводити неправильне імїя користувача
        fname_elem = self.driver.find_element(By.ID, 'FirstName')

        # вводимо неправильне імʼя користувача
        fname_elem.send_keys(firstname)

        # знаходимо поле, в яке будемо вводити неправильне прізвище
        lname_elem = self.driver.find_element(By.ID, 'LastName')

        # вводимо неправильне прізвище
        lname_elem.send_keys(lastname)

        # знаходимо поле, в яке будемо вводити неправильну адресу електронної пошти
        email_elem = self.driver.find_element(By.ID, 'EmailAddr')

        # вводимо неправильну адресу електронної пошти
        email_elem.send_keys(email)

        # знаходимо поле, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID, 'Passwd')

        # вводимо неправильний пароль
        pass_elem.send_keys(password)

        # знаходимо поле чекбокса Privacy Policy
        pp_elem = self.driver.find_element(By.ID, 'Tos')

        # відмічаємо чекбокс як прочитаний
        pp_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
