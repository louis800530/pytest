if __name__ == "__main__":
    g=[]
    f = open('A.txt', 'w', encoding = 'UTF-8')

    for i in range(1,10+1):
        g.append(i*i)
        print(g[i-1])
        f.write(str(g[i-1]))
        f.write('\n')
    print(i)
    f.close()
    f = open('A.txt', 'r', encoding = 'UTF-8')
    while True :
           i = f.readline()
           if i=='': break
           print(i,end = '')
    f.close()

def sumofAB(a=1,b=5):
    return a+b
