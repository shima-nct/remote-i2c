import argparse
from .server import RemoteI2CServer

parser = argparse.ArgumentParser(conflict_handler="error")
parser.add_argument('--bus-number', type=int, default=1)
parser.add_argument('--bind-address', type=str, default="0.0.0.0")
parser.add_argument('--bind-port', type=int, default=5446)
cli = parser.parse_args()

server = RemoteI2CServer(i2c_bus_number=cli.bus_number, host=cli.bind_address, port=cli.bind_port)
server.on_client(lambda client, remote_address: print('Accepting connection from', remote_address))
print('Starting Remote I2C Server', server)
server.serve()
