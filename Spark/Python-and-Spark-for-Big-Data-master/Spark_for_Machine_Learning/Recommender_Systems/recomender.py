from pyspark.sql  import  SparkSession

spark = SparkSession.builder.appName('rec').getOrCreate()

from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import  RegressionEvaluator

data = spark.read.csv('movielens_ratings.csv', inferSchema=True, header=True)

data.show()

data.describe().show()

training, test = data.randomSplit([0.8,0.2])

als = ALS(maxIter = 5, regParam = 0.01,userCol ='userId', itemCol = 'movieId' , ratingCol = 'rating')
model = als.fit(training)

predictions = model.transform(test)

predictions.show()


# słabe przewidywania bo mało próbek

evaluator = RegressionEvaluator(metricName='rmse', labelCol = 'rating', predictionCol  = 'prediction')

rmse = evaluator.evaluate(predictions)

print('RMSE')
print(rmse)

# wyszło 1,7 czyli na 5 gwiazdek średnio mylimy się o 2, więc dużo za dużo


# single user

single_user = test.filter(test['userId'] ==  11).select(['movieId','userId'])

# przewidzimy, czy ten user o id = 11 polubi nastepujace filmy
single_user.show()

recommendation  = model.transform(single_user)
recommendation.orderBy('prediction', ascending = False).show()
