import datetime

def questions():
    ### Prerequisite questions ###
    sex = input("Are you a male or a female? [male/female]\n").lower()
    dob = input("What is your D.O.B? [year month day]\n").lower()
    year, month, day = dob.split(' ')
    day_calc = datetime.datetime(int(year), int(month), int(day))
    day = day_calc.strftime("%a")

    return sex, day

def kradin(sex, day):
    boy = {
        "Mon" : "Kojo",
        "Tue" : "Kwabena",
        "Wed" : "Kwaku",
        "Thu" : "Yaw",
        "Fri" : "Kofi",
        "Sat" : "Kwame",
        "Sun" : "Kwasi"
    }
    
    girl = {
        "Mon" : "Adjoa",
        "Tue" : "Abena",
        "Wed" : "Akua",
        "Thu" : "Yaa",
        "Fri" : "Afua",
        "Sat" : "Ama",
        "Sun" : "Akosua"
    }

    if sex == "boy":
        return boy[day]
    else:
        return girl[day]

def main():
    sex, day = questions()
    name = kradin(sex, day)
    print(f"Your Kradin name is: {name}")


main()