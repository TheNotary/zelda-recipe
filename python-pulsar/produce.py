import pulsar
import os

protocol_url = os.getenv('PROTOCOL_URL', 'pulsar://localhost:6650')

topic_name = "my-topicc"
topic_name = "persistent://public/default/my-topicc"

def producer_routine(producer):
    while input() != 'quit':
        print("writing to pulsar")
        for i in range(160):
            producer.send(('Hello-%d' % i).encode('utf-8'))
        producer.flush()
        #stats = producer.getStats()
        #print("getNumAcksReceived" + stats.getNumAcksReceived())


def consumer_routine(consumer):
    while True:
        msg = consumer.receive()
        print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
        consumer.acknowledge(msg)



client = pulsar.Client(protocol_url)
producer = client.create_producer(topic_name,
                                  block_if_queue_full=True,
                                  batching_enabled=True,
                                  batching_max_publish_delay_ms=10)

producer_routine(producer)


client.close()
