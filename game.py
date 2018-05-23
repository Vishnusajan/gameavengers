i=0
j=0
avengers=["captain america","doctor strange","thor","hulk","iron man","black widow","spiderman","black panther"]
ThanosPower=95

def game(k):
    if k==0:
        return 92
    elif k==1:
        return 92
    elif k==2:
        return 99
    elif k==3:
        return 98
    elif k==4:
        return 97
    elif k==5:
        return 91
    elif k==6:
        return 92
    elif k==7:
        return 93
def main():
    i=0
    j=1
    while (i<8):
        if j < i:
            j = i - j
        else:
            j = j - i
        while (j<8 and i!=j):

            print('START THE GAME')
            avgpow=0
            sumpow=0
            print('Select your two heroes')
            print('select\t0-CAPTAIN AMERICA\n 1-DOCTOR STRANGE\n 2-THOR\n 3-HULK\n 4-IRON MAN\n 5-BLACK WIDOW\n 6-SPIDERMAN\n 7-BLACK PANTHER')
            m=int(input('Enter your first choice: '))
            n=int(input('enter your second choice: '))
            sumpow = sumpow + game(i)+game(j)+game(m)+game(n)
            avgpow=sumpow/4.0
            print('your superheroes are')
            print(avengers[i])
            print(avengers[j])
            print(avengers[m])
            print(avengers[n])
            if(avgpow>95):
               print('AVENGERS WON')
            else:
               print('THANOS WON')
            j=j+5
            print('enter 0 if you want to quit game')
            a=int(input('enter your choice '))
            if a==0:
              j=50
              break
        i=i+1
        if(j==50):
          break
        if i==8:
           i=0
        
    return

main()
