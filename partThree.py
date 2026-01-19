def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    T1 = float(d.replace("£",""))
    return(T1)

def percent_to_float(p):
    T2 = float(p.replace("%",""))
    T3 = float(T2/100)
    return(T3)


main()
