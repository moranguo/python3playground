from zope.interface import Interface
from zope.interface.declarations import implementer

class IHost(Interface):
    def goodmorning(self, host):
        """Say good moring to host"""

class Host:
    def goodmoring(self, guest):
        return "Good moring, %s!" % guest

if __name__ == "__main__":
    p = Host()
    hi = p.goodmoring('Tom')
    print(hi)