import os

comment1 = input("Enter text to write to the file: ")
with open("output.txt", "w") as fh:
    fh.write(comment1 + "\n")
print("Data successfully written.")
with open("output.txt", "r") as fh:
    output = fh.readlines()
    print(output)
if os.path.exists("output.txt"):
    comment2 = input("Enter additional text to append: ")
    with open("output.txt", "a") as fh:
        fh.write(comment2 + "\n")
print("Data successfully appended.")
with open("output.txt", "r") as fh:
    output = fh.readlines()
    print("Final content of output.txt:")
    print(output)
