def invertDigits(number):
    result = 0
    
    while number > 0:
        nxt_n = number % 10                # Get the remainder of integer division by 10
        result = (result * 10) + nxt_n     # Multiply result by 10 and add the calculated remainder
        number = (number - nxt_n) // 10    # Divide the number by 10 to reduce the number and get the next digit in the next iteration
        
    return result                          # The final result is the inverted number.
    
    
if __name__ == '__main__':
    n = input("Informe o numero entre a ser invertido: ")
try:
    n = int(n)
    print(invertDigits(n))
except Exception as e:
    print(e)
    
