import os
filename="sample.txt"
if os.path.exists(filename):
    print("Reading the file content:")
    content=open(filename,"rt")
    for line in content:
        print(f"Line: {line.strip()}")
    content.close()
else:
    print(f"Error: The file '{filename}' was not found.")



#another way to do this using try-catch :
'''
filename="sample.txt"
try:
    
    print("Reading the file content:")
    content=open(filename,"rt")
    for line in content:
        print(f"Line: {line.strip()}")
    content.close()
   
                       
except Exception as e:
    print(f"Error: The file '{filename}' was not found.")
'''