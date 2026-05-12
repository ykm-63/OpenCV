# Project Plan

OpenCV와 YOLO를 이용한 물품 인식/분류 서비스의 통합 계획 문서입니다.
기존 역할 분담, 주차별 계획, 회의용 체크 내용을 중복 없이 하나로 정리했습니다.

## 서비스 목표

사용자가 웹 화면에서 재고 이미지를 업로드하면 AI 서버가 물품을 인식하고, 백엔드가 결과를 DB에 저장한 뒤 화면에서 재고와 탐지 결과를 조회할 수 있게 합니다.

```text
이미지 업로드 UI
-> Spring Boot가 이미지 수신
-> Python FastAPI 서버에 분석 요청
-> OpenCV 전처리
-> YOLO 물품 탐지
-> 결과 JSON 반환
-> MariaDB 저장
-> 결과/재고 조회 UI 표시
```

## 기술 스택

| 파트 | 기술 |
| --- | --- |
| AI | Python, OpenCV, YOLOv8, FastAPI, NumPy |
| Backend | Java 17, Spring Boot, Spring Web, Spring Data JPA, Thymeleaf |
| DB | MariaDB, HeidiSQL |
| Data | Google Drive, Roboflow |
| 협업 | GitHub, Notion |

## 역할 분담

| 담당 | 역할 | 주요 업무 |
| --- | --- | --- |
| 팀장 / AI 1 | 전처리 + FastAPI + 백엔드 연동 | OpenCV 전처리, FastAPI API, JSON/API 계약, 백엔드 연동 검수 |
| AI 2 | YOLO + 라벨링 + 모델 성능 | Roboflow 라벨링, YOLO 탐지, 모델 테스트, confidence 기준 정리 |
| Backend 1 | Spring Boot API + MariaDB | FastAPI 호출, DTO, Service, JPA Entity, DB 저장 |
| Backend 2 | UI + 업로드/조회 화면 | 이미지 업로드 UI, 결과 조회 UI, 재고 조회 UI, Thymeleaf 화면 구성 |

## 저장소 운영

현재 `OpenCV` 저장소는 AI 파트 중심으로 사용합니다.
백엔드 파트는 별도 Spring Boot 저장소를 만들어도 됩니다.
두 저장소를 나누더라도 아래 API 계약만 맞추면 연동할 수 있습니다.

```text
AI 저장소:
Python, OpenCV, YOLO, FastAPI

Backend 저장소:
Spring Boot, Thymeleaf, MariaDB
```

## 폴더 기준

```text
OpenCV/
  src/
    main.py
    config.py
    api-contract.md
    api.py
    preprocess.py
    detector.py
    result_writer.py
  data/
    images/
      raw/
      test/
    videos/
      raw/
  outputs/
    original/
    processed/
    detected/
    results.json
  docs/
    project-plan.md
```

## API 계약

백엔드와 AI가 맞춰야 하는 핵심 약속입니다.

```text
POST http://127.0.0.1:8000/api/detect
Content-Type: multipart/form-data
file: 업로드 이미지 파일
```

성공 응답 예시:

```json
{
  "detections": [
    {
      "item_name": "cola",
      "count": 3,
      "confidence": 0.92,
      "image_filename": "test_001.jpg",
      "analyzed_at": "2026-05-12 12:00:00",
      "result_image_path": "outputs/detected/result_001.jpg"
    }
  ]
}
```

실패 응답 예시:

```json
{
  "error": "Image could not be analyzed"
}
```

## 응답 필드

| 필드 | 의미 |
| --- | --- |
| `item_name` | 인식된 품목명 |
| `count` | 해당 품목 개수 |
| `confidence` | 인식 신뢰도, 0~1 사이 숫자 |
| `image_filename` | 분석한 이미지 파일명 |
| `analyzed_at` | 분석 시간 |
| `result_image_path` | 탐지 결과 이미지 경로 |

## DB 기준

초기 DB 구조는 아래 3개 테이블을 기준으로 잡습니다.

```text
items
  상품 기본 정보

stocks
  현재 재고 수량

detection_logs
  AI 탐지 기록
```

AI 응답 JSON과 MariaDB 컬럼은 아래처럼 맞춥니다.

```text
item_name
count
confidence
image_filename
analyzed_at
result_image_path
```

## UI 기준

UI는 최소 2개로 구성합니다.

```text
업로드/분석 UI
  이미지 선택
  분석 요청 버튼
  업로드 성공/실패 메시지
  즉시 분석 결과 표시

결과/재고 조회 UI
  상품명
  수량
  신뢰도
  분석 시간
  결과 이미지 경로 또는 미리보기
```

## 1~2주차: 기초 세팅

목표: 개발 환경, 데이터 폴더, OpenCV 기초, 백엔드 기본 화면을 준비합니다.

### AI 1

- Python 실행 환경 확인
- `requirements.txt` 설치 확인
- OpenCV 이미지 읽기/저장 테스트
- `src/config.py` 경로 구조 확인
- 흑백 변환, resize, blur 테스트
- 전처리 결과를 `outputs/processed/`에 저장

### AI 2

- Google Drive 데이터 폴더 구조 확인
- 테스트 이미지 파일명 규칙 정리
- YOLOv8 설치 방법 조사
- Roboflow 라벨링 방식 조사
- `src/detector.py` 초안 준비

### Backend 1

- Spring Boot 프로젝트 생성
- Java 17, Spring Web, JPA, MariaDB 의존성 준비
- MariaDB 설치/접속 확인
- DB 이름과 테이블 초안 정리

### Backend 2

- Thymeleaf 기본 화면 구성
- 이미지 업로드 화면 초안 작성
- 결과 조회 화면 초안 작성

### 산출물

- 개발 환경 설치 완료
- 테스트 이미지 규칙 확정
- OpenCV 기본 전처리 결과
- 업로드/조회 화면 초안

## 3주차: 연결 준비

목표: AI 서버와 백엔드가 연동될 수 있는 모양을 먼저 만듭니다.

### AI 1

- `src/preprocess.py` 초안 작성
- FastAPI 설치 및 기본 서버 실행
- `/api/detect` 임시 JSON 반환
- 백엔드에 API 주소, 요청 방식, JSON 예시 공유

### AI 2

- YOLOv8 설치
- 샘플 이미지 탐지 준비
- `src/detector.py` 초안 작성
- 테스트 이미지와 라벨링 대상 정리

### Backend 1

- Python FastAPI 호출 방식 정리
- `multipart/form-data` 이미지 전송 준비
- AI 응답 JSON을 받을 DTO 초안 작성
- MariaDB 테이블 초안 작성

### Backend 2

- 이미지 업로드 UI 초안 작성
- 결과 표시 영역 작성
- 결과/재고 조회 UI 초안 작성

### 산출물

- FastAPI 임시 응답
- 백엔드 DTO 초안
- DB 테이블 초안
- 업로드 UI 초안

## 4주차: 샘플 탐지와 API 형식 확정

목표: YOLO 샘플 탐지를 성공시키고, 백엔드와 맞출 API 형식을 확정합니다.

### AI 1

- `/api/detect`에서 이미지 파일 받기
- 전처리 결과 저장
- 더미 JSON 응답을 정해진 형식으로 고정
- 백엔드 호출 테스트 준비

### AI 2

- YOLOv8 샘플 모델 실행
- 샘플 이미지 탐지
- confidence 추출
- 탐지 결과 이미지를 `outputs/detected/`에 저장

### Backend 1

- Spring Boot에서 FastAPI 호출 코드 준비
- DTO 필드와 AI JSON 필드 매칭
- DB 컬럼과 AI JSON 필드 매칭

### Backend 2

- 업로드 화면 개선
- 결과 목록 화면 구성
- 상품명, 수량, 신뢰도, 분석 시간 표시 위치 정리

### 산출물

- YOLO 샘플 탐지 결과
- 탐지 결과 이미지
- 확정된 API 요청/응답 형식
- 백엔드 DTO/DB 초안

## 5주차: AI 결과 형식 확정

목표: 실제 탐지 결과를 JSON으로 저장하고, DB 저장 구조와 맞춥니다.

### AI 1

- `src/result_writer.py` 작성
- `outputs/results.json` 저장
- 에러 응답 형식 추가
- 백엔드 DTO/DB 컬럼과 필드명 확인

### AI 2

- `src/detector.py` 정리
- item_name, count, confidence 추출 정리
- 결과 이미지에 bbox/label 표시
- 오탐/미탐 사례 기록

### Backend 1

- MariaDB 테이블 생성
- JPA Entity 작성
- AI 응답 JSON과 DB 컬럼 매칭

### Backend 2

- 결과 화면에 보여줄 항목 확정
- 업로드 성공/실패 메시지 정리

### 산출물

- 확정된 AI 응답 JSON
- 확정된 DB 테이블 구조
- 결과 화면 표시 항목

## 6주차: DB/웹 연결

목표: 웹 업로드 -> Python 분석 -> DB 저장 흐름을 연결합니다.

### AI 1

- FastAPI 서버 안정화
- Spring Boot에서 실제 이미지 요청 받기
- 전처리 -> YOLO -> JSON 반환 흐름 연결
- 실패 시 error JSON 반환

### AI 2

- 여러 이미지 탐지 테스트
- 탐지 결과 이미지 저장 경로 확인
- result_image_path 확인
- 탐지 실패 케이스 정리

### Backend 1

- Spring Boot에서 FastAPI 호출
- AI 응답 JSON 파싱
- MariaDB에 탐지 결과 저장
- Service/Repository 구조 정리

### Backend 2

- 웹 업로드 기능 연결
- DB에서 결과 조회
- Thymeleaf로 결과 목록 출력
- 결과 이미지 경로 표시

### 산출물

- 웹 업로드 가능
- FastAPI 호출 가능
- MariaDB 저장 가능
- 웹 결과 조회 가능

## 7~8주차: 통합/성능 테스트

목표: 전체 서비스를 완성하고 발표 시연을 준비합니다.

### AI 1

- API 응답 속도 확인
- 잘못된 파일 업로드 예외 처리
- 이미지 확장자 처리
- 백엔드 연동 오류 확인
- 최종 실행 방법 문서 정리

### AI 2

- 여러 상품 탐지 테스트
- confidence 낮은 결과 처리 기준 정리
- 결과 이미지 박스/라벨 확인
- 발표용 성공/실패 이미지 준비

### Backend 1

- DB 저장/조회 검증
- 동일 상품 재고 수량 업데이트 방식 확인
- `detection_logs` 기록 확인
- DB 예외 처리

### Backend 2

- 반응형 화면 확인
- 업로드/결과/재고 조회 화면 마무리
- 사용자 알림 메시지 정리
- 발표용 화면 흐름 정리

### 산출물

- 웹 업로드 -> AI 분석 -> DB 저장 -> 화면 출력 전체 흐름
- 실패 케이스 처리
- 발표 시연용 이미지와 시나리오
- 최종 README/docs 정리

## 팀장 체크 기준

매주 아래 항목을 확인합니다.

```text
AI 응답 JSON
= Spring Boot DTO
= MariaDB 테이블 컬럼
= 화면 표시 항목
```

추가 체크:

- 이미지/영상/결과 파일이 GitHub에 올라가지 않았는가?
- Google Drive 데이터 규칙이 지켜지는가?
- 이번 주 실행 가능한 결과물이 있는가?
- API 형식 변경을 AI/백엔드가 같이 알고 있는가?
- PR 전에 테스트 방법이 정리됐는가?

## 병합 규칙

- `main` 브랜치에는 확정된 내용만 반영합니다.
- 개인 작업은 `feature/이름` 브랜치에서 진행합니다.
- API 계약 변경은 백엔드와 협의 후 반영합니다.
- 이미지, 영상, 결과물은 GitHub에 올리지 않습니다.
