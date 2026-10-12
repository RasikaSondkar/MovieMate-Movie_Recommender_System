import gzip
import shutil
import os

input_file = "similarity.pkl"
output_file = "similarity.pkl.gz"

with open(input_file, "rb") as source:
    with gzip.open(output_file, "wb", compresslevel=9) as target:
        shutil.copyfileobj(source, target)

print("Compression completed!")
print(f"Original size: {os.path.getsize(input_file) / (1024 * 1024):.2f} MB")
print(f"Compressed size: {os.path.getsize(output_file) / (1024 * 1024):.2f} MB")