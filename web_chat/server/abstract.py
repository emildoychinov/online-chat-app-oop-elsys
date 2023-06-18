from typing import Callable

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]

# an abstract server class
class AbsServer:
    port = 80 
    debug = True

    # a private function to handle an endpoint
    def __handle__(self, endpoint: str, handle: Callable):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError
