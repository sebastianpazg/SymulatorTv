import TvInterface


class Tv(TvInterface.TvInterface):
    def __init__(self, status = False, volume = 0, channel = 1):
        self.status = status
        self.volume = volume
        self.channel = channel

    def __str__(self):
        if self.status == True:
            rep = "Tv on\n" + "Volume = " + str(self.volume) + "\nChannel = " + str(self.channel)
            return rep
        else:
            return("Tv off")

    def error(self):
        print("No button on the remote control")

    def on(self):
        self.status = True

    def off(self):
        self.status = False

    def volumeUp(self):
        if self.status == True:
            self.volume += 1

    def volumeDown(self):
        if self.status == True:
            self.volume -= 1

    def channelUp(self):
        if self.status == True:
            self.channel += 1

    def channelDown(self):
        if self.status == True:
            self.channel -= 1


def ask(question):

    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
