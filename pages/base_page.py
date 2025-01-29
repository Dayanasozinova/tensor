from typing import Tuple

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: Tuple[str, str], time: int = 10):
        """Ищем элемент по локатору
        :param locator: локатор
        :param time: время ожидания
        :return: элемент"""

        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не нашли элемент по локатору {locator}")

    def find_elements(self, locator: Tuple[str, str], time: int = 10):
        """Ищем элементы по локатору
        :param locator: локатор
        :param time: время ожидания
        :return: элементы"""

        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Не нашли элементы по локатору {locator}")

    def find_element_by_text(self, locator: Tuple[str, str], text: str, time: int = 10):
        """Ищем элемент по локатору и текстовому содержимому
        :param locator: локатор
        :param text: текст
        :param time: время ожидания
        :return: элемент"""

        return [element for element in self.find_elements(locator, time) if text in element.text][0]

    def open_page(self, url: str = "https://sbis.ru/"):
        """Открываем страницу
        :param url: url страницы
        :return: url страницы"""

        return self.driver.get(url)

    def wait_text_in_element(self, locator: Tuple[str, str], text: str):
        """Ожидаем текст внутри элемента
        :param locator: локатор
        :param text: текст
        :return: текст"""

        return WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(locator, text),
                                                   message='Не дождались нужный текст')

    def switch_to_opened_window(self):
        """Переключаемся на открытое окно"""

        self.driver.switch_to.window(self.driver.window_handles[-1])

    def check_right_title(self, title: str):
        """Проверяем наличие нужного заголовка
        :param title: заголовок"""

        assert self.driver.title == title

    def scroll_to_element(self, element: object):
        """Скролим к элементу
        :param element: элемент"""

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def check_right_url(self, reference_url: str):
        """Проверяем наличие нужного url
        :param reference_url: url"""

        assert self.driver.current_url == reference_url
