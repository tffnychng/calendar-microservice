import zmq
from datetime import date

def get_date(format):
    today = date.today()
    match format:
        case "MM-DD-YYYY":
            return today.strftime('%m-%d-%Y')
        case "MM/DD/YYYY":
            return today.strftime('%m/%d/%Y')
        case "DD-MM-YYYY":
            return today.strftime('%d-%m-%Y')
        case "DD/MM/YYYY":
            return today.strftime('%d/%m/%Y')
        case "YYYY-MM-DD":
            return today.strftime('%Y-%m-%d')
        case "YYYY/MM/DD":
            return today.strftime('%Y/%m/%d')
        case _:
            return today.strftime('%Y-%m-%d')

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5551")
    print("Calendar Service running..")

    while True:
        request = socket.recv_json()
        format = request.get("format", "YYYY-MM-DD")

        current_time = get_date(format)
        response = current_time
        socket.send_string(response)

if __name__ == "__main__":
    main()
