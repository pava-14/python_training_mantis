__author__ = 'aapav'

import random


def random_username(prefix, maxlen):
    symbols = 'ascii_letters'
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_signup_new_account(app):
    mailbox_username = 'test1111@localhost'
    mailbox_password = 'test'
    username = random_username('user_', 10)
    email = username + "@localhost"
    email = username + "@localhost"
    #temporary email
    email = 'test1111@localhost'
    password = 'test'
    #app.james.ensure_user_exist(username, password)
    app.signup.new_user(username, email, password, mailbox_username, mailbox_password)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()
