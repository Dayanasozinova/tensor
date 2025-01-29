import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContactsPage(BasePage):
    """Страница контактов
    https://tensor.ru/contacts"""

    banner = (By.CSS_SELECTOR, "[title='tensor.ru'] img")
    my_region = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
    partners_list = (By.CSS_SELECTOR, '[data-qa="items-container"]')

    def click_banner(self):
        """Кликаем по баннеру"""

        self.find_element(self.banner).click()

    def check_region(self, region_reference: str):
        """Проверяем свой регион
        :param region_reference: название региона"""

        self.wait_text_in_element(self.my_region, region_reference)
        region = self.find_element(self.my_region).text

        assert region == region_reference, 'Регион не совпадает'

    def check_partners_list(self, city: str):
        """Проверяем наличие блока списока партнеров
        :param city: название города"""

        partners = self.find_element_by_text(self.partners_list, city)
        partners.is_displayed()

    def change_region(self, region: str):
        """Меняем регион
        :param region: название региона"""

        current_reg = self.find_element(self.my_region)
        current_reg.is_displayed()
        current_reg.click()
        new_reg = self.find_element((By.CSS_SELECTOR, f'[title="{region}"]'))
        new_reg.is_displayed()
        new_reg.click()

    def check_right_url(self, region: str):
        """Проверяем региональную ссылку
        :param region: название региона в ссылке"""

        assert self.driver.current_url == f'https://saby.ru/contacts/{region}?tab=clients'
