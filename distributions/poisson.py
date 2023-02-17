import math
import matplotlib.pyplot as plt
from .general import Distribution

class Poisson(Distribution):
    """
    Poisson distribution class for calculating and visualizing a Poisson distribution.

    Args:
    mu (float): mean value of the distribution, default is 1.

    Attributes:
    mean (float): representing the mean value of the distribution
    stdev (float): representing the standard deviation value of the distribution
    data (list of floats): a list of floats to be extracted from the dataset
    """
    
    def __init__(self, mu=1):
        """Initialization method that initializes the Poisson distribution parameters and inherits the Distribution class.

        Args:
        mu (float): mean value of the distribution, default is 1.
        """
        self.mu = mu
        self.calculate_stdev()
        self.calculate_mean()
        Distribution.__init__(self, self.mean, self.stdev)

    def calculate_mean(self):
        """
        Function to calculate the mean from the given distribution data.

        Args:
        None

        Returns:
        float: mean of the data set
        """
        self.mean = self.mu
        return self.mean

    def calculate_stdev(self):
        """
        Function to calculate the standard deviation from the given distribution data.

        Args:
        None

        Returns:
        float: standard deviation of the data set
        """
        self.stdev = math.sqrt(self.mu)
        return self.stdev
    
    def replace_stats_with_data(self):
        """
        Function to calculate mu from the data set.

        Args:
        None

        Returns:
        float: the mu value calculated from the data set
        """
        self.mu = sum(self.data)/len(self.data)
        self.calculate_stdev()
        self.calculate_mean()
        return self.mu

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
        """
        Probability density function calculator for the Poisson distribution.

        Args:
        k (float): point for calculating the probability density function

        Returns:
        float: probability density function output
        """
        mu = self.mu
        return (math.pow(mu, k))*(math.exp(-mu))/(math.factorial(k))

    def plot_histogram_pdf(self, n_spaces=10):
        """
        Method to plot the normalized histogram of the data and a plot of the probability density function along the same range.

        Args:
        n_spaces (int): number of data points

        Returns:
        list: x values for the pdf plot
        list: y values for the pdf plot
        """
        # mu = self.mu
        # min_range = round(min(mu - n_spaces/2),0)
        x = []
        y = []
        tmp = 0
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp += i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):
        
        """Function to add together two Poisson distributions with mu1 and mu2
        
        Args:
            other (Poisson): Poisson instance
            
        Returns:
            Poisson: Poisson distribution
            
        """
                
        result = Poisson()
        result.mu = self.mu + other.mu
        result.calculate_mean()
        result.calculate_stdev()
        
        return result
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
    
        return "mean {}, standard deviation {}, mu {}".format(self.mean, self.stdev, self.mu)