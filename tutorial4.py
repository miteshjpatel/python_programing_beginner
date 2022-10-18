# Python IF/ELIF/ELSE

age = int(input("Input your age:"))

if age == 16:
    print('Hey you are 16!!')
elif age < 16:
    print('Your are younger then 16....')    
else:
    print('Your are older then 16')    


height = int(input('Enter your height:'))    

if height <= 1:
    print('You cannot ride, under 1m')
elif height == 5:
    print('Wow you are tall!!!')     
elif height >= 2:
    print('You can ride, over 2m')
else:
    print('You can ride')           