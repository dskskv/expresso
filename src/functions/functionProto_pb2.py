# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: functionProto.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='functionProto.proto',
  package='functionSpecification',
  serialized_pb='\n\x13\x66unctionProto.proto\x12\x15\x66unctionSpecification\";\n\x05Param\x12\x32\n\x04\x66unc\x18\x01 \x03(\x0b\x32$.functionSpecification.FunctionParam\"D\n\rFunctionParam\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08\x66uncName\x18\x02 \x02(\t\x12\x13\n\x0bincludepath\x18\x03 \x03(\t')




_PARAM = _descriptor.Descriptor(
  name='Param',
  full_name='functionSpecification.Param',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='func', full_name='functionSpecification.Param.func', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=46,
  serialized_end=105,
)


_FUNCTIONPARAM = _descriptor.Descriptor(
  name='FunctionParam',
  full_name='functionSpecification.FunctionParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='functionSpecification.FunctionParam.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='funcName', full_name='functionSpecification.FunctionParam.funcName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='includepath', full_name='functionSpecification.FunctionParam.includepath', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=107,
  serialized_end=175,
)

_PARAM.fields_by_name['func'].message_type = _FUNCTIONPARAM
DESCRIPTOR.message_types_by_name['Param'] = _PARAM
DESCRIPTOR.message_types_by_name['FunctionParam'] = _FUNCTIONPARAM

class Param(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PARAM

  # @@protoc_insertion_point(class_scope:functionSpecification.Param)

class FunctionParam(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FUNCTIONPARAM

  # @@protoc_insertion_point(class_scope:functionSpecification.FunctionParam)


# @@protoc_insertion_point(module_scope)