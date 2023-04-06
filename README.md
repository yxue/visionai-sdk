# Vision AI Live Video Analytics SDK 
*Unofficial Vision AI SDK in Python.* It's for building Live Video Analytics (LVA) program and CRUD LVA resources. 

## Installation

```commandline
pip install useful-lva-sdk
```

## Get started

Create an LVA program with this lib:

```python
from useful_lva_sdk.core.lva_graph_builder import LvaGraphBuilder
from useful_lva_sdk.core.operator import *

graph = LvaGraphBuilder("test-analysis") \
    .add_analyzer(GcsVideoSource(), "gcs_source") \
    .add_analyzer(GcsProtoSink(), "gcs_sink") \
    .add_analyzer(OccupancyCounting(), "oc") \
    .connect("oc", "gcs_sink") \
    .connect("gcs_source", "oc") \
    .build()
```

Create an analysis with this lib:

```python
from useful_lva_sdk.client.lva_client import LVAClient

analysis = graph.analysis()
client = LVAClient(
    project="PROJECT_ID",
    location="LOCATION_ID",
    cluster="CLUSTER_ID",
)
client.create_analysis(analysis.name, analysis)
```