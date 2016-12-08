# coding=UTF-8
# __author__ == ypochien
from __future__ import unicode_literals, print_function
from __future__ import absolute_import

import socket
import struct


class Machete(object):
    def __init__(self, ip, port):
        self.mitake_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mitake_sock.connect((ip, port))

    def login(self):
        pass

    def send(self, data):
        self.mitake_sock.sendall(data)

    def recv(self):
        # 接收資料
        return self.mitake_sock.recv(4096)


class Utility(object):
    @staticmethod
    def make_login_msg(user_id, user_password):
        HEAD = 0x0203
        TYPE = 0x01
        TAIL = 0x0203
        return struct.pack('2c1c10s20s2c', HEAD, TYPE, user_id, user_password, TAIL)
