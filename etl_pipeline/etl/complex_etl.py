from etl_pipeline.framework.base_etl import BaseETL
from pyspark.sql.functions import first, last, count

class complexETL(BaseETL):
    def run(self):
        print("This is the complexETL")

        user_login_data = [
            (1, "login",    "2026-01-01 10:00"),
            (1, "buy",      "2026-01-01 10:05"),
            (2, "login",    "2026-01-01 11:00"),
            (1, "logout",   "2026-01-01 10:10"),
            (2, "buy",      "2026-01-01 11:10")
        ]

        user_login_df = self.spark.createDataFrame(user_login_data, ["user_id", "event", "timestamp"])
        session_data_df = user_login_df \
            .groupBy("user_id") \
            .agg(
                first("event").alias("first_event"),
                last("event").alias("last_event"),
                count("event")
            )
        session_data_df.show()

if __name__ == "__main__":
    complexETL.execute()