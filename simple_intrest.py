def simple_interest(principal, intrest, time):
    return (principal * intrest * time) / 100
    

if __name__ == "__main__":
    p = int(input("Enter Principal amount: "))
    r = float(input("Enter Rate of interest: "))
    t = int(input("Enter Time in years: "))

    print("Simple Interest =", simple_interest(p,r,t))