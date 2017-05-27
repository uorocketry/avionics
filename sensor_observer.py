#an implementation of the Observer pattern for rocket data

class subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, data):
        print('{} got data "{}"'.format(self.name, data))

class publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def dispatch(self, data):
        for subscriber in self.subscribers:
            subscriber.update(data)
