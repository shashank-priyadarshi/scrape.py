# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [common.proto](#common-proto)
    - [AuthenticationError](#scrape-py-v1-AuthenticationError)
    - [FieldViolation](#scrape-py-v1-FieldViolation)
    - [InternalServerError](#scrape-py-v1-InternalServerError)
    - [ResourceNotFound](#scrape-py-v1-ResourceNotFound)
    - [ValidationError](#scrape-py-v1-ValidationError)
    - [product](#scrape-py-v1-product)
    - [request](#scrape-py-v1-request)
    - [response](#scrape-py-v1-response)
  
- [Scalar Value Types](#scalar-value-types)



<a name="common-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## common.proto



<a name="scrape-py-v1-AuthenticationError"></a>

### AuthenticationError



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reason | [string](#string) |  | Optional reason for authentication failure (e.g., &#34;invalid_credentials&#34;) |






<a name="scrape-py-v1-FieldViolation"></a>

### FieldViolation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  | Name of the field with the error |
| description | [string](#string) |  | Description of the validation error |






<a name="scrape-py-v1-InternalServerError"></a>

### InternalServerError



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| details | [string](#string) |  | Optional additional details about the internal server error |






<a name="scrape-py-v1-ResourceNotFound"></a>

### ResourceNotFound



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_type | [string](#string) |  | Type of resource not found (e.g., &#34;user&#34;, &#34;product&#34;) |
| resource_id | [string](#string) |  | Optional ID of the missing resource |






<a name="scrape-py-v1-ValidationError"></a>

### ValidationError



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| violations | [FieldViolation](#scrape-py-v1-FieldViolation) | repeated | List of validation errors |






<a name="scrape-py-v1-product"></a>

### product



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| title | [string](#string) |  | Title or name of the product |
| price | [string](#string) |  | Price of the product as a string It can include currency symbols. |
| imageSource | [string](#string) |  | URL or path to the product image |
| createdAt | [google.protobuf.Timestamp](#google-protobuf-Timestamp) | optional | Timestamp when the product entry was first created |
| updatedAt | [google.protobuf.Timestamp](#google-protobuf-Timestamp) | optional | Timestamp when the product entry was last updated |






<a name="scrape-py-v1-request"></a>

### request



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| url | [string](#string) |  | The URL of the web page to be scraped. |
| proxy | [string](#string) | optional | An optional proxy server to be used for the request. If not provided, the request will be made directly. |
| depth | [int32](#int32) |  | The depth of the scraping, indicating how many levels deep the scraper should follow links on the page. |
| retryDuration | [int32](#int32) | optional | An optional duration (in seconds) to wait before retrying the request in case of a failure. If not provided, a default retry duration may be used. |






<a name="scrape-py-v1-response"></a>

### response



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| status_code | [int32](#int32) |  | HTTP status code |
| message | [string](#string) |  | User-friendly error message |
| internal_error | [InternalServerError](#scrape-py-v1-InternalServerError) |  |  |
| validation_error | [ValidationError](#scrape-py-v1-ValidationError) |  |  |
| not_found | [ResourceNotFound](#scrape-py-v1-ResourceNotFound) |  |  |
| unauthorized | [AuthenticationError](#scrape-py-v1-AuthenticationError) |  |  |





 

 

 

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

