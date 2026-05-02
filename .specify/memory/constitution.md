<!--
Version change: old → new: 1.0.0 → 1.1.0
List of modified principles (old title → new title if renamed): Principles 1-3 unchanged, Principles 4-5 added
Added sections: None
Removed sections: None
Templates requiring updates (✅ updated / ⚠ pending): None
Follow-up TODOs if any placeholders intentionally deferred: None
-->
# ToDo CLI App Constitution

## Core Principles

### I. 레이어 분리
비즈니스 로직은 사용자 인터페이스와 분리된 독립 레이어에서 구현한다.

### II. 테스트 우선
테스트 코드를 구현 코드보다 먼저 작성한다.
테스트 없는 구현 코드는 허용하지 않는다.

### III. 최소 의존성
외부 패키지 설치 전 반드시 필요성을 검토한다.
불필요한 의존성은 추가하지 않는다.

### IV. 단순함 우선
지금 당장 필요하지 않은 추상화 레이어는 만들지 않는다.
명확하고 직접적인 구현을 선호한다.

### V. CLI도구 구현
이 프로젝트는 터미널 CLI 도구를 만든다.
REST API서버, GUI, 웹 인터페이스는 이 프로젝트의 범위 밖이다.

## Governance

Constitution은 모든 다른 관행보다 우선한다. 수정은 문서화, 승인, 마이그레이션 계획을 요구한다.

모든 PR/리뷰는 준수 여부를 검증해야 한다. 복잡성은 정당화되어야 한다.

**Version**: 1.1.0 | **Ratified**: 2026-05-02 | **Last Amended**: 2026-05-02
