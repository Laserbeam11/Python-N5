#311d Project
import turtle

header = "=" * 68
h = 0
a = 0
x = 0

def scoreboard():
    print()
    print(f"\n{header}\n")
    print(f"home team: {h} | away team: {a}")
    print(f"             {x}")
    print(f"\n{header}\n")
    print()

def terminal_scoreboard():

    while x < 4:
        enter_point = input("enter point:  ")
        if enter_point.lower() == "h":
            print("home team scores")
            h += 1
            scoreboard()
        elif enter_point.lower() == "a":
            print("away team scores")
            a += 1
            scoreboard()
        elif enter_point.lower() == "x":
            print("end of period")
            x += 1
            scoreboard()

            input("continue? (enter): ")
            if a == h and x == 3:
                print("overtime +5 mins")
                winner = input("who wins? (h/a): ")
                if winner.lower() == "h":
                    print("home team wins")
                    h += 1
                    scoreboard()
                    break
                elif winner.lower() == "a":
                    print("away team wins")
                    a += 1
                    scoreboard()
                    break
    
        else:
            print("error: invalid input")
            scoreboard()

    if h > a:
        print("home team wins")
    elif a > h:
        print("away team wins")
    else:
        print("tie")

def turtle_scoreboard():
    print("hi")

print()
print("ice hockey scoreboard")

print(f"\n{header}\n")
print("h: home team")
print("a: away team")
print("x: end period")
print(f"\n{header}\n")

Te_Tu = input("Turtle graphics or terminal scoreboard? (tu/te): ")

if Te_Tu.lower() == "te":
    print("terminal scoreboard selected")
    print(f"\n{header}\n")

    terminal_scoreboard()

elif Te_Tu.lower() == "tu":
    print("turtle graphics scoreboard selected")
    print(f"\n{header}\n")

    turtle_scoreboard()



