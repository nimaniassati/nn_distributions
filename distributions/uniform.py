import math
import matplotlib.pyplot as plt
from .general import Distribution

class Uniform(Distribution):
    def __init__(self, mu=1):
        pass

    def calculate_mean(self):
        pass

    def calculate_stdev(self):
        pass
    
    def replace_stats_with_data(self):
        pass

    def plot_bar(self):
        """
        Function to output a histogram of the instance variable data using matplotlib pyplot library.

        Args:
        None

        Returns:
        None
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')
        plt.show()

    def pdf(self, k):
        pass

    def plot_histogram_pdf(self, n_spaces=10):
        pass

    def __add__(self, other):
        pass
        
        
    def __repr__(self):
        pass