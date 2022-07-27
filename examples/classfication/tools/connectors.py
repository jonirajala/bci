from serial import Serial
import glob

class BaseBCIConnector:
    def connect(self):
        pass
    def read(self):
        pass

class EEGClickConnector(BaseBCIConnector):
    def __init__(self, baudrate, channels=1, port=None):
        self.port = port
        self.baudrate = baudrate
        self.channels = channels

        self.connect()

    def connect(self):
        print("Connecting to device...")
        if self.port == None:
            ports = glob.glob('/dev/tty.*')
            self.port = '/dev/cu.usbserial-14110'
        try:
            self.connection = Serial(self.port, self.baudrate)
            print(f"Connected to port {self.port}")

        except Exception as e:
            print(e)
            print("Can't connect to your EEG click device")

    def disconnect(self):
        self.connection.close()

    def read(self):
        try:

            signal = self.connection.readline().decode().strip()

            #bytesToRead = self.connection.inWaiting()
            #signal = self.connection.read(bytesToRead).decode().strip()
        except Exception as e:
            print(e)
            exit()
        return signal
    
    def write(self, output):
        self.connection.write(output.encode())
