from bt_library import Blackboard, Composite, NodeListType, ResultEnum


class Sequence(Composite):
    """
    Specific implementation of the selection composite.
    """

    def __init__(self, children: NodeListType):
        """
        Default constructor.

        :param children: List of children for this node
        """

        super().__init__(children)

    def run(self, blackboard: Blackboard):
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        child_position = self.additional_information(blackboard, 0)
        while child_position < len(self.children):
            child = self.children[child_position]
            result_child = child.run(blackboard)
            if result_child == ResultEnum.FAILED:
                return self.report_failed(blackboard, 0)

            if result_child == ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)
            child_position += 1

        return self.report_succeeded(blackboard, 0)
