# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome()
try:
    # Переходим на https://sbis.ru/
    driver.get(sbis_site)
    # Проверяем соответствие открытого сайта с требуемым по условию
    assert driver.current_url == sbis_site, 'Не верно открыт сайт'
    # Переходим в раздел "Контакты"
    tab_contact = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    tab_contact_txt = 'Контакты'
    # Проверяем соответствие теста найденного элемента и искомого по условию
    assert tab_contact.text == tab_contact_txt
    tab_contact.click()
    sleep(1)
    # Находим баннер Тензор и кликаем по нему
    banner_tensor = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor.mb-8')
    banner_tensor.click()
    driver.switch_to.window((driver.window_handles[1]))
    sleep(1)
    # Проверяем что есть блок новости "Сила в людях"
    news_banner = driver.find_elements(By.CLASS_NAME, 's-Grid-col')
    news = news_banner[7]
    # Переходим в этом блоке в "Подробнее" и проверяем что открывается https://tensor.ru/about
    detail = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", detail)
    sleep(1)
    detail.click()
    sleep(5)
    tensor_url = 'https://tensor.ru/about'
    assert driver.current_url == tensor_url, 'Не верно открыт сайт'
    print('Успешно')
finally:
    driver.quit()

