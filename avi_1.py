  
def MaxString(A, st, k):
    Rez = False
    max_len = 0
    cur_state = sta_state
    i = k
    while i < len(st):
        if st[i] == A[0][1]:
            t0 = 1
            while A[A[cur_state][2]][1] == st[i+1]:
                #print(st[i],' - ',t0)
                cur_state = A[cur_state][2]
                if cur_state == end_state:
                    max_len = max(max_len,t0)
                    #print('...',t0)
                t0 += 1
                #cur_state = A[cur_state][2]
                i+=1
                if i >= len(st)-1: break
            #print(st[i],' - ',t0)
            cur_state = A[cur_state][2]
            if cur_state == end_state:
                max_len = max(max_len,t0)
                #print('...',t0)
            
        i +=1
        cur_state = sta_state
    if max_len > 0: Rez = True
    return [Rez, max_len]


A = []
file = open('test.txt')
lst = file.readline()[:-1].split()
sta_state = int(lst[0])
end_state = int(lst[1])
while True: # Условие остановки внутри
    row = file.readline()[:-1]
    if len(row) == 0: # Проверка на конец считывания
        break
    lst = row.split()
    A.append([int(lst[0]),str(lst[1]),int(lst[2])])
file.close() # Закрываем файл

st = 'abacabccdabcdefcdabcdefdefdeabcd'
#st = 'fdabacabfd'
#st = 'abc'
#st = 'abacabcdcdabcdefdcdabcdefdefdabcdabcdefdefdeabc'# для test1.txt
k = 0
rezult = MaxString(A, st, k)
print(rezult[0],rezult[1])






        
            
