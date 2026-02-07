import time

from ..bot_state import BotState
from ..state_type import StateType


class CheckingBaitState(BotState):

    def handle(self, screen):
        self.bot.log("[CHECKING_BAIT] Checking bait...")

        time.sleep(1)

        empty_bait = 0

        if self.detector.find(screen, "empty_bait", 5, debug=True):
            empty_bait = 1
               
        if empty_bait == 1:
            self.bot.log("[CHECKING_BAIT] ⚠️  Empty bait! Replacing...")
            self.bot.stats.increment('bait_replacements')
            time.sleep(1)

            self.controller.press_key('b')
            time.sleep(1)

            x = 60 + self.window.monitor_x
            y = 313 + self.window.monitor_y

            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.move_to(x, y)
            time.sleep(0.5)
            # self.controller.click('left')
            self.controller.mouse_down('left')
            time.sleep(0.1)
            self.controller.mouse_up('left')
            time.sleep(0.5)

            # Regular Bait 310
            # x = 310 + self.window.monitor_x
            x = 535 + self.window.monitor_x
            y = 310 + self.window.monitor_y

            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.mouse_down('left')
            time.sleep(0.1)
            self.controller.mouse_up('left')
            time.sleep(0.5)

            # Max button 99
            x = 1560 + self.window.monitor_x
            y = 725 + self.window.monitor_y

            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.mouse_down('left')
            time.sleep(0.1)
            self.controller.mouse_up('left')
            time.sleep(0.5)

            # Purchase button
            x = 1210 + self.window.monitor_x
            y = 925 + self.window.monitor_y

            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.mouse_down('left')
            time.sleep(0.1)
            self.controller.mouse_up('left')
            time.sleep(0.5)

            # Confirm button
            x = 1200 + self.window.monitor_x
            y = 800 + self.window.monitor_y

            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.mouse_down('left')
            time.sleep(0.1)
            self.controller.mouse_up('left')
            time.sleep(0.5)

            self.bot.log("[CHECKING_BAIT] ✅ Bait purchased")

            self.controller.press_key('esc')
            time.sleep(1)

            self.controller.press_key('n')
            time.sleep(1)

            # Replace bait
            x = 1450 + self.window.monitor_x
            y = 590 + self.window.monitor_y

            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.mouse_down('left')
            time.sleep(0.1)
            self.controller.mouse_up('left')
            time.sleep(0.5)

            self.bot.log("[CHECKING_BAIT] ✅ Bait replaced")
        else:
            time.sleep(1)
            self.bot.log("[CHECKING_BAIT] ✅ Bait OK")

        return StateType.CASTING_BAIT
