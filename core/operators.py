from abc import abstractmethod, ABC


class Operator(ABC):
    @property
    @abstractmethod
    def operator(self):
        pass

    @property
    @abstractmethod
    def input_args(self):
        pass

    @property
    @abstractmethod
    def output_args(self):
        pass

    @property
    @abstractmethod
    def attributes(self):
        pass


class GcsVideoSource(Operator):
    @property
    def operator(self):
        return "GcsSource"

    @property
    def input_args(self):
        return []

    @property
    def output_args(self):
        return ["output_stream"]

    @property
    def attributes(self):
        return ["input_video_gcs_path"]


class GcsProtoSink(Operator):
    @property
    def operator(self):
        return "GcsProtoSink"

    @property
    def input_args(self):
        return ["annotation"]

    @property
    def output_args(self):
        return []

    @property
    def attributes(self):
        return ["output_file_gcs_path"]


class OccupancyCounting(Operator):
    @property
    def operator(self):
        return "OccupancyCounting"

    @property
    def input_args(self):
        return ["input_stream"]

    @property
    def output_args(self):
        return ["output_stream"]

    @property
    def attributes(self):
        return ["detect_person"]
