from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class response(_message.Message):
    __slots__ = ("status_code", "message", "internal_error", "validation_error", "not_found", "unauthorized")
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    UNAUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    message: str
    internal_error: InternalServerError
    validation_error: ValidationError
    not_found: ResourceNotFound
    unauthorized: AuthenticationError
    def __init__(self, status_code: _Optional[int] = ..., message: _Optional[str] = ..., internal_error: _Optional[_Union[InternalServerError, _Mapping]] = ..., validation_error: _Optional[_Union[ValidationError, _Mapping]] = ..., not_found: _Optional[_Union[ResourceNotFound, _Mapping]] = ..., unauthorized: _Optional[_Union[AuthenticationError, _Mapping]] = ...) -> None: ...

class InternalServerError(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: str
    def __init__(self, details: _Optional[str] = ...) -> None: ...

class ValidationError(_message.Message):
    __slots__ = ("violations",)
    VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    violations: _containers.RepeatedCompositeFieldContainer[FieldViolation]
    def __init__(self, violations: _Optional[_Iterable[_Union[FieldViolation, _Mapping]]] = ...) -> None: ...

class FieldViolation(_message.Message):
    __slots__ = ("field", "description")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    field: str
    description: str
    def __init__(self, field: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ResourceNotFound(_message.Message):
    __slots__ = ("resource_type", "resource_id")
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_type: str
    resource_id: str
    def __init__(self, resource_type: _Optional[str] = ..., resource_id: _Optional[str] = ...) -> None: ...

class AuthenticationError(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...
