import sip
import socket
import logging
import socketserver


PORT = 5060
hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)
message = "SIP Proxy\nIP adresa servera: " + ipaddress + "\nPort servera: " + str(PORT)
print(message)

def main():
    logging.basicConfig(format='%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(message)
    sip.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    sip.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = socketserver.UDPServer((ipaddress, PORT), sip.UDPHandler)
    server.serve_forever()

main()