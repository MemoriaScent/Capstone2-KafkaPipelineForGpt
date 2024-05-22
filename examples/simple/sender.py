from rpc.message_broker import MessageBroker

broker = MessageBroker("localhost:9092")
while True:
    # test에 있는 echo 함수를 파라미터와 함께 호출하고 결과를 출력
    param = input("text: ")
    broker.rpc_print("test", "echo", param)
