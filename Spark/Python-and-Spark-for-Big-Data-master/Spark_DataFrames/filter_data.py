from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('ops').getOrCreate()
df = spark.read.csv('appl_stock.csv', inferSchema = True, header = True)
# header oznacza, że pierwszy wiersz to nazwy kolumn

df.show()
print(df.head(3)[0])


# Pobieranie danych nie używając  sql'a

df.filter("Close < 500").show()


df.filter("Close < 500").select('Open').show()

df.filter("Close < 500").select(['Open','Close']).show()

# df.filter(df['Close'] < 500).show().select('Volume').show()

# Multiple conditions

df.filter(  (df['Close'] < 200) &  ~(df['Open'] > 200) ).show()
 # ~ to zaprzeczenie


df.filter(df['Low'] == 197.16).show()

# zamiast show collect , żebyśmy dostali dane spakowane w listę
result = df.filter(df['Low'] == 197.16).collect()

print(result)

row = result[0]

# Zamiana na słwnik

print(row.asDict())

print(row.asDict()['Volume'])
