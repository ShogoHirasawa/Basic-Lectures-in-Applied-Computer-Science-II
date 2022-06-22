## 課題1-1 ハノイの塔 再帰的処理ver
def hanoi(n, A, C, B):
    if n > 1:
        hanoi(n-1, A, B, C)  
        print(A + '->' + C)
        hanoi(n-1, B, C, A)  
    else:
        print(A + '->' + C)

n = int(input('n >> '))
hanoi(n, 'A', 'C', 'B')

