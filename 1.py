from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def process_data(self):
        self.load_data()
        self.process()
        self.save_data()

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def process(self):
        pass

    def save_data(self):
        print("Saving processed data...")


class SimpleDataProcessor(DataProcessor):
    def load_data(self):
        print("Loading data...")

    def process(self):
        print("Processing data y...")




# Використання однопроцесної програми
processor = SimpleDataProcessor()
processor.process_data()
