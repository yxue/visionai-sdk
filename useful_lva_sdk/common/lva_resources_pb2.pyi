from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from useful_lva_sdk.common import lva_pb2 as _lva_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Analysis(_message.Message):
    __slots__ = ["analysis_definition", "create_time", "disable_event_watch", "input_streams_mapping", "labels", "name", "output_streams_mapping", "update_time"]
    class InputStreamsMappingEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class OutputStreamsMappingEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ANALYSIS_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISABLE_EVENT_WATCH_FIELD_NUMBER: _ClassVar[int]
    INPUT_STREAMS_MAPPING_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_STREAMS_MAPPING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    analysis_definition: _lva_pb2.AnalysisDefinition
    create_time: _timestamp_pb2.Timestamp
    disable_event_watch: bool
    input_streams_mapping: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    name: str
    output_streams_mapping: _containers.ScalarMap[str, str]
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., analysis_definition: _Optional[_Union[_lva_pb2.AnalysisDefinition, _Mapping]] = ..., input_streams_mapping: _Optional[_Mapping[str, str]] = ..., output_streams_mapping: _Optional[_Mapping[str, str]] = ..., disable_event_watch: bool = ...) -> None: ...
