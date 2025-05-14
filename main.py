import multiprocessing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def process_data(self):
        self.load_data()
        self.process()
        self.save_data()

    def load_data(self):
        print("Loading data in multiprocessing mode...")

    @abstractmethod
    def process(self):
        pass

    def save_data(self):
        print("Saving processed data in multiprocessing mode...")


class MultiDataProcessor(DataProcessor):
    def process(self):
        # Запускаємо процеси паралельно
        process1 = multiprocessing.Process(target=self._process_part1)
        process2 = multiprocessing.Process(target=self._process_part2)
        process1.start()
        process2.start()
        process1.join()
        process2.join()

    def _process_part1(self):
        print("Processing part 1...")

    def _process_part2(self):
        print("Processing part 2...")



if __name__ == '__main__':
    processor = MultiDataProcessor()
    processor.process_data()
