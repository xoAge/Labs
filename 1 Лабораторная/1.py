#Дан двумерный массив целых чисел.
#Напишите скрипт нахождения суммы минимальных элементов из каждой строки.
#Если минимальных элементов в строке несколько, то складывать все.
import numpy as np
row = 5
a = np.array([[0, 2, -6, 5, 0],
              [1, 0, 0, -4, -3],
              [0, 1, 3, -1, -1],
              [5, 1, 2, 0, 7],
              [1, 4, 2, 3, 8]])
min = np.min(a)
for i in range(row):
    for j in range(row):
        if (a[i][j] <= min):
            min = a[i][j]
       
res = a.min(axis=1)
print(res)

    
    
            
            
        
       
    
        
   
   
            
