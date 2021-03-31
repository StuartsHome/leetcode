"""
The shoelace formula or shoelace algorithm (also known as Gauss's area formula and the surveyor's formula[1])
is a mathematical algorithm to determine the area of a simple polygon whose vertices are described by their Cartesian coordinates in the plane.

"""




aa = [[10,20], [30,40], [40,50], [60,70], [80,90]]
N = len(aa)
for i in range(N-2):                # The three for loops are offset to allow the final loop to be (i - 2), (j - 1) (k)
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print ("i: ", i, "j: ", j, "k: ",k)
