import requests
from tqdm import tqdm

ddir = "your/download/file" # << put your download directory before running the script
url = input("url >> ").strip()


fname = ddir + url.split("/")[-1]
resp = requests.get(url, stream = True)
total = int(resp.headers.get('content-length', 0))

try:
    with open(fname, 'wb') as file, tqdm(
        total = total,
        unit = 'iB',
        unit_scale = True,
        unit_divisor = 1024) as bar:
        for data in resp.iter_content(chunk_size = 1024):
            size = file.write(data)
            bar.update(size)
except Exception as e:
    print("Error: ", e)
