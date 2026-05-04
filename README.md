# OpenCV Project

## 프로젝트 개요

OpenCV 기초 전처리부터 YOLO 객체 탐지, DB/웹 연결까지 확장하는 팀 프로젝트입니다.
GitHub에는 코드와 문서만 올리고, 원본 이미지와 영상은 Google Drive로 공유합니다.

## 전체 폴더 구조

```text
OpenCV/
  README.md
  requirements.txt
  .gitignore
  src/
    README.md
    main.py
    config.py
  data/
    README.md
    images/
      raw/
      test/
    videos/
      raw/
  outputs/
    README.md
    original/
    processed/
    detected/
    results.example.json
```

## 폴더 역할

| 경로 | 역할 |
| --- | --- |
| `src/` | 실제 Python 코드가 들어가는 폴더 |
| `src/main.py` | 프로그램 실행 시작 파일 |
| `src/config.py` | 프로젝트 공통 경로 설정 파일 |
| `data/` | Google Drive에서 받은 이미지/영상 데이터를 두는 로컬 폴더 |
| `data/images/raw/` | 원본 이미지 |
| `data/images/test/` | YOLO 적용 전 테스트 이미지 |
| `data/videos/raw/` | 원본 영상 |
| `outputs/original/` | 처리할 때 복사해 둔 원본 이미지 |
| `outputs/processed/` | 흑백, 리사이즈 등 전처리 결과 |
| `outputs/detected/` | YOLO 탐지 결과 이미지 |
| `outputs/results.json` | 나중에 DB에 넣기 전 임시 결과 데이터 |

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python src/main.py
```

이미지 파일을 흑백으로 변환하려면:

```bash
python src/main.py --image data/images/test/sample.jpg --output outputs/processed/sample_gray.jpg
```

## 주차별 진행 방향

| 시기 | 핵심 목표 | 해야 할 일 |
| --- | --- | --- |
| 1~2주차 | OpenCV 기초 + 데이터셋 방향 | 이미지 읽기/저장, 흑백/전처리 테스트, 데이터셋 폴더 정리 |
| 3~4주차 | YOLO 적용 준비 | 샘플 이미지 수집, 라벨링, YOLO 모델 테스트 |
| 5주차 | AI 객체 인식 점검 | YOLO 탐지 코드, 결과 이미지 저장, 코드 리뷰 |
| 6주차 | DB/웹 연결 | 인식 결과를 DB 저장, 웹에서 결과 조회 |
| 7~8주차 | 통합/성능 테스트 | 카메라/업로드 -> YOLO -> DB -> 웹 전체 흐름 완성 |

## 결과 데이터 구조

YOLO 결과는 나중에 DB에 넣기 쉽도록 아래 정보를 기준으로 저장합니다.

```json
{
  "item_name": "sample_item",
  "count": 1,
  "confidence": 0.95,
  "image_filename": "sample.jpg",
  "analyzed_at": "2026-05-04 12:00:00",
  "result_image_path": "outputs/detected/result_001.jpg"
}
```

## 팀 작업 규칙

`main` 브랜치는 안정 버전으로 두고, 각자 기능 브랜치에서 작업한 뒤 Pull Request로 합칩니다.

```bash
git checkout -b feature/name-task
git add .
git commit -m "작업 내용"
git push origin feature/name-task
```
