from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('log_reg').getOrCreate()

from pyspark.ml.classification import LogisticRegression

my_data = spark.read.format('libsvm').load('sample_libsvm_data.txt')
my_data.show()

my_log_reg_model = LogisticRegression()
fitted_logreg = my_log_reg_model.fit(my_data)
log_summary = fitted_logreg.summary
log_summary.predictions.printSchema()

log_summary.predictions.show()
lr_train,lr_test = my_data.randomSplit([0.7,0.3])
final_model = LogisticRegression()
fit_final=final_model.fit(lr_train)
predictions_and_labels = fit_final.evaluate(lr_test)
predictions_and_labels.predictions.show()

from pyspark.ml.evaluation import (BinaryClassificationEvaluator,
                                                        MulticlassClassificationEvaluator)


my_eval = BinaryClassificationEvaluator()
my_final_roc = my_eval.evaluate(predictions_and_labels.predictions)
print(my_final_roc)
