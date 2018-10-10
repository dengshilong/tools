# -*- coding: utf-8 -*-


from confluent_kafka import Consumer, KafkaError


c = Consumer({
    'bootstrap.servers': '127.0.0.1:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest',
})

c.subscribe(['mytopic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break
    offset = msg.offset()
    partition = msg.partition()
    topic = msg.topic()
    value = msg.value()
    print(offset, partition, topic, value, msg.error())
    print('Received message: {}'.format(value))

c.close()