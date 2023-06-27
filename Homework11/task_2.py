# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

fix_online_site = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
user_login, user_password = 'насырови', 'НасыровИ123'
my_message = 'Привет, Ильшат!'

try:
    # Переходим на https://fix-online.sbis.ru/
    driver.get(fix_online_site)
    sleep(1)
    # Авторизовываемся на сайте https://fix-online.sbis.ru/
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(3)
    # Переходим в реестр "Контакты"
    driver.get('https://fix-online.sbis.ru/page/dialogs')
    sleep(2)
    # Отправляем сообщение самому себе
    new_message_btn = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    new_message_btn.click()
    sleep(1)
    search_area = driver.find_element(By.CSS_SELECTOR,
                                      '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls'
                                      '-Search__nativeField_caretEmpty.controls'
                                      '-Search__nativeField_caretEmpty_theme_default ')

    search_area.send_keys('Насыров Ильшат')
    sleep(2)
    person = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-addressee-selector__plain-list-view"]')
    person.click()
    sleep(1)
    text_editor = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    text_editor.send_keys(my_message)
    sleep(1)
    msg_send_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    msg_send_btn.click()
    sleep(1)
    close_btn = driver.find_element(By.CSS_SELECTOR, '.icon-Close')
    close_btn.click()
    sleep(1)
    # Проверяем что сообщение появилось в реестре
    messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item__content-inner')
    assert messages[0].text == my_message
    # Удаляем сообщение
    action_chains = ActionChains(driver)
    action_chains.move_to_element(messages[0])
    action_chains.context_click(messages[0])
    action_chains.perform()
    sleep(1)
    msg_options = driver.find_elements(By.CLASS_NAME, 'controls-Menu__row')
    delete_btn = msg_options[5]
    delete_btn.click()
    sleep(2)
    # Убедимся что сообщение удалилось
    messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert messages[0].text != my_message
    sleep(1)
    print('Успешно')
finally:
    driver.quit()
