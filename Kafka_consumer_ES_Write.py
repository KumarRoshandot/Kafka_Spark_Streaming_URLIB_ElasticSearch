from pyspark.sql import SparkSession
from json import loads
from Spark_Streaming_Progs.Structured_Stream.API_URL import api_url
from pyspark.sql.functions import to_json, struct, col


#def get_ES_data(api_msg):
def read_stream_data(topic_name):
    df_read = spark.readStream \
                   .format("kafka") \
                   .option("kafka.bootstrap.servers", "localhost:9092")\
                   .option("subscribe", topic_name)\
                   .load()

    #df_read_data = df_read.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING) as words")
    df_read_data_json= df_read.withColumn("json_data", col("value"))

    conf = {"es.resource": "index/type"}
    rdd = sc.newAPIHadoopRDD("org.elasticsearch.hadoop.mr.EsInputFormat", \
                             "org.apache.hadoop.io.NullWritable", "org.elasticsearch.hadoop.mr.LinkedMapWritable",
                             conf=conf)
    es_read_conf = {
        "es.nodes": "localhost",
        "es.port": "9200",
        "es.resource": "titanic/passenger",
        "es.query": q
    }

    es_rdd = sc.newAPIHadoopRDD(
        inputFormatClass="org.elasticsearch.hadoop.mr.EsInputFormat",
        keyClass="org.apache.hadoop.io.NullWritable",
        valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
        conf=es_read_conf)



if __name__ == "__main__":
    spark = SparkSession.builder\
                        .appName("Kafka Streaming") \
                        .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.1') \
                        .config('spark.jars.packages', 'org.elasticsearch.spark.sql.streaming:elasticsearch-hadoop-6.8.0') \
                        .config('es.index.auto.create', 'true')\
                        .getOrCreate()

    sc = spark.sparkContext()

    #topic name and API info
    topic, api = api_url()

    #Reading stream data for topic from kafka producer
    read_stream_data(topic)


