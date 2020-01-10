from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
def search():
    driver.get('http://www.taobao.com')
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
    element.send_keys('美食')
    submit.click()


def main():
    search()



if __name__ == '__main__':
    main()































