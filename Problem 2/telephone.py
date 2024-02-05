def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    area_code=phone_number // 10000000
    digit_456= phone_number // 10000 % 1000
    digit_678= phone_number % 10000
    
if __name__ == "__main__":
    telephone()