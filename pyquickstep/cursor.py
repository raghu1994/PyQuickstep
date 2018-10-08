import grpc

# import the generated classes
import NetworkCli_pb2
import NetworkCli_pb2_grpc

class Cursor(object):

    def __init__(self, connection):

        self.connection = connection


    def execute(self, query, args=None):

        #have to implement getting arguments for the query
        conn = self.connection
        request = NetworkCli_pb2.QueryRequest(query=query)
        response = conn.stub.SendQuery(request)
        return response.query_result







