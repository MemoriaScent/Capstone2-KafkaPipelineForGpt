# Class
> 객체를 사용한 RPC 예제

## 설명
- RPC는 원격지, 서버에 위치한 함수를 호출하는 기술입니다.
- JSON RPC는 단일 함수만 호출가능 함으로 객체를 사용할 수 없습니다!
- 단일 함수만 호출 가능함으로 객체의 메서드 호출을 희망할 경우 정적 메서드만 정상적으로 실행 가능합니다.
- Python에서 정적 메서드는 `@classmethod`라는 decorator를 명시하여 정의 가능합니다.

## 구성
- `receiver.py`는 함수가 호출되는 서버의 역할을 합니다.
  - 함수 구현체인 객체를 포함합니다.
- `sender.py`는 클라이언트 역할 입니다.

## 테스트
- 터미널을 두개 준비하고 `receiver.py`와 `sender.py`를 각각 실행합니다.
- `sender.py`에서 메시지를 입력합니다.
- 결과를 확인합니다.

## 원리
```
(sender.py) <----> (Kafka) <----> (receiver.py)
```
- `sender.py`에서 함수 호출을 희망하는 요청서를 작성합니다.
- 요청서를 MessageBroker인 Kafka로 전달합니다.
- Kafka는 `receiver.py`로 전달합니다.
- `receiver.py`에서 함수 구현체인 객체를 참조하여 함수를 실행합니다.
- 함수의 반환값을 함수 실행 결과서에 포함하여 Kafka로 전달합니다.
- Kafka는 `sender.py`에서 함수 실행 결과를 알려줍니다.
- `sender.py`에서 실행 결과를 출력 합니다.
