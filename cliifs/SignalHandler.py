import signal

class SignalHandler:
  terminate_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.terminate)
    signal.signal(signal.SIGTERM, self.terminate)

  def terminate(self,signum, frame):
    self.terminate_now = True
