from .Pages.main_page import MainPage
import time, pytest


link = 'http://qa-assignment.oblakogroup.ru/board/:pavel_plakhin'

#@pytest.mark.skip
@pytest.mark.parametrize('category', ['Семья',
                                      'Работа',
                                      'Прочее'])
def test_create_uniq_task_to_existing_category(browser, category):
    page = MainPage(browser, link)
    page.category = category
    page.open()
    page.create_uniq_task_to_present_category()
    page.should_be_task_in_category()
    #time.sleep(5)

#@pytest.mark.skip
def test_create_uniq_task_to_new_category(browser):
    page = MainPage(browser, link)
    page.open()
    page.create_uniq_task_to_new_category()
    page.should_be_task_in_category()

#@pytest.mark.skip
def test_change_status_to_performed(browser):
    page = MainPage(browser, link)
    page.open()
    page.change_status()
    page.should_be_task_mark_as_performed()

#@pytest.mark.skip
def test_change_status_to_reopen(browser):
    page = MainPage(browser, link)
    page.open()
    page.change_status()
    page.should_be_task_mark_as_open()

#@pytest.mark.skip
def test_create_task_with_empty_task_and_category(browser):
    page = MainPage(browser, link)
    page.open()
    page.create_empty_task_and_category()
    page.should_be_hidden_button()

def test_create_empty_task_to_new_category(browser):
    page = MainPage(browser, link)
    page.open()
    page.create_empty_task_to_new_category()
    page.should_be_hidden_button()



