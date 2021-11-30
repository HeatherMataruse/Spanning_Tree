#by Heather Mataruse

infinity_variable = 9999999


no_of_vertices = 7


matrix = [[0, 28, 0, 0, 0, 10, 0],
    [28, 0, 16, 0, 0, 0, 14],
    [0, 16, 0, 12, 0, 0, 0 ],
    [0, 0, 12, 0, 22, 0, 18],
    [0, 0, 0, 22, 0, 25, 24],
    [10, 0, 0, 0, 25, 0, 0],
    [0, 14, 0, 18, 34, 0, 0]]
    

visited_vertices = [0, 0, 0, 0, 0, 0, 0]


number_of_edges = 0


visited_vertices[0] = True



print("EDGE : WEIGHT\n")


while (number_of_edges < no_of_vertices - 1):
    
  
    mini = infinity_variable
    a = 0
    b = 0
    

    for k in range(no_of_vertices):
      
        if visited_vertices[k]:
            for i in range(no_of_vertices):
                if ((not visited_vertices[i]) and matrix[k][i]):  

                    if mini > matrix[k][i]:
                        mini = matrix[k][i]
                        a = k
                        b = i

    print("Node " + str(a+1) + " -" + " Node " + str(b+1) + " :  Weight " + str(matrix[a][b]))
    
  
    visited_vertices[b] = True

    number_of_edges += 1
