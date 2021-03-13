import sys

# Function to find out which of the unvisited node
# needs to be visited next

def to_be_visited():
    global visited_and_distance
    v = - 10
    # Choosing the vertex with the minimum distance

    for index in range(number_of_vertices):
        if visited_and_distance[index][0] == 0 \
        and (v < 0 or visited_and_distance[index][1] <= \
        visited_and_distance[v][1]):
            v = index
    return v

# Creating the graph as an adjacency matrix
vertices = [[0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]]
edges =  [[0, 3, 4, 0],
          [0, 0, 0.5, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 0]]

number_of_vertices = len(vertices[0])

# The first element of the lists inside visited_and_distance
# denotes if the vertex has been visited.
# The second element of the lists inside the visited_and_distance
# denotes the distance from the source.

visited_and_distance = [[0,0]]
for i in range(number_of_vertices - 1):
    visited_and_distance.append([0, sys.maxsize])

for vertex in range(number_of_vertices):
    # Finding the next vertex to be visited
    to_visit = to_be_visited()
    for neighbour_index in range(number_of_vertices):
        # Calculating the new distance for all unvisited neighbours
        # of the chosen vertex
        if vertices[to_visit][neighbour_index] == 1 and \
            visited_and_distance[neighbour_index][0] == 0:
            new_distance = visited_and_distance[to_visit][1] \
                + edges[to_visit][neighbour_index]
                # Updating the distance of the neighbour if its current distance
                # is greater than the distance that has just been calculated
            if visited_and_distance[neighbour_index][1] > new_distance:
                visited_and_distance[neighbour_index][1] = new_distance
    # Visiting the vertex found earlier
    visited_and_distance[to_visit][0] = 1

i = 0


# Printing the shortest distance from the source to each vertex
for distance in visited_and_distance:
    print("The shortest distance of", chr(ord('a') + i), \
        " from the source vertex a is:", distance[1])
    i = i + 1

# To Do
# First see if the algo worrks
# Second to see differences between other implementations - possibly using file
# - instead of adjaceny matrix
# Thirdly Implement algorithm using Citymapper constraints

if __name__ == '__main__':
    pass