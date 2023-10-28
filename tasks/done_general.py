from bt_library import Blackboard, ResultEnum, Task
from globals import GENERAL_CLEANING


class DoneGeneral(Task):
    """
    Implementation of the done with general cleaning task
    """

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        self.print_message("Done general cleaning, clearing general cleaning command")

        blackboard.set_in_environment(GENERAL_CLEANING, False)
        return self.report_succeeded(blackboard)
