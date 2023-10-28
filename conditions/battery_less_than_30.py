#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 1.0.4 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from globals import BATTERY_LEVEL


class BatteryLessThan30(btl.Condition):
    """
    Implementation of the condition "battery_level < 30".
    """

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        self.print_message("Checking battery < 30")

        return (
            self.report_succeeded(blackboard)
            if blackboard.get_in_environment(BATTERY_LEVEL, 0) < 30
            else self.report_failed(blackboard)
        )
