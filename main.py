from core.lva_graph_builder import LvaGraphBuilder
from core.operators import *

builder = LvaGraphBuilder()

print(builder.build().name)
