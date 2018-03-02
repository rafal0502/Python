from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('dates').getOrCreate()
df = spark.read.csv('appl_stock.csv', header=True, inferSchema = True)

print(df.select(['Date','Open']).show())

# Operowanie na datach

from pyspark.sql.functions import (dayofmonth,hour, dayofyear,
                                                        month,year,weekofyear,
                                                        format_number,date_format)

df.select(dayofmonth(df['Date'])).show()

df.select(hour(df['Date'])).show()

df.select(month(df['Date'])).show()


# Średnia zamykająca cena na rok
df.select(year(df['Date'])).show()
newdf = df.withColumn("Year",year(df['Date']))
result = newdf.groupBy("Year").mean().select(["Year","avg(Close)"])
new = result.withColumnRenamed("avg(Close)","Average Closing Price")
new.select(['Year',format_number('Average Closing Price',2).alias("Avg Close")]).show()
