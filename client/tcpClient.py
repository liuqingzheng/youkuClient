import socket
from conf import setting

def client_conn():
    # 先建立连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(setting.server_address)
    return client
