import pandas as PD
import numpy as np

df = pd.DataFrame(np.random.randint(0,100,size=(15, 4)), columns=list('ABCD'))

print(df)
