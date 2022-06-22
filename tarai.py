import time

def tarai(x,y,z):
    if x<=y:
        return y
    else:
        return tarai (tarai(x-1,y,z),tarai(y-1,z,x),tarai(z-1,x,y)) 

print(tarai(13,5,0))

# 処理時間の計測
time_sta = time.time()
time.sleep(1)
time_end = time.time()
tim = time_end- time_sta
print(tim)

## 環境 : MacBook Pro (13-inch, M1, 2020),OS:Monterey,Python 3.9.12
## 処理時間は　1.00506591796875　でした。
