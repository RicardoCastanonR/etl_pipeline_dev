import pyspark
from pyspark.sql import SparkSession
import importlib
from etl.window_etl import windowETL
"""
from pyspark.sql.window import Window
from pyspark.sql.functions import upper, col, sum, avg, count, first, coalesce, lit, row_number, desc, last
"""



def main():
    # args processing

    # etl selection


    spark = SparkSession.builder \
        .appName("TestApp") \
        .master("local[*]") \
        .config("spark.jars", "/opt/spark/") \
        .getOrCreate()
    config = {"key": "value"}
    etl = windowETL(config)
    
if __name__ == "__main__":
    main()
# Comented code will be passed to their own files in future
"""
 data = [("Ricardo", 27), ("Ana", 25)]
 df = spark.createDataFrame(data, ["name", "age"])
 
 df.show()
 
 spark.stop()
"""
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
"""

# Grouping & aggregation
"""
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
"""


# Join and enrichment
"""
users_data = [
    (1, "Ana"),
    (2, "Luis"),
    (3, "Maria")
]

orders_data = [
    (101, 1, 500),
    (102, 1, 300),
    (103, 2, 200)
]

users_df = spark.createDataFrame(users_data, ["user_id", "name"])
orders_df = spark.createDataFrame(orders_data, ["order_id", "user_id", "price"])

sales_2_df = users_df.join(orders_df, on="user_id", how="left") \
    .groupBy("user_id") \
    .agg(
        first("name").alias("name"), 
        coalesce(sum("price"), lit(0)).alias("total_spent")
    )
sales_2_df.show()
"""

# Complex transformation
"""
user_login_data = [
    (1, "login",    "2026-01-01 10:00"),
    (1, "buy",      "2026-01-01 10:05"),
    (2, "login",    "2026-01-01 11:00"),
    (1, "logout",   "2026-01-01 10:10"),
    (2, "buy",      "2026-01-01 11:10")
]

user_login_df = spark.createDataFrame(user_login_data, ["user_id", "event", "timestamp"])
session_data_df = user_login_df \
    .groupBy("user_id") \
    .agg(
        first("event").alias("first_event"),
        last("event").alias("last_event"),
        count("event")
    )
session_data_df.show()
"""