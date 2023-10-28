from bt_library import Task, Blackboard, ResultEnum
from globals import BATTERY_LEVEL


class Dock(Task):
    """
    Implementation of the Dock Task
    """

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        self.print_message("Docking and charged to 100%")

        blackboard.set_in_environment(BATTERY_LEVEL, 100)
        return self.report_succeeded(blackboard)
