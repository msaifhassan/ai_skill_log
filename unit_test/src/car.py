import sound
import move
import locator

class Vehicle:
    def __init__(self, auto_start=False):
        self.doors_open = False
        self.engine_running = False
        self.is_moving = False
    
    def start(self):
        if not self.engine_running:
            self.engine_running = True
        else:
            raise RuntimeError("Engine is already")

    def horn(self):
        return sound.horn()
    
    def accelerate(self, speed=5.5):
        if not self.engine_running:
            raise RuntimeError("Engine is not running")
        
        if self.doors_open:
            raise RuntimeError("Doors are open. It is dangerous to drive when door is open.")

        move.accelerate(self.engine, speed=speed)
        sound.accelerate()
    
    def brake(self):
        if not self.engine_running:
            raise RuntimeError("Engine is not running. No need to break.")

        move.stop()
        sound.brake()


    def location(self):
        return locator.current_location()
    
    

    

