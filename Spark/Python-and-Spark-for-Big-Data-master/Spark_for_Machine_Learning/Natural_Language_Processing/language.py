from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('nlp').getOrCreate()

from pyspark.ml.feature import Tokenizer, RegexTokenizer

from pyspark.sql.functions import  col,udf
from  pyspark.sql.types import IntegerType

sen_df = spark.createDataFrame ([
                (0, 'Hi I heard about Spyrk'),
                (1, 'I wish java colud use case classes'),
                (2, 'Logistic regression, models,are,neat')
                ],['id', 'sentence'])

sen_df.show()

tokenizer = Tokenizer(inputCol = 'sentence', outputCol = 'words')
regex_tokenizer = RegexTokenizer(inputCol = 'sentence', outputCol ='words',
                                                        pattern = '\\W')

count_tokens = udf(lambda words: len(words), IntegerType())
tokenized = tokenizer.transform(sen_df)

tokenized.show()

tokenized.withColumn('tokens', count_tokens(col('words'))).show()

rg_tokenized = regex_tokenizer.tranfsorm(sen_df)
rg_tokenized.withColumn('tokens', count_tokens(col('words'))).show()


from pyspark.ml.feature import StopWordsRemover

sentenceDataFrame = spark.createDataFrame([
                (0, ['I', 'saw', 'the', 'green', 'horse']),
                (1,['Mary', 'had', 'a', 'little', 'lamb'])
], ['id', 'tokens'])

remover = StopWordsRemover(inputCol = 'tokens', outputCol = 'filtered')
remover.transform(sentenceDataFrame).show()


# n-gram pomaga znalezc zaleznosci miedzy kilkoma slowami

from pyspark.ml.feature import NGram

wordDataFrame = spark.createDataFrame([
    (0, ["Hi", "I", "heard" , "about", "Spark"]),
    (1, ["I", "wish", "Java", "could", "use", "case", "classes"]),
    (2,["Logistic", "regression", "models", "are", "neat"])
], ["id", "words" ])


ngram = NGram(n=2, inputCol = 'words', outputCol = 'grams')
ngram.transform(wordDataFrame).select('grams').show(truncate=False)
