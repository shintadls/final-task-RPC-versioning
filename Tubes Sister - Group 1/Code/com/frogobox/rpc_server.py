# use xmlrpc server
# import SimpleXMLRPCServer and SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# make a requesthandler class
# from com.frogobox.config import *
import config
class RequestHandler(SimpleXMLRPCRequestHandler):
    # limit the path /RPC2
    rpc_paths = (config.BASE_CONFIG_PATH)

# declare server version
version_server = config.BASE_VERSION_SERVER

# shows server verison
print("Version Server \t: " + str(version_server))

# make server and register as a register_introspection_functions()
rpcServer = SimpleXMLRPCServer((config.BASE_CONFIG_IP_ADDRESS, config.BASE_CONFIG_PORT), requestHandler=RequestHandler)
rpcServer.register_introspection_functions()


# function to check version
def updated_version(version_client):
    if version_client == version_server:
        return True
    else:
        return False


# function to return server version value
def get_version_update():
    return version_server


# register the function
rpcServer.register_function(updated_version, 'updated_version')
rpcServer.register_function(get_version_update, 'get_version_update')

# run the server
rpcServer.serve_forever()

