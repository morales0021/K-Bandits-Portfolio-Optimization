import numpy as np

class basic:

    @classmethod
    def execute(cls, n_bandit, exploration_rate, df_bandits, steps):

        Q = np.zeros(n_bandit)
        N = np.ones(n_bandit)
        rewards = []

        for i in range(steps): # 3. Main loop
            explore = random.uniform(0, 1) < exploration_rate 
            if explore:
                # choose a random agent (bandit)
                action = random.randint(0, n_bandit - 1) # 5. Exploration: Choosing random action
            else:
                # choose the best agent (bandit)
                action = np.argmax(Q)
                
            reward = df_bandits.iloc[i,action]
            rewards.append(reward)
            N[action] += 1 # 8. Update action number
            Q[action] = Q[action] + (1/N[action]) * (reward - Q[action]) # 9. Update value dict

        return rewards,Q, N