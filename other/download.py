import os
import time


def check_file_load(file_path: str, timeout: int = 120):
    """Проверяем что файл загружен
    :param file_path: Путь к файлу
    :param timeout: Таймаут ожидания
    :return file_path путь к файлу, False если нет"""

    start_time = time.time()
    while True:
        if os.path.exists(file_path):
            return file_path
        if time.time() - start_time > timeout:
            return False
        time.sleep(1)


def check_size(file_path: str, exact_size: int):
    """Проверяем размер файла в Мб
    :param file_path: Путь к файлу
    :param exact_size: Ожидаемый размер"""

    size = str(round(os.path.getsize(file_path) / (1024 * 1024), 2))
    assert size == exact_size, 'Размер не соответствует эталону'
