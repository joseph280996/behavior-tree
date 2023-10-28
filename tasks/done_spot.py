from bt_library import Task, Blackboard
from globals import SPOT_CLEANING


class DoneSpot(Task):
    """
    Implementation of the done with spot cleaning
    """

    def run(self, blackboard: Blackboard):
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        self.print_message("Done cleaning spot, clearing instruction.")

        blackboard.set_in_environment(SPOT_CLEANING, False)

        return self.report_succeeded(blackboard)
