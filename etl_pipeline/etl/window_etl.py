
from etl_pipeline.framework.base_etl import BaseETL
from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number


class windowETL(BaseETL):
    def run(self):
        print("This is the window ETL")
        # Window functions
        
        employees_data = [
            (1, "Ana", "IT", 5000),
            (2, "Luis", "IT", 7000),
            (3, "Maria", "HR", 4000),
            (4, "Pedro", "IT", 7000),
            (5, "Juan", "HR", 4500)
        ]

        employees_df = self.spark.createDataFrame(employees_data, ["id", "name", "department", "salary"])
        rank_df = employees_df.withColumn(
            "",
            row_number().over(Window.partitionBy("department").orderBy(col("salary").desc()))
        )
        rank_df.show()

print(__name__)
if __name__ == "__main__":
    print("everything allright")
    windowETL.execute()
