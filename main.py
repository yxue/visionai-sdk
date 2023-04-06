from core.lva_graph_builder import LvaGraphBuilder
from core.operator import *

analysis = LvaGraphBuilder("test-analysis") \
    .add_analyzer(GcsVideoSource(), "gcs_source") \
    .add_analyzer(GcsProtoSink(), "gcs_sink") \
    .add_analyzer(OccupancyCounting(), "oc") \
    .connect("oc", "gcs_sink") \
    .connect("gcs_source", "oc") \
    .build().analysis()


