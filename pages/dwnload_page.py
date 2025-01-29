from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import os
import re
from other.download import check_file_load


class DownloadPage(BasePage):
    """Страница скачивания локальных версий
    https://tensor.ru/download/"""

    plugin_type = (By.CLASS_NAME, 'sbis_ru-DownloadNew-block')
    installer = (By.CLASS_NAME, 'sbis_ru-DownloadNew-loadLink__link')

    def download_installer(self, plugin_type: str, path: str):
        """Скачиваем установщик
        :param plugin_type: тип плагина
        :param path: путь к папке для скачивания
        :return: путь к скачанному файлу и эталонный размер файла"""

        installer = self.find_element_by_text(self.plugin_type, plugin_type).find_element(*self.installer)
        installer.click()
        file_path = check_file_load(os.path.join(os.getcwd(), path))

        return file_path, re.search(re.compile(r'\d{1,}\.\d{1,}'), installer.text).group()


