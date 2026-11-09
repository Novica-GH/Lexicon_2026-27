import sys
import pandas as pd

print(sys.version)
print(pd.__version__)

listings = pd.read_csv('data/listings.csv') # load the file
listings.shape listings.head() listings.info()
listings[['a', 'b']].count() # values that are NOT missing
listings[['a', 'b']] # pick columns (double brackets)
listings['x'].describe() listings['x'].nunique()
mask = listings['x'] >= 2 mask.sum() mask.mean()
listings[(mask1) & (mask2)] # & means AND
listings[cols].sort_values('x', ascending=False).head(5)