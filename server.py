# Makes the server multi-connection
import multiprocessing as mp

# Main library
import socket

# System based libraries
import os
import subprocess
import sys

# Sleep function
from time import sleep


def worker(socket: socket.socket):
    """
    The main worker function that listens for connections.

    Args:
        socket (socket.socket): socket class
    """

    # While loop makes it so that workers go back to listening immediately after finishing its task
    while True:

        try:
            # Constructs client object and collects client's address
            client, address = socket.accept()
            print(f"[NEW CONNECTION] {address} connected.")

            # Recives the name of the file
            filename = client.recv(1024).decode()

            # Creates a file, will keep it stored for record keeping
            with open(f"{filename}", "w") as file:

                # Tells client it recieved the file name
                client.send("Recieved file name".encode())

                # Receives file information and writes it to the created file
                data = client.recv(1024).decode()
                file.write(data)

                # Tells the client that it recieved the file
                client.send("File received successfully!".encode())

            # Gathers path, makes it so that this program can be run anywhere and it will execute files correctly
            path = os.path.abspath(filename)

            # Ensures that no remaining data has yet to be sent to the client
            sleep(1)

            # Sends an update to the client
            client.send(f"Executing {filename}".encode())

            # Executes the file using a subprocess
            answer = subprocess.check_output(f'{sys.executable} "{path}"')
            
            # Sends the output of the file, sleep ensures full data transfer
            client.send(f"File output: {answer.decode()}".encode())
            sleep(1)

            # Sends sentinel to the client, informing that the server is done.
            client.send("I am done".encode())
            sleep(1)
            client.close()

        except ConnectionResetError:
            print("The client has disconnected unexpectedly!")
            pass

# Runs main program
if __name__ == '__main__':

    # Sets the number of workers to the number of processors
    num_workers = mp.cpu_count()
    workers = []

    # Creates TCP socket with the port 9091
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9091))

    # Sets the number of maximum connections to the number of processors
    server.listen(num_workers)

    # Creates worker processes
    for i in range(num_workers):
        workers.append(mp.Process(worker(server)))

    # Creates workers
    for p in workers:
        p.daemon = True
        p.start()
