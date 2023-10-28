from bt_library import Task, Blackboard, ResultEnum


class CleanSpot(Task):
    """
    Implementation of the Clean Spot Task
    """

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        self.print_message("Cleaning the Spot")

        return self.report_succeeded(blackboard)
