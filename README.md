# Auto_navercafe_attendance
##This program will auto attendance in Naver cafe including Naver auto login detection passing

0.크롬드라이버를 다운받는다.
0.크롬 기본설정 파일의 위치를 찾는다 %localappdata%/Google/Chrome/User Data
1.모든 크롬창을 닫고 실행해야한다.
2.클릭할 버튼들이 꼭 자신의 화면안에 나타나 있어야한다.

##참고
selenium을 통해서는 기존 창을 이용할 수 없고 항상 새로운 창이 뜨게된다.
따라서 새로운 창을 띄울 때 기존 크롬에서 사용하는 사용차 설정들을 불러온다.
로그인 했을 때 자동로그인 방지 문구가 뜨지 않도록 크롬 기본 설정을 로드하고 중간중간에 대기시간을 넣는다.
