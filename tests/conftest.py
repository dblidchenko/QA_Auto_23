import pytest
class User:

   def __init__(self) -> None:
      self.name = None
      self.second_name = None
   
   def create(self):
      self.name = 'Dmytro'
      self.second_name = 'Blidchenko'

   def remove(self):
      self.name = ''
      self.second_name = ''

@pytest.fixture
def user():
   user = User()
   user.create()

   yield user           #все, що вказано до цього ключового слова, виколнається ДО тесту, все, що після - ПІСЛЯ тесту
                        #аналог return. Завершує роботу функції, повертаючи при цьому якесь значення
   user.remove()