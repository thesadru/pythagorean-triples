import json
from pprint import pprint
while 1:
    action = input("""exit - quit the program\nreload - reload database\nany integer - search for n as a root\nany float - search for n\n""")
    if action.lower() == 'exit':
        quit()
    elif action.lower() == 'reload':
        with open("pythagorean.json",'w') as file:
            run = 1
            while run:
                try:
                    ma,mi = int(input("maximum expected number: ")),int(input("minimum expected number: "))
                    run = 0
                except:
                    pass
            output = {"whole":{},"root":{}}
            wholeN = {}
            for a in range(mi,1+ma):
                for b in range(mi,1+ma):
                    c = a*a+b*b
                    c2 = round(c**0.5,2)
                    try:
                        output["root"][c2] += [(a,b)]
                        output["whole"][c] += [(a,b)]
                    except KeyError:
                        output["root"][c2] = [(a,b)]
                        output["whole"][c] = [(a,b)]
            file.write(json.dumps(output))
    elif '.' in action:
        try:
            with open("pythagorean.json",'r') as file:
                data = json.loads(file.read())
                pprint("possible combinations for "+action+"are:\n",data["root"][str(float(action))])
        except KeyError:
            print("not a number in current range, all numbers are rounded at 2 decimal points")
    else:
        try:
            int(action)
            try:
                with open("pythagorean.json",'r') as file:
                    data = json.loads(file.read())
                    pprint("possible combinations for "+action+"are:\n",data["whole"][str(int(action))])
            except KeyError:
                print("not a number in current range")
        except:
            print("not a possible input")