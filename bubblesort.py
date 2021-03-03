import time

def bubble_sort(data,drawdata,timetick):#timetick mein speed scale se value aayegi
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
               data[j],data[j+1]=data[j+1],data[j]
               drawdata(data,['green' if x==j or x==j+1 else 'red' for x in range(len(data))])#jin do bars pr processing ho rhi hai unko green colour ka bnaega baaki ko red colour ka,note taht bars firse bn rhe hain pichle vale htt kr aur iss baar 2 ka colur green hai baaki ka red
               time.sleep(timetick)
    drawdata(data, ['green' for x in range(len(data))])#jb sorting complete ho jaye to saare bars ko green krne ke liye
