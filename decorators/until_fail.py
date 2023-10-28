from bt_library import Decorator, Blackboard, ResultEnum, TreeNode


class UntilFail(Decorator):
    """
    Specific implementation of the until failed decorator.
    """

    def __init__(self, child: TreeNode):
        """
        Default constructor.

        :param child: Child associated to the decorator
        """

        super().__init__(child)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        result_child = self.child.run(blackboard)

        if result_child == ResultEnum.FAILED:
            return self.report_succeeded(blackboard, False)

        return self.report_running(blackboard, True)
