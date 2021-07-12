from selenium import webdriver
import math
import time
a = str(math.ceil(math.pow(math.pi, math.e)*10000))

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name("form-control first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_class_name("form-control second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control third")
    input3.send_keys("мыльце")
    button = browser.find_element_by_css_selector(".button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла