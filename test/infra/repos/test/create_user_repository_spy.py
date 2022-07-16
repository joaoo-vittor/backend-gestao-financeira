class CreateUserRepositorySpy:
    def __init__(self, connection_handler) -> None:
        self.__connection_handler = connection_handler
        self.user_data = None

    def create_user(self, user_data: dict) -> None:
        """Create user

        Args:
            user_data (CreateUserModel): model with data to create user

        Returns:
            UserModel: model with data of the user created
        """

        if user_data is None:
            return None

        self.user_data = user_data

        return {
            "name": user_data["name"] if "name" in user_data.keys() else None,
            "email": user_data["email"],
        }
