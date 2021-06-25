'''The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.'''


def tickets(people):
    # people = [25, 25, 50, 50, 100]
    bill_25 = 0
    bill_50 = 0
    Flag = True
    for i in people:
        if i == 25:
            bill_25 += 1
            continue
        if i == 50:
            if bill_25 >= 1:
                bill_25 -= 1
                bill_50 += 1
                continue
            else:
                Flag = False
                break
        if i == 100:
            
            if bill_50 >= 1 and bill_25 >= 1:
                bill_25 -= 1
                bill_50 -= 1
                continue
            if bill_25 >= 3:
                bill_25 -= 3
                continue
            else:
                Flag = False
                break
    if Flag == True:
        return "YES"
    else:
        return "NO"

    
print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25, 50, 50, 100]))
