from .interface import AnnouncementControllerInterface

from logging import getLogger

logger = getLogger(__name__)


class MailController(AnnouncementControllerInterface):
    def post(self, title: str, body: str):
        pass
