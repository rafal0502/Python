from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('cruise').getOrCreate()
df = spark.read.csv('cruise_ship_info.csv', inferSchema = True, header = True)
df.printSchema()

#print(df.head(5))

for ship in df.head(5):
    print(ship)
    print('\n')


df.groupBy('Cruise_line').count().show()

from pyspark.ml.feature import StringIndexer

indexer = StringIndexer(inputCol='Cruise_line',outputCol='cruise_cat')
indexed=indexer.fit(df).transform(df)
print(indexed.head(5))


from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

print(indexed.columns)

# bez 2 pierwszych bo ship_name bez znaczenia a crusie_line przekonwertowane do cruise_cat  i crew bo to będziemy przewidywac

assembler = VectorAssembler(inputCols= ['Age','Tonnage', 'passengers', 'length', 'cabins', 'passenger_density', 'crew', 'cruise_cat'], outputCol='features')
output = assembler.transform(indexed)
output.select('features','crew').show()

final_data = output.select(['features','crew'])
train_data, test_data = final_data.randomSplit([0.7,0.3])
train_data.describe().show()
test_data.describe().show()

# budowanie budelu regresji


from pyspark.ml.regression import LinearRegression

ship_lr = LinearRegression(labelCol='crew')
trained_ship_model = ship_lr.fit(train_data)
ship_results = trained_ship_model.evaluate(test_data)
print(ship_results.rootMeanSquaredError)
train_data.describe().show()

print(ship_results.r2)
print(ship_results.meanAbsoluteError)


# sprawdzanie silnie skorelowanych kolumn
from pyspark.sql.functions  import corr

df.describe().show()

df.select(corr('crew','passengers')).show()
