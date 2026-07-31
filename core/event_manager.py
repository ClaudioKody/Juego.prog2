
class EventManager:
    def __init__(self):
        self.listeners = {}

    def register_listener(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def unregister_listener(self, event_type, listener):
        if event_type in self.listeners:
            self.listeners[event_type].remove(listener)

    def handle_event(self, event, current_state):
        # Los eventos pueden ser manejados por el estado actual o por listeners globales
        if hasattr(current_state, 'handle_event'):
            current_state.handle_event(event)

        if event.type in self.listeners:
            for listener in self.listeners[event.type]:
                listener.handle_event(event)
