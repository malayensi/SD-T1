import grpc
from concurrent import futures
import time
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2
import json

class SearchService(pb2_grpc.SearchServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        message = request.message
        f = open('productos.json',)
        data = json.load(f)
        encontrado=False
        for i in data['products']:
            if i["name"]==message:
                encontrado=True
                result = {'name': i["name"], 'price': i["price"]}
                search_res = {'product': [result]}
                return pb2.SearchResults(**search_res)
        if encontrado==False:
                return(None)
        #result = f'Hello I am up and running received "{message}" message from you'
        #result = {'name': "nombre", 'price': 123}
        #search_res = {'product': [result]}
        #return pb2.SearchResults(**search_res)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SearchServicer_to_server(SearchService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
