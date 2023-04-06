# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from useful_lva_sdk.common import lva_resources_pb2 as google_dot_cloud_dot_visionai_dot_v1_dot_lva__resources__pb2
from useful_lva_sdk.common import lva_service_pb2 as google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


class LiveVideoAnalyticsStub(object):
    """Service describing handlers for resources. The service enables clients to run
    Live Video Analytics (LVA) on the streaming inputs.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListAnalyses = channel.unary_unary(
                '/google.cloud.visionai.v1.LiveVideoAnalytics/ListAnalyses',
                request_serializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.ListAnalysesRequest.SerializeToString,
                response_deserializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.ListAnalysesResponse.FromString,
                )
        self.GetAnalysis = channel.unary_unary(
                '/google.cloud.visionai.v1.LiveVideoAnalytics/GetAnalysis',
                request_serializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.GetAnalysisRequest.SerializeToString,
                response_deserializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__resources__pb2.Analysis.FromString,
                )
        self.CreateAnalysis = channel.unary_unary(
                '/google.cloud.visionai.v1.LiveVideoAnalytics/CreateAnalysis',
                request_serializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.CreateAnalysisRequest.SerializeToString,
                response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
                )
        self.UpdateAnalysis = channel.unary_unary(
                '/google.cloud.visionai.v1.LiveVideoAnalytics/UpdateAnalysis',
                request_serializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.UpdateAnalysisRequest.SerializeToString,
                response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
                )
        self.DeleteAnalysis = channel.unary_unary(
                '/google.cloud.visionai.v1.LiveVideoAnalytics/DeleteAnalysis',
                request_serializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.DeleteAnalysisRequest.SerializeToString,
                response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
                )


class LiveVideoAnalyticsServicer(object):
    """Service describing handlers for resources. The service enables clients to run
    Live Video Analytics (LVA) on the streaming inputs.
    """

    def ListAnalyses(self, request, context):
        """Lists Analyses in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnalysis(self, request, context):
        """Gets details of a single Analysis.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAnalysis(self, request, context):
        """Creates a new Analysis in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAnalysis(self, request, context):
        """Updates the parameters of a single Analysis.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAnalysis(self, request, context):
        """Deletes a single Analysis.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LiveVideoAnalyticsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListAnalyses': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAnalyses,
                    request_deserializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.ListAnalysesRequest.FromString,
                    response_serializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.ListAnalysesResponse.SerializeToString,
            ),
            'GetAnalysis': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnalysis,
                    request_deserializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.GetAnalysisRequest.FromString,
                    response_serializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__resources__pb2.Analysis.SerializeToString,
            ),
            'CreateAnalysis': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAnalysis,
                    request_deserializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.CreateAnalysisRequest.FromString,
                    response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
            ),
            'UpdateAnalysis': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAnalysis,
                    request_deserializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.UpdateAnalysisRequest.FromString,
                    response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
            ),
            'DeleteAnalysis': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAnalysis,
                    request_deserializer=google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.DeleteAnalysisRequest.FromString,
                    response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.cloud.visionai.v1.LiveVideoAnalytics', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LiveVideoAnalytics(object):
    """Service describing handlers for resources. The service enables clients to run
    Live Video Analytics (LVA) on the streaming inputs.
    """

    @staticmethod
    def ListAnalyses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.visionai.v1.LiveVideoAnalytics/ListAnalyses',
            google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.ListAnalysesRequest.SerializeToString,
            google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.ListAnalysesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnalysis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.visionai.v1.LiveVideoAnalytics/GetAnalysis',
            google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.GetAnalysisRequest.SerializeToString,
            google_dot_cloud_dot_visionai_dot_v1_dot_lva__resources__pb2.Analysis.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateAnalysis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.visionai.v1.LiveVideoAnalytics/CreateAnalysis',
            google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.CreateAnalysisRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAnalysis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.visionai.v1.LiveVideoAnalytics/UpdateAnalysis',
            google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.UpdateAnalysisRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAnalysis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.visionai.v1.LiveVideoAnalytics/DeleteAnalysis',
            google_dot_cloud_dot_visionai_dot_v1_dot_lva__service__pb2.DeleteAnalysisRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)