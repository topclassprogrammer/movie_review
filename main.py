from src.client import ElasticsearchClient
from src.faker_wrapper import FakerWrapper


def main():
    client = ElasticsearchClient()
    INDEX = "index_1"
    # print(client.create_index(index=INDEX, mapping={"some_field": {"type": "text"}}))
    # client.create_index(index="index_2", mapping={"some_field": {"type": "text"}})
    # client.delete_index(index="index_2")
    # response_index = client.get_index(index=INDEX)
    # print(f"{response_index = }")
    # client.update_index(index=INDEX, mapping={"some_field_2": {"type": "keyword"}})
    # client.insert_document(index=INDEX, doc_id=1, body={"some_field_1": "some_content"})
    # client.insert_document(index=INDEX, doc_id=2, body={"some_field_2": "some_content"})
    # response_doc = client.get_document(index=INDEX, doc_id=1)
    # print(f"{response_doc = }")
    # client.update_document(index=INDEX, doc_id=1, body={"some_field_3": "new_content"})
    # client.delete_document(index=INDEX, doc_id=2)

    # fw = FakerWrapper()
    # sample_data_gen = fw.generate_data(num_of_documents=10_000)
    # client.insert_document(index=INDEX, doc_id=3, body=next(sample_data_gen))
    # client.bulk_documents(index=INDEX, documents=[next(sample_data_gen) for _ in range(1000)])
    # counted_docs = client.count_documents(index=INDEX)
    # print(f"{counted_docs = }")
    # scanned_gen = client.scan_index(index=INDEX)
    # print(f"{scanned_gen = }")
    # searched_docs =  client.search_documents_by_query(index=INDEX, query={"bool": {"must": [
    #     {"range": {"imdb_rating": {"gte": 10}}},
    #     {"range": {"users_rating": {"gte": 10}}}
    #                                        ]}})
    # print(f"{searched_docs =}")
    # client.delete_documents_by_query(index=INDEX, query={"bool": {"must": [
    #     {"range": {"imdb_rating": {"gte": 10}}},
    #     {"range": {"users_rating": {"gte": 10}}}
    #                                        ]}})


if __name__ == '__main__':
    main()


