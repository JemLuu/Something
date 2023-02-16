def main():
    name = input("Enter your name: ")
    other = input("Enter your date of birth (XX/XX/XXXX): ")

    zsign = something(name,other)
    print(name, "your zodiac sign is", zsign)

def something(name, other):
    DOB = other.split("/")

    for i in range(3):
       DOB[i] = int(DOB[i])


    m = DOB[0]
    d = DOB[1]
    if(m == 3 and d >= 21 or m == 4 and d <= 19):
        return "Aries"
    elif(m == 4 and d >= 20 or m == 5 and d <= 20):
        return "Taurus"
    elif(m == 5 and d >= 21 or m == 6 and d <= 21):
        return "Gemini"
    elif(m == 6 and d >= 22 or m == 7 and d <= 22):
        return "Cancer"
    elif(m == 7 and d >= 23 or m == 8 and d <= 22):
        return "Leo"
    elif(m == 8 and d >= 23 or m == 9 and d <= 22):
        return "Virgo"
    elif(m == 9 and d >= 23 or m == 10 and d <= 23):
        return "Libra"
    elif(m == 10 and d >= 24 or m == 11 and d <= 21):
        return "Scorpius"
    elif(m == 11 and d >= 22 or m == 12 and d <= 21):
        return "Sagittarius"
    elif(m == 12 and d >= 22 or m == 1 and d <= 19):
        return "Capricornus"
    elif(m == 1 and d >= 20 or m == 2 and d <= 18):
        return "Aquarius"
    elif(m == 2 and d >= 19 or m == 3 and d <= 20):
        return "Pisces"
    else:
        return "Something went wrong"



if __name__ == "__main__":
    main()
