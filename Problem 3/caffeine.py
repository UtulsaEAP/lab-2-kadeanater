
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    caffeine_halflife_6hrs= caffeine_mg*(0.5**(6/6))
    caffeine_halflife_12hrs= caffeine_mg*(0.5**(12/6))
    caffeine_halflife_24hrs= caffeine_mg*(0.5**(24/6))

    print(f'After 6 hours: {caffeine_halflife_6hrs:.2f} mg\n'f'After 12 hours: {caffeine_halflife_12hrs:.2f} mg\n'f'After 24 hours: {caffeine_halflife_24hrs:.2f} mg')
   
if __name__ == "__main__":
    caffeine()