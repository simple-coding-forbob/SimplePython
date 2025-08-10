import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 자동으로 chromedriver.exe 설치 및 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())
# 로그인 페이지 접속
driver.get("https://quotes.toscrape.com/login")
# 사용자명(#username) 입력: admin
driver.find_element(By.ID, "username").send_keys("admin")
# 사용자명(#username) 입력: admin
driver.find_element(By.ID, "password").send_keys("admin")

# 로그인 버튼(input[type="submit"]) 클릭
driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

# 로그인 결과 확인, 1초 지연
time.sleep(1)
print("현재 URL:", driver.current_url)

# 로그인 후 첫 페이지에 나오는 첫번째 인용문 출력
t=driver.find_elements(By.CSS_SELECTOR, ".text")
quote = t[0].text
print("인용문:", quote)

# 끝내기
driver.quit()