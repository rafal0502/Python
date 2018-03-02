from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('mytree').getOrCreate()


from pyspark.ml import Pipeline
from pyspark.ml.classification import  (RandomForestClassifier, GBTClassifier,DecisionTreeClassifier)


data = spark.read.format('libsvm').load('sample_linear_regression_data.txt')

data.show()
