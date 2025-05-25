def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    input_str = input()
    num_list = input_str.split(",")
    float_list = [float(num.strip()) for num in num_list]
    return float_list

def calc_average(num_list):
    return sum(num_list) / len(num_list)

def find_min_max(num_list):
    return [min(num_list), max(num_list)]

def sort_temperature(num_list):
    return sorted(num_list)

def calc_median_temperature(num_list):
    sorted_list = sorted(num_list)
    n = len(sorted_list)
    if n % 2 == 0:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        median = sorted_list[n // 2]
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("Average =", calc_average(num_list))
    print("Minimum and Maximum =", find_min_max(num_list))
    print("Sorted List =", sort_temperature(num_list))
    print("Median =", calc_median_temperature(num_list))

if __name__ == "__main__":
    main()
