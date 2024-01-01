import pandas as pd
import numpy as np
import pdb

class explore:

    def __init__(self, method):

        self.method     = method
        self.rets_compo = None
        self.rets_added = None
        self.df_sim     = None

    def execute(self, sims, **kwargs):

        self.rets_compo = np.zeros(sims)
        self.rets_added = np.zeros(sims)
        self.df_sim = pd.DataFrame()

        for k in range(sims):
            try:
                rewards,Q,N = self.method(**kwargs)
                df_rwd = pd.DataFrame(rewards)
                ret_com = ((df_rwd+1).cumprod().iloc[-1] - 1)[0]
                ret_sum = df_rwd.sum()[0]

                self.rets_compo[k] = ret_com
                self.rets_added[k] = ret_sum

                self.df_sim = pd.concat([self.df_sim,df_rwd], axis = 1)
            
            except Exception as e :
                pdb.set_trace()