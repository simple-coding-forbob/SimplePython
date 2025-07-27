import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 자동으로 chromedriver.exe 설치 및 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())
# 로그인 페이지 접속
driver.get("https://www.saucedemo.com/")
# 사용자명(#username) 입력: admin
driver.find_element(By.ID, "user-name").send_keys("standard_user")
# 사용자명(#username) 입력: admin
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# 로그인 버튼(input[type="submit"]) 클릭
driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

# 로그인 결과 확인
time.sleep(1)
print("현재 URL:", driver.current_url)

# 로그인 후 첫 페이지에 나오는 모든 상품 가격 출력
t=driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price ")
for i in range(len(t)):
    quote = t[i].text
    print("상품: ", quote)

# 끝내기
driver.quit()