import time

def calculator():
    print("Welcome to Nooby's calculator - the absolute worst calculator of all time" )
    calc_symbol = input("type the thing u want to use: ( +, -, *, :, **[nⁿ] )" )
    if (calc_symbol == "+"):
        first_number_add = input("first: ")
        second_number_add = input("second: ")
        sum_add = float(first_number_add) + float(second_number_add)
        print(sum_add)
        time.sleep(2)
    if (calc_symbol == "-"):
        first_number_sub = input("first: ")
        second_number_sub = input("second ")
        sum_sub = float(first_number_sub) - float(second_number_sub)
        print(sum_sub)
        time.sleep(2)
    if (calc_symbol == "*"):
        f_n_m = input("first: ")
    #stands for first_number_multi
        s_n_m = input("second: ")
    #stands for second_number_multi
        s_m = float(f_n_m) * float(s_n_m)
        if s_n_m == 0:
            print("im disappointed in you")
        print(s_m)
        time.sleep(2)
    #stands for sum_multi
    if (calc_symbol == ":"):
        fnd = input("first: ")
    #fnd stands for first_number_div
        snd = input("second: ")
    #snd stands for second_number_div
        sd = float(fnd) / float(snd)
    #sd stands for sum_div
        print(sd)
        time.sleep(2)
    if (calc_symbol == "**"):
        ttp1 = input("first: ")
    #stands for to_the_power_1
        ttp2 = input("second: ")
    #stands for to_the_power_2
        ttps = float(ttp1) ** float(ttp2)
    #stands for to_the_power_sum
        print(ttps)
        time.sleep(2)

while True:
    calculator()
    restart = input('Do you want to restart? (y/n): ')
    if .lower() != 'y':
        break
