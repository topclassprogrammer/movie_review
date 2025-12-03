from src.client import ElasticsearchClient
from src.faker_wrapper import FakerWrapper


def main():
    client = ElasticsearchClient()
    INDEX = "movie_reviews"
    fw = FakerWrapper()
    sample_data_gen = fw.generate_data(num_of_documents=1000)
    client.bulk_documents(index=INDEX, documents=[next(sample_data_gen) for _ in range(1000)])


if __name__ == '__main__':
    main()
