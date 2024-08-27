import http.server
import socketserver
import os
import sys

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Set the directory to serve from
        kwargs['directory'] = kwargs.get('directory', os.getcwd())  # Default to current working directory
        super().__init__(*args, **kwargs)

    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        super().end_headers()

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <directory> <port>")
        sys.exit(1)

    directory = sys.argv[1]
    port = int(sys.argv[2])

    # Check if the specified directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory {directory} does not exist.")
        sys.exit(1)

    # Create and start the HTTP server
    with socketserver.TCPServer(("", port), lambda *args, **kwargs: MyHandler(*args, directory=directory, **kwargs)) as httpd:
        print(f"Serving at directory {directory} on port {port}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
