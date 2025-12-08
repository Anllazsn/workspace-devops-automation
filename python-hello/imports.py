import os, platform
from datetime import datetime

print("Current folder:", os.getcwd())
print("Operating system:", platform.system())
print("Date and time:", datetime.now())

print(dir(os)[:10])
