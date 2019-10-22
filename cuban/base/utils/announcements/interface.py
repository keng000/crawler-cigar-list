from abc import ABC, abstractmethod


class AnnouncementControllerInterface(ABC):
    @abstractmethod
    def post(self, title: str, body: str):
        pass


class AnnouncementController:
    def __init__(self, impl: AnnouncementControllerInterface):
        if not isinstance(impl, AnnouncementControllerInterface):
            raise RuntimeError("Interface Error")

        self.impl = impl

    def post(self, title: str, body: str):
        self.impl.post(title, body)
