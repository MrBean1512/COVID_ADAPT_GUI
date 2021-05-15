import pandas as pd
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import os
import time

def makeGraphs(dir):
    dir = dir + '\\'
    if not os.path.isfile(dir+'virus_levels.csv'):
        print("unable to open virus_levels.csv")
        return False
    if not os.path.isfile(dir+'layout.csv'):
        print("unable to open layout.csv")
        return False
    if not os.path.isfile(dir+'people.csv'):
        print("unable to open people.csv")
        return False
    print("opening files...")
    virus_levels_df = pd.read_csv(dir+'virus_levels.csv')
    # delete empty column????
    virus_levels_df = virus_levels_df.drop(virus_levels_df.columns[[1]], axis = 1)
    
    people_df = pd.read_csv(dir+'people.csv')

    print("begin graph generation")
    graphTotalVirus(virus_levels_df, dir)
    graphMeanVirus(virus_levels_df, dir)
    # graphIncidence(people_df)
    # graphPrevelence(people_df)

def graphTotalVirus(virus_levels_df:pd.DataFrame, dir:str):
    virus_levels_df["total_virus"] = virus_levels_df.iloc[:,1:].sum(axis=1)
    fig, ax = plt.subplots()
    ax.plot(virus_levels_df['time'], virus_levels_df["total_virus"])
    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Total virus level")
    fig.tight_layout()
    fig.savefig(dir+"graphTotalVirus.png")


def graphMeanVirus(virus_levels_df:pd.DataFrame, dir:str):
    virus_levels_df["mean_virus"] = virus_levels_df.iloc[:,1:].mean(axis=1)
    fig, ax = plt.subplots()
    ax.plot(virus_levels_df['time'], virus_levels_df["mean_virus"])
    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Mean virus level")
    fig.tight_layout()
    fig.savefig(dir+"graphMeanVirus.png")
    
# def graphIncidence(people_df):
    
# def graphPrevelence(people_df):