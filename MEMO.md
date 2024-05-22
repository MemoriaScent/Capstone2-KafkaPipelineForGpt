# References

## JSON RPC 2.0

https://velog.io/@dohpkim/JSON-RPC-2.0-spec#51-%EC%97%90%EB%9F%AC-%EA%B0%9D%EC%B2%B4

https://www.jsonrpc.org/specification

## Kafka

https://dev-records.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-Kafka-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%98%88%EC%A0%9C

## Kafka Security

https://zeroco.tistory.com/115
https://always-kimkim.tistory.com/entry/kafka101-security

## Python asyncio

https://dojang.io/mod/page/view.php?id=2469

## Python typing, decorator

https://medium.com/@ashley.e.shultz/type-hinting-a-decorator-that-changes-function-arguments-d603a6631c3c

https://sjquant.tistory.com/69

# Data Service

## KV

```
data set "key" "value"
data get "key"
data delete "key"
data key "startwith" "value"
```

## Docs, RDB

```
data set "users" []
data append "users" { "username": "", "password": "" }
data set "users.#100" { "username": "", password: "" }

data key "users" { "username": "user1" } # return key from users
data key "users.#" { "username": "user1" }

data get "users" # all
data get "users.#0" # with index
data get "users.#1.#2.#2"
data get "users.#10.username"
data get "users.#0-100"
data get "users.#10-100.username"
data get "users.#10-100.#2.#3-5"

data get "users" { "username": "user1" } # with filter
data get "users.#.username" {"username": "user%"}
data get "users.#.tags.#.name" {"tags": ["test"]}

-----------------------------------------------------------
data delete ...
```

```
{
  "a": {
    "b": [1, 2, 3]
  }
}


a --> { "b": [1, 2, 3] }
a.b --> [1, 2, 3]
a.b.0 --> 1
```
