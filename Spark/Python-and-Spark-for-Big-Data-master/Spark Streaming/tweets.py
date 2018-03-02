from pyspark import SparkContext

from pyspark.streaming import StreamingContext
sc  = SparkContext('local[2]', 'NetworkWordCount')
ssc = StreamingContext(sc, 1)

lines  = ssc.socketTextStream('localhost', 9997)

words = lines.flatMap(lambda line: line.split(' '))

pairs = words.map(lambda word: (word,1))
word_counts = pairs.reduceByKey(lambda num1, num2: num1 + num2)

word_counts.pprint()
ssc.start()
