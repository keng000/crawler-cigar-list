from abc import ABC, abstractmethod


class AnnouncementControllerInterface(ABC):
    @abstractmethod
    def post(self, title: str, body: str):
        pass
