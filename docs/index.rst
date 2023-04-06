Welcome to Useful LVA SDK's documentation!
==========================================

This document lists APIs provided by useful_lva_sdk.

Installation
============
.. code-block:: bash

    pip install useful-lva-sdk

Examples
========
.. code-block:: python
   :linenos:

    from useful_lva_sdk.core.lva_graph_builder import LvaGraphBuilder
    from useful_lva_sdk.core.operator import *
    from useful_lva_sdk.client.lva_client import LVAClient

    analysis = LvaGraphBuilder("test-analysis") \
        .add_analyzer(GcsVideoSource(), "gcs_source") \
        .add_analyzer(GcsProtoSink(), "gcs_sink") \
        .add_analyzer(OccupancyCounting(), "oc") \
        .connect("oc", "gcs_sink") \
        .connect("gcs_source", "oc") \
        .build().analysis()

    client = LVAClient(
        project="PROJECT_ID",
        location="LOCATION_ID",
        cluster="CLUSTER_ID",
    )
    client.create_analysis(analysis.name, analysis)


Python APIs
===========

.. toctree::
   :maxdepth: 2

   api/operators
   api/lva_client
   api/lva_graph
   api/lva_graph_builder
