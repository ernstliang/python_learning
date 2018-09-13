# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_grpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_grpc.proto',
  package='test_grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0ftest_grpc.proto\x12\ttest_grpc\"\x1b\n\x0bTestRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\")\n\x0cTestResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\"\"\n\nAddRequest\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"+\n\x0b\x41\x64\x64Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06result\x18\x02 \x01(\x05\x32\x82\x01\n\x08TestGrpc\x12>\n\tTestHello\x12\x16.test_grpc.TestRequest\x1a\x17.test_grpc.TestResponse\"\x00\x12\x36\n\x03\x41\x64\x64\x12\x15.test_grpc.AddRequest\x1a\x16.test_grpc.AddResponse\"\x00\x62\x06proto3')
)




_TESTREQUEST = _descriptor.Descriptor(
  name='TestRequest',
  full_name='test_grpc.TestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test_grpc.TestRequest.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=57,
)


_TESTRESPONSE = _descriptor.Descriptor(
  name='TestResponse',
  full_name='test_grpc.TestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='test_grpc.TestResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='test_grpc.TestResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=100,
)


_ADDREQUEST = _descriptor.Descriptor(
  name='AddRequest',
  full_name='test_grpc.AddRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='test_grpc.AddRequest.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='test_grpc.AddRequest.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=136,
)


_ADDRESPONSE = _descriptor.Descriptor(
  name='AddResponse',
  full_name='test_grpc.AddResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='test_grpc.AddResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='test_grpc.AddResponse.result', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['TestRequest'] = _TESTREQUEST
DESCRIPTOR.message_types_by_name['TestResponse'] = _TESTRESPONSE
DESCRIPTOR.message_types_by_name['AddRequest'] = _ADDREQUEST
DESCRIPTOR.message_types_by_name['AddResponse'] = _ADDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestRequest = _reflection.GeneratedProtocolMessageType('TestRequest', (_message.Message,), dict(
  DESCRIPTOR = _TESTREQUEST,
  __module__ = 'test_grpc_pb2'
  # @@protoc_insertion_point(class_scope:test_grpc.TestRequest)
  ))
_sym_db.RegisterMessage(TestRequest)

TestResponse = _reflection.GeneratedProtocolMessageType('TestResponse', (_message.Message,), dict(
  DESCRIPTOR = _TESTRESPONSE,
  __module__ = 'test_grpc_pb2'
  # @@protoc_insertion_point(class_scope:test_grpc.TestResponse)
  ))
_sym_db.RegisterMessage(TestResponse)

AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDREQUEST,
  __module__ = 'test_grpc_pb2'
  # @@protoc_insertion_point(class_scope:test_grpc.AddRequest)
  ))
_sym_db.RegisterMessage(AddRequest)

AddResponse = _reflection.GeneratedProtocolMessageType('AddResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESPONSE,
  __module__ = 'test_grpc_pb2'
  # @@protoc_insertion_point(class_scope:test_grpc.AddResponse)
  ))
_sym_db.RegisterMessage(AddResponse)



_TESTGRPC = _descriptor.ServiceDescriptor(
  name='TestGrpc',
  full_name='test_grpc.TestGrpc',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=184,
  serialized_end=314,
  methods=[
  _descriptor.MethodDescriptor(
    name='TestHello',
    full_name='test_grpc.TestGrpc.TestHello',
    index=0,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Add',
    full_name='test_grpc.TestGrpc.Add',
    index=1,
    containing_service=None,
    input_type=_ADDREQUEST,
    output_type=_ADDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTGRPC)

DESCRIPTOR.services_by_name['TestGrpc'] = _TESTGRPC

# @@protoc_insertion_point(module_scope)
