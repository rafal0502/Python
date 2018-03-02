from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('nlp').getOrCreate()

data = spark.read.csv('SMSSpamCollection', inferSchema=True,
                                   sep='\t')

data = data.withColumnRenamed('_c0', 'class').withColumnRenamed('_c1','text')

data.show()


from pyspark.sql.functions import  length


# sprawdzamy jaka długosc wyrazu w kolumnie text
data = data.withColumn('length', length(data['text']))
data.show()


# sprawdzam srednia dlugosc tekstu w kolumnie w zlaznosci czy spam czy ham (groupBy kolumna class)
data.groupBy('class').mean().show()


from pyspark.ml.feature import (Tokenizer, StopWordsRemover,
                                                    CountVectorizer,IDF,StringIndexer)

# tworzy ze slow listę slow
tokenizer = Tokenizer(inputCol= 'text', outputCol = 'token_text')

# usuwa niepotrzebne slowa
stop_remove = StopWordsRemover(inputCol = 'token_text',outputCol = 'stop_token')

count_vec = CountVectorizer(inputCol = 'stop_token', outputCol = 'c_vec')

# liczymy jakas czestotliwosc
idf = IDF(inputCol='c_vec', outputCol = 'tf_idf')

# konwertujemy do liczb
ham_spam_to_numeric = StringIndexer(inputCol = 'class', outputCol='label')

from pyspark.ml.feature import VectorAssembler

clean_up  = VectorAssembler(inputCols=['tf_idf', 'length'], outputCol ='features')

# budujemy model

from pyspark.ml.classification import  NaiveBayes

nb = NaiveBayes()

from pyspark.ml import Pipeline
data_prep_pipe = Pipeline(stages=[ham_spam_to_numeric, tokenizer,
                                                         stop_remove, count_vec, idf,clean_up])

cleaner = data_prep_pipe.fit(data)
clean_data = cleaner.transform(data)

clean_data = clean_data.select('label', 'features')
clean_data.show()

training, test = clean_data.randomSplit([0.7, 0.3])
spam_detector = nb.fit(training)

data.printSchema()

test_results = spam_detector.transform(test)
test_results.show()

from pyspark.ml.evaluation import MulticlassClassificationEvaluator

acc_eval = MulticlassClassificationEvaluator()
acc = acc_eval.evaluate(test_results)
print('ACC of NB Model')
print(acc)
