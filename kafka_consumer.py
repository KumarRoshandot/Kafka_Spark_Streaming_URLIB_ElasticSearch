from kafka import KafkaConsumer
from json import loads
from Spark_Streaming_Progs.Structured_Stream.API_URL import api_url
from pyspark.sql.functions import to_json, struct, col


def read_stream_data(consumer):
    for message in consumer:
        message = loads(message.value)
        #Elastic search data in { "id: { the rest of your json}} form
        print(message['results'][0]['gender'])

if __name__ == "__main__":
    # topic name and API info
    topic, api = api_url()

    consumer = KafkaConsumer(
                            topic,
                            bootstrap_servers=['localhost:9092'],
                            auto_offset_reset='earliest',
                            enable_auto_commit=True,
                            group_id='my-group',
                            value_deserializer=lambda x: loads(x.decode('ascii'))
                            )

    #Reading stream data for topic from kafka producer
    read_stream_data(consumer)




