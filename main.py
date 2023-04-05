from core.lva_graph_builder import LvaGraphBuilder
from core.operator import *

g = LvaGraphBuilder("test-analysis").\
    add_analyzer(GcsVideoSource(), "gcs_source").\
    add_analyzer(GcsProtoSink(), "gcs_sink").\
    connect("gcs_source", "gcs_sink")\
    .build()
