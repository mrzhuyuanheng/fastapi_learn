from nicegui import ui

# Simulate Ui Class
class Demo:
    _instance = None
    def __init__(self):
        if Demo._instance is not None:
            raise Exception("Demo is a singleton class. Use get_instance() to get the instance.")
        self.number = 1
    
    def show_ui(self):
        v = ui.checkbox('visible', value=True)
        with ui.column().bind_visibility_from(v, 'value'):
            ui.slider(min=1, max=100).bind_value(self, 'number')
            ui.number().bind_value(self, 'number')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


