# Implementation Plan: CLI ToDo Management App

**Branch**: `001-todo-app` | **Date**: 2026-05-03 | **Spec**: `specs/001-todo-app/spec.md`
**Input**: Feature specification from `specs/001-todo-app/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

Python 3.12 기반 터미널 CLI ToDo 앱입니다. 비즈니스 로직은 `todo_lib/` 안에서 독립적으로 구현하고, `cli/` 레이어는 `todo_lib`를 호출해 명령어를 실행합니다. 데이터는 SQLite 로컬 파일에 저장하며, 명령어는 `todo add`, `todo list`, `todo done`, `todo delete`로 구성됩니다. 테스트는 `pytest`와 `pytest-cov`로 먼저 작성하고, 의존성은 `typer`와 `sqlalchemy`로 최소화합니다.

## Technical Context

**Language/Version**: Python 3.12  
**Primary Dependencies**: Typer, SQLAlchemy  
**Storage**: SQLite 로컬 파일 기반 저장소  
**Testing**: pytest, pytest-cov  
**Target Platform**: 개인 개발자 터미널 환경 (Windows/macOS/Linux)  
**Project Type**: CLI 애플리케이션  
**Performance Goals**: 100개 항목 기준 목록 조회 및 필터링 2초 이내, 1000개 이상 항목 저장/조회 지원  
**Constraints**: 최소 의존성 유지, REST/API/GUI 배제, 로컬 SQLite만 사용, 추상 인터페이스 금지  
**Scale/Scope**: 단일 사용자 개인 생산성 도구, 동시 접근 고려 대상 아님

## Constitution Check

- **I. 레이어 분리**: 비즈니스 로직은 `todo_lib/`에 위치하고, `cli/`는 라이브러리 호출만 수행합니다.
- **II. 테스트 우선**: `tests/`에 pytest 테스트를 먼저 작성하여 구현을 검증합니다.
- **III. 최소 의존성**: 런타임 의존성은 `typer`, `sqlalchemy`로 제한하며, 개발 의존성은 `pytest`, `pytest-cov`로 유지합니다.
- **IV. 단순함 우선**: `ITodoRepository` 같은 추상 인터페이스를 도입하지 않고, 간단한 클래스와 함수로 구현합니다.
- **V. CLI도구 구현**: `todo` 명령어만 제공하고 REST/API/GUI는 배제합니다.

이 계획은 Constitution 원칙을 충족하며, 별도의 위배 항목은 없습니다.

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-app/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── cli-commands.md
└── spec.md
```

### Source Code (repository root)

```text
todo_lib/
├── __init__.py
├── models.py
├── storage.py
└── service.py

cli/
├── __init__.py
└── main.py

tests/
├── conftest.py
├── test_add.py
├── test_list.py
├── test_done.py
└── test_delete.py

pyproject.toml
```

**Structure Decision**: 단일 프로젝트 구조를 선택했습니다. `todo_lib/`는 독립 비즈니스 레이어로 동작하며, `cli/`는 명령어 파싱과 라이브러리 호출에 집중합니다. 테스트 코드와 도구는 `tests/`에서 분리하여 `테스트 우선` 원칙을 지킵니다.

## Complexity Tracking

> 현재 Constitution Check는 위배 항목이 없으므로 복잡성 추적 표는 필요하지 않습니다.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
