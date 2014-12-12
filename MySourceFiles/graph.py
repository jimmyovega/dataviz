"""Part II of Visualization project"""

from collections import Counter
from parse import parse

import csv
import matplotlib.pyplot as plt
import numpy as np


MY_FILE = "../data/sample_sfpd_incident_all.csv"

def visualize_days():
    """Visualize data by day of the week"""

    #grab parsed data object and save it to the data_file variable
    data_file = parse(MY_FILE,",")

    #make a variable called counter that will iterate though each line
    #in the parsed data object and count how many incidents has happened
    #on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    #Now we are separating the values according to days of the week
    data_list = [
        counter["Monday"],
        counter["Tuesday"],
        counter["Wednesday"],
        counter["Thursday"],
        counter["Friday"],
        counter["Saturday"],
        counter["Sunday"]
    ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    #Put data into plot
    plt.plot(data_list)

    #Assign labels alongside with the plot data
    plt.xticks(range(len(day_tuple)),day_tuple)

    #Save the graph into a PNG format
    plt.savefig("Days.png")

    #Close figure
    plt.clf()

def visualize_type():
    """Visualize data category in a bar graph"""
    data_file = parse(MY_FILE,",")

    #Same as visualize_days except it returns a dict where it sums the total incidents in a Category
    counter = Counter(item["Category"] for item in data_file)

    #Sets the labels based on the keys of our counter
    labels = tuple(counter.keys())

    #Set where the label hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5

    #Width of each bar
    width = 0.5

    #Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)

    #Assign labels and tick location to x-axis
    plt.xticks(xlocations + width/2, labels, rotation=90)

    #Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.4)

    #Make the overall graph/figure larger
    plt.rcParams['figure.figsize']= 12,8

    #Save the graph into "Type.png"
    plt.savefig("Type.png")

    #Close figure
    plt.clf()


def main():
    visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()
