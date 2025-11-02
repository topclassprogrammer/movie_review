import yaml
from faker import Faker
from src.logger import Logger


class FakerWrapper:
    def __init__(self):
        with open("mapping/faker_mapping.yml", "r", encoding="utf-8") as f:
            self.mapping = yaml.safe_load(f)
        self.logger = Logger()
        self.faker = Faker(locale='en_US')
        self.logger.logger.debug("Initialized FakerWrapper")

    def generate_data(self, mapping=None, num_of_documents=1):
        if mapping is None:
            mapping = self.mapping
        for i in range(num_of_documents):
            document = {}
            for key, value in mapping.items():
                faker_method = value.get("faker")
                kwargs = value.get("kwargs", {})
                document[key] = getattr(self.faker, faker_method)(**kwargs)
            yield document
        self.logger.logger.info(f"Generated {num_of_documents} documents")

