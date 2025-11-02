import functools

from elasticsearch import BadRequestError
from elasticsearch.exceptions import ConnectionError, NotFoundError, RequestError
from src.logger import Logger

logger = Logger()


def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFoundError as e:
            logger.logger.error(f"Index or document not found: {e}")
        except RequestError as e:
            logger.logger.error(f"Invalid request: {e}")
        except ConnectionError as e:
            logger.logger.error(f"Connection failed: {e}")
        except Exception as e:
            logger.logger.error(f'General error: {str(e)}')
    return wrapper



