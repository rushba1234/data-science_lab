filename=input("Enter the file name:")
with open(filename,"r")as f:
    line_count=sum(1 for line in f)
    print("Number of lines:",line_count)
