#  -*- coding:utf-8 -*-
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import  (StructField,StringType, IntegerType,StructType)




spark = SparkSession.builder.appName('Basics').getOrCreate()
df = spark.read.json('people.json')

df.show()
df.printSchema()
print(df.columns)

df.describe().show()

# Zmiana typu zmiennej age z longa na integer

data_schema =  [ StructField('age', IntegerType(),True) , StructField('name', StringType(), True)]
final_struct = StructType(fields=data_schema)
df = spark.read.json('people.json', schema = final_struct)
df.printSchema()

 # Pobranie danych z date frame

df.select('age').show() #  (pobranie kolumny age)
df.head(2)[0]  # pobranie 2 wiersszy (w liście)

# Stworzenie nowej kolumny
df.withColumn('newage', df['age'] * 2).show()

# Zmiana nazwy kolumny
df.withColumnRenamed('age', 'my_new_age').show()


# Użycie sql'a
df.createOrReplaceTempView('people')    # stworzenie widoku
results = spark.sql("SELECT * FROM people ")
results.show()


new_results = spark.sql("SELECT * FROM people WHERE  age = 30")
new_results.show()
