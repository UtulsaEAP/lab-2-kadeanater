
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    caffeine_halflife_6hrs= float(caffeine_mg / 2)
    caffeine_halflife_12hrs=float(caffeine_halflife_6hrs / 2)
    caffeine_halflife_24hrs=float(caffeine_halflife_12hrs / 2)

    print('After 6 Hours:')
    print(caffeine_halflife_6hrs)
    print('After 12 Hours:')
    print(caffeine_halflife_12hrs)
    print('After 24 Hours:')
    print(caffeine_halflife_24hrs)
if __name__ == "__main__":
    caffeine()