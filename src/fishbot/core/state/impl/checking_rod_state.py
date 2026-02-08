import time

from ..bot_state import BotState
from ..state_type import StateType


class CheckingRodState(BotState):

    def _buy_new_rod(self):
        self.bot.log(f"[CHECKING_ROD] ❌ Maximum rod breaks reached ({self.config.max_rod_breaks}). Buying new rod.")
        self.controller.press_key('b')
        time.sleep(1)

        self.controller.press_key('b')
        time.sleep(1)

        x = 60 + self.window.monitor_x
        y = 313 + self.window.monitor_y

        self.controller.move_to(x, y)
        time.sleep(0.5)
        self.controller.move_to(x, y)
        time.sleep(0.5)
        self.controller.mouse_down('left')
        time.sleep(0.1)
        self.controller.mouse_up('left')
        time.sleep(0.5)

        # Regular Rod 
        x = 775 + self.window.monitor_x
        y = 310 + self.window.monitor_y
        if self.config.rod_type == 2:
            # Sturdy Rod
            x = 1245 + self.window.monitor_x
        elif self.config.rod_type == 3:
            # Flexible Rod
            x = 1475 + self.window.monitor_x

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

        self.bot.log("[CHECKING_ROD] ✅ Rod purchased")

        self.controller.press_key('esc')
        time.sleep(1)

    def handle(self, screen):
        self.bot.log("[CHECKING_ROD] Checking rod...")

        time.sleep(1)

        total_rod_breaks = self.bot.stats.get('rod_breaks')

        if total_rod_breaks is not None and total_rod_breaks > 0 and total_rod_breaks % self.config.max_rod_breaks == 0:
            self._buy_new_rod()

        found_rod = 0

        if self.detector.find(screen, "flex_rod", 5, debug=True):
            found_rod = 1

        if found_rod == 0 and self.detector.find(screen, "sturdy_rod", 5, debug=self.bot.debug_mode):
            found_rod = 1

        if found_rod == 0 and self.detector.find(screen, "reg_rod", 5, debug=self.bot.debug_mode):
            found_rod = 1
               
        if found_rod == 0:
            self.bot.log("[CHECKING_ROD] ⚠️  Broken rod! Replacing...")
            self.bot.stats.increment('rod_breaks')
            time.sleep(1)

            self.controller.press_key('m')
            time.sleep(1)

            x = 1650 + self.window.monitor_x
            y = 580 + self.window.monitor_y

            self.controller.move_to(x, y)
            time.sleep(0.5)
            self.controller.move_to(x, y)
            time.sleep(0.5)
            # self.controller.click('left')
            self.controller.mouse_down('left')
            time.sleep(0.1)
            self.controller.mouse_up('left')
            time.sleep(1)

            self.bot.log("[CHECKING_ROD] ✅ Rod replaced")
        else:
            time.sleep(1)
            self.bot.log("[CHECKING_ROD] ✅ Rod OK")

        return StateType.CHECKING_BAIT
