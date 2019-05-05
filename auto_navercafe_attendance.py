from selenium import webdriver
from time import sleep, time
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
options.add_argument('disable-infobars')
options.add_argument("--user-data-dir=C:/Users/arki1/AppData/Local/Google/Chrome/User Data") # 크롬 기본설정 데이터 가져오기

driver = webdriver.Chrome('chromedriver', chrome_options=options) # 크롬 드라이버 로드

sleep(0.5)
driver.get('https://nid.naver.com/nidlogin.login') # 로그인 페이지 접속
sleep(0.5)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click() #로그인 버튼 클릭

sleep(0.5)
driver.get('https://cafe.naver.com/dalcomi0') # 카페 주소
sleep(0.5)

while True: # 해당 시간이 되면 실행
    now = datetime.now()
    if now.minute == 0: # 0분에 맞춰 실행, now.hour를 이용해 시간 설정 
        break

start = time()
driver.find_element_by_xpath('//*[@id="menuLink6"]').click() # 출석게시판 버튼의 xpath
driver.switch_to_frame('cafe_main') # 게시글 작성 textarea가 포함된 iframe
driver.find_element_by_name('attendancePost.content').send_keys('t') # 게시글 작성
driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/a/img').click() #출석체크 완료
end = time()
print('소요시간 : ', (end-start), '초')
