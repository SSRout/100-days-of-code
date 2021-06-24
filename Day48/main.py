from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path="D:\Handson\chromedriver\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

'''driver.get("https://www.cricbuzz.com/")
search=driver.find_element_by_name("search")
# search.click()
search.send_keys("india")
search.send_keys(Keys.ENTER)
driver.quit()'''

driver.get("https://www.youtube.com/")
try:

    driver.implicitly_wait(2500)
    wait = WebDriverWait(driver, 500)
    search=wait.until(EC.visibility_of_element_located((By.ID,"search")))
    search.click()
    search.send_keys("Python")
    search.send_keys(Keys.ENTER)

    driver.implicitly_wait(4500)
    paly=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='contents']/ytd-video-renderer[1]/div[@id='dismissible']/ytd-thumbnail")))
    driver.implicitly_wait(4500)
    paly.click()

finally:
    driver.quit()
