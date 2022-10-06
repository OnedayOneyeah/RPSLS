# Queue for update

class Queue:
    def __init__(self):
        self._data = ["None", "None", "None", "None", "None", "None", "None", "None", "None", "None"]

    def update(self,x):
        self._data.append(x)
        del self._data[0]

    def rtnqueue(self):
        return self._data
        
