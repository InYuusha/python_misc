from selenium import webdriver

driver =webdriver.Firefox(executable_path='C:\\Program Files\\geckodriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()
search=driver.find_element_by_name('q')
search.clear()
search.send_keys("phones")
search.submit()

