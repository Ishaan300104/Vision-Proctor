import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file to check its structure
file_path = "yolov5\\runs\\train\\exp6\\results.csv"
data = pd.read_csv(file_path)

# Clean up column names by stripping leading and trailing spaces
data.columns = data.columns.str.strip()

# We have three different metrics - Training, Validation and overall metrics
train_metrics = ['train/box_loss', 'train/obj_loss', 'train/cls_loss']
overall_metrics = ['metrics/precision', 'metrics/recall', 'metrics/mAP_0.5', 'metrics/mAP_0.5:0.95']
val_metrics = ['val/box_loss', 'val/obj_loss', 'val/cls_loss']

# Function to include all metrics, separating them as train, validation, and overall metrics (precision, recall, mAP)
def plot_full_separate_metrics(data, train_metrics, val_metrics, overall_metrics):
    epochs = data['epoch']
    
    # Plotting training metrics
    fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(8, 12), constrained_layout=True)
    axs = axs.flatten()

    for i, metric in enumerate(train_metrics):
        axs[i].plot(epochs, data[metric], color='slateblue', linewidth=1, marker='o', markersize=2)
        axs[i].set_title(f'Training {metric.replace("_", " ").title()}', fontsize=14, fontweight='bold')
        axs[i].set_xlabel("Epoch", fontsize=12)
        axs[i].set_ylabel(metric, fontsize=12)
        axs[i].grid(True)

    plt.suptitle("Training Metrics", fontsize=16, fontweight='bold')
    plt.show()

    # Plotting validation metrics
    fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(8, 12), constrained_layout=True)
    axs = axs.flatten()

    for i, metric in enumerate(val_metrics):
        axs[i].plot(epochs, data[metric], color='g', linewidth=1, marker='o', markersize=2)
        axs[i].set_title(f'Validation {metric.replace("_", " ").title()}', fontsize=14, fontweight='bold')
        axs[i].set_xlabel("Epoch", fontsize=12)
        axs[i].set_ylabel(metric, fontsize=12)
        axs[i].grid(True)

    plt.suptitle("Validation Metrics", fontsize=16, fontweight='bold')
    plt.show()

    # Plotting overall metrics - precision, recall, mAP
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10), constrained_layout=True)
    axs = axs.flatten()

    for i, metric in enumerate(overall_metrics):
        axs[i].plot(epochs, data[metric], color='deeppink', linewidth=1, marker='o', markersize=2)
        axs[i].set_title(f'{metric.replace("_", " ").title()}', fontsize=14, fontweight='bold')
        axs[i].set_xlabel("Epoch", fontsize=12)
        axs[i].set_ylabel(metric, fontsize=12)
        axs[i].grid(True)

    plt.suptitle("Overall Metrics: Precision, Recall, mAP", fontsize=16, fontweight='bold')
    plt.show()

# Plot the training, validation, and overall metrics separately
plot_full_separate_metrics(data, train_metrics, val_metrics, overall_metrics)
