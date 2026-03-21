import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import upper, col, sum, avg, count


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

# Grouping & aggregation
sales = [
    ("product A", "tech", 100),
    ("product B", "tech", 200),
    ("product C", "home", 50),
    ("product D", "home", 10),
    ("product E", "care", 300)
]

sales_df = spark.createDataFrame(sales, ["product", "category", "price"])

sales_dst_df = sales_df.groupBy("category").agg( \
        sum("price").alias("total"),
        avg("price").alias("average"),
        count("product").alias("amount")
    )
    

sales_dst_df.show()
