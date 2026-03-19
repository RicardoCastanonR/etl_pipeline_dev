import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TestApp") \
    .config("spark.jars", "/opt/spark/") \
    .getOrCreate()

data = [("Ricardo", 27), ("Ana", 25)]
df = spark.createDataFrame(data, ["name", "age"])

df.show()

spark.stop()