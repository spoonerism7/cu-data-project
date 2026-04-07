from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()

# username, password, folder, permissions
authorizer.add_user("user", "12345", "ftp_root", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = "Test FTP server ready."

server = FTPServer(("127.0.0.1", 2121), handler)

print("FTP server running on 127.0.0.1:21")
server.serve_forever()