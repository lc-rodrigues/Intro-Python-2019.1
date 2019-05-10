import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Comparar com a imagem na mesma pasta chamada "CMShistogram (para comparar)"

ds = pd.read_csv('DoubleMuRun2011A.csv')
invariant_mass_1 = ds['M']

no_bins = 500
# Let's calculate the logarithms of the masses and weighs.
inv_mass_log = np.log10(invariant_mass_1)
weights = []
for a in invariant_mass_1:
    weights.append(no_bins/np.log(10)/a)

# Let's plot the weighted histogram.
plt.hist(inv_mass_log, no_bins, range=(-0.5,2.5), weights=weights, lw=0, color="darkgrey")
plt.yscale('log')

# Naming the labels and the title.
plt.xlabel('log10(invariant mass) [log10(GeV)]')
plt.ylabel('Number of the events')
plt.title('The histogram of the invariant masses of two muons \n')
plt.show()