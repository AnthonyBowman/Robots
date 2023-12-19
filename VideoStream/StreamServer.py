import socket
import time
import picamera

while True:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24

        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', 8000))
        server_socket.listen(0)

    
        # Accept a single connection and make a file-like object out of it
        try:
            print("Waiting for a connection...")
            connection = server_socket.accept()[0].makefile('wb')
            try:
                print("Connection established. Starting streaming...")
                camera.start_recording(connection, format='h264')
                camera.wait_recording(1200)  # Stream for 20 minutes (adjust as needed)
            finally:
                print("Stopping streaming and closing connection...")
                camera.stop_recording()
                connection.close()
        finally:
            server_socket.close()

        print("Waiting for the next connection...")
        # Sleep for a short time before attempting to accept a new connection
        time.sleep(3)  # Adjust as needed
