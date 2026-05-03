# Research: CLI ToDo Management App

## Decision: Python 3.12

- 선택된 이유: 최신 Python 기능과 타입 힌트 지원을 활용하면서, `uv` 기반 패키지 관리와 호환되는 안정적 런타임입니다.
- 대안 고려: Python 3.11은 널리 사용되나, 계획된 개발 환경과 최신 문서 우선 적용을 위해 3.12를 선택했습니다.

## Decision: Typer for CLI

- 선택된 이유: 선언적 명령어 정의, 자동 도움말 생성, 파라미터 검증을 통해 CLI 구현이 간결해집니다.
- 대안 고려: `argparse`는 추가 의존성이 없지만, 명령어 관리와 입력 검증이 더 절차적이고 코드가 늘어납니다.

## Decision: SQLAlchemy for persistence

- 선택된 이유: 단일 테이블 SQLite 모델을 객체 지향적으로 표현할 수 있으며, 데이터 검증과 마이그레이션 준비가 용이합니다.
- 대안 고려: 표준 `sqlite3`는 더 적은 추상화 레이어를 제공하지만, 데이터 모델 유지 보수 측면에서 SQLAlchemy가 더 명확합니다.

## Decision: SQLite 로컬 파일 저장소

- 선택된 이유: 서버 불필요, 파일 기반 영속성이 단일 개발자 CLI 툴에 적합합니다.
- 대안 고려: JSON/CSV 파일은 간단하지만 필터링·정렬·확장성 측면에서 SQL이 더 강력합니다.

## Decision: pytest + pytest-cov for tests

- 선택된 이유: 테스트 우선 원칙에 부합하며, 빠른 단위 테스트 작성과 커버리지 측정이 가능합니다.
- 대안 고려: 표준 `unittest`는 추가 의존성이 없지만, pytest의 표현력과 플러그인 생태계가 개발 생산성을 높입니다.

## Decision: 최소 의존성 유지

- 사용 패키지: Typer, SQLAlchemy, pytest, pytest-cov
- 추가 패키지 금지: 이 외 패키지는 해당 단계에서 도입하지 않습니다.

## Alternatives considered

- `peewee` 대신 SQLAlchemy: `peewee`는 간결하지만, SQLAlchemy가 더 널리 사용되고 확장성이 큽니다.
- `click` 대신 Typer: Typer가 타입 친화적이며 코드 가독성이 높습니다.
- JSON 파일 대신 SQLite: 복잡한 검색/필터 요구사항을 만족하기 위해 SQLite가 더 적합합니다.
