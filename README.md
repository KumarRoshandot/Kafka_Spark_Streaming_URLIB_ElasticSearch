# Kafka_Spark_Streaming_Usecase
- This is a Use Case done for integration of Kafka with Spark Streaming
- Build Kafka Producer Homemade fetching Data from API (URLLIB).
- Build Consumer as Spark Streaming, Do something with data and write it to ElasticSearch

---
## Requirement Flow
- The Story is to Get The Data from WorldClock API' each Second ( It can be any other API's for Use Case)
- The Data from the API will be Fed to Kafka Producer
- Once the Producer Start sending data as Stream , the Consuming Side will be either Spark Streaming or Kafka Consumer
- The Spark Streaming i will be using for Consuming Data is through Structured Streaming ( Spark 2.4.3)
- The Kafka Consumer code is also there for further Changes.
- The Idea for Now is to Save the data in NoSql DB ( MongoDB for Now) 
- I have Run this in Pycharm Editor in Windows 10.

---
### prerequisite for the code to Execute :-
 
1) IF working in Shell then need to have Java(8) , Spark (2.4.3) installed 
2) If Using some Editor ( Pycharm or Eclipse ) then download PYSPARK, Kafka Library on Your Project Editor

---
### Steps to Execute all :-
1)  Download all files and keep it in one folder( Package)
2)  Run kafka_producer.py in one terminal or in some Editor( Pycharm)
3)  The Kafka Producer has started runnning and it will send the data from world clock API to localhost:9092
4)  Then to consume that data and do something with it then we have to run Consumer side code .
-   kafka_consumer_ES_Write.py ( Spark Streaming will consume, Here Data will be converted to DataFrames and Write data to MongoDB)
-   kafka_consumer.py ( This is Kafka Util , which u can consume data and write Python code to Write it anywhere , the data will be a python Object )
	  
	  
---
Construction in progress....	  
