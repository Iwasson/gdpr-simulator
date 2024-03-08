import matplotlib.pyplot as plt

def display_histogram(data):
    plt.hist(data, bins=max(data) - min(data) + 1, align='left', rwidth=0.8)
    plt.xlabel('Integers')
    plt.ylabel('Frequency')
    plt.title('Histogram of Integers')
    plt.grid(axis='y', alpha=0.75)
    #plt.show()
    plt.savefig('webapp/static/link_dist.png')
    