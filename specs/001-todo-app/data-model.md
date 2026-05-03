# Data Model: CLI ToDo Management App

## Entities

### Todo Item

- `id`: 고유 식별자, 정수 자동 증가
- `title`: 작업 제목, 문자열, 필수, 비어 있을 수 없음
- `description`: 작업 상세 설명, 문자열, 선택
- `due_date`: 마감일, 날짜, 선택
- `priority`: 우선순위, 문자열, 선택, 허용 값: `high`, `medium`, `low`
- `completed`: 완료 상태, 불리언, 기본값 `false`
- `created_at`: 생성 시각, 타임스탬프
- `updated_at`: 마지막 수정 시각, 타임스탬프

## Relationships

- 본 기능은 단일 엔터티 모델을 중심으로 하며, 다른 엔터티와 관계를 가지지 않습니다.

## Validation rules

- `title`은 반드시 존재해야 합니다.
- `priority`가 제공되면, 허용 값(`high`, `medium`, `low`)이어야 합니다.
- `due_date`가 제공되면, ISO 형식(`YYYY-MM-DD`)으로 파싱 가능합니다.
- `completed`는 `true` 또는 `false`만 허용됩니다.

## Storage schema

- 데이터는 로컬 SQLite로 영속 저장됩니다.
- 테이블 이름: `todos`
- 컬럼 매핑: Python 객체 필드와 1:1 대응

## Notes

- 별도 `description` 엔터티는 도입하지 않고, Todo Item은 단일 테이블로 유지합니다.
- 레이어 분리 원칙을 위해 ORM 모델은 `todo_lib` 내부에서 관리하고, CLI 코드에서는 직접 데이터 저장 로직을 호출하지 않습니다.
