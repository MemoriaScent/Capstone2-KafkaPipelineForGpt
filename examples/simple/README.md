# Simple
> 아주 단순한 RPC 예제

## 설명
- RPC는 원격지, 서버에 위치한 함수를 호출하는 기술입니다.

## 구성
- `methods.py`는 호출하고 싶은 함수가 존재합니다.
- `receiver.py`는 함수가 호출되는 서버의 역할을 합니다.
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
- `receiver.py`에서 함수 구현체인 `methods.py`를 참조하여 함수를 실행합니다.
- 함수의 반환값을 함수 실행 결과서에 포함하여 Kafka로 전달합니다.
- Kafka는 `sender.py`에서 함수 실행 결과를 알려줍니다.
- `sender.py`에서 실행 결과를 출력 합니다.
