from .base_page import BasePage
from .locators import BasePageLocators, NewTaskLocators
from selenium.webdriver.support.ui import Select
import time


class MainPage(BasePage):
    def create_uniq_task_to_present_category(self):
        self.go_to_intfc_create_new_task()
        self.select_category()
        self.add_new_uniq_taks()
        time.sleep(2)
        self.submit_task()
        time.sleep(2)


    def go_to_intfc_create_new_task(self):
        task_button = self.browser.find_element(*BasePageLocators.BUTTON_ADD_TODO)
        task_button.click()

    def select_category(self):
        select = Select(self.browser.find_element_by_tag_name("select"))
        select.select_by_visible_text(f"{self.category}")

    def add_new_uniq_taks(self):
        self.some_text()
        task_input = self.browser.find_element(*NewTaskLocators.TASK_NAME_INPUT)
        task_input.clear()
        task_input.send_keys(self.task_name)

    def submit_task(self):
        self.browser.find_element(*NewTaskLocators.SUBMIT_BUTTON).click()


