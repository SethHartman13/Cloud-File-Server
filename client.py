# Main library
import socket

# Time based functions
from time import perf_counter as stopwatch
from time import sleep


# Sets up the IP address so that the client can call the server.
IP = "10.40.4.120"

# The server needs this port to be correct!
PORT = 9091
ADDR = (IP, PORT)

# Sets packet size limit to 1024 bytes
PACKET_SIZE = 1024


def main(file_name: str) -> None:
    """
    Main program that communicates with the server program by sending a
    python file.

    Args:
        file_name (str): name of the python file being sent to the servers.
    """
    print("starting process")

    # Starts a TCP Socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Function that connects the client to the server (based upon ip address and port)
    server.connect(ADDR)

    # Opening the file and storing the information from the file
    with open(file_name, "r") as file:
        data = file.read()

    # Sends the file_name to the server by converting the str object into a byte object
    server.send(file_name.encode())

    # Recieves message from the server by converting the byte object to str object
    msg = server.recv(PACKET_SIZE).decode()

    # Sends the file data to the server by converting the str object into a byte object
    server.sendall(data.encode())

    # Tells the client to listen for messages from the server
    try:
        while True:
            sleep(1)
            msg = server.recv(PACKET_SIZE).decode()
            msg.strip()

            # If the server has not sent anything
            if msg == "":
                pass

            # If the server has sent anything
            else:
                # Checks for sentinel, telling the client the server is done.
                if msg == "I am done":
                    server.close()
                    break

                # Prints out message from server
                else:
                    print(f"[SERVER] {msg}")
                    sleep(1)

    # This error occurs when the server closes unexpectedly
    except ConnectionResetError:
        print("[SERVER] Server closed unexpectedly!")


# Runs program if executed directly
if __name__ == "__main__":

    # Ensures proper user input
    while True:
        file_name = input(
            "What is the name of the python file you wish to be sent to the server? ")

        try:
            with open(file_name) as file_test:
                print(f"{file_name} has been found!")

        except:
            print("That file does not exist! Please enter an existing python file. ")

        else:
            break

    # Start stopwatch
    begin_time = stopwatch()

    # Run main file
    main(file_name)

    # End stopwatch
    total_time = "{:.2f}".format(stopwatch() - begin_time)
    print(f'Total time = {total_time} sec')
