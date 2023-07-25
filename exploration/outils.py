import pandas as pd

def stats(returns):
    mean = pd.DataFrame(returns).mean()[0]
    std  = pd.DataFrame(returns).std()[0]

    return mean, std