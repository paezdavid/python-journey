import os

def checkFolderSize(dir):
    totalSizeBytes = 0
    for root, dirs, files in os.walk(dir, topdown=True):
        for item in files:
            totalSizeBytes += os.path.getsize(os.path.join(root, item))

    totalSizeMegabytes = totalSizeBytes / 1024 / 1024
    totalSizeKilobytes = totalSizeBytes / 1024
    print(str(round(totalSizeKilobytes, 2)) + " KB")
    print(str(round(totalSizeMegabytes, 2)) + " MB")

## WINDOWS ADVICE
## When calling the function we need to escape the string by adding an 'r' before it, like so:
## checkFolderSize(r'my\path')