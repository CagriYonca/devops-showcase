class Server:
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

    def listener(self, username, password):
        if (username == self.username) and (password == self.password):
            return True
        else:
            return False


class Network(object):
    def __init__(self, ip_addr, username, password):
        self.server = Server(ip_addr, username, password)

    def connect(self, ip_addr, username, password):
        if (self.server.ip_addr == ip_addr) and (self.server.listener(username, password)):
            return 'Connection successful'
        else:
            return 'Connection broken'


class Client:
    def __init__(self, network, ip_addr, username, password):
        self.network = network
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

    def connect(self):
        print(self.network.connect(self.ip_addr, self.username, self.password))


network = Network('127.0.0.1', 'admin', '123')
client = Client(network, '127.0.0.1', 'admin', '123')
client.connect()
