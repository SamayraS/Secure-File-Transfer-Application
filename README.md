# Secure File Transfer Application

A simple and secure file transfer application built using Python. This project demonstrates secure file transfer with encryption, file compression, and a graphical user interface (GUI) using `tkinter`. The application consists of a server and a client that communicate over TCP.

## Features

- **Secure Encryption:** Files are encrypted using `cryptography`'s Fernet symmetric encryption.
- **File Compression:** Files are compressed using `zlib` before transfer to optimize performance.
- **Progressive GUI:** A user-friendly GUI built with `tkinter` for both server and client sides.
- **Checksum Verification:** Files are verified for integrity using SHA-256 checksum.
- **Multi-File Transfer:** The server can send multiple files sequentially.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/file-transfer-project.git
   cd file-transfer-project
2.**Install Dependencies: Ensure you have Python installed, then install the required libraries:**
bash
pip install cryptography

3. **Usage**
Run the Server:
Open a terminal and navigate to the project directory.
Start the server:

```bash
python server.py
```
The server GUI will open, allowing you to select a file to send.

Run the Client:
Open another terminal and navigate to the project directory.
Start the client:
```bash
python client.py
```
The client GUI will open, allowing you to select a directory to save the received file.

4. **How It Works**
Server Side:
Selects a file to send through the GUI.
Compresses and encrypts the file.
Sends the file and its checksum to the client.

Client Side:
Receives the file and its checksum.
Decrypts and decompresses the file.
Verifies the file integrity using the checksum.

5. **Additional Information**
Encryption Key: An encryption key is generated and saved as encryption.key. Ensure this file is present in the same directory as the scripts for successful encryption and decryption.
Error Handling: Errors are logged and displayed to the user for better debugging.
