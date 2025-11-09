import os
import lzma
from tqdm import tqdm

def xz_decompress(directory):
    files = []
    for filename in os.listdir(directory):
        if filename.endswith('.xz') and os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)
    return files
        
folder_path = "F:/LocalLLM/datasets/extracted_data/openwebtext"
output_file_train = "output_train.txt"
output_file_val = "output_val.txt"
vocab_file = "vocab.txt"

files = xz_decompress(folder_path)
total_files = len(files)
split_idx = int(total_files * 0.9)
files_train = files[:split_idx]
files_val = files[split_idx:]

vocab = set()

# train files
with open(output_file_train, 'w', encoding='utf-8') as outfile:
    for filename in tqdm(files_train, total=len(files_train)):

        file_path = os.path.join(folder_path, filename)
        with lzma.open(file_path, 'rt', encoding='utf-8') as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            vocab.update(characters)
            
# validation files
with open(output_file_val, 'w', encoding='utf-8') as outfile:
    for filename in tqdm(files_val, total=len(files_val)):

        file_path = os.path.join(folder_path, filename)
        with lzma.open(file_path, 'rt', encoding='utf-8') as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            vocab.update(characters)
        
with open(vocab_file, 'w', encoding='utf-8') as vocab_out:
    for i in vocab:
        vocab_out.write(i + '\n')