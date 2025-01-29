from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    """Главная страница
    https://sbis.ru/"""

    contacts = (By.CLASS_NAME, "sbisru-Header-ContactsMenu")
    more = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu__arrow-icon')
    footer_navs = (By.CLASS_NAME, 'sbisru-Footer__link')

    def open_contact_page(self):
        """Открываем cтраницу контакты"""

        self.find_element(self.contacts).click()
        self.find_element(self.more).click()

    def open_download_local_version(self):
        """Открываем страницу скачивания локальных версий"""

        self.find_element_by_text(self.footer_navs, 'Скачать локальные версии').click()
