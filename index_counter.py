#!/usr/bin/env python3
import os

## Steps to run this script:
## FIRST, run swap_pair_index_counter.sh - this pulls all the json files for the current pairs
## SECOND, run counter.py - this will tell you the indexes and what they should be updated to for every reward campaign
## Everything else useful can be found here: https://docs.google.com/spreadsheets/d/1QbqYW07XHW7GHUnolOQA8BPbw8qCBX4yxDCRshLyLaU/edit?usp=sharing

filepath = "./pair_staking_config_jsons/"

def count_index(pair_name_json):
    data = open(filepath + pair_name_json, "r")
    counter = 0;
    for line in data:
        counter+=1
    print(f"{pair_name_json :<20}" + " \tcurrent index: " + f"{compute_current_campaign_index(counter) :<5}" + "\t | Update To -> " + new_campaign_index(counter) + " for new rewards campaign.")

## -15 is the standard number of lines of all of the LP reward config file + closing bracket info
## 11 is the number of lines per campaign index
## 0 based index so we need to subtract off. If a token has no campaign it will appear as "-1"
def compute_current_campaign_index(total_lines):
    return str(int((total_lines-15) / 11)-1)

def new_campaign_index(total_lines):
    return str(int((((total_lines-15) / 11))))

my_path = "/home/astgeorge/SecretCLITooling/pair_staking_config_jsons"
file_list = []

for (directory, subdirectories, files) in os.walk(my_path):
    file_list.extend(files)

## run index counter on each file in the subdirectory
for x in file_list:
    count_index(x)


