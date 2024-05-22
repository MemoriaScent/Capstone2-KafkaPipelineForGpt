import bcrypt
from rpc.message_broker import MessageBroker


broker = MessageBroker("localhost:9092")


class UserMethods:
    @staticmethod
    def create(username: str, password: str, level: int):
        data = {
            "username": username,
            "encrypted_password": bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
            "level": level
        }
        broker.rpc("data", "append", "users", data)

    @staticmethod
    def info(username: str):
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass



def main():
    broker.serve(UserMethods, "user")


if __name__ == "__main__":
    main()
