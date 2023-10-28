from bt_library import Blackboard, ResultEnum, Task


class CleanFloor(Task):
    """
    Implementation of the Clean Floor Task
    """

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        self.print_message("Cleaning Floor")
        is_success = input("Is there anything else to clean? [y/n]")
        return (
            self.report_succeeded(blackboard)
            if is_success == "y"
            else self.report_failed(blackboard)
        )
