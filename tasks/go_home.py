from bt_library import Task, Blackboard, ResultEnum
from globals import HOME_PATH


class GoHome(Task):
    """
    Implementation of the Task "Go Home".
    """

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        homepath = blackboard.get_in_environment(HOME_PATH, "")
        self.print_message(
            "Going back home to dock using the following path " + homepath
        )
        return self.report_succeeded(blackboard)
