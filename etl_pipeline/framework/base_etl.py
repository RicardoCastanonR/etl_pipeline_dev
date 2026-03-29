from abc import ABC, abstractmethod
import pyspark
from pyspark.sql import SparkSession

class BaseETL(ABC):
    def __init__(self, config: dict):
        print("This is the entry poin for any ETL")
        self.spark = self.create_spark()
        self.config = config


    def create_spark(self):
        builder = SparkSession.builder \
        .appName("TestApp") \
        .master("local[*]") \
        .config("spark.jars", "/opt/spark/") \
        
        return builder.getOrCreate()


    def config_parser(self):
        print("Check correctness of config entries")
        # TODO: check if all the config entries are correc or accepted
    
    @classmethod
    def execute(cls):
        config = cls.config_parser(cls)
        etl = cls(config)
        etl.run()


    @abstractmethod
    def run(self):
        print("BaseETL")
        pass


if __name__ == "__main__":
    pass