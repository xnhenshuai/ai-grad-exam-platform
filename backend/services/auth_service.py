from datetime import datetime

# Placeholder authentication service
# NOTE: Phase 1 skeleton only, mock behavior.
# TODO: replace with JWT / token-based authentication and password hashing for production.

class AuthService:
    def register_user(self, username: str, password: str):
        # TODO: implement hashing + DB persistence
        return {"id": 1, "username": username}

    def authenticate_user(self, username: str, password: str):
        # TODO: lookup user, verify password
        if username == "test" and password == "secret":
            return {"id": 1, "username": username}
        return None

    def get_current_user(self, token: str):
        # TODO: decode JWT
        return {"id": 1, "username": "test"}
