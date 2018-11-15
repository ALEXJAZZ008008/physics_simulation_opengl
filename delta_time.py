import time


class DeltaTime(object):
    def __init__(self):
        self.previous_time = self.get_current_time()
        self.current_time = self.previous_time
        self.delta_time = self.current_time - self.previous_time

    @staticmethod
    def get_current_time():
        return time.time()

    def update_previous_time(self):
        self.previous_time = self.current_time

    def update_current_time(self):
        self.current_time = self.get_current_time()

    def update_delta_time(self):
        self.delta_time = self.get_current_time() - self.previous_time
