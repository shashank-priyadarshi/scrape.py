from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class request(_message.Message):
    __slots__ = ("url", "proxy", "depth", "retryDuration")
    URL_FIELD_NUMBER: _ClassVar[int]
    PROXY_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    RETRYDURATION_FIELD_NUMBER: _ClassVar[int]
    url: str
    proxy: str
    depth: int
    retryDuration: int
    def __init__(self, url: _Optional[str] = ..., proxy: _Optional[str] = ..., depth: _Optional[int] = ..., retryDuration: _Optional[int] = ...) -> None: ...

class product(_message.Message):
    __slots__ = ("title", "price", "imageSource", "createdAt", "updatedAt")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGESOURCE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    title: str
    price: str
    imageSource: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, title: _Optional[str] = ..., price: _Optional[str] = ..., imageSource: _Optional[str] = ..., createdAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
