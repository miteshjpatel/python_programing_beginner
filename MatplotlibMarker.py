#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Qt5Agg')  # W3 code 'Agg' did not display so I had to install PyQt5 and user Qt5Agg

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


