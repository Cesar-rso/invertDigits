def invertDigits(number):
    n = []
    result = 0
    
    while number > 0:                       # This loop gets the last digit from the number 
        nxt_n = number % 10                 # with a modulus operation and stores it in the array n.
        n.append(nxt_n)                     # Then subtract it from the original number and divides
        number = (number - nxt_n) // 10     # the number by 10 to completely remove the last digit.
        
    for digit in n:                         # This loops through the array n and for each number
        result = (result * 10) + digit      # in it, the current result is multiplied by 10 and
                                            # added the current number.
    return result                           # The final result is the inverted number.
    
    
if __name__ == '__main__':
    n = input("Informe o numero entre a ser invertido: ")
try:
    n = int(n)
    print(invertDigits(n))
except Exception as e:
    print(e)
    
