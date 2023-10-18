
f=open("demo","w")
f.write("writing new content")
f.close()
f=open("demo")
print(f.read())