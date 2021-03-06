# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data.proto',
  package='exercise',
  syntax='proto3',
  serialized_pb=b'\n\ndata.proto\x12\x08\x65xercise\"\t\n\x07Payload\"E\n\x04\x43\x61rd\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\"\n\x07payload\x18\x03 \x01(\x0b\x32\x11.exercise.Payload\"\xcd\x01\n\x04\x44\x65\x63k\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65\x63kId\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12(\n\x05\x63\x61rds\x18\x04 \x03(\x0b\x32\x19.exercise.Deck.CardsEntry\x12\x11\n\tpageToken\x18\x05 \x01(\x05\x12\x15\n\rnextPageToken\x18\x06 \x01(\x05\x1a<\n\nCardsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.exercise.Card:\x02\x38\x01\x62\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='exercise.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=33,
)


_CARD = _descriptor.Descriptor(
  name='Card',
  full_name='exercise.Card',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='exercise.Card.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='exercise.Card.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='exercise.Card.payload', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=104,
)


_DECK_CARDSENTRY = _descriptor.Descriptor(
  name='CardsEntry',
  full_name='exercise.Deck.CardsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='exercise.Deck.CardsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='exercise.Deck.CardsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=312,
)

_DECK = _descriptor.Descriptor(
  name='Deck',
  full_name='exercise.Deck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='exercise.Deck.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deckId', full_name='exercise.Deck.deckId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='exercise.Deck.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cards', full_name='exercise.Deck.cards', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pageToken', full_name='exercise.Deck.pageToken', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nextPageToken', full_name='exercise.Deck.nextPageToken', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DECK_CARDSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=312,
)

_CARD.fields_by_name['payload'].message_type = _PAYLOAD
_DECK_CARDSENTRY.fields_by_name['value'].message_type = _CARD
_DECK_CARDSENTRY.containing_type = _DECK
_DECK.fields_by_name['cards'].message_type = _DECK_CARDSENTRY
DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD
DESCRIPTOR.message_types_by_name['Card'] = _CARD
DESCRIPTOR.message_types_by_name['Deck'] = _DECK

Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(
  DESCRIPTOR = _PAYLOAD,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:exercise.Payload)
  ))
_sym_db.RegisterMessage(Payload)

Card = _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), dict(
  DESCRIPTOR = _CARD,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:exercise.Card)
  ))
_sym_db.RegisterMessage(Card)

Deck = _reflection.GeneratedProtocolMessageType('Deck', (_message.Message,), dict(

  CardsEntry = _reflection.GeneratedProtocolMessageType('CardsEntry', (_message.Message,), dict(
    DESCRIPTOR = _DECK_CARDSENTRY,
    __module__ = 'data_pb2'
    # @@protoc_insertion_point(class_scope:exercise.Deck.CardsEntry)
    ))
  ,
  DESCRIPTOR = _DECK,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:exercise.Deck)
  ))
_sym_db.RegisterMessage(Deck)
_sym_db.RegisterMessage(Deck.CardsEntry)


_DECK_CARDSENTRY.has_options = True
_DECK_CARDSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
