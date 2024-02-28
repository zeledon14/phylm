import os
import glob
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
tokenizer.pre_tokenizer = Whitespace()
raw_data_path= '../data/raw/'
file_list= glob.glob(os.path.join(raw_data_path,'*.txt'))
tokenizer.train(file_list, trainer)
tokenizer.save("../data/tokenizer/tokenizer.json")