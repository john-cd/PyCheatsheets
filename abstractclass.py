import abc

class AbstractClass(object):
  __metaclass__ = abc.ABCMeta # Python 2.x

  @abc.abstractmethod
    def abstractMethod(self):
        """Description"""
        return

class ConcreteClass(AbstractClass):
    def __init__(self):
        self.me = "me"

c = ConcreteClass()
c.abstractMethod()