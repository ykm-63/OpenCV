# AI API Contract

백엔드와 AI 파트가 맞춰야 하는 FastAPI 요청/응답 형식입니다.
3~4주차에는 실제 YOLO가 완성되지 않아도, 아래 형식의 더미 JSON을 먼저 반환해서 백엔드 개발을 진행합니다.

## API

```text
POST http://127.0.0.1:8000/api/detect
```

## Request

```text
Content-Type: multipart/form-data
file: 업로드 이미지 파일
```

백엔드는 이미지 파일 1장을 `file` 필드명으로 전송합니다.

## Success Response

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

## Response Fields

| 필드 | 의미 |
| --- | --- |
| `item_name` | 인식된 품목명 |
| `count` | 해당 품목 개수 |
| `confidence` | 인식 신뢰도, 0~1 사이 숫자 |
| `image_filename` | 분석한 이미지 파일명 |
| `analyzed_at` | 분석 시간 |
| `result_image_path` | 박스가 그려진 결과 이미지 경로 |

## Error Response

```json
{
  "error": "Image could not be analyzed"
}
```

## Backend DTO 기준

백엔드는 아래 필드명 기준으로 DTO를 맞춥니다.

```text
itemName
count
confidence
imageFilename
analyzedAt
resultImagePath
```

## DB 컬럼 기준

MariaDB 테이블은 아래 컬럼 기준으로 맞춥니다.

```text
item_name
count
confidence
image_filename
analyzed_at
result_image_path
```

## Important Rules

- 백엔드는 파일 필드명을 `file`로 보냅니다.
- AI는 `detections` 배열로 응답합니다.
- 한 이미지 안에 여러 품목이 있으면 `detections` 배열 안에 여러 객체를 넣습니다.
- `confidence`는 0~1 사이 숫자로 반환합니다.
- `analyzed_at`은 날짜/시간 문자열로 반환합니다.
