from etl_pipeline.framework.base_etl import BaseETL
from pyspark.sql.functions import first, coalesce, lit, sum

class joinETL(BaseETL):
    def run(self):
        print("This is the join ETL")

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

        users_df = self.spark.createDataFrame(users_data, ["user_id", "name"])
        orders_df = self.spark.createDataFrame(orders_data, ["order_id", "user_id", "price"])

        sales_2_df = users_df.join(orders_df, on="user_id", how="left") \
            .groupBy("user_id") \
            .agg(
                first("name").alias("name"), 
                coalesce(sum("price"), lit(0)).alias("total_spent")
            )
        sales_2_df.show()

if __name__ == "__main__":
    joinETL.execute()
