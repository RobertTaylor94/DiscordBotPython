

class UserData():
    def __init__(self, interaction):
        self.interaction = interaction

    def get_user(self):
        return User(self.interaction.user.id, self.interaction.user.nick, self.interaction.user.display_avatar.url, self.interaction.user.color)

class User():
    def __init__(self, id, nick, avatar_url, color):
        self.id = id
        self.nick = nick
        self.avatar_url = avatar_url
        self.color = color