import time

class Timer:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        
        self.total_seconds = 0

    def set_minutes(self, num_minutes):
        self.total_seconds = num_minutes * 60
        self._convert_seconds_to_all()
                
    def _convert_seconds_to_all(self):
        self.hours = self.total_seconds // 60 // 60 
        self.minutes = self.total_seconds // 60 % 60
        self.seconds = self.total_seconds % 60
    
    def _get_update(self):
        return [self.hours,self.minutes,self.seconds]
    
    
if __name__ == "__main__":
    test = Timer()
    test.set_minutes(15)
    print(test.minutes)



