import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# -------------------------------
# Sampling Functions
# -------------------------------
def sample_means (data,sample_size,n_samples = 1000):
    """
    generate samle means from population array 
    Parameter :
    - data :  1D array --> the population
    - sample_size : int , size of each sample 
    - n_samoles: int , number of samples to draw
    Returns:
    - list of sample mean 
    """
    means = [np.random.choice(data , size = sample_size , replace = True).mean()for _ in range (n_samples)]
    return means
# -------------------------------
# Plotting Helper
# -------------------------------
def plot_histogram (data , bins = 30 , title = None , xlabel = None , ylabel = "Frequency"):
    """
    Plot histogram with optional title , xlabel
    Parameter : 
    data : 1D array 
    bins : int , number of bins
    title : str , optional
    xlabel : str , optional 
    ylabel : str , default "frequency"
    """
    sns.histplot(data, bins=bins, kde=True)
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    plt.ylabel(ylabel)
# -------------------------------
# Confidence Interval Function
# -------------------------------
def confidence_interval(data, confidence=0.95):
    """
    Compute the confidence interval for a 1D array.

    Parameters:
    - data: 1D array-like of sample values
    - confidence: float, e.g., 0.95 for 95%

    Returns:
    - tuple (lower_bound, upper_bound)
    """
    mean = np.mean(data)
    se = np.std(data, ddof=1) / np.sqrt(len(data))
    
    # z-score for common confidence levels
    z_scores = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
    z = z_scores.get(confidence, 1.96)
    
    return mean - z * se, mean + z * se
# -------------------------------
#Seed Setter for Reproducibility
# -------------------------------
def set_seed(seed=42):
    """
    Set random seed for reproducibility.
    """
    np.random.seed(seed)