#an implementation of the Observer pattern for rocket data


class subscriber(object):
    def __init__(self, name):
        super(subscriber,self).__init__
        self.name = name
    def update(self, data):
        print('{} got data "{}"'.format(self.name, data))
        #classes that use this should override it to suit their needs

class publisher(object):
    def __init__(self):
        super(publisher,self).__init__
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def dispatch(self, data):
        for subscriber in self.subscribers:
            subscriber.update(data)
