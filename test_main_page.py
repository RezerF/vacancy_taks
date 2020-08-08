from .Pages.main_page import MainPage
import time, pytest

@pytest.mark.parametrize('category', ['Семья',
                                      'Работа',
                                      'Прочее'])
def test_create_uniq_task_to_existing_category(browser, category):
    link = 'http://qa-assignment.oblakogroup.ru/board/:pavel_plakhin22'
    page = MainPage(browser, link)
    page.category = category
    page.open()
    page.create_uniq_task_to_present_category()
    page.should_be_task_in_category()
    #time.sleep(5)




