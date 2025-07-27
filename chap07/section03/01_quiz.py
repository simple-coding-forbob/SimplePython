from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# options=Options()
# options.add_argument("--headless")  # 브라우저 숨기고 실행하고 싶을 때 사용

# 자동으로 chromedriver.exe 설치 및 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())
driver.get("https://www.simple-coding.com/guest-book/")
# title 보기
results=driver.find_elements(By.CSS_SELECTOR, "a")

for i in results:
    print(i.get_attribute("href"), end=" ")
    print(i.text)

# 끝내기
driver.quit()
