# Quickstart: CLI ToDo Management App

## 1. 환경 준비

1. Python 3.12가 설치되어 있어야 합니다.
2. `uv` 패키지 관리자를 설치합니다.

```powershell
python -m pip install uv
```

3. 이 프로젝트 루트에서 `pyproject.toml`을 작성하거나, 이후 `uv install`을 실행할 수 있도록 `uv` 설정을 준비합니다.

## 2. 의존성 설치

```powershell
uv install typer sqlalchemy pytest pytest-cov
```

## 3. 테스트 실행

```powershell
uv run python -m pytest
```

## 4. CLI 실행 예시

### 항목 추가
```powershell
todo add "Buy groceries" --due 2026-05-10 --priority high
```

### 전체 목록 조회
```powershell
todo list
```

### 상태별 필터 조회
```powershell
todo list --filter pending
```

### 우선순위별 필터 조회
```powershell
todo list --priority medium
```

### 항목 완료 처리
```powershell
todo done 3
```

### 항목 삭제
```powershell
todo delete 3
```

## 5. 추가 참고

- 로컬 저장소는 SQLite 파일로 관리됩니다.
- `tests/` 폴더에 작성된 pytest 테스트를 먼저 실행하여 구현을 검증합니다.
