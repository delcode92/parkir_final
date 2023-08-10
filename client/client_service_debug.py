#CLIENT

# client - server connection via socket programming

import sys, socket, logging
from logging.handlers import TimedRotatingFileHandler
from time import sleep
import threading


class Client:
    
    
    def __init__(self) -> None:
        
        # self.initDebug()
        self.s = None
        self.stat = False
        self.first_connect = False

        host = sys.argv[1]
        port = sys.argv[2]
        self.connect_client(host, port)

        # socket_thread = threading.Thread(target=self.connect_client, args=(host, port))
        # socket_thread.start()

        
    
    def initDebug(self):
        
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.NOTSET)
        self.logfile_path = "../logging/log_file.log"

        # our first handler is a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler_format = '%(levelname)s: %(message)s'
        console_handler.setFormatter(logging.Formatter(console_handler_format))

        # start logging and show messages

        # the second handler is a file handler
        file_handler = logging.FileHandler(self.logfile_path)
        file_handler.setLevel(logging.INFO)
        file_handler_format = '%(asctime)s | %(levelname)s | %(lineno)d: %(message)s'
        file_handler.setFormatter(logging.Formatter(file_handler_format))

        # clear log file every 1 day
        rotate = TimedRotatingFileHandler('sample.log', when='D', interval=1, backupCount=0, encoding=None, delay=False, utc=False)
        
        self.logger.addHandler(rotate)
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        

    def connect_client(self, h, p):
        # connect_stat = False
        
        while True:

            try:
                self.s.sendall( bytes(f"client({h}) connected", 'utf-8') )
                # if not self.first_connect:
                #     self.s.sendall( bytes(f"client({h}) connected", 'utf-8') )
                #     self.first_connect = True
            except:
                print("can't connect to server 1")

                try:
                    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    self.s.connect((h, int(p)))

                    # self.s.sendall( bytes(f"client({h}) connected", 'utf-8') )
                    # self.logger.info("success connect to server")

                except Exception as e:
                    print("can't connect to server 2")
                    # self.logger.info("can't connect to server")
                    # self.logger.error( str(e) )

            
            if not self.stat:
                input_data_thread = threading.Thread(target=self.send_data)
                input_data_thread.start()
                
                self.stat=True

            sleep(1)

    
    def get_data(self, data):

        # send rfid value to server socket
        self.s.sendall( bytes(data, 'utf-8') )
        res = self.s.recv(1024)

        return res
    
    
    def send_img(self, data):

        # send rfid value to server socket
        # self.s.sendall( bytes(data, 'utf-8') )
        self.s.sendall( data )
        res = self.s.recv(1024)

        return res

    def send_data(self):
        # self.s.setblocking()
        self.s.settimeout(2)

        while True:
            # print("rfid thread ... ")
            
            try:
                data = input("input data: ")
            
                self.s.sendall( bytes(data, 'utf-8') )
                res = self.s.recv(1024)

                print("===> result: ",res)
            except Exception as e:
                print(str(e))
            
            sleep(1)

        
    
Client()