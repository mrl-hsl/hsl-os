from SheardMemory.HardwareShm import Acutators
import numpy as np
class AcuatorManager():
    def __init__(self,interface):
        self.acutators = Acutators()
        self.acutators.init()
        self.interface = interface
        for k,v in enumerate(np.ones(6)): 
            self.acutators.tourqe_enable[k+1] = v
        self.acutators.tourqe_enable_update.value = 1.0
        
        
    def update(self):
        #print(self.acutators.tourqe_enable_update.value)
        if self.acutators.tourqe_enable_update.value == 1:
            #self.set_tourqe_enable()
            print("tourqe updated!")
            self.acutators.tourqe_enable_update.value = 0.0
        
        if self.acutators.goal_position_update.value == 1:
            self.set_goal_position()
            print("goal Pose updated!")
            self.acutators.goal_position_update.value = 0
        
        if self.acutators.p_position_update.value == 1:
            self.set_p_position()
            self.acutators.p_position_update.value = 0
        
        if self.acutators.i_position_update.value == 1:
            self.set_i_position()
            self.acutators.i_position_update.value = 0
        
        if self.acutators.d_position_update.value == 1:
            self.set_d_position()
            self.acutators.d_position_update.value = 0
        
        # if self.acutators.present_position_update.value == 0:
        self.get_present_position()
        

    def set_goal_position(self):
        data = []
        for i in range(1,2):
            data.append((i,int(self.acutators.goal_position[i])))
        print(data)
        self.interface.set_goal_position(data)


    def set_p_position(self):
        pass


    def set_i_position(self):
        pass


    def set_d_position(self):
        pass


    def set_tourqe_enable(self):
        data = []
        for i in range(1,2):
            data.append((i,int(self.acutators.tourqe_enable[i])))
        print(data)
        self.interface.set_goal_position(data)
        
    
    def get_present_position(self):
        ids= []
        for i in range(1,2):
            ids.append(i)
        print(ids)
        print(self.interface.get_present_position(ids))
        
        