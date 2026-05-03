# CLI Command Contract: ToDo Management App

## Command surface

### `todo add "<제목>" [--due YYYY-MM-DD] [--priority high|medium|low]`

- 목적: 새로운 ToDo 항목을 추가합니다.
- 입력:
  - `제목` (필수)
  - `--due` (선택): 마감일
  - `--priority` (선택): `high`, `medium`, `low`
- 출력: 생성된 항목의 ID 및 요약 정보
- 오류:
  - 제목이 없으면 오류
  - 우선순위 값이 허용되지 않으면 오류
  - 마감일 형식이 잘못되면 오류

### `todo list [--filter done|pending] [--priority high|medium|low]`

- 목적: 저장된 ToDo 항목을 조회합니다.
- 입력:
  - `--filter` (선택): `done` 또는 `pending`
  - `--priority` (선택): `high`, `medium`, `low`
- 출력: 조건에 맞는 항목 목록
- 동작:
  - 필터가 없으면 모든 항목을 반환
  - 상태 필터와 우선순위 필터를 함께 사용할 수 있다

### `todo done <id>`

- 목적: 특정 항목을 완료로 표시합니다.
- 입력:
  - `id` (필수): 완료할 항목의 ID
- 출력: 완료 처리 결과 메시지
- 오류:
  - ID가 존재하지 않으면 오류

### `todo delete <id>`

- 목적: 특정 항목을 삭제합니다.
- 입력:
  - `id` (필수): 삭제할 항목의 ID
- 출력: 삭제 결과 메시지
- 오류:
  - ID가 존재하지 않으면 오류

## Contract notes

- CLI는 순수 텍스트 입출력으로 동작합니다.
- REST API, GUI, 웹 인터페이스는 이 계약에 포함되지 않습니다.
- 명령어 문법은 Typer 기반으로 구현됩니다.
