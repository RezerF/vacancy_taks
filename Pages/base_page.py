import random
import string
from selenium.webdriver.common.by import By
from .locators import NewTaskLocators, BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.task_name = ""
        self.category = ''

    def open(self):
        self.browser.get(self.url)

    def set_task_name(self):
        text = ''.join(random.choice(string.ascii_letters) for _ in range(12))
        self.__setattr__('task_name', text)

    def category_name(self):
        text = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        self.__setattr__('category', text)

    def should_be_task_in_category(self):
        todolist = self.browser.find_element(By.XPATH, f'//h2[text()="{self.category}"]/parent::*')
        html_list = todolist.get_attribute("innerHTML")
        assert (self.task_name in html_list), 'Task not to be present to-do list'

    def should_be_task_mark_as_performed(self):
        task_milk = self.browser.find_element(*BasePageLocators.PARENT_BUY_MILK)
        task_milk_closed = 'style="text-decoration: line-through;"'
        html_list = task_milk.get_attribute("innerHTML")
        assert (task_milk_closed in html_list), 'Task not to be closed'

    def should_be_task_mark_as_open(self):
        task_milk = self.browser.find_element(*BasePageLocators.PARENT_BUY_MILK)
        task_milk_open = 'style="text-decoration: none;"'
        html_list = task_milk.get_attribute("innerHTML")
        assert (task_milk_open in html_list), 'Task is closed'

    def should_be_hidden_button(self):
        submit = self.browser.find_element(*NewTaskLocators.SUBMIT_BUTTON)
        assert not submit.is_displayed(), 'Submit button is active'

