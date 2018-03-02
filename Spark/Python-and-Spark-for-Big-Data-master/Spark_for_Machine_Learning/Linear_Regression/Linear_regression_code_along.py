from  pyspark.sql import SparkSession

spark = SparkSession.builder.appName('lr_example').getOrCreate()

from pyspark.ml.regression import LinearRegression


data = spark.read.csv('Ecommerce_Customers.csv', inferSchema= True, header = True)
data.printSchema()

for item in data.head(1)[0]:
    print (item)


from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

print(data.columns)

# tworzymy wektor danych
assembler = VectorAssembler(inputCols =[ 'Avg Session Length', 'Time on App', 'Time on Website', 'Length of Membership'],
                                                outputCol = 'features')
output = assembler.transform(data)
output.printSchema()

print(output.head(1))

final_data = output.select('features', 'Yearly Amount Spent')

final_data.show()


train_data, test_data = final_data.randomSplit([0.7, 0.3])
test_data.describe().show()


lr = LinearRegression(labelCol = 'Yearly Amount Spent')
lr_model = lr.fit(train_data)
test_results = lr_model.evaluate(test_data)
test_results.residuals.show()        # to różnica miedzy wartościami przewidywanymi a tymi faktycznymi



print(test_results.rootMeanSquaredError)    # różnica między przewidywanymi a faktycznymi

final_data.describe().show()

print(test_results.r2)          #  w ilu procentach jest 'wyjasnoina? ' zmiennosc danych


###########################

unlabeled_data = test_data.select('features')
unlabeled_data.show()

predictions = lr_model.transform(unlabeled_data)
predictions.show()
