def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height * height)
    print("bmi = " +str(bmi))
    if (bmi<18.5):
        print("Under Weight")
    elif (18.5<bmi<25):
        print("Normal Weight")
    else:
        print("Over Weight")




calculate_bmi(weight=57, height=1.73)
