import requests

url = "https://www.simple-coding.com"
response = requests.get(url)

print("응답 코드:", response.status_code) # 상태 코드(OK(200) 등)
print("HTML 내용 앞부분:")
print(response.text[:1000])  # 1000자만 출력
