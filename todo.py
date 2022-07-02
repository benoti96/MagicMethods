class Todo:
    def __init__(self, name):
        self.name = name
        self. items = []

    def add(self, item):
          self.items.append(item)
       #referenced by programmers
    def __repr__(self):
        return f"Todo('{self.name}')"

  