#Problems:
'''
1. User gives the data like this:
kerala-tiruvanantapuram karnataka-bengaluru tamilnadu-chennai
You have to separate the states and store in the list states[] and also the seperated capitals must be stored in capitals[]
'''

def states_capitals(strings):
    states = []
    capitals = []

    

    for data in state_and_capitals:
        # Split each pair by hyphen to separate state and capital
        state, capital = data.split('-')
        states.append(state)
        capitals.append(capital)

    return states, capitals

# Read user input and split with spaces
state_and_capitals = [strings for strings in input("Enter the state and capital  :").split(' ')]

states, capitals = states_capitals(state_and_capitals)

print("States:", states)
print("Capitals:", capitals)

