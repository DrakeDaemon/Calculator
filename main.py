import time

# Calculator

def calc():
    while True:
        try:
            print('Simple Calculator. made by JSmile_')
            time.sleep(0.5)
            inp = int(input('Please enter operation: \n1.Add\n2.Substract\n3.Divide\n4.Multiply\n5.Exit\n'))
            if inp == 5:
                print('Shutting off.')
                exit()
            x = float(input('Enter first number: '))
            y = float(input('Enter second number: '))
            if inp == 1:
                print(x+y)
                exit()
            elif inp == 2:
                print(x-y)
                exit()
            elif inp == 3:
                print(x/y)
                exit()
            elif inp == 4:
                print(x*y)
                exit()
        except ValueError:
            print('Invalid data.')
        except KeyboardInterrupt:
            print('Shutting off.')
            exit()

# Running
if __name__ == "__main__":
    calc()
