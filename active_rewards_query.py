
#!/usr/bin/env python3
import os
import json
import time

## Steps to run this script:
## FIRST, run swap_pair_index_counter.sh - this pulls all the json files for the current pairs
## SECOND, python3 active_rewards_query.py - this will tell you the current number of rewards per day per pool
## Everything else useful can be found here, and be sure to update in here: https://docs.google.com/spreadsheets/d/1QbqYW07XHW7GHUnolOQA8BPbw8qCBX4yxDCRshLyLaU/edit?usp=sharing

filepath = "./pair_staking_config_jsons/"
current_date = time.time() ## Grabs the current unix timestamp

my_path = "/home/astgeorge/SecretCLITooling/pair_staking_config_jsons/ATOM_stATOM.json"
SHD_contract_address = 'secret153wu605vvp934xhd4k9dtd640zsep5jkesstdm' 

def current_active_rewards(json_file):
    SHD_reward_rate = 0
    secondary_token_rate = 0;
    secondary_token_decimals = 0;
    token_2_str = "Token #2 per day: "
    ## Opening JSON file
    f = open("./pair_staking_config_jsons/" + json_file, "r")
    data = (json.load(f))

    for x in range(len(data['reward_tokens'])):
        if(data['reward_tokens'][x]['token']['address'] == SHD_contract_address and ( data['reward_tokens'][x]['valid_to'] > current_date )): ##ensure we only accept active campaigns
            SHD_reward_rate = data['reward_tokens'][x]['reward_per_second']
        else:
            if (data['reward_tokens'][x]['valid_to'] > current_date): ##ensure we only accept active campaigns
                secondary_token_rate = data['reward_tokens'][x]['reward_per_second']
                secondary_token_decimals = data['reward_tokens'][x]['decimals']
    print(f"{json_file :<20}" + "\t" "SHD per day:\t" + f"{str((int(SHD_reward_rate) * 86400)/pow(10,8)) : <20}" + "\t"+  f"{token_2_str : <20}" + "\t" + str((int(secondary_token_rate) * 86400)/pow(10,int(secondary_token_decimals))))

path = "/home/astgeorge/SecretCLITooling/pair_staking_config_jsons"
file_list = []

for (directory, subdirectories, files) in os.walk(path):
    file_list.extend(files)

## pull active rewards from every item in the directory
for x in file_list:
    current_active_rewards(x)

