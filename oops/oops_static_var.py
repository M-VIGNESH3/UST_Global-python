class Counter:
    count = 0  # static variable
    
    def __init__(self):
        # Wrong way to modify static variable
        self.count += 1  # This creates an instance variable!
        
        # Right way to modify static variable
        Counter.count += 1
        
# Create some counters
c1 = Counter()
print(Counter.count)  # Output: 1

c2 = Counter()
print(Counter.count)  # Output: 2

# Let's check instance values
print(c1.count)      # Output: 2
print(c2.count)      # Output: 2