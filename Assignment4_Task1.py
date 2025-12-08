try:
    with open("sample.txt", "rt")as fh:
     data = fh.readlines()

except FileNotFoundError:
    with open("sample.txt", "wt") as fh:
      fh.write("This is a sample tex file\n")
      fh.write("It contains multiple lies.")

finally:
    with open("sample.txt", "rt")as fh:
        data = fh.readlines()
print(data)