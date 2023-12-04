from discord import Color as c

class UserData():
    def __init__(self, interaction):
        self.interaction = interaction

    def get_user(self):
        id = self.interaction.user.id
        print(id)
        if id == 552625879725899789: # JN
            color = c.red()
        elif id == 464817930484449281: # FW
            color = c.teal()
        elif id == 543839114106241025: #L
            color = c.dark_blue()
        elif id == 554293774201913346: # JP
            color = c.purple()
        elif id == 665229112314560515: # RS
            color = c.green()
        elif id == 427116626446516224: # RT
            color = c.gold()
        else:
            color = c.random()

        return User(self.interaction.user.id, self.interaction.user.nick, self.interaction.user.display_avatar.url, color)

class User():
    def __init__(self, id, nick, avatar_url, color):
        self.id = id
        self.nick = nick
        self.avatar_url = avatar_url
        self.color = color