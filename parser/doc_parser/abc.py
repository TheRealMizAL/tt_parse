from abc import ABC, abstractmethod


class AbstractDocument(ABC):
    """
    Base class for all types of documents
    """
    @abstractmethod
    async def parse(self):
        pass
