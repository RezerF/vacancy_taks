import random
import string
from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.task_name = ""
        self.category = ''

    def open(self):
        self.browser.get(self.url)

    def some_text(self):
        text = ''.join(random.choice(string.ascii_letters) for _ in range(12))
        self.__setattr__('task_name', text)

    def should_be_task_in_category(self):
        todolist = self.browser.find_element(By.XPATH, f'//h2[text()="{self.category}"]/parent::*')
        html_list = todolist.get_attribute("innerHTML")
        assert (self.task_name in html_list), 'Task not to be present on page'

