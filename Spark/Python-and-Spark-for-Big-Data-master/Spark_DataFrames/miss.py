from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('miss').getOrCreate()
df = spark.read.csv('ContainsNull.csv',header=True, inferSchema=True)

df.show()


# usunięcie wszystkich danych gdzie jest jakiś null
df.na.drop().show()

# usunięcie takich, które majs >= 2 nulle
df.na.drop(thresh=2).show()

# jeśli mamy jakąkolwiek null to usuwamy
df.na.drop(how= 'any').show()

# ropatrujemy dokladna kolumne
df.na.drop(subset=['Sales']).show()

# wypełnienie pustych danych
df.printSchema()

df.na.fill('FILL VALUE').show()

# teraz wypełniamy tylko numeryczne wartości
df.na.fill(0).show()

# teraz wypełniamy konkretną kolumnę
df.na.fill('No Name', subset=['Name']).show()

# wypełnienie missingów średnią

from pyspark.sql.functions import mean

mean_val = df.select(mean(df['Sales'])).collect()

print(mean_val)

mean_sales = mean_val[0][0]
df.na.fill(mean_sales,['Sales']).show()

# wszystko w jednej linii
df.na.fill(df.select(mean(df['Sales'])).collect()[0][0],['Sales']).show()
