# coding=UTF-8
# __author__ == ypochien
from __future__ import absolute_import

import asyncore
import socket


class Machete(asyncore):
    def __init__(self, ip, port):
        self.mitake_address = (ip, port)
        self.mitake_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mitake_sock.connect(self.mitake_address)
    
    def login(self):
        pass
            
    def send(self, data):
        self.mitake_sock.sendall(data)
    
    def recv(self):
        # 接收資料
        return self.mitake_sock.recv(4096)
