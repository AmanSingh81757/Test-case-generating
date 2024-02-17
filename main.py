import os

fs =  3 # number of Files
print("Generating Test Cases")
for i in range(fs):
    os.system("py generate.py > extra/in%s.txt"%("0"+str(i) if i<10 else str(i)))
    print("file %d generated"%i)
print("Test Cases Generated\n")



os.system("g++ chintu.cpp -o solution")
print("Compiling Solutions")
for i in range(fs):
    os.system(".\solution < extra/in%s.txt > extra/out%s.txt"%("0"+str(i) if i<10 else str(i),"0"+str(i) if i<10 else str(i)))
print("Solutions Compiled\n")



# print("Verifying Solutions")
# for i in range(fs):
#     print("file  %d"%i)
#     os.system("echo \"in%s.txt out%s.txt\" | python3 verify.py"%("0"+str(i) if i<10 else str(i),"0"+str(i) if i<10 else str(i)))

# print("Solutions Verified\n")
