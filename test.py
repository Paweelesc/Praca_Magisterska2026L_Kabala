import os

folders = [
    "audio/ref",
    "audio/anchor",
    "audio/Auraliz_12",
    "audio/Auraliz_24",
    "audio/auraliz_48",
]

for folder in folders:
    print(f"\n--- {folder} ---")
    if os.path.isdir(folder):
        for f in os.listdir(folder):
            print(repr(f))
    else:
        print("BRAK FOLDERU")