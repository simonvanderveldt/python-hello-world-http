#!/usr/bin/python
# From http://www.acmesystems.it/python_httpserver
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import sys

PORT_NUMBER = 8080

hellostring = "Hello world\n"

if len(sys.argv) > 1:
    hellostring = "Hello world: " + sys.argv[1:][0] + "\n"


class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(hellostring)
        return

try:
    #Create a web server and define the handler to manage the incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
