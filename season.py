mon=input("enter month ")
date=int(input("enter date "))
if date>31:
    print("invalid")
    if mon=="feb":
        if date>28:
            print("invalid")
elif(mon=="mar" and date>=20) or (mon=="apr")or (mon=="may")or (mon=="jun"and date<=20):
    season="summer"
elif(mon=="jun" and date>=21) or (mon=="jul")or (mon=="aug")or (mon=="sep"and date<=21):
    season="spring"
elif(mon=="sep" and date>=22) or (mon=="oct")or (mon=="nov")or (mon=="dec"and date<=20):
    season="fall"
else:
    season="winter"
    print("the season is ",season)
