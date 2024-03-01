import os
import glob
import json
from transformers import PreTrainedTokenizerFast

tokenizer = PreTrainedTokenizerFast(tokenizer_file="../data/tokenizer/tokenizer.json")

raw_data_path= '../data/raw/'
processed_data_path='../data/processed/'
file_list= glob.glob(os.path.join(raw_data_path,'*.txt'))
for file in file_list:
    title=file.split('/')[-1].split('.')[0]
    text_file = open(file, "r")
    #text_str= text_file.read()
    #text_str= text_str.replace("\n", "\n [CLS]")
    #print(text_str)
    indi_list=tokenizer.encode(text_file.read())
    text_file.close()
    with open(os.path.join(processed_data_path,title+'.json'), "w") as save_file:
        json.dump({'indices':indi_list}, save_file)