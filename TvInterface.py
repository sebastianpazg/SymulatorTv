from abc import ABC, abstractmethod


class TvInterface(object):
    @abstractmethod
    def error(self): pass
    def on(self): pass
    def off(self): pass
    def volumUp(self): pass
    def volumeDown(self): pass
    def channelUp(self): pass
    def channelDown(self): pass
    def ask(self): pass