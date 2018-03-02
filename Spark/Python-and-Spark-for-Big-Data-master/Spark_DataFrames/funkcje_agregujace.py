from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('aggs').getOrCreate()

df = spark.read.csv('sales_info.csv', inferSchema = True, header = True)

df.show()

df.printSchema()

df.groupBy("Company ")

df.groupBy('Company').mean().show()


df.groupBy('Company').sum().show()

df.groupBy('Company').max().show()
df.groupBy('Company').min().show()
df.groupBy('Company').count().show()


df.agg({ 'Sales' : 'max' }).show()

# To samo co użycie df.groupBy('Company').max().show()
group_data = df.groupBy("Company")
group_data.agg({'Sales':'max'}).show()


from pyspark.sql.functions import   countDistinct, avg, stddev


df.select(countDistinct('Sales')).show()

df.select(avg('Sales').alias('Average Sales')).show()


df.select(stddev('Sales')).show()


from pyspark.sql.functions import format_number

sales_std = df.select(stddev("Sales").alias('std'))
sales_std.select(format_number('std',2)).show()

df.show()
df.orderBy("Sales").show()

# wpisujemy aktualną kolumnę a nie jej nazwe żeby ulozyc w porzadku
df.orderBy(df['Sales'].desc())
