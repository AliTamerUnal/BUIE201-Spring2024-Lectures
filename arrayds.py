class Array:
    def __init__(self) -> None:
        self.size = 0
        self.data = None

    def __getitem__(self, index):
        if index >= 0 and index < self.size:
            return self.data[index]
        return None
    
    def __setitem__(self, index, value):
        if index >= 0 and index < self.size:
            self.data[index] = value
      
    # O(n)
    def insert(self, value):
        # CODE REQUIRED
        # allocate new data O(1)
        new_size = self.size + 1
        new_data = [None] * new_size

        # copy existing elements to the new data O(n)
        for i in range(self.size):
            new_data[i] = self.data[i]

        #insert the new item at the end O(1)
        new_data[self.size] = value

        # update attributes O(1)
        self.size = new_size
        self.data = new_data

    # O(n)
    def insert_front(self, value):
        # allocate new data
        new_size = self.size + 1
        new_data = [None] * new_size

        # copy existing elements to the new data
        for i in range(self.size):
            new_data[i + 1] = self.data[i]

        #insert the new item at the beginning
        new_data[0] = value

        # update attributes 
        self.size = new_size
        self.data = new_data

    # O(n)
    # A possible implementation of Python in operator 
    def find(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return True
        return False
    
    # O(1)
    def count(self):
        return self.size
    
    def contains(self, other):
        if self.size >= other.size:
            for i in range (self.size - other.size + 1):
                all_same = True
                for j in range (other.size):
                    if self.data[i + j] != other.data[j]:
                        all_same = False
                        break
                if all_same:
                    return True
        return False


my_array = Array()
my_array.insert(4)
my_array.insert(5)
my_array.insert(2)
my_array.insert(1)

print(my_array[2])
my_array[2] = 15
print(my_array[2])

other = Array()
other.insert(2)
other.insert(1)

result1 = my_array.contains(other)

other2 = Array()
other2.insert(1)
other2.insert(2)

result2 = my_array.contains(other2)