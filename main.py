import sip
import socket
import logging
import time
import socketserver
import sys

PORT = 5060
hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)
print("SIP Proxy\n"
      "IP adresa servera: " + ipaddress + "\n"
      "Port servera: " + str(PORT))

def main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    logging.info(ipaddress)
    sip.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    sip.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = socketserver.UDPServer((ipaddress, PORT), sip.UDPHandler)
    server.serve_forever()

main()