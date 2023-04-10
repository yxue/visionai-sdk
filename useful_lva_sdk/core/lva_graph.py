"""LVA graph library"""
import queue

from graphviz import Digraph

from useful_lva_sdk.common.lva_pb2 import AnalysisDefinition, AnalyzerDefinition
from useful_lva_sdk.common.lva_resources_pb2 import Analysis
from useful_lva_sdk.core.operator import Operator


class Vertex:
    """Vertex in the LVA graph."""

    def __init__(self, operator: Operator, name: str):
        """
        Instantiate a Vertex.

        :param operator: The operator name.
        :param name: The analyzer name.
        """
        self.operator = operator
        self.name = name


class Edge:
    """Edge in the LVA graph."""

    def __init__(self, src: str, dst: str, name: str):
        """
        Instantiate an Edge.

        :param src: The source analyzer.
        :param dst: The destination analyzer.
        :param name: The streaming channel between source and destination analyzer.
        """
        self.src = src
        self.dst = dst
        self.name = name


class LvaGraph:
    """LVA graph"""

    def __init__(self, name: str):
        """
        Instantiate an LVA graph.

        :param name: The name of the graph.
        :type name: string
        """
        self.name = name
        self._vertices: dict[str, Vertex] = {}
        self._edges_in: dict[str, list[Edge]] = {}
        self._edges_out: dict[str, list[Edge]] = {}
        self._out_degrees: dict[str, int] = {}

    def add_vertex(self, operator: Operator, name: str) -> None:
        """
        Add a vertex to the LVA graph.

        :param operator: The operator name.
        :param name: The analyzer name.
        """
        self._vertices[name] = Vertex(operator, name)

    def add_edge(self, src: str, dst: str, channel: str) -> None:
        """
        Add an edge to the LVA graph.

        :param src: The source analyzer.
        :param dst: The destination analyzer.
        :param channel: The streaming channel between the source and destination analyzer.
        """
        if dst not in self._edges_in:
            self._edges_in[dst] = []
        if src not in self._edges_out:
            self._edges_out[src] = []
        if src not in self._out_degrees:
            self._out_degrees[src] = 0
        self._edges_in[dst].append(Edge(src, dst, channel))
        self._edges_out[src].append(Edge(src, dst, channel))
        self._out_degrees[src] += 1

    def display(self):
        """
        Display shows the LVA graph with graph viz.

        **Note: Graphviz is required for this function.**
        """
        graph = Digraph()
        que: queue.Queue[Vertex] = queue.Queue()
        out_degrees = self._out_degrees
        for operator in self._vertices.values():
            if operator.name not in out_degrees or out_degrees[operator.name] == 0:
                que.put(operator)
        while not que.empty():
            vertex = que.get()
            graph.node(vertex.name, f'{vertex.operator.name}({vertex.name})')
            if vertex.name in self._edges_in:
                for edge in self._edges_in[vertex.name]:
                    graph.edge(edge.src, vertex.name, f'{edge.src}:{edge.name}')
                    out_degrees[edge.src] -= 1
                    if out_degrees[edge.src] == 0:
                        que.put(self._vertices[edge.src])
        graph.render(view=True)
        return self

    def analysis(self) -> Analysis:
        """
        Analysis converts the LVA graph to an Analysis resource.

        :return: The LVA analysis.
        :rtype: Analysis.
        """
        analyzers: list[AnalyzerDefinition] = []
        que: queue.Queue[Vertex] = queue.Queue()
        out_degrees = self._out_degrees
        for operator in self._vertices.values():
            if operator.name not in out_degrees or out_degrees[operator.name] == 0:
                que.put(operator)
        while not que.empty():
            vertex = que.get()
            analyzer = AnalyzerDefinition(
                analyzer=vertex.name,
                operator=vertex.operator.name,
            )
            if vertex.name in self._edges_in:
                for edge in self._edges_in[vertex.name]:
                    analyzer.inputs.append(
                        AnalyzerDefinition.StreamInput(input=f'{edge.src}:{edge.name}'))
                    out_degrees[edge.src] -= 1
                    if out_degrees[edge.src] == 0:
                        que.put(self._vertices[edge.src])
            analyzers.append(analyzer)
        return Analysis(
            name=self.name,
            analysis_definition=AnalysisDefinition(analyzers=analyzers),
            disable_event_watch=True)
