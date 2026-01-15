import os
import urllib.request

urls = [
    "https://nvlabs-fi-cdn.nvidia.com/edm2/raw-snapshots/edm2-img512-s/edm2-img512-s-2147483-0.100.pkl",
    "https://nvlabs-fi-cdn.nvidia.com/edm2/raw-snapshots/edm2-img512-s/edm2-img512-s-0134217-0.100.pkl",
    "https://nvlabs-fi-cdn.nvidia.com/edm2/raw-snapshots/edm2-img512-xs-uncond/edm2-img512-xs-uncond-2147483-0.100.pkl",
]

os.makedirs("checkpoints", exist_ok=True)

for url in urls:
    filename = os.path.join("checkpoints", url.split("/")[-1])
    print(f"Downloading {filename}")
    urllib.request.urlretrieve(url, filename)
