from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path="D:\Handson\chromedriver\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.cricbuzz.com/")
search=driver.find_element_by_name("search")
# search.click()
search.send_keys("india")
search.send_keys(Keys.ENTER)
driver.quit()