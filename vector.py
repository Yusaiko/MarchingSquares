import random, math

class createVector:
    def __init__(self, *args):
        self.length = len(args)
        self.x = 0
        self.y = 0
        self.z = 0

        if len(args) > 0:
            self.x = args[0]

            if len(args) > 1:
                self.y = args[1]
                
                if len(args) > 2:
                        raise ValueError("Zu viele Stellen!")   