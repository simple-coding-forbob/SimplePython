import requests

url = "https://www.simple-coding.com/contact/"
response = requests.get(url)

print("응답 코드:", response.status_code) # 상태 코드(OK(200) 등)
print("HTML 내용 앞부분:")
print(response.text)  # 전체 페이지 내용 가져오기
