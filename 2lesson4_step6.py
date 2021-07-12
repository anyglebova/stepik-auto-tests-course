from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(12)

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    button1 = browser.find_element_by_css_selector("[type='submit']")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    option1 = browser.find_element_by_id("input_value")
    x = option1.text
    y = calc(x)
    option1 = browser.find_element_by_id("answer")
    option1.send_keys(y)


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