import sound
import move
import locator

class Car:
    def __init__(self, auto_start=False):
        self.doors_open = False
        self.engine_running = False
        self.is_moving = False
    
    def start(self):
        """
        Starts the engine of the car if it is not already running. If the engine is already running, a RuntimeError is raised.

        Parameters:
            self (Car): The current instance of the Car class.

        Raises:
            RuntimeError: If the engine is already running.

        Returns:
            None
        """
        if not self.engine_running:
            self.engine_running = True
        else:
            raise RuntimeError("Engine is running already")

    def horn(self):
        return sound.horn()
    
    def accelerate(self, speed=5.5):
        if not self.engine_running:
            raise RuntimeError("Engine is not running")
        
        if self.doors_open:
            raise RuntimeError("Doors are open. It is dangerous to drive when door is open.")

        moved = move.accelerate(speed=speed)
        self.is_moving = True
        return sound.accelerate()
    
    def brake(self) -> None:
        """
        Brake the car if the engine is running. If the engine is not running, a RuntimeError is raised.

        Parameters:
            self (Car): The current instance of the Car class.

        Raises:
            RuntimeError: If the engine is not running.

        Returns:
            None
        """
        if not self.engine_running:
            raise RuntimeError("Engine is not running. No need to break.")

        move.stop()
        sound.brake()


    def location(self):
        return locator.current_location()
    
    

    

