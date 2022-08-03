# 북(BOOKTRIP)

### 프로젝트 설명

책을 읽은 뒤 감동받은 내용을 남기고 싶을 때, 다른 사람들의 리뷰를 보고 읽을만한 책을 고르고 싶을 때, booktrip을 이용해보세요. booktrip은 한국에서 발간되는 다양한 책들을 한 곳에 모아 보고 책에 대한 리뷰를 남길 수 있어요.

### 역할분담

로그인.회원가입: 김고은  상세조회: 이지수  크롤링: 김정수 리뷰작성: 전대훈

### 구현 목표

인터파트 BOOK openapi를 가져와서 베스트셀러들을 출력해준 후 이에 대한 리뷰를 기입할 수 있는 
정보 및 리뷰 사이트

### 개발해야 하는 기능들

- 로그인,회원가입 김고은
- 관광지별 리뷰 목록 조회 / get / 상세 페이지에 리뷰 표시. (response) 이지수
- 반려동물 동반 관광지 크롤링 / get / 페이지에 관광지 리스트(response) 김정수
- 리뷰 작성 / post / 상세 페이지에 신규 리뷰 표시. (response)  전대훈

### DATABASE 
- mongoDB, aws EC2

### Tool
- pycharm