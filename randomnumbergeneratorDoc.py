# ============================================================================== Import Section
# imports the random module, provides various functions to generate random numbers, among other utilities
# imports the pyplot submodule from the matplotlib library, commonly used for creating static, animated, and interactive visualizations in Python, alias plot is used to refer to it in the rest of the code

# ============================================================================== Data Section
# creates a list of 1000 random numbers using a list comprehension (random.gauss(0, 1)), generates a random number following a Gaussian (normal) distribution with a mean of 0 and a standard deviation of 1. The for _ in range(1000) part repeats the generation of a random number 1000 times. The underscore (_) is a conventional way to indicate that the loop variable is not used

# ============================================================================== Plot Section
# creates a histogram of the data list. (data) is the list of 1000 random values to be visualized. (bins=30) is specifies the number of bins (bars) in the histogram. Here, the data is divided into 30 intervals. (density=True) is normalizes the histogram such that the area under the histogram equals 1, making it a probability density rather than a count of occurrences. This allows it to represent the shape of the distribution

# displays the generated histogram. It opens a window with the plotted graph, showing the distribution of the data
