import statistics


def main():
    display_main_menu()
    float_list = get_user_input()
    calc_average(float_list)
    find_min_max(float_list)
    sort_temperature(float_list)
    calc_median_temperature(float_list)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    print("Enter numbers: ")
    x = input()
    u = x.split(",")
    float_list = [float(num) for num in u]
    print(float_list)
    return float_list

def calc_average(float_list):
    average = sum(float_list) / len(float_list)
    print("Average:", average)

def find_min_max(float_list):
    minimum = min(float_list)
    maximum = max(float_list)
    print ("max = ", maximum)
    print ("min = ", minimum)

def sort_temperature(float_list):
    sorted_list = sorted(float_list)
    print("sorted temperature in ascending order :",sorted_list)

def calc_median_temperature(float_list):
    median = statistics.median(float_list)
    print ("median = ", median)







if __name__ == "__main__":
    main()

