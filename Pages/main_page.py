from .base_page import BasePage
from .locators import BasePageLocators, NewTaskLocators
from selenium.webdriver.support.ui import Select
import time


class MainPage(BasePage):
    def create_uniq_task_to_present_category(self):
        self.go_to_intfc_create_new_task()
        self.select_category()
        self.add_new_uniq_taks()
        self.submit_task()

    def create_uniq_task_to_new_category(self):
        self.go_to_intfc_create_new_task()
        self.select_new_category()
        self.add_new_uniq_taks()
        self.add_new_uniq_category()
        self.submit_task()

    def create_empty_task_to_new_category(self):
        self.go_to_intfc_create_new_task()
        self.select_new_category()
        self.add_new_uniq_category()

    def create_empty_task_and_category(self):
        self.go_to_intfc_create_new_task()
        self.select_new_category()

    def go_to_intfc_create_new_task(self):
        task_button = self.browser.find_element(*BasePageLocators.BUTTON_ADD_TODO)
        task_button.click()

    def select_category(self):
        select = Select(self.browser.find_element_by_tag_name("select"))
        select.select_by_visible_text(f"{self.category}")

    def select_new_category(self):
        select = Select(self.browser.find_element_by_tag_name("select"))
        select.select_by_visible_text("Создать новый список")


    def add_new_uniq_taks(self):
        self.set_task_name()
        task_input = self.browser.find_element(*NewTaskLocators.TASK_NAME_INPUT)
        task_input.clear()
        task_input.send_keys(self.task_name)

    def submit_task(self):
        self.browser.find_element(*NewTaskLocators.SUBMIT_BUTTON).click()

    def add_new_uniq_category(self):
        self.category_name()
        category_input = self.browser.find_element(*NewTaskLocators.CATEGORY_NEW_NAME)
        category_input.clear()
        category_input.send_keys(self.category)

    def change_status(self):
        buy_milk = self.browser.find_element(*BasePageLocators.CHECK_BOX_BUY_MILK)
        buy_milk.click()




