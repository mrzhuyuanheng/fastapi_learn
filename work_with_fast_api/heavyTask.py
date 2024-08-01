
# Simulate UartBurn Class
class HeavyTask():
    def __init__(self):
        self.port = 0

    def mock_progress_changed(self, progress):
        self.cbProgress(progress)

    async def listen(self, cbProgress):
        self.cbProgress = cbProgress
        print(f"listening on port")

