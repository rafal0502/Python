import findspark

findspark.init('/home/rafal/spark-2.1.0-bin-hadoop2.7')


from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc

# Can only run this once.
sc = SparkContext()

ssc = StreamingContext(sc, 10)
sqlContext = SQLContext(sc)

socket_stream = ssc.socketTextStream("127.0.0.1", 9997)

lines = socket_stream.window(20)

from collections import namedtuple
fields = ("tag", "count")
Tweet = namedtuple( 'Tweet' , fields)

#Use Parenthesis for multiple lines or use | .
(lines.flatMap( lambda text: text.split(  " " )  ) # Splits to a list
.filter ( lambda word : word.lower().startswith("#") ) # Checks for hashtag
.map( lambda word: ( word.lower() , 1) ) # Lower cases the word
.reduceByKey ( lambda a, b : a + b) # Reduces
.map( lambda rec: Tweet ( rec[0], rec[1] ) ) # Stores in a Tweet Object
.foreachRDD( lambda rdd: rdd.toDF().sort ( desc("count") ) # Sorts
.limit(10).registerTempTable("tweets") ) ) # Register to a table


ssc.start()
