class Action:
    def __init__(self, action_name: str):
        self.action_name = action_name

    def action(self):
        return self.action_name

# Action class should be functor but not simple class -2 points
