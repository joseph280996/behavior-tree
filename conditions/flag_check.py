from bt_library import Blackboard, ResultEnum, Condition


class FlagCheck(Condition):
    flag: str
    """
    Implementation of the condition "spot".
    """

    def __init__(self, flag: str):
        """
        Default constructor.

        :param flag: the boolean flag in Blackboard to check
        """

        super().__init__()
        self.flag = flag

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        self.print_message("Checking is " + self.flag)

        return (
            self.report_succeeded(blackboard)
            if blackboard.get_in_environment(self.flag, 0)
            else self.report_failed(blackboard)
        )
