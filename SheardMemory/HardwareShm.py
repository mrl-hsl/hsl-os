from SheardMemory.PyShm import pyShm

segment_name = "HardwareShm"

class Acutators():
    def __init__(self,_segment_name = segment_name):
        pyShm.open_or_create_shm(segment_name,1000000)
        self.segment_name = _segment_name
        print(self.segment_name)
    
        self.tourqe_enable    = pyShm.vector(self.segment_name,"tourqe_enable")
        self.tourqe_enable_update = pyShm.scalar(self.segment_name,"tourqe_enabl_update")

        self.goal_position    = pyShm.vector(self.segment_name,"goal_position")
        self.goal_position_update = pyShm.scalar(self.segment_name,"goal_position_update")
        
        self.present_position = pyShm.vector(self.segment_name,"present_position")
        self.present_position_update = pyShm.scalar(self.segment_name,"present_position_update")
        
        self.p_position       = pyShm.vector(self.segment_name,"p_position")
        self.p_position_update = pyShm.scalar(self.segment_name,"p_position_update")
        
        self.i_position       = pyShm.vector(self.segment_name,"i_position")
        self.i_position_update = pyShm.scalar(self.segment_name,"i_position_update")
        
        self.d_position       = pyShm.vector(self.segment_name,"d_position")
        self.d_position_update = pyShm.scalar(self.segment_name,"d_position_update")
        print("__init__shm")
    
    
    def init(self):
        self.init = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.goal_position.extend(self.init)
        self.present_position.extend(self.init)
        self.tourqe_enable.extend(self.init)
        self.p_position.extend(self.init)
        self.d_position.extend(self.init)
        self.i_position.extend(self.init)
        
class Imu():
    def __init__(self,_segment_name, *args, **kwargs):
        pyShm.open_or_create_shm(segment_name,1000000)
        self.segment_name = _segment_name
        self.gyro = pyShm.vector(self.segment_name,"gyro")
        self.accl = pyShm.vector(self.segment_name,"accl")
        self.angle = pyShm.vector(self.segment_name,"angle")
    def init(self):
        self.init = [0,0,0]
        self.gyro.extend(self.init)
        self.accl.extend(self.init)
        self.angle.extend(self.init)

class Buttons():
    def __init__(self,_segment_name, *args, **kwargs):
        pyShm.open_or_create_shm(segment_name,1000000)
        self.segment_name = _segment_name
        self.btn1 = pyShm.scalar(self.segment_name,"btn1")
        self.btn2 = pyShm.scalar(self.segment_name,"btn2")
        
class Battry():
    def __init__(self,_segment_name, *args, **kwargs):
        pyShm.open_or_create_shm(segment_name,1000000)
        self.segment_name = _segment_name
        self.lvel = pyShm.scalar(self.segment_name,"battryLvel")