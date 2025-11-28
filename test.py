import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5551")

print("MM-DD-YYYY format")
socket.send_json({"format": "MM-DD-YYYY"})
response = socket.recv_string()
print(response)

print("DD-MM-YYYY format")
socket.send_json({"format": "DD-MM-YYYY"})
response = socket.recv_string()
print(response)

print("YYYY-MM-DD format")
socket.send_json({"format": "YYYY-MM-DD"})
response = socket.recv_string()
print(response)

print("YYYY/MM/DD format")
socket.send_json({"format": "YYYY/MM/DD"})
response = socket.recv_string()
print(response)