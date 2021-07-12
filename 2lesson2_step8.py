from selenium import webdriver
import time
import os



try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    option1 = browser.find_element_by_name("firstname")
    option1.send_keys("Ответ")
    option2 = browser.find_element_by_name("lastname")
    option2.send_keys("Ответ")
    option3 = browser.find_element_by_name("email")
    option3.send_keys("Ответ")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'шаги.txt')
    send = browser.find_element_by_id("file")
    send.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()