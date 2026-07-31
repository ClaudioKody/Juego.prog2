
class StateManager:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, state_name, state_object):
        self.states[state_name] = state_object

    def change_state(self, state_name):
        if self.current_state:
            self.current_state.exit()
        self.current_state = self.states.get(state_name)
        if self.current_state:
            self.current_state.enter()

    def get_current_state(self):
        return self.current_state
