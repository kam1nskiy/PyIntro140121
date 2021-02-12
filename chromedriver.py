


from selenium import webdriver

driver = webdriver.Chrome("C:\Users\kaminskyi\Downloads\chromedriver_win32")

driver.get("http://testwisely.com/demo")
driver.find_element_by_link_text("Recommend Selenium").click()
driver.quit()