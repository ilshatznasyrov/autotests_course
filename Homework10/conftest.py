import pytest
import datetime

@pytest.fixture(scope='class')
def print_time():
    print(f'\n Время начала: {datetime.datetime.now().strftime("%H:%M:%S")}')
    yield
    print(f'\n Время завершения: {datetime.datetime.now().strftime("%H:%M:%S")}')

@pytest.fixture(scope='function')
def print_work_time():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print(f'\n Время выполнения: {end - start}')