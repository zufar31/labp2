def main():
    calculate_bmi(weight=57, height=1.73)
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height * height)
    print("bmi = " +str(bmi))
    if (bmi<18.5):
        print("Under Weight")
        return -1
    elif (18.5<bmi<25):
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1


if __name__ == "__main__":
    main()

