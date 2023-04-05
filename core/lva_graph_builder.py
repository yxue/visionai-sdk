from core.lva_graph import LvaGraph


class LvaGraphBuilder:
    """
    Instantiate an LVA graph builder.
    """
    def __init__(self):
        self.graph = LvaGraph("hello")

    def add_source(self, operator):
        pass

    """
    Build the LVA graph.
    
    :return: The LVA graph.
    :rtype: lva_graph.LvaGraph
    """
    def build(self):
        return self.graph
