import time

from .base_interceptor import BaseInterceptor


class BaitCheckInterceptor(BaseInterceptor):

    def check(self, screen):

        if self.detector.find(screen, "empty_bait"):
            self.bot.log("[CHECKING_BAIT] ⚠️ Empty bait! Replacing...")

            self.controller.release_all_controls()
            return True

        return False