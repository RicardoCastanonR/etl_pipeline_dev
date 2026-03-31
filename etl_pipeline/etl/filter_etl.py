from etl_pipeline.framework.base_etl import BaseETL
from pyspark.sql.functions import upper, col

class filterETL(BaseETL):
    def run(self):
        data = [
            (1, "Ana", 23, "US"),
            (2, "Luis", 17, "MX"),
            (3, "John", 30, "US"),
            (4, "Maria", 15, "MX")
        ]

        df = self.spark.createDataFrame(data, ["id", "name", "age", "country"])

        filtered_df = df \
            .filter(df.age >= 18) \
            .withColumn("name", upper(col("name")))

        filtered_df.show()

if __name__ == "__main__":
    filterETL.execute()