import socket
import threading
import base64
import hashlib
import time
from modules.randomData import generate_random_message


def parse_headers(data):
    """
    Parse HTTP headers from the received data.

    Parameters:
    - data (str): The raw data containing HTTP headers.

    Returns:
    - dict: A dictionary containing parsed headers.

    Made by Andre Ribeiro <andrepedroribeiro@ua.pt>
    """
    headers = {}
    lines = data.splitlines()
    for line in lines[1:]:
        if ": " in line:
            key, value = line.split(": ", 1)
            headers[key.lower()] = value
    return headers


def send_message(client_socket, message, fin_bit):
    """
    Send a WebSocket message to the client.

    Parameters:
    - client_socket (socket.socket): The client socket.
    - message (str): The message to send.
    - fin_bit (int): The FIN bit for the WebSocket frame.

    Returns:
    - None

    Made by Andre Ribeiro <andrepedroribeiro@ua.pt>
    """
    try:
        # Check if the socket is still open
        client_socket.getpeername()
    except OSError:
        print("Client disconnected.")
        return

    # WebSocket frame construction
    opcode = 0x01  # Assuming text frame
    frame = bytearray([0x80 | fin_bit | opcode, len(message)])
    frame.extend(message.encode("utf-8"))

    # Send the WebSocket frame
    client_socket.send(frame)


def handle_client(client_socket):
    """
    Handle the WebSocket handshake and data exchange with a client.

    Parameters:
    - client_socket (socket.socket): The client socket.

    Returns:
    - None

    Made by Andre Ribeiro <andrepedroribeiro@ua.pt>
    """
    # Handle the WebSocket handshake
    request = client_socket.recv(1024).decode("utf-8")
    headers = parse_headers(request)

    response = "HTTP/1.1 101 Switching Protocols\r\n"
    response += "Connection: Upgrade\r\n"
    response += "Upgrade: websocket\r\n"
    response += "Sec-WebSocket-Accept: {}\r\n\r\n".format(
        base64.b64encode(
            hashlib.sha1(
                (
                    headers["sec-websocket-key"]
                    + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
                ).encode("utf-8")
            ).digest()
        ).decode("utf-8")
    )

    print("Sent:", response)

    # Send the WebSocket handshake response
    client_socket.send(response.encode("utf-8"))

    # WebSocket data exchange loop
    control = True
    counter = 0
    while counter < 300:  # Replace with true or use a control variable
        try:
            message = generate_random_message()
            if len(message) > 125:
                # Split large messages into fragments
                fragments = [message[j : j + 125] for j in range(0, len(message), 125)]
                print("Fragments:", fragments)
                for l, fragment in enumerate(fragments):
                    fin_bit = (
                        0 if l == len(fragments) - 1 else 0x80
                    )  # 0x80 for the last fragment, 0 otherwise
                    send_message(client_socket, fragment, fin_bit)
                    time.sleep(0.05)
            else:
                send_message(client_socket, message, fin_bit=0x00)
            time.sleep(0.05)
            counter += 1
            print(counter)
        except Exception as e:
            print("Error:", str(e))
            client_socket.close()
            exit(1)
            break

    # Close the client socket after data exchange
    client_socket.close()


def start_server():
    """
    Start the WebSocket server.

    Returns:
    - None

    Made by Andre Ribeiro <andrepedroribeiro@ua.pt>
    """
    PORT = 8765
    ADDRESS = "localhost"
    # Create a server socket and start listening
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ADDRESS, PORT))
    server.listen(5)

    print(f"[INFO] Server listening on port {PORT}...")

    while True:
        # Accept incoming client connections
        client, addr = server.accept()
        print("[INFO] Accepted connection from {}:{}".format(addr[0], addr[1]))

        # Handle each client in a separate thread
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
