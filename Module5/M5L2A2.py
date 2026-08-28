# M5L2A2: Employee in and Out
# Activity 2: Exploring Constructor (__init__) and Destructor (__del__) Object Lifecycles

# Create Class
class Employee:
    # Initializing
    def __init__(self):
        print('Employee created')

    # Calling destructor
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')
