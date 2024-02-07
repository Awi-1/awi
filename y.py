print("Привет сушатель, попробуй угадать заданное число")
number = int(input("Введите число для оценки: "))
if (number == 52):
    print("win")
else:
    if (number > 52):
        print("Число слишком большое")
    elif (number < 52):
        print("Число слишком маленькое")
    
    number = int(input("Введите число для оценки: "))

    if (number == 52):
        print("win")

    else:
        if (number > 52):
            print("Число слишком большое")
        elif (number < 52):
            print("Число слишком маленькое")
        
        number = int(input("Введите число для оценки: "))

        if (number == 52):
             print("win")
        else:
            if (number > 52):
                print("Число слишком большое")
            elif (number < 52):
                print("Число слишком маленькое")
            
            number = int(input("Введите число для оценки: "))

            if (number == 52):
                print("win")
            else:
                if (number > 52):
                    print("Число слишком большое")
                elif (number < 52):
                    print("Число слишком маленькое")
                
                number = int(input("Введите число для оценки: "))

                if (number == 52):
                    print("win")
                else:
                    print("Конец игры")






