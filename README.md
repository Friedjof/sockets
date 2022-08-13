# Sockets
This project is a simple example of a socket server and client.
Sockets are used to send and receive data through a network.
The default host is localhost, and the default port is 9997.
This project is specially for wrapping a text file into an object and send it as JSON to a connected client.

## Start the server
```bash
python server.py
```
The server will start on port 9997.
## Start the client
```bash
python client.py
```
The client will connect to the server on port 9997.

## The Client
The client connects to the server.
In the next a command line starts.
Here you can type a path to a text file. The server will send the file to the client in JSON format.
### Example
```bash
Dateipfad: server-file.txt
```
The answer will be a JSON object like this:
```json
{
    "file_name": "/home/friedjof/sockets/server-file.txt",
    "file_content": "Hello World"
}
```

# Thanks for reading
I hope this helps you to understand the basics of sockets and how to send simple text files through sockets.
If you have any questions, feel free to contact me. You can find me on GitHub: [@friedjof](https://github.com/friedjof)
You can also write an issue on GitHub: [sockets/issues](https://github.com/Friedjof/sockets/issues)