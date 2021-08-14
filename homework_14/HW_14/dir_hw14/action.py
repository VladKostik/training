class Action:
    def __init__(self, action_name: str):
        self.action_name = action_name

    def action(self):
        return self.action_name
