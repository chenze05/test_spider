# # selenium 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()


# # selenium 2
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://qqsh.gamebbs.qq.com/forum.php')
# node = browser.find_element_by_id('pt')
# print(type(node))
# print(node)


# # selenium 3
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# # selenium 4
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://qqsh.gamebbs.qq.com/forum.php')
# node = browser.find_element_by_id('pt')
# print(node.id)
# print(type(node.location))
# print(node.location)
# print(node.size)

# # selenium 5
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser, 10)
# input = wait.until(ec.presence_of_element_located((By.ID, 'q')))
# button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input)
# print(button)

# selenium 6
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')  # 执行脚本来开启新页签
print(browser.window_handles)  # 获取当前所有页签
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')

