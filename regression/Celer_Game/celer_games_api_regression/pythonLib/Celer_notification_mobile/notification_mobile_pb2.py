# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notification_mobile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import common_mobile_pb2 as common__mobile__pb2
import error__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='notification_mobile.proto',
  package='notification',
  syntax='proto3',
  serialized_options=b'\n network.celer.proto.notificationB\022NotificationMobileZ0github.com/celer-network/x-proto-go/notification\272\002\014Notification',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19notification_mobile.proto\x12\x0cnotification\x1a\x1bgoogle/protobuf/empty.proto\x1a\x13\x63ommon_mobile.proto\x1a\x0b\x65rror.proto\"\xc5\x01\n\x17RegisterEndpointRequest\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\t\x12(\n firebase_push_notification_token\x18\x03 \x01(\t\x12\x13\n\x0b\x61pp_version\x18\x04 \x01(\t\x12\'\n\x0b\x64\x65vice_type\x18\x05 \x01(\x0e\x32\x12.common.DeviceType\x12\x1f\n\x17push_permission_granted\x18\x06 \x01(\x08\"<\n\x18RegisterEndpointResponse\x12 \n\x05\x65rror\x18\x01 \x01(\x0b\x32\x11.err.BackendError\"Y\n\x18\x43lickNotificationRequest\x12 \n\x18notification_metadata_id\x18\x01 \x01(\x03\x12\x1b\n\x13notification_log_id\x18\x02 \x01(\x03\"P\n\x0e\x46\x63mDataMessage\x12\x33\n\x0bnew_history\x18\x01 \x01(\x0b\x32\x1c.notification.NewHistoryItemH\x00\x42\t\n\x07payload\"\x1d\n\x0eNewHistoryItem\x12\x0b\n\x03won\x18\x01 \x01(\x08\"}\n\x1cGetPopupInAppMessagesRequest\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\t\x12\x13\n\x0b\x61pp_version\x18\x03 \x01(\t\x12\'\n\x0b\x64\x65vice_type\x18\x04 \x01(\x0e\x32\x12.common.DeviceType\"\x81\x01\n\x1dGetPopupInAppMessagesResponse\x12 \n\x05\x65rror\x18\x01 \x01(\x0b\x32\x11.err.BackendError\x12>\n\x15popup_in_app_messages\x18\x02 \x03(\x0b\x32\x1f.notification.PopupInAppMessage\"m\n\x1dGetBannerInAppMessagesRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61pp_version\x18\x02 \x01(\t\x12\'\n\x0b\x64\x65vice_type\x18\x03 \x01(\x0e\x32\x12.common.DeviceType\"\x84\x01\n\x1eGetBannerInAppMessagesResponse\x12 \n\x05\x65rror\x18\x01 \x01(\x0b\x32\x11.err.BackendError\x12@\n\x16\x62\x61nner_in_app_messages\x18\x02 \x03(\x0b\x32 .notification.BannerInAppMessage\"\xbd\x01\n\x11PopupInAppMessage\x12 \n\x18notification_metadata_id\x18\x01 \x01(\x03\x12\x11\n\timage_url\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x13\n\x0b\x62utton_text\x18\x06 \x01(\t\x12\x0f\n\x07game_id\x18\x07 \x03(\t\x12\x1b\n\x13notification_log_id\x18\x08 \x01(\x03\"\xda\x01\n\x12\x42\x61nnerInAppMessage\x12 \n\x18notification_metadata_id\x18\x01 \x01(\x03\x12\x11\n\timage_url\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x13\n\x0b\x62utton_text\x18\x06 \x01(\t\x12\x18\n\x10\x64isplay_duration\x18\x07 \x01(\x03\x12\x11\n\tseen_time\x18\x08 \x01(\x04\x12\x1b\n\x13notification_log_id\x18\t \x01(\x03\"^\n\x1dMarkInAppMessageAsSeenRequest\x12 \n\x18notification_metadata_id\x18\x01 \x01(\x03\x12\x1b\n\x13notification_log_id\x18\x02 \x01(\x03\"c\n\"MarkPushNotificationNotSeenRequest\x12 \n\x18notification_metadata_id\x18\x01 \x01(\x03\x12\x1b\n\x13notification_log_id\x18\x02 \x01(\x03\x32\xff\x04\n\x06Mobile\x12\x63\n\x10RegisterEndpoint\x12%.notification.RegisterEndpointRequest\x1a&.notification.RegisterEndpointResponse\"\x00\x12U\n\x11\x43lickNotification\x12&.notification.ClickNotificationRequest\x1a\x16.google.protobuf.Empty\"\x00\x12r\n\x15GetPopupInAppMessages\x12*.notification.GetPopupInAppMessagesRequest\x1a+.notification.GetPopupInAppMessagesResponse\"\x00\x12u\n\x16GetBannerInAppMessages\x12+.notification.GetBannerInAppMessagesRequest\x1a,.notification.GetBannerInAppMessagesResponse\"\x00\x12\x63\n\x1aMarkInAppMessageAsSeenById\x12+.notification.MarkInAppMessageAsSeenRequest\x1a\x16.google.protobuf.Empty\"\x00\x12i\n\x1bMarkPushNotificationNotSeen\x12\x30.notification.MarkPushNotificationNotSeenRequest\x1a\x16.google.protobuf.Empty\"\x00\x42w\n network.celer.proto.notificationB\x12NotificationMobileZ0github.com/celer-network/x-proto-go/notification\xba\x02\x0cNotificationb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,common__mobile__pb2.DESCRIPTOR,error__pb2.DESCRIPTOR,])




_REGISTERENDPOINTREQUEST = _descriptor.Descriptor(
  name='RegisterEndpointRequest',
  full_name='notification.RegisterEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='notification.RegisterEndpointRequest.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='notification.RegisterEndpointRequest.app_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='firebase_push_notification_token', full_name='notification.RegisterEndpointRequest.firebase_push_notification_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_version', full_name='notification.RegisterEndpointRequest.app_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='notification.RegisterEndpointRequest.device_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='push_permission_granted', full_name='notification.RegisterEndpointRequest.push_permission_granted', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=107,
  serialized_end=304,
)


_REGISTERENDPOINTRESPONSE = _descriptor.Descriptor(
  name='RegisterEndpointResponse',
  full_name='notification.RegisterEndpointResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='notification.RegisterEndpointResponse.error', index=0,
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
  serialized_start=306,
  serialized_end=366,
)


_CLICKNOTIFICATIONREQUEST = _descriptor.Descriptor(
  name='ClickNotificationRequest',
  full_name='notification.ClickNotificationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_metadata_id', full_name='notification.ClickNotificationRequest.notification_metadata_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification_log_id', full_name='notification.ClickNotificationRequest.notification_log_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=368,
  serialized_end=457,
)


_FCMDATAMESSAGE = _descriptor.Descriptor(
  name='FcmDataMessage',
  full_name='notification.FcmDataMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_history', full_name='notification.FcmDataMessage.new_history', index=0,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='notification.FcmDataMessage.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=459,
  serialized_end=539,
)


_NEWHISTORYITEM = _descriptor.Descriptor(
  name='NewHistoryItem',
  full_name='notification.NewHistoryItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='won', full_name='notification.NewHistoryItem.won', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=541,
  serialized_end=570,
)


_GETPOPUPINAPPMESSAGESREQUEST = _descriptor.Descriptor(
  name='GetPopupInAppMessagesRequest',
  full_name='notification.GetPopupInAppMessagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_id', full_name='notification.GetPopupInAppMessagesRequest.game_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='notification.GetPopupInAppMessagesRequest.app_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_version', full_name='notification.GetPopupInAppMessagesRequest.app_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='notification.GetPopupInAppMessagesRequest.device_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=572,
  serialized_end=697,
)


_GETPOPUPINAPPMESSAGESRESPONSE = _descriptor.Descriptor(
  name='GetPopupInAppMessagesResponse',
  full_name='notification.GetPopupInAppMessagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='notification.GetPopupInAppMessagesResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='popup_in_app_messages', full_name='notification.GetPopupInAppMessagesResponse.popup_in_app_messages', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=700,
  serialized_end=829,
)


_GETBANNERINAPPMESSAGESREQUEST = _descriptor.Descriptor(
  name='GetBannerInAppMessagesRequest',
  full_name='notification.GetBannerInAppMessagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='notification.GetBannerInAppMessagesRequest.app_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_version', full_name='notification.GetBannerInAppMessagesRequest.app_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='notification.GetBannerInAppMessagesRequest.device_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=831,
  serialized_end=940,
)


_GETBANNERINAPPMESSAGESRESPONSE = _descriptor.Descriptor(
  name='GetBannerInAppMessagesResponse',
  full_name='notification.GetBannerInAppMessagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='notification.GetBannerInAppMessagesResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='banner_in_app_messages', full_name='notification.GetBannerInAppMessagesResponse.banner_in_app_messages', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=943,
  serialized_end=1075,
)


_POPUPINAPPMESSAGE = _descriptor.Descriptor(
  name='PopupInAppMessage',
  full_name='notification.PopupInAppMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_metadata_id', full_name='notification.PopupInAppMessage.notification_metadata_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='notification.PopupInAppMessage.image_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='link', full_name='notification.PopupInAppMessage.link', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='notification.PopupInAppMessage.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='notification.PopupInAppMessage.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='button_text', full_name='notification.PopupInAppMessage.button_text', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='game_id', full_name='notification.PopupInAppMessage.game_id', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification_log_id', full_name='notification.PopupInAppMessage.notification_log_id', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1078,
  serialized_end=1267,
)


_BANNERINAPPMESSAGE = _descriptor.Descriptor(
  name='BannerInAppMessage',
  full_name='notification.BannerInAppMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_metadata_id', full_name='notification.BannerInAppMessage.notification_metadata_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='notification.BannerInAppMessage.image_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='link', full_name='notification.BannerInAppMessage.link', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='notification.BannerInAppMessage.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='notification.BannerInAppMessage.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='button_text', full_name='notification.BannerInAppMessage.button_text', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_duration', full_name='notification.BannerInAppMessage.display_duration', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seen_time', full_name='notification.BannerInAppMessage.seen_time', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification_log_id', full_name='notification.BannerInAppMessage.notification_log_id', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1270,
  serialized_end=1488,
)


_MARKINAPPMESSAGEASSEENREQUEST = _descriptor.Descriptor(
  name='MarkInAppMessageAsSeenRequest',
  full_name='notification.MarkInAppMessageAsSeenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_metadata_id', full_name='notification.MarkInAppMessageAsSeenRequest.notification_metadata_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification_log_id', full_name='notification.MarkInAppMessageAsSeenRequest.notification_log_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1490,
  serialized_end=1584,
)


_MARKPUSHNOTIFICATIONNOTSEENREQUEST = _descriptor.Descriptor(
  name='MarkPushNotificationNotSeenRequest',
  full_name='notification.MarkPushNotificationNotSeenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_metadata_id', full_name='notification.MarkPushNotificationNotSeenRequest.notification_metadata_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification_log_id', full_name='notification.MarkPushNotificationNotSeenRequest.notification_log_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1586,
  serialized_end=1685,
)

_REGISTERENDPOINTREQUEST.fields_by_name['device_type'].enum_type = common__mobile__pb2._DEVICETYPE
_REGISTERENDPOINTRESPONSE.fields_by_name['error'].message_type = error__pb2._BACKENDERROR
_FCMDATAMESSAGE.fields_by_name['new_history'].message_type = _NEWHISTORYITEM
_FCMDATAMESSAGE.oneofs_by_name['payload'].fields.append(
  _FCMDATAMESSAGE.fields_by_name['new_history'])
_FCMDATAMESSAGE.fields_by_name['new_history'].containing_oneof = _FCMDATAMESSAGE.oneofs_by_name['payload']
_GETPOPUPINAPPMESSAGESREQUEST.fields_by_name['device_type'].enum_type = common__mobile__pb2._DEVICETYPE
_GETPOPUPINAPPMESSAGESRESPONSE.fields_by_name['error'].message_type = error__pb2._BACKENDERROR
_GETPOPUPINAPPMESSAGESRESPONSE.fields_by_name['popup_in_app_messages'].message_type = _POPUPINAPPMESSAGE
_GETBANNERINAPPMESSAGESREQUEST.fields_by_name['device_type'].enum_type = common__mobile__pb2._DEVICETYPE
_GETBANNERINAPPMESSAGESRESPONSE.fields_by_name['error'].message_type = error__pb2._BACKENDERROR
_GETBANNERINAPPMESSAGESRESPONSE.fields_by_name['banner_in_app_messages'].message_type = _BANNERINAPPMESSAGE
DESCRIPTOR.message_types_by_name['RegisterEndpointRequest'] = _REGISTERENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['RegisterEndpointResponse'] = _REGISTERENDPOINTRESPONSE
DESCRIPTOR.message_types_by_name['ClickNotificationRequest'] = _CLICKNOTIFICATIONREQUEST
DESCRIPTOR.message_types_by_name['FcmDataMessage'] = _FCMDATAMESSAGE
DESCRIPTOR.message_types_by_name['NewHistoryItem'] = _NEWHISTORYITEM
DESCRIPTOR.message_types_by_name['GetPopupInAppMessagesRequest'] = _GETPOPUPINAPPMESSAGESREQUEST
DESCRIPTOR.message_types_by_name['GetPopupInAppMessagesResponse'] = _GETPOPUPINAPPMESSAGESRESPONSE
DESCRIPTOR.message_types_by_name['GetBannerInAppMessagesRequest'] = _GETBANNERINAPPMESSAGESREQUEST
DESCRIPTOR.message_types_by_name['GetBannerInAppMessagesResponse'] = _GETBANNERINAPPMESSAGESRESPONSE
DESCRIPTOR.message_types_by_name['PopupInAppMessage'] = _POPUPINAPPMESSAGE
DESCRIPTOR.message_types_by_name['BannerInAppMessage'] = _BANNERINAPPMESSAGE
DESCRIPTOR.message_types_by_name['MarkInAppMessageAsSeenRequest'] = _MARKINAPPMESSAGEASSEENREQUEST
DESCRIPTOR.message_types_by_name['MarkPushNotificationNotSeenRequest'] = _MARKPUSHNOTIFICATIONNOTSEENREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterEndpointRequest = _reflection.GeneratedProtocolMessageType('RegisterEndpointRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERENDPOINTREQUEST,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.RegisterEndpointRequest)
  })
_sym_db.RegisterMessage(RegisterEndpointRequest)

RegisterEndpointResponse = _reflection.GeneratedProtocolMessageType('RegisterEndpointResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERENDPOINTRESPONSE,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.RegisterEndpointResponse)
  })
_sym_db.RegisterMessage(RegisterEndpointResponse)

ClickNotificationRequest = _reflection.GeneratedProtocolMessageType('ClickNotificationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLICKNOTIFICATIONREQUEST,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.ClickNotificationRequest)
  })
_sym_db.RegisterMessage(ClickNotificationRequest)

FcmDataMessage = _reflection.GeneratedProtocolMessageType('FcmDataMessage', (_message.Message,), {
  'DESCRIPTOR' : _FCMDATAMESSAGE,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.FcmDataMessage)
  })
_sym_db.RegisterMessage(FcmDataMessage)

NewHistoryItem = _reflection.GeneratedProtocolMessageType('NewHistoryItem', (_message.Message,), {
  'DESCRIPTOR' : _NEWHISTORYITEM,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.NewHistoryItem)
  })
_sym_db.RegisterMessage(NewHistoryItem)

GetPopupInAppMessagesRequest = _reflection.GeneratedProtocolMessageType('GetPopupInAppMessagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPOPUPINAPPMESSAGESREQUEST,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.GetPopupInAppMessagesRequest)
  })
_sym_db.RegisterMessage(GetPopupInAppMessagesRequest)

GetPopupInAppMessagesResponse = _reflection.GeneratedProtocolMessageType('GetPopupInAppMessagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPOPUPINAPPMESSAGESRESPONSE,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.GetPopupInAppMessagesResponse)
  })
_sym_db.RegisterMessage(GetPopupInAppMessagesResponse)

GetBannerInAppMessagesRequest = _reflection.GeneratedProtocolMessageType('GetBannerInAppMessagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBANNERINAPPMESSAGESREQUEST,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.GetBannerInAppMessagesRequest)
  })
_sym_db.RegisterMessage(GetBannerInAppMessagesRequest)

GetBannerInAppMessagesResponse = _reflection.GeneratedProtocolMessageType('GetBannerInAppMessagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBANNERINAPPMESSAGESRESPONSE,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.GetBannerInAppMessagesResponse)
  })
_sym_db.RegisterMessage(GetBannerInAppMessagesResponse)

PopupInAppMessage = _reflection.GeneratedProtocolMessageType('PopupInAppMessage', (_message.Message,), {
  'DESCRIPTOR' : _POPUPINAPPMESSAGE,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.PopupInAppMessage)
  })
_sym_db.RegisterMessage(PopupInAppMessage)

BannerInAppMessage = _reflection.GeneratedProtocolMessageType('BannerInAppMessage', (_message.Message,), {
  'DESCRIPTOR' : _BANNERINAPPMESSAGE,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.BannerInAppMessage)
  })
_sym_db.RegisterMessage(BannerInAppMessage)

MarkInAppMessageAsSeenRequest = _reflection.GeneratedProtocolMessageType('MarkInAppMessageAsSeenRequest', (_message.Message,), {
  'DESCRIPTOR' : _MARKINAPPMESSAGEASSEENREQUEST,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.MarkInAppMessageAsSeenRequest)
  })
_sym_db.RegisterMessage(MarkInAppMessageAsSeenRequest)

MarkPushNotificationNotSeenRequest = _reflection.GeneratedProtocolMessageType('MarkPushNotificationNotSeenRequest', (_message.Message,), {
  'DESCRIPTOR' : _MARKPUSHNOTIFICATIONNOTSEENREQUEST,
  '__module__' : 'notification_mobile_pb2'
  # @@protoc_insertion_point(class_scope:notification.MarkPushNotificationNotSeenRequest)
  })
_sym_db.RegisterMessage(MarkPushNotificationNotSeenRequest)


DESCRIPTOR._options = None

_MOBILE = _descriptor.ServiceDescriptor(
  name='Mobile',
  full_name='notification.Mobile',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1688,
  serialized_end=2327,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterEndpoint',
    full_name='notification.Mobile.RegisterEndpoint',
    index=0,
    containing_service=None,
    input_type=_REGISTERENDPOINTREQUEST,
    output_type=_REGISTERENDPOINTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ClickNotification',
    full_name='notification.Mobile.ClickNotification',
    index=1,
    containing_service=None,
    input_type=_CLICKNOTIFICATIONREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetPopupInAppMessages',
    full_name='notification.Mobile.GetPopupInAppMessages',
    index=2,
    containing_service=None,
    input_type=_GETPOPUPINAPPMESSAGESREQUEST,
    output_type=_GETPOPUPINAPPMESSAGESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBannerInAppMessages',
    full_name='notification.Mobile.GetBannerInAppMessages',
    index=3,
    containing_service=None,
    input_type=_GETBANNERINAPPMESSAGESREQUEST,
    output_type=_GETBANNERINAPPMESSAGESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MarkInAppMessageAsSeenById',
    full_name='notification.Mobile.MarkInAppMessageAsSeenById',
    index=4,
    containing_service=None,
    input_type=_MARKINAPPMESSAGEASSEENREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MarkPushNotificationNotSeen',
    full_name='notification.Mobile.MarkPushNotificationNotSeen',
    index=5,
    containing_service=None,
    input_type=_MARKPUSHNOTIFICATIONNOTSEENREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MOBILE)

DESCRIPTOR.services_by_name['Mobile'] = _MOBILE

# @@protoc_insertion_point(module_scope)