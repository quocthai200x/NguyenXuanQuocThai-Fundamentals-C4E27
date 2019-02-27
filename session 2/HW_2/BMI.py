h =(int(input("Enter your height (cm) : ")))/100

w = (int(input("Enter your weight (kg) : ")))

BMI=w/(h*h)

if BMI < 16 :
    print ('your BMI :','%.2f'% BMI,' -> you are severely underweight')
elif 16 <= BMI <= 18.5 :
    print('your BMI :','%.2f'%BMI,' -> you are underweight')
elif 18.5 < BMI <25 :
    print ('your BMI :','%.2f'%BMI,' -> you are normal')
elif 25 <= BMI <30 :
    print ('your BMI :','%.2f'%BMI,' -> you are overweight')
else : 
    print ('your BMI :','%.2f'%BMI,' -> you are obese')

