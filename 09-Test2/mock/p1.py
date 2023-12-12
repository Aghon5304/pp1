def f(player1,player2):
    countP1=0
    countP2=0
    for x in player1:
        if( x == "A" or "K" or "Q" or "J" or "T"):
            countP1+=10
        else:
            countP1+=int(x)
    for x in player2:
        if( x == "A" or "K" or "Q" or "J" or "T"):
            countP2+=10
        else:
            countP2+=int(x)
    return countP1>countP2

if __name__ == "__main__":
    print(f("9532","K8"))