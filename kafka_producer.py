from time import sleep
from json import dumps
from kafka import KafkaProducer
from Get_api_data import get_api
from API_URL import api_url

def connect_kafka():
    # topic name and API info
    topic, api = api_url()

    # connection with message broker
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda m: dumps(m).encode('ascii'))
    get_api_new = get_api()
    return producer, get_api_new, topic, api

def on_send_success(record_metadata):
    print("topic name: " + record_metadata.topic)
    print("number of partition: " + record_metadata.partition)
    print("offset: " + record_metadata.offset)


def on_send_error(record_exception):
    print("Exception : " + record_exception)


if __name__ == "__main__":

    producer, get_api_new, topic, api = connect_kafka()
    while True:
        message_data = get_api_new.get_data(api)
        # print(message_data)

        producer.send(topic, key=b'message', value=message_data) \
            .add_callback(on_send_success) \
            .add_errback(on_send_error)
        producer.flush()
        sleep(5)
