user_input=str(input("Enter text to write to the file:"))
file=open("output.txt","wt")
file.write(user_input)
print(f"Data written to successfully output.txt")
file.close()
################################################################
additional_input=str(input("Enter Additional text to append:"))
file=open("output.txt","at")
file.write("\n" + additional_input)
file.close()
################################################################
file=open("output.txt","rt")
CONTENT=file.readlines()
for i in CONTENT:
    print(i.strip())