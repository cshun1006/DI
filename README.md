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
1. 서울특별시 스마트횡단보도 설치현황
  (https://www.data.go.kr/data/15079885/fileData.do)

2. 서울특별시 옐로우카펫위치 정보
  (https://www.data.go.kr/data/15034354/fileData.do)

3. 서울특별시 과속방지턱
  (https://www.data.go.kr/data/15043012/fileData.do)

4. 전국무인교통단속카메라표준데이터
  (https://www.data.go.kr/data/15028200/standard.do)

5. 전국스마트가로등표준데이터
  (https://www.data.go.kr/data/15028205/standard.do)

6. 서울특별시 공영주차장 안내정보
  (http://data.seoul.go.kr/dataList/OA-13122/S/1/datasetView.do#AXexec )

7. 어린이보호구역 지정현황(2021.6월말 기준)

  (http://data.seoul.go.kr/dataList/OA-2799/F/1/datasetView.do)



* 크롤링 데이터 : 구글 지도(Google Map)에 검색 키워드와 좌표, 일정 범위(zoom)을 입력해 가져온 주변 정보
  * 키워드 : [어린이, 초등학교, 놀이터, 키즈카페, 소아과, 학원, 요양원, 경로당, 공원, IC, 요금소, 버스터미널, 관광지, 숙박업소, 시장, 주차장, 술집]



---

## 수행도구
- 프로젝트 기획/소통/버전관리: 구글 독스, 줌, 디스코드, GitHub
- WBS(간트) : Asana, Excel
- 데이터 파이프라인 구축 : Python, PySpark, Hadoop, AWS, MongoDB, RDBMS(MySQL), Django

---
## 역할분담
- 팀장: 전동준(크롤링) 
- 팀원1: 박지영(키워드 선정, AWS 구축)
- 팀원2: 이재원(크롤링)
- 팀원3: 조성헌(키워드 선정, AWS 구축)
- 공통 
  1. 데이터 수집 및 가공
  2. ERD 설계
  3. 테이블 정의서
  4. Django 대시보드 만들기
  5. PPT 작성

---
## 일정 
- 3/16 : 팀 결성
- 3/17 ~ 3/19 : 주제 선정 및 프로젝트 기획
- 3/20 ~ 3/21 : 공공데이터 수집 및 가공 ( 데이터 수집 /사고다발지역 api - json / 인프라 데이터.csv 전처리 )
- 3/22 ~ 3/27 : 크롤링( 키워드 선정 (네이버뉴스크롤링) , 키워드 받아서 구글맵 주변찾기 크롤링)
- 3/24 ~ 3/27 : AWS구축(하둡과 스파크 연결, 가공된 데이터 하둡에 저장)
- 3/24 ~ 3/27 : ERD 설계 , 테이블정의서 
- 3/27 ~ 3/30 : 스파크에서 DB로 저장, 크론탭 
- 3/28 ~ 3/31 : Django로 대시보드 만들기
- 3/30 ~ 4/1 : 포트폴리오(PPT) 작성 및 발표 준비(리허설)
---
## commit 규칙
- "날짜_이름_작업명"
- ex) "0319_홍길동_db수정"

---
