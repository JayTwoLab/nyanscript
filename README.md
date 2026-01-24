
# 🐾 냥스크립트 (`NyanScript`)

> **"집사가 코드를 짜면, 고양이가 실행한다냥!"** > **The world's cutest esoteric programming language.**

냥스크립트(NyanScript)는 고양이의 습성을 모티브로 한 한국어 기반의 난해한 프로그래밍 언어(Esoteric Language)입니다.

Python을 기반으로 동작하며, 딱딱한 영어 문법 대신 귀여운 고양이 용어로 코딩할 수 있습니다.

<br />

## ✨ 특징 (Features)

* **고양이 친화적 문법:** `while` 대신 `꾹꾹이`, `print` 대신 `야옹`을 사용합니다.
* **파이썬 호환:** `.nyan` 파일을 파이썬 코드로 변환(Transpile)하여 실행하므로, 파이썬의 모든 라이브러리(`import random`, `time` 등)를 사용할 수 있습니다.
* **쉬운 난이도:** 구조는 파이썬과 유사하여 초보 집사도 쉽게 배울 수 있습니다.

<br />

## 📦 설치 및 실행 방법 (Installation & Usage)

### 1. 필수 조건

* Python 3.x 가 설치되어 있어야 합니다.

<br />

### 2. 실행 방법

프로젝트 폴더에 `nyan.py` (인터프리터)와 `.nyan` (소스 코드) 파일이 있어야 합니다.

```bash
# 기본 실행 명령어
python nyan.py [파일이름.nyan]

```

**예시:**

```bash
python nyan.py hello.nyan

```

<br />

---

## 📚 문법 가이드 (Syntax Guide)

냥스크립트는 **들여쓰기(Indentation)**가 매우 중요합니다. 블록(`{ }`)을 사용할 때 들여쓰기 줄을 잘 맞춰주세요.

| 기능 | 냥스크립트 (Keyword) | 파이썬 (Python) | 설명 |
| --- | --- | --- | --- |
| **시작** | `기지개 { ... }` | `if __name__ == "__main__":` | 프로그램의 시작점입니다. |
| **종료** | `식빵굽기` | `pass` | 프로그램의 끝을 알립니다. |
| **변수** | `박스 [이름] = [값]` | `[이름] = [값]` | 변수를 선언합니다. |
| **출력** | `야옹(...)` | `print(...)` | 화면에 내용을 출력합니다. |
| **입력** | `쫑긋(...)` | `input(...)` | 사용자의 입력을 받습니다. |
| **반복** | `꾹꾹이 (조건) { ... }` | `while (조건):` | 조건이 참일 동안 반복합니다. |
| **조건** | `간식주면 (조건) { ... }` | `if (조건):` | 조건이 참이면 실행합니다. |
| **그 외** | `아니면 { ... }` | `else:` | 조건이 거짓이면 실행합니다. |
| **참/거짓** | `잡았다` / `놓쳤다` | `True` / `False` | 불리언(Boolean) 값입니다. |
| **에러** | `하악질(...)` | `raise Exception(...)` | 강제로 에러를 발생시킵니다. |
| **대기** | `낮잠(초)` | `time.sleep(초)` | 지정한 시간만큼 멈춥니다. |
| **주석** | `그루밍: ...` | `# ...` | 실행되지 않는 설명글입니다. |

<br />

---

## 🐈 코드 예제 (Examples)

### 1. Hello World (안녕 세상아)

```javascript
기지개 {
    야옹("안녕? 나는 코딩하는 고양이다냥!")
} 식빵굽기

```

<br />

### 2. 츄르 먹기 (반복문)

```javascript
기지개 {
    박스 츄르 = 3
    
    꾹꾹이 (츄르 > 0) {
        야옹("냠냠... 남은 츄르: ", 츄르)
        츄르 = 츄르 - 1
    }
    
    야옹("꺼억! 잘 먹었다냥.")
} 식빵굽기

```

---

<br />

## 🛠️ 개발 환경 구조 (File Structure)

```text
📂 Project_Nyan
├── 📜 README.md       # 프로젝트 설명서
├── 🐍 nyan.py         # 냥스크립트 인터프리터 (Core)
├── 🐱 hello.nyan      # 예제 코드
└── 🐱 fibo.nyan       # 예제 코드

```

<br />

## ⚖️ 라이선스 (License)

이 프로젝트는 **Mozilla Public License Version 2.0 (MPL 2.0)** 을 따릅니다.

> This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at [https://mozilla.org/MPL/2.0/](https://mozilla.org/MPL/2.0/).

소스 코드를 수정하여 배포할 경우, 해당 파일의 소스 코드를 공개해야 합니다. 단, 실행 파일 형태의 배포나 다른 라이선스를 가진 코드와 결합하여 사용하는 것은 더 자유롭습니다.

---

Made with 🐟 and 🧶 by j2doll
