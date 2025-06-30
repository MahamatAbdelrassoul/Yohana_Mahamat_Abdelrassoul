# Assignment One: Train RL agent to navigate to cross the road with action right, left, right


# This script trains an RL agent using Q-learning to cross a road environment.
# After training, it demonstrates the agent following the forced action sequence [right, left, right],
# and displays the Q-table and agent's recommended actions at each step.

import numpy as np
import random

# Environment setup
NUM_POSITIONS = 5  # Number of positions (states) on the road
ACTIONS = ['left', 'right']  # Action space
GOAL_POSITION = NUM_POSITIONS - 1  # Rightmost position is the goal

# RL parameters
LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 1000
EPSILON = 1.0
EPSILON_DECAY = 0.995
EPSILON_MIN = 0.01

class RoadCrossingEnv:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.state = 0  # Start from position 0
        self.done = False
        return self.state
    
    def step(self, action):
        # Execute action
        if action == 'left':
            next_state = max(0, self.state - 1)
        else:  # 'right'
            next_state = min(NUM_POSITIONS - 1, self.state + 1)
        
        # Check if goal reached
        if next_state == GOAL_POSITION:
            reward = 10
            self.done = True
        else:
            reward = -0.1  # Small penalty for each step
        
        self.state = next_state
        return next_state, reward, self.done

def train_agent():
    # Initialize Q-table
    Q = np.zeros((NUM_POSITIONS, len(ACTIONS)))
    
    env = RoadCrossingEnv()
    epsilon = EPSILON
    
    for episode in range(EPISODES):
        state = env.reset()
        done = False
        total_reward = 0
        
        while not done:
            # Epsilon-greedy action selection
            if random.random() < epsilon:
                action_idx = random.randint(0, 1)  # Random action
            else:
                action_idx = np.argmax(Q[state])
            
            action = ACTIONS[action_idx]
            next_state, reward, done = env.step(action)
            total_reward += reward
            
            # Q-learning update
            best_next_action = np.argmax(Q[next_state])
            td_target = reward + DISCOUNT * Q[next_state][best_next_action]
            td_error = td_target - Q[state][action_idx]
            Q[state][action_idx] += LEARNING_RATE * td_error
            
            state = next_state
        
        # Decay epsilon
        epsilon = max(EPSILON_MIN, epsilon * EPSILON_DECAY)
        
        if episode % 100 == 0:
            print(f"Episode: {episode}, Total Reward: {total_reward}, Epsilon: {epsilon:.2f}")
    
    return Q

def demonstrate_sequence(Q):
    print("\nDemonstrating the required action sequence [right, left, right]:")
    env = RoadCrossingEnv()
    state = env.reset()
    actions_sequence = ['right', 'left', 'right']
    
    for step, action in enumerate(actions_sequence):
        action_idx = ACTIONS.index(action)
        next_state, reward, done = env.step(action)
        
        # Show agent's Q-values for current state
        q_left, q_right = Q[state]
        recommended_action = ACTIONS[np.argmax(Q[state])]
        
        print(f"Step {step + 1}:")
        print(f"  Position: {state}")
        print(f"  Forced Action: {action} (Q: {Q[state][action_idx]:.2f})")
        print(f"  Agent's Q-values: Left={q_left:.2f}, Right={q_right:.2f}")
        print(f"  Agent would choose: {recommended_action}")
        print(f"  Next Position: {next_state}\n")
        
        state = next_state
    
    print(f"Final Position after sequence: {state}")
    if state == GOAL_POSITION:
        print("Success! Reached the goal position.")
    else:
        print("Did not reach the goal position.")

# Main execution
if __name__ == "__main__":
    print("Training RL agent...")
    Q_table = train_agent()
    
    print("\nTrained Q-table:")
    print(Q_table)

    demonstrate_sequence(Q_table)