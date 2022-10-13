class array:
    def __init__(self, max_length):
        self.array = []
        self.max_length = max_length
        

    def apnd(self, item): 
        if len(self.array) < self.max_length:
            self.array.append(item)
        else:
            print("Exceeds allocated array size.")
            quit()
        
    
    def rplc(self, addr, item):
        if addr <= len(self.array):
            self.array[addr] = item
        else:
            print("Index out of range.")

    def reinit(self, new_array):
        if len(new_array) <= self.max_length:
            self.array = new_array

