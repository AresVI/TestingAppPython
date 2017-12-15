# -*- coding: utf-8 -*-

from src.utils.request import Request


class Session:

    @classmethod
    def login(cls, username, password):
        path = "api/authenticate"

        data = {
            "password": username,
            "username": password
        }

        response = Request.execute_post_request(path, data)

        return response['id_token']

    @classmethod
    def logout(cls):
        print("Logout not implemented")

    @classmethod
    def login_with_admin(cls):
        return Session.login("admin", "admin")

    @classmethod
    def login_with_administrative(cls):
        return Session.login("administrativo", "administrativo")

    @classmethod
    def login_with_auditor(cls):
        return Session.login("auditor1", "auditor1")