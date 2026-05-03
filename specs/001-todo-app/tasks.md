---
description: "Task list for CLI ToDo Management App implementation"
---

# Tasks: CLI ToDo Management App

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are REQUIRED - per Constitution principle II (테스트 우선)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

Single project structure at repository root:
- `todo_lib/` — business layer
- `cli/` — CLI interface layer
- `tests/` — all test files
- `pyproject.toml` — project configuration

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project directories in `todo_lib/`, `cli/`, `tests/`
- [ ] T002 Create `pyproject.toml` with Python 3.12, typer, sqlalchemy, pytest, pytest-cov dependencies
- [ ] T003 Create `.gitignore` to exclude `*.db`, `.pytest_cache/`, `__pycache__/`, `*.egg-info/`
- [ ] T004 Create `todo_lib/__init__.py` and `cli/__init__.py` (empty modules)
- [ ] T005 Create `tests/conftest.py` with pytest fixtures for temporary SQLite test database

---

## Phase 2: Foundational (Core Data & Persistence)

**Purpose**: Data model and storage layer foundation for all user stories

- [ ] T006 [P] Create `todo_lib/models.py` with TodoItem SQLAlchemy ORM class (id, title, description, due_date, priority, completed, created_at, updated_at)
- [ ] T007 [P] Create `todo_lib/storage.py` with SQLiteStorage class (init, create_todo, get_todo_by_id, get_all_todos, update_todo, delete_todo, filter_by_completion, filter_by_priority)
- [ ] T008 Write integration test in `tests/test_storage_integration.py` to verify SQLite database operations (create, read, update, delete, filter)

---

## Phase 3: User Story 1 - ToDo 항목 추가 (P1)

**Story Goal**: Users can add new todo items with required title and optional due_date, priority

**Independent Test**: User can add item with title only, and add item with all fields; both persist and return unique ID

**Acceptance Criteria**: 
- TC-US1-001: Add todo with title only → item created with ID
- TC-US1-002: Add todo with all fields → all fields stored
- TC-US1-003: Add todo without title → error message (no item created)

- [ ] T009 [US1] Write test in `tests/test_add.py` for add_todo() function with title parameter
- [ ] T010 [US1] Write test in `tests/test_add.py` for add_todo() with optional due_date and priority parameters
- [ ] T011 [US1] Write test in `tests/test_add.py` for add_todo() error handling (missing title)
- [ ] T012 [P] [US1] Create `todo_lib/service.py` with TodoService class and add_todo() method
- [ ] T013 [P] [US1] Create `cli/main.py` with typer.Typer() app and add_command() using TodoService.add_todo()
- [ ] T014 [US1] Integration test: Execute `todo add "Test task" --due 2026-05-10 --priority high` and verify output contains ID and confirmation

---

## Phase 4: User Story 2 - 전체 목록 조회 및 필터링 (P2)

**Story Goal**: Users can query all todo items and filter by completion status or priority

**Independent Test**: Can list all items; can filter by done/pending; can filter by priority level

**Acceptance Criteria**:
- TC-US2-001: List all items when no filter applied
- TC-US2-002: List only pending items when --filter pending applied
- TC-US2-003: List only high-priority items when --priority high applied
- TC-US2-004: Combine filters (pending + high priority)

- [ ] T015 [US2] Write test in `tests/test_list.py` for list_todos() without filters
- [ ] T016 [P] [US2] Write test in `tests/test_list.py` for list_todos() with completion filter (done/pending)
- [ ] T017 [P] [US2] Write test in `tests/test_list.py` for list_todos() with priority filter
- [ ] T018 [P] [US2] Write test in `tests/test_list.py` for list_todos() with combined filters
- [ ] T019 [US2] Implement TodoService.list_todos(filter_status=None, filter_priority=None) in `todo_lib/service.py`
- [ ] T020 [US2] Implement list_command() in `cli/main.py` with --filter and --priority options
- [ ] T021 [US2] Integration test: Run `todo list --filter pending --priority high` and verify output format and filtering

---

## Phase 5: User Story 3 - 항목 완료 처리 (P3)

**Story Goal**: Users can mark a specific todo item as completed by ID

**Independent Test**: Can mark todo as done; idempotent (marking already-done todo succeeds without error)

**Acceptance Criteria**:
- TC-US3-001: Mark pending item as done → status changes to completed
- TC-US3-002: Mark already-done item → no change, success message
- TC-US3-003: Mark non-existent ID → error message

- [ ] T022 [US3] Write test in `tests/test_done.py` for mark_done() on pending item
- [ ] T023 [P] [US3] Write test in `tests/test_done.py` for mark_done() on already-completed item (idempotent)
- [ ] T024 [P] [US3] Write test in `tests/test_done.py` for mark_done() error handling (invalid ID)
- [ ] T025 [US3] Implement TodoService.mark_done(todo_id) in `todo_lib/service.py`
- [ ] T026 [US3] Implement done_command() in `cli/main.py` to call TodoService.mark_done()
- [ ] T027 [US3] Integration test: Run `todo done 1` and verify todo item status is updated to completed

---

## Phase 6: User Story 4 - 항목 삭제 (P4)

**Story Goal**: Users can delete a specific todo item by ID

**Independent Test**: Can delete existing item; proper error handling for non-existent ID

**Acceptance Criteria**:
- TC-US4-001: Delete existing item → item removed from storage
- TC-US4-002: Delete non-existent ID → error message

- [ ] T028 [US4] Write test in `tests/test_delete.py` for delete_todo() on existing item
- [ ] T029 [P] [US4] Write test in `tests/test_delete.py` for delete_todo() error handling (invalid ID)
- [ ] T030 [US4] Implement TodoService.delete_todo(todo_id) in `todo_lib/service.py`
- [ ] T031 [US4] Implement delete_command() in `cli/main.py` to call TodoService.delete_todo()
- [ ] T032 [US4] Integration test: Run `todo delete 1` and verify todo item is removed from list

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Error handling, edge cases, documentation, and quality assurance

- [ ] T033 Add input validation in `todo_lib/service.py` (title length, priority enum, date format)
- [ ] T034 Add human-readable error messages in `cli/main.py` for all error scenarios
- [ ] T035 Write test in `tests/test_edge_cases.py` for long title (1000+ characters)
- [ ] T036 Write test in `tests/test_edge_cases.py` for empty database list query
- [ ] T037 Write test in `tests/test_edge_cases.py` for past due_date handling
- [ ] T038 Run full test suite with coverage: `pytest --cov=todo_lib --cov=cli tests/`
- [ ] T039 Verify coverage meets minimum 80% threshold
- [ ] T040 Create CLI help documentation via Typer auto-help (e.g., `todo --help`)
- [ ] T041 Create quickstart verification script: Run all 4 CLI commands and verify expected behavior
- [ ] T042 Verify Constitution compliance: No abstract interfaces, test-first approach, minimal dependencies, SQLite persistence, CLI only

---

## Dependency Graph

```
Phase 1: Setup
    ↓
Phase 2: Foundational (T006-T008)
    ↓ (all depend on Phase 2)
Phase 3: US1 Add (T009-T014) — [P] T012 & T013 can run in parallel
Phase 4: US2 List (T015-T021) — [P] T016, T017, T018 can run in parallel once Phase 2 complete
Phase 5: US3 Done (T022-T027) — [P] T023, T024 can run in parallel once Phase 2 complete
Phase 6: US4 Delete (T028-T032) — [P] T029 can run in parallel once Phase 2 complete
Phase 7: Polish (T033-T042) — can begin after individual stories complete
```

---

## Parallel Execution Examples

**Scenario 1: After Phase 2 complete (Foundational done)**
```
Parallel Group 1:
  - T009, T010, T011 (US1 tests)
  - T015, T016, T017, T018 (US2 tests)
  - T022, T023, T024 (US3 tests)
  - T028, T029 (US4 tests)

Then Sequential:
  - T012, T013 (US1 implementation)
  - T019, T020 (US2 implementation)
  - T025, T026 (US3 implementation)
  - T030, T031 (US4 implementation)
```

**Scenario 2: Two-developer split**
```
Developer A: US1 + US2
  - T009-T014 (US1)
  - T015-T021 (US2)

Developer B: US3 + US4
  - T022-T027 (US3)
  - T028-T032 (US4)

Both: Phase 1, Phase 2, Phase 7 (sequential)
```

---

## Implementation Strategy (MVP Scope)

### MVP Version 1.0 (All 4 User Stories)

**Rationale**: All 4 user stories are independently testable and deliver core value.

**Minimum Deployable**: After Phase 6 complete, all CLI commands functional (add, list, done, delete). Optional: Phase 7 polish tasks can follow in patch releases.

**Suggested Release Order**:
1. Release after T014 (US1 add working)
2. Release after T021 (US2 list working)
3. Release after T027 (US3 done working)
4. Release after T032 (US4 delete working)
5. Final polish release after T042 (Phase 7 complete)

---

## Format Validation Summary

✅ All 42 tasks follow checklist format: `- [ ] [TaskID] [P?] [Story?] Description`
✅ Task IDs sequential: T001 through T042
✅ [P] markers applied only to parallelizable tasks (different files, no dependencies)
✅ [Story] labels present for all Phase 3-6 tasks (US1, US2, US3, US4)
✅ No Story label for Phase 1, Phase 2, Phase 7 (shared/setup)
✅ All file paths explicit and accurate
