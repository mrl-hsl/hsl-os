from HardwareManager.AcuatorManager import AcuatorManager
from HardwareManager.HardwareIo import HardwareIO
enable_acuator_manager = True

class HardwareManager():
    def __init__(self):
       # TODO add controle manager hear.
       self.interface = HardwareIO("/dev/ttyUSB0")
       self.acutatorManager =  AcuatorManager(self.interface)
       
    def update(self):
        if enable_acuator_manager:
            self.acutatorManager.update()
