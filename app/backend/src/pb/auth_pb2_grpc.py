# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pb import auth_pb2 as pb_dot_auth__pb2


class AuthStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/auth.Auth/Login',
                request_serializer=pb_dot_auth__pb2.LoginReq.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.LoginRes.FromString,
                )
        self.Signup = channel.unary_unary(
                '/auth.Auth/Signup',
                request_serializer=pb_dot_auth__pb2.SignupReq.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.SignupRes.FromString,
                )
        self.CompleteTokenLogin = channel.unary_unary(
                '/auth.Auth/CompleteTokenLogin',
                request_serializer=pb_dot_auth__pb2.CompleteTokenLoginReq.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.AuthRes.FromString,
                )
        self.UsernameValid = channel.unary_unary(
                '/auth.Auth/UsernameValid',
                request_serializer=pb_dot_auth__pb2.UsernameValidReq.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.UsernameValidRes.FromString,
                )
        self.SignupTokenInfo = channel.unary_unary(
                '/auth.Auth/SignupTokenInfo',
                request_serializer=pb_dot_auth__pb2.SignupTokenInfoReq.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.SignupTokenInfoRes.FromString,
                )
        self.CompleteSignup = channel.unary_unary(
                '/auth.Auth/CompleteSignup',
                request_serializer=pb_dot_auth__pb2.CompleteSignupReq.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.AuthRes.FromString,
                )
        self.Authenticate = channel.unary_unary(
                '/auth.Auth/Authenticate',
                request_serializer=pb_dot_auth__pb2.AuthReq.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.AuthRes.FromString,
                )
        self.Deauthenticate = channel.unary_unary(
                '/auth.Auth/Deauthenticate',
                request_serializer=pb_dot_auth__pb2.DeAuthReq.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.DeAuthRes.FromString,
                )


class AuthServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Login(self, request, context):
        """First step of login flow
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Signup(self, request, context):
        """First step of signup flow
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteTokenLogin(self, request, context):
        """Complete a login after receiving an email with a login token
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UsernameValid(self, request, context):
        """Check whether the username is valid
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignupTokenInfo(self, request, context):
        """returns info about a signup token
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteSignup(self, request, context):
        """Complete the signup form
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Authenticate(self, request, context):
        """Auth a user with username + password
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deauthenticate(self, request, context):
        """Invalidate a session, deauthing a user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=pb_dot_auth__pb2.LoginReq.FromString,
                    response_serializer=pb_dot_auth__pb2.LoginRes.SerializeToString,
            ),
            'Signup': grpc.unary_unary_rpc_method_handler(
                    servicer.Signup,
                    request_deserializer=pb_dot_auth__pb2.SignupReq.FromString,
                    response_serializer=pb_dot_auth__pb2.SignupRes.SerializeToString,
            ),
            'CompleteTokenLogin': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteTokenLogin,
                    request_deserializer=pb_dot_auth__pb2.CompleteTokenLoginReq.FromString,
                    response_serializer=pb_dot_auth__pb2.AuthRes.SerializeToString,
            ),
            'UsernameValid': grpc.unary_unary_rpc_method_handler(
                    servicer.UsernameValid,
                    request_deserializer=pb_dot_auth__pb2.UsernameValidReq.FromString,
                    response_serializer=pb_dot_auth__pb2.UsernameValidRes.SerializeToString,
            ),
            'SignupTokenInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.SignupTokenInfo,
                    request_deserializer=pb_dot_auth__pb2.SignupTokenInfoReq.FromString,
                    response_serializer=pb_dot_auth__pb2.SignupTokenInfoRes.SerializeToString,
            ),
            'CompleteSignup': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteSignup,
                    request_deserializer=pb_dot_auth__pb2.CompleteSignupReq.FromString,
                    response_serializer=pb_dot_auth__pb2.AuthRes.SerializeToString,
            ),
            'Authenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.Authenticate,
                    request_deserializer=pb_dot_auth__pb2.AuthReq.FromString,
                    response_serializer=pb_dot_auth__pb2.AuthRes.SerializeToString,
            ),
            'Deauthenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.Deauthenticate,
                    request_deserializer=pb_dot_auth__pb2.DeAuthReq.FromString,
                    response_serializer=pb_dot_auth__pb2.DeAuthRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.Auth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Auth(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Login',
            pb_dot_auth__pb2.LoginReq.SerializeToString,
            pb_dot_auth__pb2.LoginRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Signup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Signup',
            pb_dot_auth__pb2.SignupReq.SerializeToString,
            pb_dot_auth__pb2.SignupRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompleteTokenLogin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/CompleteTokenLogin',
            pb_dot_auth__pb2.CompleteTokenLoginReq.SerializeToString,
            pb_dot_auth__pb2.AuthRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UsernameValid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/UsernameValid',
            pb_dot_auth__pb2.UsernameValidReq.SerializeToString,
            pb_dot_auth__pb2.UsernameValidRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignupTokenInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/SignupTokenInfo',
            pb_dot_auth__pb2.SignupTokenInfoReq.SerializeToString,
            pb_dot_auth__pb2.SignupTokenInfoRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompleteSignup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/CompleteSignup',
            pb_dot_auth__pb2.CompleteSignupReq.SerializeToString,
            pb_dot_auth__pb2.AuthRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Authenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Authenticate',
            pb_dot_auth__pb2.AuthReq.SerializeToString,
            pb_dot_auth__pb2.AuthRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deauthenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Deauthenticate',
            pb_dot_auth__pb2.DeAuthReq.SerializeToString,
            pb_dot_auth__pb2.DeAuthRes.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)