
# import the generated classes
import NetworkCli_pb2
from quickstepresult import QuickstepResult

class Cursor(object):

    def __init__(self, connection):

        self.connection = connection
        self.rownumber = 0
        self.rowcount = -1
        self._executed = None
        self._rows = None



    def execute(self, query, args=None):

        #have to implement getting arguments for the query
        conn = self.connection
        request = NetworkCli_pb2.QueryRequest(query=query)
        response = conn.stub.SendQuery(request)
        self._executed = query
        result = QuickstepResult(conn)
        result.parse_response(response)
        self.get_result(result)
        return result.affected_rows


    def get_result(self, result):

        self._rows = result.rows
        self._rowcount = result.affected_rows