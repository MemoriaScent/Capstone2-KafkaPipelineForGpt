import msgpack
from kafka import KafkaProducer

producer = KafkaProducer(
    compression_type=None,
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: msgpack.packb(x, use_bin_type=True),
)

future = producer.send("test", value={"hello": "world"})
producer.flush()
print(future.get())
