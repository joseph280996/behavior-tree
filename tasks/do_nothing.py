from bt_library import Blackboard, ResultEnum, Task


class DoNothing(Task):
    """
    Implementation of the Do Nothing Task
    """

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        self.print_message("Nothing to do here, stand by for further instruction.")
        return self.report_succeeded(blackboard)
