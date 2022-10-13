# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# # добавили строки в ветке test1

n = 10
# print(list(range(1, n + 1)))
# print([x for x in range(1, n + 1)])
# print(list(range(1, n+1)))

import time
from webbrowser import BaseBrowser
from selenium import webdriver
driver = webdriver.Chrome ()
from selenium.webdriver.common.by import By

driver.get(‘web page URL)
from webdriver_manager.chrome import ChromeDriverManager
MainPage = driver.find_element(By.XPATH, ‘your Xpath’).click()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
from webdriver_manager.chrome import ChromeDriverManager
