import socket
import hashlib
import zlib
import os 
from cryptography.fernet import Fernet
from tkinter import Tk, filedialog, Button, Label

# Load the encryption key
with open('encryption.key', 'rb') as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

def decompress_file(file_path):
    with open(file_path, 'rb') as file:
        compressed_data = file.read()
        data = zlib.decompress(compressed_data)
    return data

def receive_file(save_path, client_socket):
    try:
        # Receive the file name
        file_name = client_socket.recv(1024).decode()
        file_path = os.path.join(save_path, file_name)

        # Receive file content
        with open(file_path, 'wb') as file:
            while True:
                encrypted_chunk = client_socket.recv(1024)
                if not encrypted_chunk:
                    break
                chunk = cipher_suite.decrypt(encrypted_chunk)
                file.write(chunk)
        
        # Receive checksum
        checksum = client_socket.recv(1024).decode()

        # Verify checksum
        with open(file_path, 'rb') as file:
            file_data = file.read()
            actual_checksum = hashlib.sha256(file_data).hexdigest()
            if actual_checksum == checksum:
                print("File received and verified successfully!")
            else:
                print("File checksum does not match. Possible corruption.")
    except Exception as e:
        print(f"Error receiving file: {e}")

def select_save_location():
    save_path = filedialog.askdirectory()
    if save_path:
        receive_file(save_path, client_socket)

def main():
    global client_socket
    # Set up the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Create a simple GUI for save location selection
    root = Tk()
    root.title("File Transfer Client")
    Label(root, text="Select a directory to save the file:").pack(pady=10)
    Button(root, text="Choose Directory", command=select_save_location).pack(pady=20)
    root.mainloop()

    # Close connection
    client_socket.close()

if __name__ == '__main__':
    main()
