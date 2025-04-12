import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

def save_plot(fig, filename):
    """Save a matplotlib figure to the figures folder."""
    os.makedirs("figures", exist_ok=True)
    fig.savefig(os.path.join("figures", filename), bbox_inches="tight")

def plot_predictions(y_true, y_pred, title="Predicted vs Actual"):
    """Scatter plot comparing predicted and actual values."""
    fig, ax = plt.subplots()
    sns.scatterplot(x=y_true, y=y_pred, ax=ax)
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title(title)
    return fig
