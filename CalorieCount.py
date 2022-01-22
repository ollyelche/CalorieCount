#a code that has an array of 'morning' 'afternoon' and 'night'. Also has an array of calories lost based on the amount of minutes and pace I ran. 

calories = [] 
string = ''
amount = 0
entry = []
morning = []
afternoon = []
night = []
total, total1, total2, totalcalories, total3 = 0, 0, 0, 0, 0

with open("CalCountOut.doc", "a") as outFile:
    print("Starting from? [morning/afternoon/night]: ")
    while True:
        start = input()
        endloop = 'N'
        if start == "morning" or start == 'Morning':
            outFile.write('Morning intake ')
            outFile.write("\n")
            while endloop == 'N' or endloop == 'n':
                entry =  input("Enter entry: ")
                amount = input("Enter calorie for entry: ")
                morning.append('| ' + entry + ' : ' + amount + ' Calories ')
                amount = int(amount)
                total += amount
                endloop = input("Is that all? [Y/N]: ")
            for i in morning:
                outFile.write(i)
            total1 = str(total)
            outFile.write('\n')
            outFile.write('Total morning calories = ' + total1)
            start = input('Continue to [afternoon/night]: ')
            break
        if start == 'afternoon' or start == 'Afternoon':
            outFile.write('Afternoon intake ')
            outFile.write("\n")
            while endloop == 'N' or endloop == 'n':
                amount = 0
                total = 0
                entry =  input("Enter entry: ")
                amount = input("Enter calorie for entry: ")
                afternoon.append('| ' + entry + ' : ' + amount + ' Calories ')
                amount = int(amount)
                total += amount
                endloop = input("Is that all? [Y/N] ")
            for i in afternoon:
                outFile.write(i)
            total2 = str(total)
            outFile.write('\n')
            outFile.write('Total afternoon calories = ' + total2)
            start = input('Continue to [night/morning/afternoon]: ')
            break
        if start == 'night' or start == 'Night':
            outFile.write('Night intake ')
            outFile.write("\n")
            while endloop == 'N' or endloop == 'n':
                amount = 0
                total = 0
                entry =  input("Enter entry: ")
                amount = input("Enter calorie for entry: ")
                night.append('| ' + entry + ' : ' + amount + ' Calories ')
                amount = int(amount)
                total += amount
                endloop = input("Is that all? [Y/N] ")
            for i in night:
                outFile.write(i)
            total3 = str(total)
            outFile.write('\n')
            outFile.write('Total afternoon calories = ' + total3)
            break
        outFile.write('\n')
        totalcalories = total1 + total2 + total3
        totalcalories = str(totalcalories)
        outFile.write('Total calories: ' + totalcalories)
        print('Please Enter either Morning, Afternoon, or Night! ')

    
    
outFile.close()

#add frequent meals, add a calculator for amount ran, calories per cup of coffee
#    