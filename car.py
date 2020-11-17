carstart = False
while True:
    smash = input("> ").lower()
    if smash == 'help':
        print("START - To start the car")
        print("STOP - to stop the car")
        print("QUIT - to exit")
    elif smash == 'start':
        if carstart:
            print("car is already moving")
        else:
            carstart = True
            print("the car has started moving")
    elif smash == 'stop':
        if not carstart:
            print("the car is already stopped.")

        else:
            carstart = False
            print("car stopped.")
    elif smash== 'quit':
        break
    else:
        print(f"type 'help'(without quote) to know more")
