import pulsar
import os
import time

protocol_url = os.getenv('PROTOCOL_URL', 'pulsar://localhost:6650')


client = pulsar.Client(protocol_url)
#producer = client.create_producer('my-topic')

consumer = client.subscribe('my-topicc', 'my-subscription')

def producer_routine(client, producer):
    for i in range(10):
        producer.send(('Hello-%d' % i).encode('utf-8'))



def consumer_routine(consumer):
    while True:
        msg = consumer.receive()
        print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
        consumer.acknowledge(msg)
        #time.sleep(2)



#producer_routine(client, producer)

consumer_routine(consumer)



client.close()
