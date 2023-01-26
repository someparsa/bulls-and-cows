import random

lngt = int(input("How many numbers? "))
rnds = int(input("How many rounds? "))
hlps = input("Do you need help? [Y/N] ")

rng=range(0,10)
hdn = random.sample(rng, lngt)

# print(hdn)

gss = [0 for i in range(lngt)]
ctr = [str(i) for i in range(lngt)]

for nr in range (rnds):
    cnr = rnds - nr

    for i in range (lngt):
        if lngt == 1:
            gss[i] = int(input("Number: "))

        else:
            gss[i] = int(input("Number " + str(i+1) + ": "))

    ck = 0

    for j in gss:
        if j in hdn:
            ck += 1
    
    tj = 0

    for i in range (lngt):


        if gss[i] in hdn:
            ctr[i] = 'Y'
        else:
            ctr[i] = 'N'
        
        if gss[i] == hdn[i]:
            tj += 1
            ctr[i] = 'C'

    if gss != hdn:
        print('\n*** fail ***')
        print('remaining rounds', cnr-1)
        print('correct guess:', ck)
        print('correct place:', tj)
        print('your guess:', gss)
        if hlps == 'Y':
            print(' ')
            print('Hint:', ctr)
            print('C: correct guess - correct position')
            print('Y: correct guess - incorrect position')
            print('Y: incorrect guess')
        print(' ')

        if cnr-1 == 0:
            print('Game Over! Answer:', hdn)
            print(' ')

    elif gss == hdn:
        print('\n*** succeed ***')
        print('remaining rounds', cnr-1)
        print('correct guess:', ck)
        print('correct place:', tj)
        print('your guess:', gss)
        print(' ')

        break
