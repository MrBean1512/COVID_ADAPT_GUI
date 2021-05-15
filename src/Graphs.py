import pandas as pd
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import os

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

    people_raw_df = pd.read_csv(dir+'people.csv')
    people_times_df = people_raw_df.iloc[::10, 0:1] # get every 10th row (only need the time)
    people_times_df.reset_index(drop=True, inplace=True) # reindex so that indexes are continuous
    # reshape status to be per time entry
    people_status_df = pd.DataFrame(people_raw_df[' status'].values.reshape(-1, 10), columns=['p0','p1','p2','p3','p4','p5','p6','p7','p8','p9'])
    people_df = pd.concat([people_times_df, people_status_df], axis=1) #recombine the two dfs

    print("begin graph generation")
    graphTotalVirus(virus_levels_df, dir)
    graphMeanVirus(virus_levels_df, dir)
    graphIncidence(people_df, dir)
    graphPrevelence(people_df, dir)

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
    
def graphIncidence(people_df:pd.DataFrame, dir:str):
    people_df["incidence"] = people_df.iloc[:,1:].apply(lambda row: sum(row[1:]==2) ,axis=1)
    fig, ax = plt.subplots()
    ax.plot(people_df['time'], people_df["incidence"])
    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Incidence")
    fig.tight_layout()
    fig.savefig(dir+"graphIncidence.png")
    
def graphPrevelence(people_df:pd.DataFrame, dir:str):
    people_df["prevelence"] = people_df.iloc[:,1:].apply(lambda row: sum(row[1:]==2) + sum(row[1:]==3) ,axis=1)
    fig, ax = plt.subplots()
    ax.plot(people_df['time'], people_df["prevelence"])
    ax.set_xlabel("Time (minutes)")
    ax.set_ylabel("Prevelence")
    fig.tight_layout()
    fig.savefig(dir+"graphPrevelence.png")