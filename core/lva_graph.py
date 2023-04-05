class Vertex:
    """Vertex in the LVA graph."""

    """
    Instantiate a Vertex.
    
    :param operator: The operator name.
    :param name: The analyzer name.
    """
    def __init__(self, operator, name):
        self.operator = operator
        self.name = name


class Edge:
    """Edge in the LVA graph."""

    """
    Instantiate an Edge.
    
    :param src: The source analyzer.
    :param dst: The destination analyzer.
    :param ch: The streaming channel between source and destination analyzer.
    """
    def __init__(self, src, dst, ch):
        self.src = src
        self.dst = dst
        self.ch = ch


class LvaGraph:
    """
    Instantiate an LVA graph.

    :param name: The name of the graph.
    :type name: string
    """

    def __init__(self, name):
        self.name = name
        self._vertices: list[Vertex] = []
        self._edges: dict[str, list[Edge]] = {}

    """
    Add a vertex to the LVA graph.
    
    :param operator: The operator name.
    :param name: The analyzer name.
    """
    def add_vertex(self, operator, name) -> None:
        self._vertices.append(Vertex(operator, name))

    """
    Add an edge to the LVA graph.
    
    :param src: The source analyzer.
    :param dst: The destination analyzer.
    :param ch: The streaming channel between the source and destination analyzer.
    """
    def add_edge(self, src, dst, ch) -> None:
        if src not in self._edges:
            self._edges[src] = []
        self._edges[src].append(Edge(src, dst, ch))
