from rpc.message_broker import MessageBroker


class Methods:
    @classmethod
    def echo(cls, text):
        return f"RPC {text}!"


broker = MessageBroker("localhost:9092")
# methods 모듈은 내부에 echo 함수를 가지고 있음
broker.serve(Methods, "test")
