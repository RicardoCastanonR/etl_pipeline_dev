from abc import ABC, abstractmethod

class BaseETL(ABC):
    def __init__(self, spark, config: dict):
        print("This is the entry poin for any ETL")
        self.spark = spark
        self.config = config

    
    def config_parser(self):
        print("Check correctness of config entries")
    
    @abstractmethod
    def run(self):
        pass

    