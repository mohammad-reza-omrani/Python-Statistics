# ============================================================================== Import Section
import random                                                                    # line 2
import matplotlib.pyplot as plot                                                 # line 3

# ============================================================================== Data Section
data = [random.gauss(0, 1) for _ in range(1000)]                                 # line 6

# ============================================================================== Plot Section
plot.hist(data, bins=30, density=True)                                           # line 9
plot.show()                                                                      # line 11


#    ======================================================================================================
# documented in randomnumbergenerator.py
