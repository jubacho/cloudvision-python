# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/dashboard.v1/dashboard.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from fmp import extensions_pb2 as fmp_dot_extensions__pb2
from fmp import wrappers_pb2 as fmp_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='arista/dashboard.v1/dashboard.proto',
  package='arista.dashboard.v1',
  syntax='proto3',
  serialized_options=b'Z.arista/resources/arista/dashboard.v1;dashboard',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#arista/dashboard.v1/dashboard.proto\x12\x13\x61rista.dashboard.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x14\x66mp/extensions.proto\x1a\x12\x66mp/wrappers.proto\"\\\n\x08Position\x12\'\n\x01x\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\'\n\x01y\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"g\n\nDimensions\x12+\n\x05width\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12,\n\x06height\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"\xce\x02\n\x06Widget\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x08position\x18\x03 \x01(\x0b\x32\x1d.arista.dashboard.v1.Position\x12\x33\n\ndimensions\x18\x04 \x01(\x0b\x32\x1f.arista.dashboard.v1.Dimensions\x12*\n\x04type\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06inputs\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08location\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"6\n\x07Widgets\x12+\n\x06values\x18\x01 \x03(\x0b\x32\x1b.arista.dashboard.v1.Widget\"H\n\x0c\x44\x61shboardKey\x12\x32\n\x0c\x64\x61shboard_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\xd7\x01\n\x0f\x44\x61shboardConfig\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07widgets\x18\x04 \x01(\x0b\x32\x1c.arista.dashboard.v1.Widgets:\x06\xfa\x8d\x19\x02rw\"\xb1\x01\n\x11\x44\x61shboardMetadata\x12\x34\n\x0eschema_version\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nlegacy_key\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0elegacy_version\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"+\n\x06\x46ilter\x12!\n\x04tags\x18\x01 \x01(\x0b\x32\x13.fmp.RepeatedString\"\xe8\x03\n\tDashboard\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\ncreated_by\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x10last_modified_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x10last_modified_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x39\n\tmeta_data\x18\x06 \x01(\x0b\x32&.arista.dashboard.v1.DashboardMetadata\x12*\n\x04name\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07widgets\x18\t \x01(\x0b\x32\x1c.arista.dashboard.v1.Widgets:\x12\xfa\x8d\x19\x02ro\x8a\x8e\x19\x08[]Filter\"]\n\x15GlobalDashboardConfig\x12<\n\x11\x64\x65\x66\x61ult_dashboard\x18\x01 \x01(\x0b\x32!.arista.dashboard.v1.DashboardKey:\x06\xa2\x8e\x19\x02rwB0Z.arista/resources/arista/dashboard.v1;dashboardb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,fmp_dot_extensions__pb2.DESCRIPTOR,fmp_dot_wrappers__pb2.DESCRIPTOR,])




_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='arista.dashboard.v1.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='arista.dashboard.v1.Position.x', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='arista.dashboard.v1.Position.y', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=167,
  serialized_end=259,
)


_DIMENSIONS = _descriptor.Descriptor(
  name='Dimensions',
  full_name='arista.dashboard.v1.Dimensions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='arista.dashboard.v1.Dimensions.width', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='arista.dashboard.v1.Dimensions.height', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=261,
  serialized_end=364,
)


_WIDGET = _descriptor.Descriptor(
  name='Widget',
  full_name='arista.dashboard.v1.Widget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='arista.dashboard.v1.Widget.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='arista.dashboard.v1.Widget.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position', full_name='arista.dashboard.v1.Widget.position', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='arista.dashboard.v1.Widget.dimensions', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='arista.dashboard.v1.Widget.type', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='arista.dashboard.v1.Widget.inputs', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='arista.dashboard.v1.Widget.location', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=367,
  serialized_end=701,
)


_WIDGETS = _descriptor.Descriptor(
  name='Widgets',
  full_name='arista.dashboard.v1.Widgets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='arista.dashboard.v1.Widgets.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=703,
  serialized_end=757,
)


_DASHBOARDKEY = _descriptor.Descriptor(
  name='DashboardKey',
  full_name='arista.dashboard.v1.DashboardKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dashboard_id', full_name='arista.dashboard.v1.DashboardKey.dashboard_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\200\216\031\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=759,
  serialized_end=831,
)


_DASHBOARDCONFIG = _descriptor.Descriptor(
  name='DashboardConfig',
  full_name='arista.dashboard.v1.DashboardConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='arista.dashboard.v1.DashboardConfig.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='arista.dashboard.v1.DashboardConfig.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='arista.dashboard.v1.DashboardConfig.description', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='widgets', full_name='arista.dashboard.v1.DashboardConfig.widgets', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\215\031\002rw',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=834,
  serialized_end=1049,
)


_DASHBOARDMETADATA = _descriptor.Descriptor(
  name='DashboardMetadata',
  full_name='arista.dashboard.v1.DashboardMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema_version', full_name='arista.dashboard.v1.DashboardMetadata.schema_version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='legacy_key', full_name='arista.dashboard.v1.DashboardMetadata.legacy_key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='legacy_version', full_name='arista.dashboard.v1.DashboardMetadata.legacy_version', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1052,
  serialized_end=1229,
)


_FILTER = _descriptor.Descriptor(
  name='Filter',
  full_name='arista.dashboard.v1.Filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='arista.dashboard.v1.Filter.tags', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1231,
  serialized_end=1274,
)


_DASHBOARD = _descriptor.Descriptor(
  name='Dashboard',
  full_name='arista.dashboard.v1.Dashboard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='arista.dashboard.v1.Dashboard.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='arista.dashboard.v1.Dashboard.created_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_by', full_name='arista.dashboard.v1.Dashboard.created_by', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_modified_at', full_name='arista.dashboard.v1.Dashboard.last_modified_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_modified_by', full_name='arista.dashboard.v1.Dashboard.last_modified_by', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta_data', full_name='arista.dashboard.v1.Dashboard.meta_data', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='arista.dashboard.v1.Dashboard.name', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='arista.dashboard.v1.Dashboard.description', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='widgets', full_name='arista.dashboard.v1.Dashboard.widgets', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\215\031\002ro\212\216\031\010[]Filter',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1277,
  serialized_end=1765,
)


_GLOBALDASHBOARDCONFIG = _descriptor.Descriptor(
  name='GlobalDashboardConfig',
  full_name='arista.dashboard.v1.GlobalDashboardConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='default_dashboard', full_name='arista.dashboard.v1.GlobalDashboardConfig.default_dashboard', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\242\216\031\002rw',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1767,
  serialized_end=1860,
)

_POSITION.fields_by_name['x'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_POSITION.fields_by_name['y'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_DIMENSIONS.fields_by_name['width'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_DIMENSIONS.fields_by_name['height'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_WIDGET.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_WIDGET.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_WIDGET.fields_by_name['position'].message_type = _POSITION
_WIDGET.fields_by_name['dimensions'].message_type = _DIMENSIONS
_WIDGET.fields_by_name['type'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_WIDGET.fields_by_name['inputs'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_WIDGET.fields_by_name['location'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_WIDGETS.fields_by_name['values'].message_type = _WIDGET
_DASHBOARDKEY.fields_by_name['dashboard_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DASHBOARDCONFIG.fields_by_name['key'].message_type = _DASHBOARDKEY
_DASHBOARDCONFIG.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DASHBOARDCONFIG.fields_by_name['description'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DASHBOARDCONFIG.fields_by_name['widgets'].message_type = _WIDGETS
_DASHBOARDMETADATA.fields_by_name['schema_version'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DASHBOARDMETADATA.fields_by_name['legacy_key'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DASHBOARDMETADATA.fields_by_name['legacy_version'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_FILTER.fields_by_name['tags'].message_type = fmp_dot_wrappers__pb2._REPEATEDSTRING
_DASHBOARD.fields_by_name['key'].message_type = _DASHBOARDKEY
_DASHBOARD.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DASHBOARD.fields_by_name['created_by'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DASHBOARD.fields_by_name['last_modified_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DASHBOARD.fields_by_name['last_modified_by'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DASHBOARD.fields_by_name['meta_data'].message_type = _DASHBOARDMETADATA
_DASHBOARD.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DASHBOARD.fields_by_name['description'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DASHBOARD.fields_by_name['widgets'].message_type = _WIDGETS
_GLOBALDASHBOARDCONFIG.fields_by_name['default_dashboard'].message_type = _DASHBOARDKEY
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Dimensions'] = _DIMENSIONS
DESCRIPTOR.message_types_by_name['Widget'] = _WIDGET
DESCRIPTOR.message_types_by_name['Widgets'] = _WIDGETS
DESCRIPTOR.message_types_by_name['DashboardKey'] = _DASHBOARDKEY
DESCRIPTOR.message_types_by_name['DashboardConfig'] = _DASHBOARDCONFIG
DESCRIPTOR.message_types_by_name['DashboardMetadata'] = _DASHBOARDMETADATA
DESCRIPTOR.message_types_by_name['Filter'] = _FILTER
DESCRIPTOR.message_types_by_name['Dashboard'] = _DASHBOARD
DESCRIPTOR.message_types_by_name['GlobalDashboardConfig'] = _GLOBALDASHBOARDCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'arista.dashboard.v1.dashboard_pb2'
  # @@protoc_insertion_point(class_scope:arista.dashboard.v1.Position)
  })
_sym_db.RegisterMessage(Position)

Dimensions = _reflection.GeneratedProtocolMessageType('Dimensions', (_message.Message,), {
  'DESCRIPTOR' : _DIMENSIONS,
  '__module__' : 'arista.dashboard.v1.dashboard_pb2'
  # @@protoc_insertion_point(class_scope:arista.dashboard.v1.Dimensions)
  })
_sym_db.RegisterMessage(Dimensions)

Widget = _reflection.GeneratedProtocolMessageType('Widget', (_message.Message,), {
  'DESCRIPTOR' : _WIDGET,
  '__module__' : 'arista.dashboard.v1.dashboard_pb2'
  # @@protoc_insertion_point(class_scope:arista.dashboard.v1.Widget)
  })
_sym_db.RegisterMessage(Widget)

Widgets = _reflection.GeneratedProtocolMessageType('Widgets', (_message.Message,), {
  'DESCRIPTOR' : _WIDGETS,
  '__module__' : 'arista.dashboard.v1.dashboard_pb2'
  # @@protoc_insertion_point(class_scope:arista.dashboard.v1.Widgets)
  })
_sym_db.RegisterMessage(Widgets)

DashboardKey = _reflection.GeneratedProtocolMessageType('DashboardKey', (_message.Message,), {
  'DESCRIPTOR' : _DASHBOARDKEY,
  '__module__' : 'arista.dashboard.v1.dashboard_pb2'
  # @@protoc_insertion_point(class_scope:arista.dashboard.v1.DashboardKey)
  })
_sym_db.RegisterMessage(DashboardKey)

DashboardConfig = _reflection.GeneratedProtocolMessageType('DashboardConfig', (_message.Message,), {
  'DESCRIPTOR' : _DASHBOARDCONFIG,
  '__module__' : 'arista.dashboard.v1.dashboard_pb2'
  # @@protoc_insertion_point(class_scope:arista.dashboard.v1.DashboardConfig)
  })
_sym_db.RegisterMessage(DashboardConfig)

DashboardMetadata = _reflection.GeneratedProtocolMessageType('DashboardMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DASHBOARDMETADATA,
  '__module__' : 'arista.dashboard.v1.dashboard_pb2'
  # @@protoc_insertion_point(class_scope:arista.dashboard.v1.DashboardMetadata)
  })
_sym_db.RegisterMessage(DashboardMetadata)

Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {
  'DESCRIPTOR' : _FILTER,
  '__module__' : 'arista.dashboard.v1.dashboard_pb2'
  # @@protoc_insertion_point(class_scope:arista.dashboard.v1.Filter)
  })
_sym_db.RegisterMessage(Filter)

Dashboard = _reflection.GeneratedProtocolMessageType('Dashboard', (_message.Message,), {
  'DESCRIPTOR' : _DASHBOARD,
  '__module__' : 'arista.dashboard.v1.dashboard_pb2'
  # @@protoc_insertion_point(class_scope:arista.dashboard.v1.Dashboard)
  })
_sym_db.RegisterMessage(Dashboard)

GlobalDashboardConfig = _reflection.GeneratedProtocolMessageType('GlobalDashboardConfig', (_message.Message,), {
  'DESCRIPTOR' : _GLOBALDASHBOARDCONFIG,
  '__module__' : 'arista.dashboard.v1.dashboard_pb2'
  # @@protoc_insertion_point(class_scope:arista.dashboard.v1.GlobalDashboardConfig)
  })
_sym_db.RegisterMessage(GlobalDashboardConfig)


DESCRIPTOR._options = None
_DASHBOARDKEY._options = None
_DASHBOARDCONFIG._options = None
_DASHBOARD._options = None
_GLOBALDASHBOARDCONFIG._options = None
# @@protoc_insertion_point(module_scope)
