import time
import ds1621

class Temperature: 

    def __init__(self, i2c):
        self.temp = 0
        self.last_read = -999
        self.sensor = ds1621.DS1621(i2c=i2c)

    def read_temp(self):
        if(time.time() > self.last_read + 60):
            self.sensor.start_conversion()
            self.temp = self.sensor.read_temperature()/2
        return self.temp
