# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import data_pb2 as data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='exercise',
  syntax='proto3',
  serialized_pb=b'\n\rservice.proto\x12\x08\x65xercise\x1a\ndata.proto\"\x1d\n\x0b\x44\x65\x63kRequest\x12\x0e\n\x06\x64\x65\x63kId\x18\x01 \x01(\t\",\n\x0c\x44\x65\x63kResponse\x12\x1c\n\x04\x64\x65\x63k\x18\x01 \x01(\x0b\x32\x0e.exercise.Deck\"G\n\x0fUserDeckRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x11\n\tpaginated\x18\x02 \x01(\x08\x12\x11\n\tpageToken\x18\x03 \x01(\x05\"\x86\x01\n\x10UserDeckResponse\x12\x34\n\x05\x64\x65\x63ks\x18\x01 \x03(\x0b\x32%.exercise.UserDeckResponse.DecksEntry\x1a<\n\nDecksEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.exercise.Deck:\x02\x38\x01\x32\xe3\x01\n\rDataRetrieval\x12:\n\x07GetDeck\x12\x15.exercise.DeckRequest\x1a\x16.exercise.DeckResponse\"\x00\x12\x46\n\x0bGetUserDeck\x12\x19.exercise.UserDeckRequest\x1a\x1a.exercise.UserDeckResponse\"\x00\x12N\n\x13GetDetailedUserDeck\x12\x19.exercise.UserDeckRequest\x1a\x1a.exercise.UserDeckResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[data__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DECKREQUEST = _descriptor.Descriptor(
  name='DeckRequest',
  full_name='exercise.DeckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deckId', full_name='exercise.DeckRequest.deckId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=39,
  serialized_end=68,
)


_DECKRESPONSE = _descriptor.Descriptor(
  name='DeckResponse',
  full_name='exercise.DeckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deck', full_name='exercise.DeckResponse.deck', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=70,
  serialized_end=114,
)


_USERDECKREQUEST = _descriptor.Descriptor(
  name='UserDeckRequest',
  full_name='exercise.UserDeckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='exercise.UserDeckRequest.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='paginated', full_name='exercise.UserDeckRequest.paginated', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pageToken', full_name='exercise.UserDeckRequest.pageToken', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=116,
  serialized_end=187,
)


_USERDECKRESPONSE_DECKSENTRY = _descriptor.Descriptor(
  name='DecksEntry',
  full_name='exercise.UserDeckResponse.DecksEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='exercise.UserDeckResponse.DecksEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='exercise.UserDeckResponse.DecksEntry.value', index=1,
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
  serialized_start=264,
  serialized_end=324,
)

_USERDECKRESPONSE = _descriptor.Descriptor(
  name='UserDeckResponse',
  full_name='exercise.UserDeckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='decks', full_name='exercise.UserDeckResponse.decks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_USERDECKRESPONSE_DECKSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=324,
)

_DECKRESPONSE.fields_by_name['deck'].message_type = data__pb2._DECK
_USERDECKRESPONSE_DECKSENTRY.fields_by_name['value'].message_type = data__pb2._DECK
_USERDECKRESPONSE_DECKSENTRY.containing_type = _USERDECKRESPONSE
_USERDECKRESPONSE.fields_by_name['decks'].message_type = _USERDECKRESPONSE_DECKSENTRY
DESCRIPTOR.message_types_by_name['DeckRequest'] = _DECKREQUEST
DESCRIPTOR.message_types_by_name['DeckResponse'] = _DECKRESPONSE
DESCRIPTOR.message_types_by_name['UserDeckRequest'] = _USERDECKREQUEST
DESCRIPTOR.message_types_by_name['UserDeckResponse'] = _USERDECKRESPONSE

DeckRequest = _reflection.GeneratedProtocolMessageType('DeckRequest', (_message.Message,), dict(
  DESCRIPTOR = _DECKREQUEST,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:exercise.DeckRequest)
  ))
_sym_db.RegisterMessage(DeckRequest)

DeckResponse = _reflection.GeneratedProtocolMessageType('DeckResponse', (_message.Message,), dict(
  DESCRIPTOR = _DECKRESPONSE,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:exercise.DeckResponse)
  ))
_sym_db.RegisterMessage(DeckResponse)

UserDeckRequest = _reflection.GeneratedProtocolMessageType('UserDeckRequest', (_message.Message,), dict(
  DESCRIPTOR = _USERDECKREQUEST,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:exercise.UserDeckRequest)
  ))
_sym_db.RegisterMessage(UserDeckRequest)

UserDeckResponse = _reflection.GeneratedProtocolMessageType('UserDeckResponse', (_message.Message,), dict(

  DecksEntry = _reflection.GeneratedProtocolMessageType('DecksEntry', (_message.Message,), dict(
    DESCRIPTOR = _USERDECKRESPONSE_DECKSENTRY,
    __module__ = 'service_pb2'
    # @@protoc_insertion_point(class_scope:exercise.UserDeckResponse.DecksEntry)
    ))
  ,
  DESCRIPTOR = _USERDECKRESPONSE,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:exercise.UserDeckResponse)
  ))
_sym_db.RegisterMessage(UserDeckResponse)
_sym_db.RegisterMessage(UserDeckResponse.DecksEntry)


_USERDECKRESPONSE_DECKSENTRY.has_options = True
_USERDECKRESPONSE_DECKSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
class EarlyAdopterDataRetrievalServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetDeck(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetUserDeck(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetDetailedUserDeck(self, request, context):
    raise NotImplementedError()
class EarlyAdopterDataRetrievalServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterDataRetrievalStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetDeck(self, request):
    raise NotImplementedError()
  GetDeck.async = None
  @abc.abstractmethod
  def GetUserDeck(self, request):
    raise NotImplementedError()
  GetUserDeck.async = None
  @abc.abstractmethod
  def GetDetailedUserDeck(self, request):
    raise NotImplementedError()
  GetDetailedUserDeck.async = None
def early_adopter_create_DataRetrieval_server(servicer, port, private_key=None, certificate_chain=None):
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  method_service_descriptions = {
    "GetDeck": alpha_utilities.unary_unary_service_description(
      servicer.GetDeck,
      service_pb2.DeckRequest.FromString,
      service_pb2.DeckResponse.SerializeToString,
    ),
    "GetDetailedUserDeck": alpha_utilities.unary_unary_service_description(
      servicer.GetDetailedUserDeck,
      service_pb2.UserDeckRequest.FromString,
      service_pb2.UserDeckResponse.SerializeToString,
    ),
    "GetUserDeck": alpha_utilities.unary_unary_service_description(
      servicer.GetUserDeck,
      service_pb2.UserDeckRequest.FromString,
      service_pb2.UserDeckResponse.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("exercise.DataRetrieval", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_DataRetrieval_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  method_invocation_descriptions = {
    "GetDeck": alpha_utilities.unary_unary_invocation_description(
      service_pb2.DeckRequest.SerializeToString,
      service_pb2.DeckResponse.FromString,
    ),
    "GetDetailedUserDeck": alpha_utilities.unary_unary_invocation_description(
      service_pb2.UserDeckRequest.SerializeToString,
      service_pb2.UserDeckResponse.FromString,
    ),
    "GetUserDeck": alpha_utilities.unary_unary_invocation_description(
      service_pb2.UserDeckRequest.SerializeToString,
      service_pb2.UserDeckResponse.FromString,
    ),
  }
  return early_adopter_implementations.stub("exercise.DataRetrieval", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaDataRetrievalServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetDeck(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetUserDeck(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetDetailedUserDeck(self, request, context):
    raise NotImplementedError()

class BetaDataRetrievalStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetDeck(self, request, timeout):
    raise NotImplementedError()
  GetDeck.future = None
  @abc.abstractmethod
  def GetUserDeck(self, request, timeout):
    raise NotImplementedError()
  GetUserDeck.future = None
  @abc.abstractmethod
  def GetDetailedUserDeck(self, request, timeout):
    raise NotImplementedError()
  GetDetailedUserDeck.future = None

def beta_create_DataRetrieval_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  request_deserializers = {
    ('exercise.DataRetrieval', 'GetDeck'): service_pb2.DeckRequest.FromString,
    ('exercise.DataRetrieval', 'GetDetailedUserDeck'): service_pb2.UserDeckRequest.FromString,
    ('exercise.DataRetrieval', 'GetUserDeck'): service_pb2.UserDeckRequest.FromString,
  }
  response_serializers = {
    ('exercise.DataRetrieval', 'GetDeck'): service_pb2.DeckResponse.SerializeToString,
    ('exercise.DataRetrieval', 'GetDetailedUserDeck'): service_pb2.UserDeckResponse.SerializeToString,
    ('exercise.DataRetrieval', 'GetUserDeck'): service_pb2.UserDeckResponse.SerializeToString,
  }
  method_implementations = {
    ('exercise.DataRetrieval', 'GetDeck'): face_utilities.unary_unary_inline(servicer.GetDeck),
    ('exercise.DataRetrieval', 'GetDetailedUserDeck'): face_utilities.unary_unary_inline(servicer.GetDetailedUserDeck),
    ('exercise.DataRetrieval', 'GetUserDeck'): face_utilities.unary_unary_inline(servicer.GetUserDeck),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_DataRetrieval_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  import service_pb2
  request_serializers = {
    ('exercise.DataRetrieval', 'GetDeck'): service_pb2.DeckRequest.SerializeToString,
    ('exercise.DataRetrieval', 'GetDetailedUserDeck'): service_pb2.UserDeckRequest.SerializeToString,
    ('exercise.DataRetrieval', 'GetUserDeck'): service_pb2.UserDeckRequest.SerializeToString,
  }
  response_deserializers = {
    ('exercise.DataRetrieval', 'GetDeck'): service_pb2.DeckResponse.FromString,
    ('exercise.DataRetrieval', 'GetDetailedUserDeck'): service_pb2.UserDeckResponse.FromString,
    ('exercise.DataRetrieval', 'GetUserDeck'): service_pb2.UserDeckResponse.FromString,
  }
  cardinalities = {
    'GetDeck': cardinality.Cardinality.UNARY_UNARY,
    'GetDetailedUserDeck': cardinality.Cardinality.UNARY_UNARY,
    'GetUserDeck': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'exercise.DataRetrieval', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
