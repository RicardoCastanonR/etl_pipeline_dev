from etl_pipeline.framework.base_etl import BaseETL
from pyspark.sql.functions import sum, avg, count

class groupingETL(BaseETL):
    def run(self):
        sales = [
            ("product A", "tech", 100),
            ("product B", "tech", 200),
            ("product C", "home", 50),
            ("product D", "home", 10),
            ("product E", "care", 300)
        ]

        sales_df = self.spark.createDataFrame(sales, ["product", "category", "price"])

        sales_dst_df = sales_df.groupBy("category").agg( \
                sum("price").alias("total"),
                avg("price").alias("average"),
                count("product").alias("amount")
            )

        sales_dst_df.show()


if __name__ == "__main__":
    groupingETL.execute()