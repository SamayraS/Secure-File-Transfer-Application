import socket
import hashlib
import os
import logging
import zlib
from cryptography.fernet import Fernet
from tkinter import Tk, filedialog, Button, Label

# Configure logging
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Generate and save a key for encryption/decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)
with open('encryption.key', 'wb') as key_file:
    key_file.write(key)

def compress_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        compressed_data = zlib.compress(data)
    return compressed_data

def send_file(file_path, client_socket):
    try:
        compressed_data = compress_file(file_path)
        # Send the file name
        file_name = os.path.basename(file_path).encode()
        client_socket.send(file_name)
        
        # Send the compressed file content
        client_socket.sendall(compressed_data)

        # Send a checksum
        checksum = hashlib.sha256(compressed_data).hexdigest()
        client_socket.send(checksum.encode())
        logging.info(f"File {file_path} sent successfully.")
    except Exception as e:
        logging.error(f"Error sending file {file_path}: {e}")

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        send_file(file_path, client_socket)

def main():
    # Set up the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server listening on port 12345")

    # Accept a client connection
    global client_socket
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Create a simple GUI for file selection
    root = Tk()
    root.title("File Transfer Server")
    Label(root, text="Select a file to send:").pack(pady=10)
    Button(root, text="Choose File", command=select_file).pack(pady=20)
    root.mainloop()

    # Close connections
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()
