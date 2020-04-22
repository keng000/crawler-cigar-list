from logging import getLogger

from .interface import AnnouncementControllerInterface

logger = getLogger(__name__)


class MailController(AnnouncementControllerInterface):
    def post(self, title: str, body: str):
        pass