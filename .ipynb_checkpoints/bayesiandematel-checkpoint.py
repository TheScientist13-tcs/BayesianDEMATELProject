from scipy.stats import beta
import warnings
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
warnings.filterwarnings("ignore", "is_categorical_dtype")
warnings.filterwarnings("ignore", "use_inf_as_na")

    
class Score:
    def __init__(self, score, concentration, label=""): ## concentration is how much the distribution concentrates on the score
        self.k = score
        self.kappa = concentration
        self.label = label
        self.alpha_k, self.beta_k = self._compute_beta_dist_params(self.k, self.kappa)
        self.dist = beta(a=self.alpha_k, b=self.beta_k, loc=1, scale=4)
    
    def _compute_beta_dist_params(self, k, kappa):
        alpha_k = ((k-1)/4)*(kappa - 2) + 1
        beta_k = (1 - (k-1)/4)*(kappa - 2) + 1 
        return alpha_k, beta_k
    
    def pdf(self, x):
        return self.dist.pdf(x)
    
    def cdf(self,x):
        return self.dist.cdf(x)
    
    def sample(self, n=1):
        return self.dist.rvs(size=n)
    
    def plot_pdf(self):
        x = np.linspace(1,5, num=1000)
        sns.lineplot(x=x, y=list(map(self.pdf, x)))
        if self.label == "":
            plt.title(f"Probability Density Plot")
        else:
            plt.title(f"Probability Density of {self.label}")
        plt.xlabel("X")
        plt.ylabel("Beta density")
        plt.show()
        
class DEMATEL:
    def __init__(self, adjacency, num_concepts):
        self.adjacency = adjacency
        self.num_concepts = num_concepts
        
    def compute_total_relation_matrix():
        pass