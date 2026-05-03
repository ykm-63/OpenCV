# OpenCV Project

## 프로젝트 개요

OpenCV를 활용한 이미지/영상 처리 프로젝트입니다.

## 폴더 구조

```text
OpenCV/
  README.md
  requirements.txt
  .gitignore
  src/
    main.py
    config.py
  data/
    README.md
  outputs/
    .gitkeep
```

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
python src/main.py --image data/images/sample.jpg --output outputs/gray_sample.jpg
```
