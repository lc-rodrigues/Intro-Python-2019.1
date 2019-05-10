# Let's import the needed modules.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# With this line the data is imported and saved to the variable "ds".
ds = pd.read_csv('DoubleMuRun2011A.csv')

great_etas = ds[(np.absolute(ds.eta1) > 1.52) & (np.absolute(ds.eta2) > 1.52)]
small_etas = ds[(np.absolute(ds.eta1) < 0.38) & (np.absolute(ds.eta2) < 0.38)]

# Let's print out some information about the selection
print('Amount of all events = %d' % len(ds))
print('Amount of the events where the pseudorapidity of the both muons have been large = %d' %len(great_etas))
print('Amount of the events where the pseudorapidity of the both muons have been small = %d' %len(small_etas))

# Let's differ the invariant masses of the large and small pseudorapidity
# events for making the histograms.
inv_mass_great = great_etas['M']
inv_mass_small = small_etas['M']

# Let's use the matplotlib.pyplot module to create a custom size
# figure where the two histograms will be plotted.
f = plt.figure(1)
f.set_figheight(15)
f.set_figwidth(15)
plt.subplot(211)
plt.hist(inv_mass_great, bins=120, range=(60,120))
plt.ylabel('great etas, number of events', fontsize=20)
plt.subplot(212)
plt.hist(inv_mass_small, bins=120, range=(60,120))
plt.ylabel('small etas, number of events', fontsize=20)
plt.xlabel('invariant mass [GeV]', fontsize=20)
plt.show()