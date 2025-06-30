# Assignment: Train RL agent to navigate to cross the road with action right, left, right
# This script trains an RL agent using Q-learning to cross a road environment.
# After training, it demonstrates the agent following the forced action sequence [right, left, right],
# and displays the Q-table and agent's recommended actions at each step.

# Import necessary library
import numpy as  np
import random 


# Environment setup
road_length = 5  # The road will have 5 position 0, 4, our goal is to reach position 4
actions = ['left', 'right']  #Agent can take left and right 1 right, 2, for left 

# Q-table Initialization
Q = np.zeros((road_length, len(actions)))  # Is the core of Q-learning which initialise Q table

# Hyper parameters 
episodes = 1000 # Number  of training interations, leads to better learning rates
learning_rate = 0.8  # 0 , 1 Alpha learning rate, helps agent to adapt more quickly
gamma = 0.9 # it will have a high rewards
epsilon = 0.3 # helps the agent to discover news paths # exploration rates 

# Training loop 
for episode in range(episodes):
    state = 0 # Start position 0

    while state != 4:  # Goal is position 4
        # Epsilon greedy action selection
        if random.uniform(0, 1) < epsilon:  
            action = random.randint(0, 1) # Explore: random action
        else:
            action = np.argmax(Q[state])  # Exploit: best known action

        # Take action
        if action == 0:  # Move Left
            next_state = max(0, state - 1)
        else:  # Move Right
            next_state = min(road_length - 1, state + 1)

        # Reward
        if next_state == 4:
            reward = 10
        else:
            reward = -1

        # Q-learning update
        Q[state, action] += learning_rate * (reward + gamma * np.max(Q[next_state]) - Q[state, action])

        state = next_state

# Show final Q-table after training
print("\nFinal Q-table after training:")
print(Q)

# Demonstrate agent path with actions right, left, right
print("\n Agent path with actions [right, left, right]:")

state = 0  # Start from position 0
actions_sequence = [1, 0, 1]  # 1: right, 0: left, 1: right

for step, action in enumerate(actions_sequence):
    if action == 0:  # Move Left
        next_state = max(0, state - 1)
        action_name = "Left"
    else:  # Move Right
        next_state = min(road_length - 1, state + 1)
        action_name = "Right"
    print(f"Step {step + 1}: Position {state} -> Action {action_name} -> Next Position {next_state}")
    state = next_state

print(f"Final Position after sequence: {state}")