#Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает, преобразует 
#и выводит на экран числа по определенному правилу. Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь.
#Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения использовать нельзя.
#Шеснадцатиричные нечетные числа, не превышающие 4096 в десятичной СС, у которых 2 справа цифра равна С.
#Вывести числа и их количество. Минимальное число вывести прописью.


z = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять',
    'A':'десять', 'B':'одиннадцать', 'C': 'двенадцать', 'D':'тринадцать',
     'E':'четырнадцать', 'F':'пятнадцать'}          #словарь
             
buf_r = 1                       #размер чтения
w_buf = ''                      #рабочий буфер
w_buf_len = buf_r               #длина рабочего буфера
d_min = 4096
s_min = ''
k = 0
with open("text.txt") as file:
    buf = file.read(buf_r)
    if not buf:
        print("Файл пуст")
    while buf:
        while buf >= '0' and buf <= 'F':
            w_buf += buf
            buf = file.read(buf_r)         #условия для обработки блока
        if len(w_buf) > 1:
            fb = True
            if w_buf[-2] != 'C':
                fb = False
        if fb and len(w_buf) > 1:
            if w_buf[-2] == 'C' and len(w_buf) < 4:
                d = int(w_buf, 16)
                if d % 2 == 1:
                    k += 1
                    print(w_buf)
                    if d < d_min:
                        d_min = d
                        s_min = w_buf
        w_buf = ''
        buf = file.read(buf_r)
    print(k)
    if d_min == 4096:
        print('нет подходящих чисел')
    else:
        print('минимальное число=', s_min)      #замена из словаря
        for i in range(len(s_min)):
            j = s_min[i]
            print(j + ' - ',z[s_min[i]])
                
    
    
            
            
        
       
    
        
   
   
            
