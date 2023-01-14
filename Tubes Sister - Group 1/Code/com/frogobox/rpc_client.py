# import library xmlrpc client because it will be used for rpc
import xmlrpc.client

# import config file
import config

# make stub/skeleton (proxy) on client
rpcServer = xmlrpc.client.ServerProxy(config.BASE_CONFIG_URL)

# version from the client
version_client = config.BASE_VERSION_CLIENT

# shows client version
print("Version Client \t: " + str(version_client))
print("-- Checking Version From Server --")
print("Version Server \t: " + str(rpcServer.get_version_update()))  # shows server version
print()
print("Result : ")

print("----------------------------------")
if rpcServer.updated_version(version_client):  # Checking server and client version
    print("Latest Version Apps - No Need Update")
else:
    inputUser = input("Do you want upgrade version? (Y/N) ")
    if inputUser == 'y':
        # Update client version
        version_client = rpcServer.get_version_update()
        print("Thanks For Update")
        print("Version Client \t : " + str(version_client))
    elif inputUser == 'n':
        # Not updating client version
        print("Your version not updated")
        print("Version Client \t : " + str(version_client))
    else:
        print("Updating Error")
print("----------------------------------")


