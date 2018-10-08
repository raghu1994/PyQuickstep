
import grpc

# import the generated classes
import NetworkCli_pb2
import NetworkCli_pb2_grpc

from cursor import Cursor

class Connection():

    def __init__(self, host=None, port=None, cursorclass=Cursor):

        self.host = host
        self.port = port
        self.channel = None
        self.stub = None
        self.cursorclass = cursorclass

        #create channel and stub
        self.connect()

    def connect(self):

        insecure_channel = self.host+":"+self.port
        self.channel = grpc.insecure_channel(insecure_channel)
        self.stub = NetworkCli_pb2_grpc.NetworkCliStub(self.channel)

    def cursor(self, cursor=None):

        if cursor:
            return cursor(self)
        return self.cursorclass(self)
