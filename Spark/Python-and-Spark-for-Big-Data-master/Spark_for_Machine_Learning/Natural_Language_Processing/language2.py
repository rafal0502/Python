from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('nlp').getOrCreate()

from pyspark.ml.feature import HashingTF, IDF, Tokenizer

sentenceData = spark.createDataFrame([
    (0.0, "Hi I heard about Spark"),
    (0.0, "I wish Java could use case classes"),
    (1.0, "Logistic regression models are neat")
], ["label","sentence"])

sentenceData.show()

tokenizer = Tokenizer(inputCol = 'sentence', outputCol ='words')
words_data = tokenizer.transform(sentenceData)
words_data.show(truncate=False)

hashing_tf = HashingTF(inputCol = 'words', outputCol='rawFeatures')
featurized_data = hashing_tf.tranfsorm(words_data)
idf = IDF(inputCol='rawFeatures', outputCol = 'features')
idf_model = idf.fit(featurized_data)
rescaled_data  = idf_model.transform(featurized_data)
rescaled_data.select('label','features').show(truncate=False)


from pyspark.ml.feature import CountVectorizer

df = spark.createDataFrame ([
    (0, "a,b,c".split(" ")),
    (1,"a b b c a".split(" "))
], ["id", "words"])

df.show()


cv = CountVectorizer(inputCol='words', outputCol = 'features',
                                   vocabSize = 3, minDF = 2.0)

model = cv.fit(df)
result = model.transform(df)
result.show(truncate=False)
