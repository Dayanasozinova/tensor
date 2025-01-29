from pages.contacts_page import ContactsPage
from pages.dwnload_page import DownloadPage
from pages.main_page import MainPage
from pages.tensor_page import TensorPage
from other.logger import Logger
from other.download import check_size

loger = Logger().logger


def test_pages(browser):
    loger.info('Переходим на страницу Контакты')
    main_page = MainPage(browser)
    main_page.open_page()
    main_page.open_contact_page()

    loger.info('Переходим на страницу Тензор')
    contacts_page = ContactsPage(browser)
    contacts_page.click_banner()

    loger.info('Проверяем наличие блока с названием "Сила в людах"')
    tensor_page = TensorPage(browser)
    tensor_page.switch_to_opened_window()
    tensor_page.check_strong_of_people_block_title_displayed()
    tensor_page.open_details()
    tensor_page.check_right_url('https://tensor.ru/about')
    tensor_page.check_working_displayed()

    loger.info('Проверяем размеры фотографии')
    tensor_page.check_equality_of_size()


def test_change_region(browser):
    loger.info('Открываем начальную страницу')
    main_page = MainPage(browser)
    main_page.open_page()

    loger.info('Открываем страницу Контакты')
    main_page.open_contact_page()

    loger.info('Проверяем домашний регион')
    contacts_page = ContactsPage(browser)
    contacts_page.check_region('Республика Татарстан')
    contacts_page.check_partners_list('Казань')

    loger.info('Проверяем смену региона на Камчатский край')
    contacts_page.change_region('Камчатский край')
    contacts_page.check_region('Камчатский край')
    contacts_page.check_partners_list('Петропавловск-Камчатский')
    contacts_page.check_right_url('41-kamchatskij-kraj')
    contacts_page.check_right_title('Saby Контакты — Камчатский край')


def test_download_plugin(browser):
    loger.info('Открываем страницу загрузки плагина')
    main_page = MainPage(browser)
    main_page.open_page()
    main_page.open_download_local_version()
    download_page = DownloadPage(browser)

    loger.info('Загружаем плагин')
    file_path, exact_size = download_page.download_installer('Веб-установщик', 'sbisplugin-setup-web.exe')

    loger.info('Проверяем размер файла')
    check_size(file_path, exact_size)
