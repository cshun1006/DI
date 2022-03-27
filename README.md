# DI

공공데이터 대시보드 프로젝트

---

## 프로젝트 :  사고다발지역 주변 시설 분석을 통한 사고유형 유추 및 교통 인프라 재고의 필요성   

## 구성원

: 각자 이름 옆에 [branch](https://backlog.com/git-tutorial/kr/stepup/stepup2_2.html) 만들고 이름 작성해주세요.

* 전동준: `dongjun`
* 박지영: `zziyyung`
* 이재원: `jaewon`
* 조성헌: `seongheon`

---
## 데이터 파이프라인 구축 과정
1. 프로젝트 기획 및 주제 선정
2. WBS 작성(프로젝트 계획 및 역할 분담)
2. 데이터 수집(OpenAPI, csv, 크롤링 활용)
3. 데이터 전처리 및 도구 선정
4. ERD 작성
5. Django를 이용한 Dashboard 제작

---
## 데이터소개
* 교통사고 데이터
1. 도로교통공단_보행노인사고다발지역정보서비스 (https://www.data.go.kr/data/15057666/openapi.do)
2. 도로교통공단_연휴기간별사고 다발지역정보 조회 서비스 (https://www.data.go.kr/data/15058759/openapi.do)
3. 도로교통공단_보행어린이사고다발지역정보서비스 (https://www.data.go.kr/data/15058925/openapi.do)
4. 도로교통공단_지자체별사고 다발지역정보 조회 서비스
(https://www.data.go.kr/data/15057467/openapi.do)
5. 도로교통공단_스쿨존어린이사고다발지역정보서비스
(https://www.data.go.kr/data/15058311/openapi.do)
6. 도로교통공단_보행자무단횡단사고다발지역정보서비스
(https://www.data.go.kr/data/15058578/openapi.do)
7. 도로교통공단_부문별_음주운전_교통사고
(https://www.data.go.kr/data/15094170/fileData.do#tab-layer-file)



* 인프라 데이터
1. 서울특별시 관악구_스마트횡단보도 설치현황
(https://www.data.go.kr/data/15079885/fileData.do)
2. 서울특별시 서대문구_안심이 CCTV 설치 현황
(https://www.data.go.kr/data/15081865/fileData.do)
3. 서울특별시 송파구_옐로우카펫위치 정보
(https://www.data.go.kr/data/15034354/fileData.do)
4. 서울특별시 동작구_과속방지턱
(https://www.data.go.kr/data/15043012/fileData.do)
5. 부산광역시_서구_무인주차단속카메라
(https://www.data.go.kr/data/15040437/fileData.do)
6. 전국스마트가로등표준데이터
(https://www.data.go.kr/data/15028205/standard.do)



---

## 수행도구
- 프로젝트 기획 : 구글 독스, 줌
- WBS(간트) : Asana 사용
- 데이터 파이프라인 구축 : Python, PySpark, Hadoop, AWS, MongoDB, RDBMS(MySQL, Oracle 중에서 고를 거야), Django

---
## 역할분담
- 팀장: 전동준 
- 팀원1: 박지영
- 팀원2: 이재원
- 팀원3: 조성헌

---
## 일정 
- 03/16 : 팀 결성
- 03/17 ~ 03/19 : 주제 선정 및 프로젝트 기획
- 3/20 ~ 3/00 : 공공데이터 수집 및 가공
- 3/00 ~ 3/00 : 크롤링
- 3/00 ~ 3/00 : 하둡과 스파크 연결
- 3/00 ~ 3/00 : 가공된 데이터 하둡에 저장
- 3/00 ~ 3/00 : ERD 설계
- 3/00 ~ 3/00 : 스파크에서 DB로 저장
- 3/00 ~ 3/00 : AWS구축 (크론탭) 
- 3/00 ~ 3/00 : Django로 대시보드 만들기
- 3/00 ~ 3/00 : 포트폴리오(PPT) 작성 및 발표 준비(리허설)
---
## commit 규칙
- "날짜_이름_작업명"
- ex) "0319_홍길동_db수정"
---
