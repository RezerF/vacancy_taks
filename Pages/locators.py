from selenium.webdriver.common.by import By


class BasePageLocators():
    BUTTON_ADD_TODO = (By.CSS_SELECTOR, '#add_new_todo')
    TODO_LISTS = (By.CSS_SELECTOR, '[class="col-lg-4 col-md-6 col-sm-6 col-xs-12"]:')
    CHECK_BOX_BUY_MILK = (By.CSS_SELECTOR, 'label[id="7264"]')
    PARENT_BUY_MILK = (By.XPATH, '//label[@id="7264"]/parent::*')


class NewTaskLocators():
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, '#select_category')
    CATEGORY_NEW_LIST = (By.XPATH, '//select/option[text()="Создать новый список"]')
    CATEGORY_FAMILY = (By.XPATH, '//select/option[text()="Семья"]')
    CATEGORY_NEW_NAME = (By.CSS_SELECTOR, '#project_title')
    TASK_NAME_INPUT = (By.CSS_SELECTOR, '#project_text')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit_add_todo')



