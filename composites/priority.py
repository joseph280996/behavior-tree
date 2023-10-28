from bt_library import Blackboard, ResultEnum, Composite, NodeListType


class Priority(Composite):
    """
    Speicfic implementation of the Priority Composite
    """

    def __init__(self, children: NodeListType):
        """
        Default constructor.

        :param children: List of children for this node
        """

        super().__init__(sorted(children, key=lambda x: x.id))

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        for child in self.children:
            result_child = child.run(blackboard)
            if result_child == ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard, 0)

            if result_child == ResultEnum.RUNNING:
                return self.report_running(blackboard)

        return self.report_failed(blackboard, 0)
