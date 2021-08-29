__author__ = 'aapav'

from telnetlib import Telnet


class JamesHelper:

    def __init__(self, app):
        self.app = app

    def ensure_user_exist(self, username, password):
        session = JamesHelper.Session('localhost', '4555', 'root', 'root')
        if session.is_user_registered(username):
            session.reset_password(username, password)
        else:
            session.create_user(username, password)
        session.quit()

    class Session:

        def read_until(self, text):
            self.telnet.read_until(text.encode('ascii'), 5)

        def __init__(self, host, port, username, password):
            self.telnet = Telnet(host, port, 5)
            self.telnet.read_until('Login id:', 5)
            self.telnet.write(username + '\n')
            self.telnet.read_until('Password:', 5)
            self.telnet.write(password + '\n')
            self.telnet.read_until('Welcome root. HELP for a list of commands', 5)

        def is_user_registered(self, username):
            self.telnet.write(f'verify {username}\n')
            res = self.telnet.expect(['exists', 'does not exist'], 5)
            return res[0] == 0

        def create_user(self, username, password):
            self.telnet.write(f'adduser {username} {password}\n')
            self.telnet.read_until(f'User {username} added', 5)

        def reset_password(self, username, password):
            self.telnet.write(f'setpassword {username} {password}\n')
            self.telnet.read_until(f'Password for {username} reset', 5)

        def quit(self):
            self.telnet.write('quit\n')
