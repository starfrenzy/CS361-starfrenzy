#
#   CS361 client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "A message from CS361" to server, expects the same message back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to CS361 server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print(f"Sending request {request} ...")
    socket.send_string("A message from CS361")

    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")
