# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import league_mobile_pb2 as league__mobile__pb2


class MobileStub(object):
    """League Mobile API service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetActiveLeague = channel.unary_unary(
                '/league.Mobile/GetActiveLeague',
                request_serializer=league__mobile__pb2.LeagueTypeRequest.SerializeToString,
                response_deserializer=league__mobile__pb2.ActiveLeagueResponse.FromString,
                )
        self.GetActiveLeagues = channel.unary_unary(
                '/league.Mobile/GetActiveLeagues',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=league__mobile__pb2.ActiveLeaguesResponse.FromString,
                )
        self.GetActiveLeagueRankings = channel.unary_unary(
                '/league.Mobile/GetActiveLeagueRankings',
                request_serializer=league__mobile__pb2.GetActiveLeagueRankingsRequest.SerializeToString,
                response_deserializer=league__mobile__pb2.LeagueRankingsResponse.FromString,
                )
        self.GetLeagueRankings = channel.unary_unary(
                '/league.Mobile/GetLeagueRankings',
                request_serializer=league__mobile__pb2.GetLeagueRankingsRequest.SerializeToString,
                response_deserializer=league__mobile__pb2.LeagueRankingsResponse.FromString,
                )
        self.GetMyActiveLeagueRanking = channel.unary_unary(
                '/league.Mobile/GetMyActiveLeagueRanking',
                request_serializer=league__mobile__pb2.LeagueTypeRequest.SerializeToString,
                response_deserializer=league__mobile__pb2.LeagueRankingResponse.FromString,
                )
        self.GetMyLeagueRanking = channel.unary_unary(
                '/league.Mobile/GetMyLeagueRanking',
                request_serializer=league__mobile__pb2.LeagueIdStringRequest.SerializeToString,
                response_deserializer=league__mobile__pb2.LeagueRankingResponse.FromString,
                )
        self.GetLastLeagueResults = channel.unary_unary(
                '/league.Mobile/GetLastLeagueResults',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=league__mobile__pb2.LastLeagueResultsResponse.FromString,
                )


class MobileServicer(object):
    """League Mobile API service
    """

    def GetActiveLeague(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActiveLeagues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActiveLeagueRankings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLeagueRankings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMyActiveLeagueRanking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMyLeagueRanking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastLeagueResults(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MobileServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetActiveLeague': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActiveLeague,
                    request_deserializer=league__mobile__pb2.LeagueTypeRequest.FromString,
                    response_serializer=league__mobile__pb2.ActiveLeagueResponse.SerializeToString,
            ),
            'GetActiveLeagues': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActiveLeagues,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=league__mobile__pb2.ActiveLeaguesResponse.SerializeToString,
            ),
            'GetActiveLeagueRankings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActiveLeagueRankings,
                    request_deserializer=league__mobile__pb2.GetActiveLeagueRankingsRequest.FromString,
                    response_serializer=league__mobile__pb2.LeagueRankingsResponse.SerializeToString,
            ),
            'GetLeagueRankings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLeagueRankings,
                    request_deserializer=league__mobile__pb2.GetLeagueRankingsRequest.FromString,
                    response_serializer=league__mobile__pb2.LeagueRankingsResponse.SerializeToString,
            ),
            'GetMyActiveLeagueRanking': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMyActiveLeagueRanking,
                    request_deserializer=league__mobile__pb2.LeagueTypeRequest.FromString,
                    response_serializer=league__mobile__pb2.LeagueRankingResponse.SerializeToString,
            ),
            'GetMyLeagueRanking': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMyLeagueRanking,
                    request_deserializer=league__mobile__pb2.LeagueIdStringRequest.FromString,
                    response_serializer=league__mobile__pb2.LeagueRankingResponse.SerializeToString,
            ),
            'GetLastLeagueResults': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastLeagueResults,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=league__mobile__pb2.LastLeagueResultsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'league.Mobile', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mobile(object):
    """League Mobile API service
    """

    @staticmethod
    def GetActiveLeague(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/league.Mobile/GetActiveLeague',
            league__mobile__pb2.LeagueTypeRequest.SerializeToString,
            league__mobile__pb2.ActiveLeagueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActiveLeagues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/league.Mobile/GetActiveLeagues',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            league__mobile__pb2.ActiveLeaguesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActiveLeagueRankings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/league.Mobile/GetActiveLeagueRankings',
            league__mobile__pb2.GetActiveLeagueRankingsRequest.SerializeToString,
            league__mobile__pb2.LeagueRankingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLeagueRankings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/league.Mobile/GetLeagueRankings',
            league__mobile__pb2.GetLeagueRankingsRequest.SerializeToString,
            league__mobile__pb2.LeagueRankingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMyActiveLeagueRanking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/league.Mobile/GetMyActiveLeagueRanking',
            league__mobile__pb2.LeagueTypeRequest.SerializeToString,
            league__mobile__pb2.LeagueRankingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMyLeagueRanking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/league.Mobile/GetMyLeagueRanking',
            league__mobile__pb2.LeagueIdStringRequest.SerializeToString,
            league__mobile__pb2.LeagueRankingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLastLeagueResults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/league.Mobile/GetLastLeagueResults',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            league__mobile__pb2.LastLeagueResultsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)