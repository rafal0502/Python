from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('lrex').getOrCreate()

from pyspark.ml.regression import LinearRegression

training = spark.read.format('libsvm').load('sample_linear_regression_data.txt')
training.show()

lr = LinearRegression(featuresCol='features', labelCol = 'label', predictionCol='prediction')

lrModel = lr.fit(training)

print(lrModel.coefficients)
print(lrModel.intercept)


training_summary = lrModel.summary
# print(training_summary.rootMeanSqueredError)


# Dzielenie zbioru ne treningowy i testowy

all_data = spark.read.format('libsvm').load('sample_linear_regression_data.txt')
split_object = all_data.randomSplit([0.7,0.3])


train_data, test_data = all_data.randomSplit([0.7,0.3])
train_data.describe().show()
test_data.describe().show()


correct_model = lr.fit(train_data)

test_results = correct_model.evaluate(test_data)
test_results.residuals.show()

# na danych bez label'a

unlabeled_data = test_data.select('features')

predictions = correct_model.transform(unlabeled_data)
predictions.show()
