
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here
    print(f'This house is ${(current_price)}. The change is ${(current_price-last_month_price)} since last month.\nThe estimated mothly mortgage is ${((current_price* 0.051) / 12):.2f}.')
if __name__ == "__main__":
    real_estate()