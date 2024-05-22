import msgpack
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    group_id="default",
    value_deserializer=lambda x: msgpack.unpackb(x, raw=False),
    consumer_timeout_ms=10,
)

consumer.subscribe("test")
print(consumer.subscription())

try:
    while True:
        for message in consumer:
            print(message)
            consumer.commit()
except KeyboardInterrupt:
    pass
