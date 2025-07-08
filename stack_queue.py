class Queue(object):
    """A Queue class """
 
    def __init__(self, data=[]):
    	self.data = data
    def enqueue(self, data):
    	self.data.append(data)
    def dequeue(self):
    	if self.is_empty():
    		return
    	else:
    		return self.data.pop(0)
    def is_empty(self):
    	return len(self.data) == 0
    def size(self):
    	return len(self.data)

 
 
class Stack(object):
	"""A Stack class """
	
    def __init__(self):
    	self.data = []
    def push(self, data): 
    	self.data.append(data)
    def pop(self):
    	if self.is_empty():
    		return
    	else: 
    	   	return self.data.pop(-1)
    def is_empty(self):
    	return len(self.data) == 0
    def peak(self):
    	return self.data[-1]
    def size(self):
    	return len(self.data)
    def __repr__(self):
    	return "Stack Object with: {}".format(self.data)