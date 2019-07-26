#!/usr/bin/env python
# coding: utf-8

# In[1]:


from maze_env import Maze
from RL_brain import QLearningTable

def update():
    for episode in range(20):
        # initial observation
        observation = env.reset()

        ## RL choose action based on observation  ##
        action = RL.choose_action(str(observation))
        
        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            ## RL choose action based on next observation#
            
            ## RL learn from this transition (s, a, r, s, a) ==> Sarsa ##
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation 
            observation = observation_
            
            ## swap action ##

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    env.after(100, update)
    env.mainloop()

