#!/usr/bin/env python3

import argparse

import sys
import socket
import ssl
import base64
DEBUG_MODE = True

context = ssl.create_default_context()

class SMTP:
    def __init__(self, socket):
        self.socket = socket

    def cmd(self, *args, size=1024, status=None):
        if args:
            cmd = args[0] + "\r\n"
            self.socket.send(cmd.encode())
        recv = self.socket.recv(size).decode()
        if DEBUG_MODE:
            print(recv)

        if status and recv[:3] != str(status):
            print("{} reply not received from server.".format(status))


def send_mail(from_addr, password, mail_server, to_addr, message):
    # Fill in the code to talk to the mail server here. Read the file
    # read-first.md to find out how to set up a mail server for testing. A log
    # of a telnet session with your mail server may be (very) useful here.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection_socket:

        connection_socket.connect((mail_server, 25))

        smtp = SMTP(connection_socket)

        smtp.cmd(status=220)

        smtp.cmd('helo {}'.format(mail_server), status = 250)

        smtp.cmd('AUTH LOGIN', status=334)

        user = base64.b64encode(from_addr.encode()).decode()
        smtp.cmd(user, status=334)

        pw = base64.b64encode(password.encode()).decode()
        smtp.cmd(pw, status=235)

        smtp.cmd('MAIL FROM: <{}>'.format(from_addr, status=250))

        smtp.cmd('RCPT TO: <{}>'.format(to_addr, status=250))

        smtp.cmd("DATA", status=354)

        msg = ("From: Test Example <{0}>\n"
               "To: <{1}>\n"
               "Subject: {2}\n"
               "{3}\n"
               "\r\n.")
        msg.format(from_addr, to_addr, 'hello', message)
        smtp.cmd(msg, status=250)

        smtp.cmd("QUIT", status=221)
        return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('my_address', type=str)
    parser.add_argument('my_password', type=str)
    parser.add_argument('mail_server', type=str)
    parser.add_argument('their_address', type=str)
    parser.add_argument('message', type=str)
    args = parser.parse_args()

    send_mail(args.my_address, args.my_password, args.mail_server, args.their_address, args.message)

    # success
    return 0

if __name__ == "__main__":
    sys.exit(main())
