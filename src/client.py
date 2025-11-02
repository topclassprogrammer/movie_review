from elasticsearch import Elasticsearch, helpers
from elasticsearch.helpers import bulk
from faker import generator

from src.exception_handler import handle_exceptions

from src.configuration import Configuration
from src.logger import Logger


class ElasticsearchClient:
    def __init__(self):
        self.config = Configuration('elasticsearch_config.yml').config
        self.logger = Logger()
        self.client = self.connect_to_elasticsearch()


    @handle_exceptions
    def connect_to_elasticsearch(self) -> Elasticsearch | None:
        client = Elasticsearch(f"{self.config['host']}:{self.config['port']}",
                               verify_certs=False,
                               basic_auth=(self.config['username'], self.config['password']))
        if client.ping():
            self.logger.logger.debug("Connected to Elasticsearch")
            return client
        else:
            self.logger.logger.debug("Failed to connect to Elasticsearch")
            return

    @handle_exceptions
    def get_index(self, index: int | str) -> dict | None:
        response = self.client.indices.get(index=index)
        self.logger.logger.info(f"Getting index: {index}")
        return response

    @handle_exceptions
    def create_index(self, index: int | str, mapping: dict) -> dict | None:
        response = self.client.indices.create(
            index=index, body={"mappings": {"properties": mapping}})
        self.logger.logger.info(f"Created index: {index}")
        return response

    @handle_exceptions
    def update_index(self, index: int | str, mapping: dict) -> dict | None:
        response = self.client.indices.put_mapping(
            index=index, body={"properties": mapping})
        self.logger.logger.info(f"Updated index: {index}")
        return response

    @handle_exceptions
    def delete_index(self, index: int | str) -> dict | None:
        response = self.client.indices.delete(index=index)
        self.logger.logger.info(f"Deleted index: {index}")
        return response

    @handle_exceptions
    def get_document(self, index: int | str, doc_id: int | str) -> dict | None:
        response = self.client.get(index=index, id=doc_id)
        self.logger.logger.info(f"Getting document with id {doc_id}")
        return response["_source"]

    @handle_exceptions
    def search_documents_by_query(self, index, query):
        response = self.client.search(index=index, body={"query": query})
        self.logger.logger.info(f'Search executed on index {index} with query {query}')
        return response['hits']['hits']

    @handle_exceptions
    def insert_document(self, index: int | str, doc_id: int | str, body: dict) -> dict:
        response = self.client.index(index=index, id=doc_id, body=body)
        self.logger.logger.info(f"Inserted document with id {doc_id}")
        return response

    @handle_exceptions
    def update_document(self, index: int | str, doc_id: int | str, body: dict) -> dict | None:
        response = self.client.update(index=index, id=doc_id, body={"doc": body})
        self.logger.logger.info(f"Updated document with id {doc_id}")
        return response

    @handle_exceptions
    def delete_document(self, index: int | str, doc_id: int | str) -> dict | None:
        response = self.client.delete(index=index, id=doc_id)
        self.logger.logger.info(f"Deleted document with id {doc_id}")
        return response

    @handle_exceptions
    def delete_documents_by_query(self, index, query):
        response = self.client.delete_by_query(index=index, body={"query": query})
        self.logger.logger.info(f"Deleting documents executed on index {index} with query {query}")
        return response

    @handle_exceptions
    def scan_index(self, index) -> generator:
        response = helpers.scan(self.client, index=index)
        for doc in response:
            yield doc['_source']
        self.logger.logger.info(f"Scanned index: {index}")
        return response

    @handle_exceptions
    def bulk_documents(self, index: int | str, documents: list[dict]) -> tuple[int, list]:
        actions = [{"_index": index, "_source": doc} for doc in documents]
        response = bulk(self.client, actions)
        self.logger.logger.info(f"Bulked {len(documents)} documents into index {index}")
        return response

    @handle_exceptions
    def count_documents(self, index: int | str) -> int:
        self.client.indices.refresh(index=index)
        response = self.client.count(index=index)
        self.logger.logger.info(f"Counted documents {response['count']} in index {index}")
        return response['count']



