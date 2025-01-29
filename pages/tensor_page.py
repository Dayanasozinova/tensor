from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TensorPage(BasePage):
    """Страница Тензор
    tensor.ru"""

    strong_of_people_block = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content")
    working = (By.CSS_SELECTOR, '.tensor_ru-About__block3')
    image = (By.CSS_SELECTOR, '.tensor_ru-About__block3-image-wrapper img')

    def check_strong_of_people_block_title_displayed(self):
        """Проверяем что блок отображается"""

        self.find_element(self.strong_of_people_block).find_element(By.CLASS_NAME,
                                                                    'tensor_ru-Index__card-title').is_displayed()

    def open_details(self):
        """Кликаем по кнопке Подробнее"""

        find_more = self.find_element(self.strong_of_people_block).find_element(By.CLASS_NAME, 'tensor_ru-link')
        self.scroll_to_element(find_more)
        find_more.is_displayed()
        find_more.click()

    def check_working_displayed(self):
        """Проверяем что раздел Работаем отображается"""

        self.find_element(self.working).is_displayed()

    def check_equality_of_size(self):
        """Проверяем, что размеры у всех фотографий хронологии равны"""

        img_element = self.find_element(self.image)
        size_reference = (img_element.get_attribute('width'), img_element.get_attribute('height'))
        for img_elm in self.find_elements(self.image):
            assert size_reference == (
                img_elm.get_attribute('width'), img_elm.get_attribute('height')), 'Размеры изображений не равны'
