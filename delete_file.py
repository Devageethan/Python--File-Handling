import os
s=os.remove("demo1")
print(s,"file removed")

if os.path.exists("demo1"):
    os.remove("demo1")
    print("file removed")
else:
    print("file not exists")