def RPN(expression):
    stack = []
    for i in expression.split(' '): # スペースで文字を区切る
        if i == '+':
            b, a = stack.pop(), stack.pop() 
            stack.append(a + b) # スタック処理

        elif i == '-':
            b, a = stack.pop(), stack.pop() 
            stack.append(a - b)# スタック処理

        elif i == '*':
            b, a = stack.pop(), stack.pop() 
            stack.append(a * b)# スタック処理

        elif i == '/':
            b, a = stack.pop(), stack.pop() 
            stack.append(a / b) # スタック処理

        else:
            stack.append(int(i))    # 数値として変換

    return stack.pop() # 計算結果を返す

if __name__ == '__main__':
    expression = '1 2 4 + 3 4 + - 5 6 * 7 * -'    
    result = RPN(expression)

    print(f"{expression} → {result}")