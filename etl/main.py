import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import upper, col

spark = SparkSession.builder \
    .appName("TestApp") \
    .config("spark.jars", "/opt/spark/") \
    .getOrCreate()

"""
 data = [("Ricardo", 27), ("Ana", 25)]
 df = spark.createDataFrame(data, ["name", "age"])
 
 df.show()
 
 spark.stop()
"""

data = [
    (1, "Ana", 23, "US"),
    (2, "Luis", 17, "MX"),
    (3, "John", 30, "US"),
    (4, "Maria", 15, "MX")
]

df = spark.createDataFrame(data, ["id", "name", "age", "country"])

filtered_df = df \
    .filter(df.age >= 18) \
    .withColumn("name", upper(col("name")))

filtered_df.show()
