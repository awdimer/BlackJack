import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
import pgzrun
from pgzhelper import *
import random
club2 = Actor("2_of_clubs")
club3 = Actor("3_of_clubs")
club4 = Actor("4_of_clubs")
club5 = Actor("5_of_clubs")
club6 = Actor("6_of_clubs")
club7 = Actor("7_of_clubs")
club8 = Actor("8_of_clubs")
club9 = Actor("9_of_clubs")
club10 = Actor("10_of_clubs")
clubJack = Actor("jack_of_clubs2")
clubQueen = Actor("queen_of_clubs2")
clubKing = Actor("king_of_clubs2")
clubAce = Actor("ace_of_clubs")

spade2 = Actor("2_of_spades")
spade3 = Actor("3_of_spades")
spade4 = Actor("4_of_spades")
spade5 = Actor("5_of_spades")
spade6 = Actor("6_of_spades")
spade7 = Actor("7_of_spades")
spade8 = Actor("8_of_spades")
spade9 = Actor("9_of_spades")
spade10 = Actor("10_of_spades")
spadeJack = Actor("jack_of_spades")
spadeQueen = Actor("queen_of_spades")
spadeKing = Actor("king_of_spades")
spadeAce = Actor("ace_of_spades")



diamond2 = Actor("2_of_diamonds")
diamond3 = Actor("3_of_diamonds")
diamond4 = Actor("4_of_diamonds")
diamond5 = Actor("5_of_diamonds")
diamond6 = Actor("6_of_diamonds")
diamond7 = Actor("7_of_diamonds")
diamond8 = Actor("8_of_diamonds")
diamond9 = Actor("9_of_diamonds")
diamond10 = Actor("10_of_diamonds")
diamondJack = Actor("jack_of_diamonds2")
diamondQueen = Actor("queen_of_diamonds2")
diamondKing = Actor("king_of_diamonds2")
diamondAce = Actor("ace_of_diamonds")

heart2 = Actor("2_of_hearts")
heart3 = Actor("3_of_hearts")
heart4 = Actor("4_of_hearts")
heart5 = Actor("5_of_hearts")
heart6 = Actor("6_of_hearts")
heart7 = Actor("7_of_hearts")
heart8 = Actor("8_of_hearts")
heart9 = Actor("9_of_hearts")
heart10 = Actor("10_of_hearts")
heartJack = Actor("jack_of_hearts2")
heartQueen = Actor("queen_of_hearts2")
heartKing = Actor("king_of_hearts2")
heartAce = Actor("ace_of_hearts")
gameStart = True
money = 100

spade2_draw = False
spade3_draw = False
spade4_draw = False
spade5_draw = False
spade6_draw = False
spade7_draw = False
spade8_draw = False
spade9_draw = False
spade10_draw = False
spadeJack_draw = False
spadeQueen_draw = False
spadeKing_draw = False
spadeAce_draw = False

club2_draw = False
club3_draw = False
club4_draw = False
club5_draw = False
club6_draw = False
club7_draw = False
club8_draw = False
club9_draw = False
club10_draw = False
clubJack_draw = False
clubQueen_draw = False
clubKing_draw = False
clubAce_draw = False

diamond2_draw = False
diamond3_draw = False
diamond4_draw = False
diamond5_draw = False
diamond6_draw = False
diamond7_draw = False
diamond8_draw = False
diamond9_draw = False
diamond10_draw = False
diamondJack_draw = False
diamondQueen_draw = False
diamondKing_draw = False
diamondAce_draw = False

heart2_draw = False
heart3_draw = False
heart4_draw = False
heart5_draw = False
heart6_draw = False
heart7_draw = False
heart8_draw = False
heart9_draw = False
heart10_draw = False
heartJack_draw = False
heartQueen_draw = False
heartKing_draw = False
heartAce_draw = False

spade2_draw1 = False
spade3_draw1 = False
spade4_draw1 = False
spade5_draw1 = False
spade6_draw1 = False
spade7_draw1 = False
spade8_draw1 = False
spade9_draw1 = False
spade10_draw1 = False
spadeJack_draw1 = False
spadeQueen_draw1 = False
spadeKing_draw1 = False
spadeAce_draw1 = False

club2_draw1 = False
club3_draw1 = False
club4_draw1 = False
club5_draw1 = False
club6_draw1 = False
club7_draw1 = False
club8_draw1 = False
club9_draw1 = False
club10_draw1 = False
clubJack_draw1 = False
clubQueen_draw1 = False
clubKing_draw1 = False
clubAce_draw1 = False

diamond2_draw1 = False
diamond3_draw1 = False
diamond4_draw1 = False
diamond5_draw1 = False
diamond6_draw1 = False
diamond7_draw1 = False
diamond8_draw1 = False
diamond9_draw1 = False
diamond10_draw1 = False
diamondJack_draw1 = False
diamondQueen_draw1 = False
diamondKing_draw1 = False
diamondAce_draw1 = False

heart2_draw1 = False
heart3_draw1 = False
heart4_draw1 = False
heart5_draw1 = False
heart6_draw1 = False
heart7_draw1 = False
heart8_draw1 = False
heart9_draw1 = False
heart10_draw1 = False
heartJack_draw1 = False
heartQueen_draw1 = False
heartKing_draw1 = False
heartAce_draw1 = False


playerWin2 = False
playerLoose = False
roundStart = False
hit1 = False
stand1 = False
bet2 = False
stopBet = False
again_draw = False
moneyback1 = False
doubleDown1 = False
gameOver1 = False
doubleGenerate1 = False

play = Actor("play")
hit = Actor("hit")
stand = Actor("stand")
bet = Actor("bet")
double = Actor("double")
playerWin1 = Actor("playerwin")
houseWin = Actor("housewin")
again = Actor("again")
tie = Actor("tie")
doubledown = Actor("doubledown")


WIDTH = 1000
HEIGHT = 1000

botcardCount = 0
cardCount = 0

betAmount = 0
doubleDownamount = 0


def generateCard():
    global cardCount,heartAce_draw,cardSelect,spade2_draw1,heart6_draw1,heart7_draw1,club2_draw,club3_draw,club4_draw,club5_draw,club6_draw,club7_draw,club8_draw,club9_draw,club10_draw,clubJack_draw,clubQueen_draw,clubKing_draw,clubAce_draw,spade2_draw,spade3_draw,spade4_draw,spade5_draw,spade6_draw,spade7_draw,spade8_draw,spade9_draw,spade10_draw,spadeJack_draw,spadeQueen_draw,spadeKing_draw,spadeAce_draw,diamond2_draw,diamond3_draw,diamond4_draw,diamond5_draw,diamond6_draw,diamond7_draw,diamond8_draw,diamond9_draw,diamond10_draw,diamondJack_draw,diamondQueen_draw,diamondKing_draw,diamondAce_draw,heart2_draw,heart3_draw,heart4_draw,heart5_draw,heart6_draw,heart7_draw,heart8_draw,heart9_draw,heart10_draw,heartJack_draw,heartQueen_draw,heartKing_draw,heartAce_draw,spade2_draw1,spade3_draw1,spade4_draw1,spade5_draw1,spade6_draw1,spade7_draw1,spade8_draw1,spade9_draw1,spade10_draw1,spadeJack_draw1,spadeQueen_draw1,spadeKing_draw1,spadeAce_draw1,club2_draw1,club3_draw1,club4_draw1,club5_draw1,club6_draw1,club7_draw1,club8_draw1,club9_draw1,club10_draw1,clubJack_draw1,clubQueen_draw1,clubKing_draw1,clubAce_draw1,diamond2_draw1,diamond3_draw1,diamond4_draw1,diamond5_draw1,diamond6_draw1,diamond7_draw1,diamond8_draw1,diamond9_draw1,diamond10_draw1,diamondJack_draw1,diamondQueen_draw1,diamondKing_draw1,diamondAce_draw1,heart2_draw1,heart3_draw1,heart4_draw1,heart5_draw1,heart6_draw1heart7_draw1,heart8_draw1,heart9_draw1,heart10_draw1,heartJack_draw1,heartQueen_draw1,heartKing_draw1,heartAce_draw1

    spade2_draw1 = False
    spade3_draw1 = False
    spade4_draw1 = False
    spade5_draw1 = False
    spade6_draw1 = False
    spade7_draw1 = False
    spade8_draw1 = False
    spade9_draw1 = False
    spade10_draw1 = False
    spadeJack_draw1 = False
    spadeQueen_draw1 = False
    spadeKing_draw1 = False
    spadeAce_draw1 = False

    club2_draw1 = False
    club3_draw1 = False
    club4_draw1 = False
    club5_draw1 = False
    club6_draw1 = False
    club7_draw1 = False
    club8_draw1 = False
    club9_draw1 = False
    club10_draw1 = False
    clubJack_draw1 = False
    clubQueen_draw1 = False
    clubKing_draw1 = False
    clubAce_draw1 = False

    diamond2_draw1 = False
    diamond3_draw1 = False
    diamond4_draw1 = False
    diamond5_draw1 = False
    diamond6_draw1 = False
    diamond7_draw1 = False
    diamond8_draw1 = False
    diamond9_draw1 = False
    diamond10_draw1 = False
    diamondJack_draw1 = False
    diamondQueen_draw1 = False
    diamondKing_draw1 = False
    diamondAce_draw1 = False

    heart2_draw1 = False
    heart3_draw1 = False
    heart4_draw1 = False
    heart5_draw1 = False
    heart6_draw1 = False
    heart7_draw1 = False
    heart8_draw1 = False
    heart9_draw1 = False
    heart10_draw1 = False
    heartJack_draw1 = False
    heartQueen_draw1 = False
    heartKing_draw1 = False
    heartAce_draw1 = False


    cardSelect = random.randint(0,51)
    print(cardSelect)
    if cardSelect == 0:
        spade2_draw = True
    if cardSelect == 1:
        spade3_draw = True
    if cardSelect == 2:
        spade4_draw = True
    if cardSelect == 3:
        spade5_draw = True
    if cardSelect == 4:
        spade6_draw = True
    if cardSelect == 5:
        spade7_draw = True
    if cardSelect == 6:
        spade8_draw = True
    if cardSelect == 7:
        spade9_draw = True
    if cardSelect == 8:
        spade10_draw = True
    if cardSelect == 9:
        spadeJack_draw = True
    if cardSelect == 10:
        spadeQueen_draw = True
    if cardSelect == 11:
        spadeKing_draw = True
    if cardSelect == 12:
        spadeAce_draw = True


    if cardSelect == 13:
        club2_draw = True
    if cardSelect == 14:
        club3_draw = True
    if cardSelect == 15:
        club4_draw = True
    if cardSelect == 16:
        club5_draw = True
    if cardSelect == 17:
        club6_draw = True
    if cardSelect == 18:
        club7_draw = True
    if cardSelect == 19:
        club8_draw = True
    if cardSelect == 20:
        club9_draw = True
    if cardSelect == 21:
        club10_draw = True
    if cardSelect == 22:
        clubJack_draw = True
    if cardSelect == 23:
        clubQueen_draw = True
    if cardSelect == 24:
        clubKing_draw = True
    if cardSelect == 25:
        clubAce_draw = True


    if cardSelect == 26:
        diamond2_draw = True
    if cardSelect == 27:
        diamond3_draw = True
    if cardSelect == 28:
        diamond4_draw = True
    if cardSelect == 29:
        diamond5_draw = True
    if cardSelect == 30:
        diamond6_draw = True
    if cardSelect == 31:
        diamond7_draw = True
    if cardSelect == 32:
        diamond8_draw = True
    if cardSelect == 33:
        diamond9_draw = True
    if cardSelect == 34:
        diamond10_draw = True
    if cardSelect == 35:
        diamondJack_draw = True
    if cardSelect == 36:
        diamondQueen_draw = True
    if cardSelect == 37:
        diamondKing_draw = True
    if cardSelect == 38:
        diamondAce_draw = True


    if cardSelect == 39:
        heart2_draw = True
    if cardSelect == 40:
        heart3_draw = True
    if cardSelect == 41:
        heart4_draw = True
    if cardSelect == 42:
        heart5_draw = True
    if cardSelect == 43:
        heart6_draw = True
    if cardSelect == 44:
        heart7_draw = True
    if cardSelect == 45:
        heart8_draw = True
    if cardSelect == 46:
        heart9_draw = True
    if cardSelect == 47:
        heart10_draw = True
    if cardSelect == 48:
        heartJack_draw = True
    if cardSelect == 49:
        heartQueen_draw = True
    if cardSelect == 50:
        heartKing_draw = True
    if cardSelect == 51:
        heartAce_draw = True





    if cardSelect == 0:
        spade2_draw1 = True
    if cardSelect == 1:
        spade3_draw1 = True
    if cardSelect == 2:
        spade4_draw1 = True
    if cardSelect == 3:
        spade5_draw1 = True
    if cardSelect == 4:
        spade6_draw1 = True
    if cardSelect == 5:
        spade7_draw1 = True
    if cardSelect == 6:
        spade8_draw1 = True
    if cardSelect == 7:
        spade9_draw1 = True
    if cardSelect == 8:
        spade10_draw1 = True
    if cardSelect == 9:
        spadeJack_draw1 = True
    if cardSelect == 10:
        spadeQueen_draw1 = True
    if cardSelect == 11:
        spadeKing_draw1 = True
    if cardSelect == 12:
        spadeAce_draw1 = True


    if cardSelect == 13:
        club2_draw1 = True
    if cardSelect == 14:
        club3_draw1 = True
    if cardSelect == 15:
        club4_draw1 = True
    if cardSelect == 16:
        club5_draw1 = True
    if cardSelect == 17:
        club6_draw1 = True
    if cardSelect == 18:
        club7_draw1 = True
    if cardSelect == 19:
        club8_draw1 = True
    if cardSelect == 20:
        club9_draw1 = True
    if cardSelect == 21:
        club10_draw1 = True
    if cardSelect == 22:
        clubJack_draw1 = True
    if cardSelect == 23:
        clubQueen_draw1 = True
    if cardSelect == 24:
        clubKing_draw1 = True
    if cardSelect == 25:
        clubAce_draw1 = True


    if cardSelect == 26:
        diamond2_draw1 = True
    if cardSelect == 27:
        diamond3_draw1 = True
    if cardSelect == 28:
        diamond4_draw1 = True
    if cardSelect == 29:
        diamond5_draw1 = True
    if cardSelect == 30:
        diamond6_draw1 = True
    if cardSelect == 31:
        diamond7_draw1 = True
    if cardSelect == 32:
        diamond8_draw1 = True
    if cardSelect == 33:
        diamond9_draw1 = True
    if cardSelect == 34:
        diamond10_draw1 = True
    if cardSelect == 35:
        diamondJack_draw1 = True
    if cardSelect == 36:
        diamondQueen_draw1 = True
    if cardSelect == 37:
        diamondKing_draw1 = True
    if cardSelect == 38:
        diamondAce_draw1 = True


    if cardSelect == 39:
        heart2_draw1 = True
    if cardSelect == 40:
        heart3_draw1 = True
    if cardSelect == 41:
        heart4_draw1 = True
    if cardSelect == 42:
        heart5_draw1 = True
    if cardSelect == 43:
        heart6_draw1 = True
    if cardSelect == 44:
        heart7_draw1 = True
    if cardSelect == 45:
        heart8_draw1 = True
    if cardSelect == 46:
        heart9_draw1 = True
    if cardSelect == 47:
        heart10_draw1 = True
    if cardSelect == 48:
        heartJack_draw1 = True
    if cardSelect == 49:
        heartQueen_draw1 = True
    if cardSelect == 50:
        heartKing_draw1 = True
    if cardSelect == 51:
        heartAce_draw1 = True


def generateCard1():
    global cardCount, cardSelect, club2_draw, club3_draw, club4_draw, club5_draw, club6_draw, club7_draw, club8_draw, club9_draw, club10_draw, clubJack_draw, clubQueen_draw, clubKing_draw, clubAce_draw, spade2_draw, spade3_draw, spade4_draw, spade5_draw, spade6_draw, spade7_draw, spade8_draw, spade9_draw, spade10_draw, spadeJack_draw, spadeQueen_draw, spadeKing_draw, spadeAce_draw, diamond2_draw, diamond3_draw, diamond4_draw, diamond5_draw, diamond6_draw, diamond7_draw, diamond8_draw, diamond9_draw, diamond10_draw, diamondJack_draw, diamondQueen_draw, diamondKing_draw, diamondAce_draw, heart2_draw, heart3_draw, heart4_draw, heart5_draw, heart6_draw, heart7_draw, heart8_draw, heart9_draw, heart10_draw, heartJack_draw, heartQueen_draw, heartKing_draw, heartAce_draw,spade2_draw1,spade3_draw1,spade4_draw1,spade5_draw1,spade6_draw1,spade7_draw1,spade8_draw1,spade9_draw1,spade10_draw1,spadeJack_draw1,spadeQueen_draw1,spadeKing_draw1,spadeAce_draw1,club2_draw1,club3_draw1,club4_draw1,club5_draw1,club6_draw1,club7_draw1,club8_draw1,club9_draw1,club10_draw1,clubJack_draw1,clubQueen_draw1,clubKing_draw1,clubAce_draw1,diamond2_draw1,diamond3_draw1,diamond4_draw1,diamond5_draw1,diamond6_draw1,diamond7_draw1,diamond8_draw1,diamond9_draw1,diamond10_draw1,diamondJack_draw1,diamondQueen_draw1,diamondKing_draw1,diamondAce_draw1,heart2_draw1,heart3_draw1,heart4_draw1,heart5_draw1,heart6_draw1,heart7_draw1,heart8_draw1,heart9_draw1,heart10_draw1,heartJack_draw1,heartQueen_draw1,heartKing_draw1,heartAce_draw1
    spade2_draw1 = False
    spade3_draw1 = False
    spade4_draw1 = False
    spade5_draw1 = False
    spade6_draw1 = False
    spade7_draw1 = False
    spade8_draw1 = False
    spade9_draw1 = False
    spade10_draw1 = False
    spadeJack_draw1 = False
    spadeQueen_draw1 = False
    spadeKing_draw1 = False
    spadeAce_draw1 = False

    club2_draw1 = False
    club3_draw1 = False
    club4_draw1 = False
    club5_draw1 = False
    club6_draw1 = False
    club7_draw1 = False
    club8_draw1 = False
    club9_draw1 = False
    club10_draw1 = False
    clubJack_draw1 = False
    clubQueen_draw1 = False
    clubKing_draw1 = False
    clubAce_draw1 = False

    diamond2_draw1 = False
    diamond3_draw1 = False
    diamond4_draw1 = False
    diamond5_draw1 = False
    diamond6_draw1 = False
    diamond7_draw1 = False
    diamond8_draw1 = False
    diamond9_draw1 = False
    diamond10_draw1 = False
    diamondJack_draw1 = False
    diamondQueen_draw1 = False
    diamondKing_draw1 = False
    diamondAce_draw1 = False

    heart2_draw1 = False
    heart3_draw1 = False
    heart4_draw1 = False
    heart5_draw1 = False
    heart6_draw1 = False
    heart7_draw1 = False
    heart8_draw1 = False
    heart9_draw1 = False
    heart10_draw1 = False
    heartJack_draw1 = False
    heartQueen_draw1 = False
    heartKing_draw1 = False
    heartAce_draw1 = False

    time.sleep(1)
    cardSelect = random.randint(0, 51)
    if cardSelect == 0:
        spade2_draw = True
    if cardSelect == 1:
        spade3_draw = True
    if cardSelect == 2:
        spade4_draw = True
    if cardSelect == 3:
        spade5_draw = True
    if cardSelect == 4:
        spade6_draw = True
    if cardSelect == 5:
        spade7_draw = True
    if cardSelect == 6:
        spade8_draw = True
    if cardSelect == 7:
        spade9_draw = True
    if cardSelect == 8:
        spade10_draw = True
    if cardSelect == 9:
        spadeJack_draw = True
    if cardSelect == 10:
        spadeQueen_draw = True
    if cardSelect == 11:
        spadeKing_draw = True
    if cardSelect == 12:
        spadeAce_draw = True

    if cardSelect == 13:
        club2_draw = True
    if cardSelect == 14:
        club3_draw = True
    if cardSelect == 15:
        club4_draw = True
    if cardSelect == 16:
        club5_draw = True
    if cardSelect == 17:
        club6_draw = True
    if cardSelect == 18:
        club7_draw = True
    if cardSelect == 19:
        club8_draw = True
    if cardSelect == 20:
        club9_draw = True
    if cardSelect == 21:
        club10_draw = True
    if cardSelect == 22:
        clubJack_draw = True
    if cardSelect == 23:
        clubQueen_draw = True
    if cardSelect == 24:
        clubKing_draw = True
    if cardSelect == 25:
        clubAce_draw = True

    if cardSelect == 26:
        diamond2_draw = True
    if cardSelect == 27:
        diamond3_draw = True
    if cardSelect == 28:
        diamond4_draw = True
    if cardSelect == 29:
        diamond5_draw = True
    if cardSelect == 30:
        diamond6_draw = True
    if cardSelect == 31:
        diamond7_draw = True
    if cardSelect == 32:
        diamond8_draw = True
    if cardSelect == 33:
        diamond9_draw = True
    if cardSelect == 34:
        diamond10_draw = True
    if cardSelect == 35:
        diamondJack_draw = True
    if cardSelect == 36:
        diamondQueen_draw = True
    if cardSelect == 37:
        diamondKing_draw = True
    if cardSelect == 38:
        diamondAce_draw = True

    if cardSelect == 39:
        heart2_draw = True
    if cardSelect == 40:
        heart3_draw = True
    if cardSelect == 41:
        heart4_draw = True
    if cardSelect == 42:
        heart5_draw = True
    if cardSelect == 43:
        heart6_draw = True
    if cardSelect == 44:
        heart7_draw = True
    if cardSelect == 45:
        heart8_draw = True
    if cardSelect == 46:
        heart9_draw = True
    if cardSelect == 47:
        heart10_draw = True
    if cardSelect == 48:
        heartJack_draw = True
    if cardSelect == 49:
        heartQueen_draw = True
    if cardSelect == 50:
        heartKing_draw = True
    if cardSelect == 51:
        heartAce_draw = True

    if cardSelect == 0:
        spade2_draw1 = True
    if cardSelect == 1:
        spade3_draw1 = True
    if cardSelect == 2:
        spade4_draw1 = True
    if cardSelect == 3:
        spade5_draw1 = True
    if cardSelect == 4:
        spade6_draw1 = True
    if cardSelect == 5:
        spade7_draw1 = True
    if cardSelect == 6:
        spade8_draw1 = True
    if cardSelect == 7:
        spade9_draw1 = True
    if cardSelect == 8:
        spade10_draw1 = True
    if cardSelect == 9:
        spadeJack_draw1 = True
    if cardSelect == 10:
        spadeQueen_draw1 = True
    if cardSelect == 11:
        spadeKing_draw1 = True
    if cardSelect == 12:
        spadeAce_draw1 = True


    if cardSelect == 13:
        club2_draw1 = True
    if cardSelect == 14:
        club3_draw1 = True
    if cardSelect == 15:
        club4_draw1 = True
    if cardSelect == 16:
        club5_draw1 = True
    if cardSelect == 17:
        club6_draw1 = True
    if cardSelect == 18:
        club7_draw1 = True
    if cardSelect == 19:
        club8_draw1 = True
    if cardSelect == 20:
        club9_draw1 = True
    if cardSelect == 21:
        club10_draw1 = True
    if cardSelect == 22:
        clubJack_draw1 = True
    if cardSelect == 23:
        clubQueen_draw1 = True
    if cardSelect == 24:
        clubKing_draw1 = True
    if cardSelect == 25:
        clubAce_draw1 = True


    if cardSelect == 26:
        diamond2_draw1 = True
    if cardSelect == 27:
        diamond3_draw1 = True
    if cardSelect == 28:
        diamond4_draw1 = True
    if cardSelect == 29:
        diamond5_draw1 = True
    if cardSelect == 30:
        diamond6_draw1 = True
    if cardSelect == 31:
        diamond7_draw1 = True
    if cardSelect == 32:
        diamond8_draw1 = True
    if cardSelect == 33:
        diamond9_draw1 = True
    if cardSelect == 34:
        diamond10_draw1 = True
    if cardSelect == 35:
        diamondJack_draw1 = True
    if cardSelect == 36:
        diamondQueen_draw1 = True
    if cardSelect == 37:
        diamondKing_draw1 = True
    if cardSelect == 38:
        diamondAce_draw1 = True

    if cardSelect == 39:
        heart2_draw1 = True
    if cardSelect == 40:
        heart3_draw1 = True
    if cardSelect == 41:
        heart4_draw1 = True
    if cardSelect == 42:
        heart5_draw1 = True
    if cardSelect == 43:
        heart6_draw1 = True
    if cardSelect == 44:
        heart7_draw1 = True
    if cardSelect == 45:
        heart8_draw1 = True
    if cardSelect == 46:
        heart9_draw1 = True
    if cardSelect == 47:
        heart10_draw1 = True
    if cardSelect == 48:
        heartJack_draw1 = True
    if cardSelect == 49:
        heartQueen_draw1 = True
    if cardSelect == 50:
        heartKing_draw1 = True
    if cardSelect == 51:
        heartAce_draw1 = True

def draw():
    global botcardCount, hit1,cardCount, roundStart,club2_draw,club3_draw,club4_draw,club5_draw,club6_draw,club7_draw,club8_draw,club9_draw,club10_draw,clubJack_draw,clubQueen_draw,clubKing_draw,clubAce_draw,spade2_draw,spade3_draw,spade4_draw,spade5_draw,spade6_draw,spade7_draw,spade8_draw,spade9_draw,spade10_draw,spadeJack_draw,spadeQueen_draw,spadeKing_draw,spadeAce_draw,diamond2_draw,diamond3_draw,diamond4_draw,diamond5_draw,diamond6_draw,diamond7_draw,diamond8_draw,diamond9_draw,diamond10_draw,diamondJack_draw,diamondQueen_draw,diamondKing_draw,diamondAce_draw,heart2_draw,heart3_draw,heart4_draw,heart5_draw,heart6_draw,heart7_draw,heart8_draw,heart9_draw,heart10_draw,heartJack_draw,heartQueen_draw,heartKing_draw,heartAce_draw
    screen.clear()
    screen.blit("background", (0,0))

    if gameOver1 == True:
        card1reset()
        screen.clear()
        screen.draw.text("Out of Money", color="white", center=(WIDTH / 2, HEIGHT/ 2 ), fontsize=200)

    if again_draw == True and gameOver1 == False:
        card1reset()
        screen.clear()
        again.draw()
        if playerWin2 == True:
            playerWin1.draw()
        if playerLoose == True:
            houseWin.draw()
        if moneyback1 == True:
            tie.draw()
    if gameOver1 == False:
        screen.draw.text(str(cardCount), color="white", center=(800, 800), fontsize=100)
        screen.draw.text(str(botcardCount), color="white", center=(800, 300), fontsize=100)
        screen.draw.text("Money:" + str(money), color="white", center=(800, 100), fontsize=100)
        screen.draw.text("Bet:" + str(betAmount), color="white", center=(150, 100), fontsize=100)
        if again_draw == False:
            hit.draw()
            stand.draw()
            if stopBet == False:
                bet.draw()
            if doubleDown1 == True:
                doubledown.draw()

    if spade2_draw1 == True:
        spade2.draw()
    if spade3_draw1 == True:
        spade3.draw()
    if spade4_draw1 == True:
        spade4.draw()
    if spade5_draw1 == True:
        spade5.draw()
    if spade6_draw1 == True:
        spade6.draw()
    if spade7_draw1 == True:
        spade7.draw()
    if spade8_draw1 == True:
        spade8.draw()
    if spade9_draw1 == True:
        spade9.draw()
    if spade10_draw1 == True:
        spade10.draw()
    if spadeJack_draw1 == True:
        spadeJack.draw()
    if spadeQueen_draw1 == True:
        spadeQueen.draw()
    if spadeKing_draw1 == True:
        spadeKing.draw()
    if spadeAce_draw1 == True:
        spadeAce.draw()


    if club2_draw1 == True:
        club2.draw()
    if club3_draw1 == True:
        club3.draw()
    if club4_draw1 == True:
        club4.draw()
    if club5_draw1 == True:
        club5.draw()
    if club6_draw1 == True:
        club6.draw()
    if club7_draw1 == True:
        club7.draw()
    if club8_draw1 == True:
        club8.draw()
    if club9_draw1 == True:
        club9.draw()
    if club10_draw1 == True:
        club10.draw()
    if clubJack_draw1 == True:
        clubJack.draw()
    if clubQueen_draw1 == True:
        clubQueen.draw()
    if clubKing_draw1 == True:
        clubKing.draw()
    if clubAce_draw1 == True:
        clubAce.draw()


    if diamond2_draw1 == True:
        diamond2.draw()
    if diamond3_draw1 == True:
        diamond3.draw()
    if diamond4_draw1 == True:
        diamond4.draw()
    if diamond5_draw1 == True:
        diamond5.draw()
    if diamond6_draw1 == True:
        diamond6.draw()
    if diamond7_draw1 == True:
        diamond7.draw()
    if diamond8_draw1 == True:
        diamond8.draw()
    if diamond9_draw1 == True:
        diamond9.draw()
    if diamond10_draw1 == True:
        diamond10.draw()
    if diamondJack_draw1 == True:
        diamondJack.draw()
    if diamondQueen_draw1 == True:
        diamondQueen.draw()
    if diamondKing_draw1 == True:
        diamondKing.draw()
    if diamondAce_draw1 == True:
        diamondAce.draw()


    if heart2_draw1 == True:
        heart2.draw()
    if heart3_draw1 == True:
        heart3.draw()
    if heart4_draw1 == True:
        heart4.draw()
    if heart5_draw1 == True:
        heart5.draw()
    if heart6_draw1 == True:
        heart6.draw()
    if heart7_draw1 == True:
        heart7.draw()
    if heart8_draw1 == True:
        heart8.draw()
    if heart9_draw1 == True:
        heart9.draw()
    if heart10_draw1 == True:
        heart10.draw()
    if heartJack_draw1 == True:
        heartJack.draw()
    if heartQueen_draw1 == True:
        heartQueen.draw()
    if heartKing_draw1 == True:
        heartKing.draw()
    if heartAce_draw1 == True:
        heartAce.draw()

def update():
    global stopBet,botcardCount,stand1,cardCount,hit1,club2_draw,club3_draw,club4_draw,club5_draw,club6_draw,club7_draw,club8_draw,club9_draw,club10_draw,clubJack_draw,clubQueen_draw,clubKing_draw,clubAce_draw,spade2_draw,spade3_draw,spade4_draw,spade5_draw,spade6_draw,spade7_draw,spade8_draw,spade9_draw,spade10_draw,spadeJack_draw,spadeQueen_draw,spadeKing_draw,spadeAce_draw,diamond2_draw,diamond3_draw,diamond4_draw,diamond5_draw,diamond6_draw,diamond7_draw,diamond8_draw,diamond9_draw,diamond10_draw,diamondJack_draw,diamondQueen_draw,diamondKing_draw,diamondAce_draw,heart2_draw,heart3_draw,heart4_draw,heart5_draw,heart6_draw,heart7_draw,heart8_draw,heart9_draw,heart10_draw,heartJack_draw,heartQueen_draw,heartKing_draw,heartAce_draw,spade2_draw1,spade3_draw1,spade4_draw1,spade5_draw1,spade6_draw1,spade7_draw1,spade8_draw1,spade9_draw1,spade10_draw1,spadeJack_draw1,spadeQueen_draw1,spadeKing_draw1,spadeAce_draw1,club2_draw1,club3_draw1,club4_draw1,club5_draw1,club6_draw1,club7_draw1,club8_draw1,club9_draw1,club10_draw1,clubJack_draw1,clubQueen_draw1,clubKing_draw1,clubAce_draw1,diamond2_draw1,diamond3_draw1,diamond4_draw1,diamond5_draw1,diamond6_draw1,diamond7_draw1,diamond8_draw1,diamond9_draw1,diamond10_draw1,diamondJack_draw1,diamondQueen_draw1,diamondKing_draw1,diamondAce_draw1,heart2_draw1,heart3_draw1,heart4_draw1,heart5_draw1,heart6_draw1,heart7_draw1,heart8_draw1,heart9_draw1,heart10_draw1,heartJack_draw1,heartQueen_draw1,heartKing_draw1,heartAce_draw1,doubleDown1
    tie.x = WIDTH / 2
    tie.y = HEIGHT / 2

    again.scale = .2
    again.x = WIDTH / 2
    again.y = 100

    hit.scale = 0.3
    hit.x = WIDTH/2
    hit.y = 650

    stand.scale = 0.3
    stand.x = WIDTH/2
    stand.y = 850

    doubledown.scale = 0.3
    doubledown.x = 800
    doubledown.y = 600

    bet.scale = 0.3
    bet.x = 800
    bet.y = 600

    playerWin1.x = WIDTH / 2
    playerWin1.y = HEIGHT / 2


    houseWin.x = WIDTH / 2
    houseWin.y = HEIGHT / 2

    spade2.x = 250
    spade2.y = HEIGHT / 2
    spade2.scale = 0.5

    spade3.x = 250
    spade3.y = HEIGHT / 2
    spade3.scale = 0.5

    spade4.x = 250
    spade4.y = HEIGHT / 2
    spade4.scale = 0.5

    spade5.x = 250
    spade5.y = HEIGHT / 2
    spade5.scale = 0.5

    spade6.x = 250
    spade6.y = HEIGHT / 2
    spade6.scale = 0.5

    spade7.x = 250
    spade7.y = HEIGHT / 2
    spade7.scale = 0.5

    spade8.x = 250
    spade8.y = HEIGHT / 2
    spade8.scale = 0.5

    spade9.x = 250
    spade9.y = HEIGHT / 2
    spade9.scale = 0.5

    spade10.x = 250
    spade10.y = HEIGHT / 2
    spade10.scale = 0.5

    spadeJack.x = 250
    spadeJack.y = HEIGHT / 2
    spadeJack.scale = 0.5

    spadeQueen.x = 250
    spadeQueen.y = HEIGHT / 2
    spadeQueen.scale = 0.5

    spadeKing.x = 250
    spadeKing.y = HEIGHT / 2
    spadeKing.scale = 0.5

    spadeAce.x = 250
    spadeAce.y = HEIGHT / 2
    spadeAce.scale = 0.5



    club2.x = 250
    club2.y = HEIGHT / 2
    club2.scale = 0.5

    club3.x = 250
    club3.y = HEIGHT / 2
    club3.scale = 0.5

    club4.x = 250
    club4.y = HEIGHT / 2
    club4.scale = 0.5

    club5.x = 250
    club5.y = HEIGHT / 2
    club5.scale = 0.5

    club6.x = 250
    club6.y = HEIGHT / 2
    club6.scale = 0.5

    club7.x = 250
    club7.y = HEIGHT / 2
    club7.scale = 0.5

    club8.x = 250
    club8.y = HEIGHT / 2
    club8.scale = 0.5

    club9.x = 250
    club9.y = HEIGHT / 2
    club9.scale = 0.5

    club10.x = 250
    club10.y = HEIGHT / 2
    club10.scale = 0.5

    clubJack.x = 250
    clubJack.y = HEIGHT / 2
    clubJack.scale = 0.5

    clubQueen.x = 250
    clubQueen.y = HEIGHT / 2
    clubQueen.scale = 0.5

    clubKing.x = 250
    clubKing.y = HEIGHT / 2
    clubKing.scale = 0.5

    clubAce.x = 250
    clubAce.y = HEIGHT / 2
    clubAce.scale = 0.5




    diamond2.x = 250
    diamond2.y = HEIGHT / 2
    diamond2.scale = 0.5

    diamond3.x = 250
    diamond3.y = HEIGHT / 2
    diamond3.scale = 0.5

    diamond4.x = 250
    diamond4.y = HEIGHT / 2
    diamond4.scale = 0.5

    diamond5.x = 250
    diamond5.y = HEIGHT / 2
    diamond5.scale = 0.5

    diamond6.x = 250
    diamond6.y = HEIGHT / 2
    diamond6.scale = 0.5

    diamond7.x = 250
    diamond7.y = HEIGHT / 2
    diamond7.scale = 0.5

    diamond8.x = 250
    diamond8.y = HEIGHT / 2
    diamond8.scale = 0.5

    diamond9.x = 250
    diamond9.y = HEIGHT / 2
    diamond9.scale = 0.5

    diamond10.x = 250
    diamond10.y = HEIGHT / 2
    diamond10.scale = 0.5

    diamondJack.x = 250
    diamondJack.y = HEIGHT / 2
    diamondJack.scale = 0.5

    diamondQueen.x = 250
    diamondQueen.y = HEIGHT / 2
    diamondQueen.scale = 0.5

    diamondKing.x = 250
    diamondKing.y = HEIGHT / 2
    diamondKing.scale = 0.5

    diamondAce.x = 250
    diamondAce.y = HEIGHT / 2
    diamondAce.scale = 0.5





    heart2.x = 250
    heart2.y = HEIGHT / 2
    heart2.scale = 0.5

    heart3.x = 250
    heart3.y = HEIGHT / 2
    heart3.scale = 0.5

    heart4.x = 250
    heart4.y = HEIGHT / 2
    heart4.scale = 0.5

    heart5.x = 250
    heart5.y = HEIGHT / 2
    heart5.scale = 0.5

    heart6.x = 250
    heart6.y = HEIGHT / 2
    heart6.scale = 0.5

    heart7.x = 250
    heart7.y = HEIGHT / 2
    heart7.scale = 0.5

    heart8.x = 250
    heart8.y = HEIGHT / 2
    heart8.scale = 0.5

    heart9.x = 250
    heart9.y = HEIGHT / 2
    heart9.scale = 0.5

    heart10.x = 250
    heart10.y = HEIGHT / 2
    heart10.scale = 0.5

    heartJack.x = 250
    heartJack.y = HEIGHT / 2
    heartJack.scale = 0.5

    heartQueen.x = 250
    heartQueen.y = HEIGHT / 2
    heartQueen.scale = 0.5

    heartKing.x = 250
    heartKing.y = HEIGHT / 2
    heartKing.scale = 0.5

    heartAce.x = 250
    heartAce.y = HEIGHT / 2
    heartAce.scale = 0.5



    if stand1 == True:
        if botcardCount < cardCount and botcardCount < 21:
            generateCard1()
            stopBet = True
            doubleDown1 = False

            if spade2_draw == True:
                botcardCount += 2
            if spade3_draw == True:
                botcardCount += 3
            if spade4_draw == True:
                botcardCount += 4
            if spade5_draw == True:
                botcardCount += 5
            if spade6_draw == True:
                botcardCount += 6
            if spade7_draw == True:
                botcardCount += 7
            if spade8_draw == True:
                botcardCount += 8
            if spade9_draw == True:
                botcardCount += 9
            if spade10_draw == True:
                botcardCount += 10
            if spadeJack_draw == True:
                botcardCount += 10
            if spadeQueen_draw == True:
                botcardCount += 10
            if spadeKing_draw == True:
                botcardCount += 10
            if spadeAce_draw == True:
                if botcardCount >= 12:
                    botcardCount += 1
                else:
                    botcardCount += 10

            if club2_draw == True:
                botcardCount += 2
            if club3_draw == True:
                botcardCount += 3
            if club4_draw == True:
                botcardCount += 4
            if club5_draw == True:
                botcardCount += 5
            if club6_draw == True:
                botcardCount += 6
            if club7_draw == True:
                botcardCount += 7
            if club8_draw == True:
                botcardCount += 8
            if club9_draw == True:
                botcardCount += 9
            if spade10_draw == True:
                botcardCount += 10
            if clubJack_draw == True:
                botcardCount += 10
            if clubQueen_draw == True:
                botcardCount += 10
            if clubKing_draw == True:
                botcardCount += 10
            if clubAce_draw == True:
                if botcardCount >= 12:
                    botcardCount += 1
                else:
                    botcardCount += 10

            if diamond2_draw == True:
                botcardCount += 2
            if diamond3_draw == True:
                botcardCount += 3
            if diamond4_draw == True:
                botcardCount += 4
            if diamond5_draw == True:
                botcardCount += 5
            if diamond6_draw == True:
                botcardCount += 6
            if diamond7_draw == True:
                botcardCount += 7
            if diamond8_draw == True:
                botcardCount += 8
            if diamond9_draw == True:
                botcardCount += 9
            if diamond10_draw == True:
                botcardCount += 10
            if diamondJack_draw == True:
                botcardCount += 10
            if diamondQueen_draw == True:
                botcardCount += 10
            if diamondKing_draw == True:
                botcardCount += 10
            if diamondAce_draw == True:
                if botcardCount >= 12:
                    botcardCount += 1
                else:
                    botcardCount += 10

            if heart2_draw == True:
                botcardCount += 2
            if heart3_draw == True:
                botcardCount += 3
            if heart4_draw == True:
                botcardCount += 4
            if heart5_draw == True:
                botcardCount += 5
            if heart6_draw == True:
                botcardCount += 6
            if heart7_draw == True:
                botcardCount += 7
            if heart8_draw == True:
                botcardCount += 8
            if heart9_draw == True:
                botcardCount += 9
            if heart10_draw == True:
                botcardCount += 10
            if heartJack_draw == True:
                botcardCount += 10
            if heartQueen_draw == True:
                botcardCount += 10
            if heartKing_draw == True:
                botcardCount += 10
            if heartAce_draw == True:
                if botcardCount >= 12:
                    botcardCount += 1
                else:
                    botcardCount += 10
            cardreset()
        else:
            bust()
            cardreset()


    if hit1 == True and stand1 == False:
        if cardCount < 21:
            stopBet = True
            doubleDown1 = True
            generateCard()
            if spade2_draw == True:
                cardCount += 2
            if spade3_draw == True:
                cardCount += 3
            if spade4_draw == True:
                cardCount += 4
            if spade5_draw == True:
                cardCount += 5
            if spade6_draw == True:
                cardCount += 6
            if spade7_draw == True:
                cardCount += 7
            if spade8_draw == True:
                cardCount += 8
            if spade9_draw == True:
                cardCount += 9
            if spade10_draw == True:
                cardCount += 10
            if spadeJack_draw == True:
                cardCount += 10
            if spadeQueen_draw == True:
                cardCount += 10
            if spadeKing_draw == True:
                cardCount += 10
            if spadeAce_draw == True:
                if cardCount >= 12:
                    cardCount += 1
                else:
                    cardCount += 10

            if club2_draw == True:
                cardCount += 2
            if club3_draw == True:
                cardCount += 3
            if club4_draw == True:
                cardCount += 4
            if club5_draw == True:
                cardCount += 5
            if club6_draw == True:
                cardCount += 6
            if club7_draw == True:
                cardCount += 7
            if club8_draw == True:
                cardCount += 8
            if club9_draw == True:
                cardCount += 9
            if spade10_draw == True:
                cardCount += 10
            if clubJack_draw == True:
                cardCount += 10
            if clubQueen_draw == True:
                cardCount += 10
            if clubKing_draw == True:
                cardCount += 10
            if clubAce_draw == True:
                if cardCount >= 12:
                    cardCount += 1
                else:
                    cardCount += 10

            if diamond2_draw == True:
                cardCount += 2
            if diamond3_draw == True:
                cardCount += 3
            if diamond4_draw == True:
                cardCount += 4
            if diamond5_draw == True:
                cardCount += 5
            if diamond6_draw == True:
                cardCount += 6
            if diamond7_draw == True:
                cardCount += 7
            if diamond8_draw == True:
                cardCount += 8
            if diamond9_draw == True:
                cardCount += 9
            if diamond10_draw == True:
                cardCount += 10
            if diamondJack_draw == True:
                cardCount += 10
            if diamondQueen_draw == True:
                cardCount += 10
            if diamondKing_draw == True:
                cardCount += 10
            if diamondAce_draw == True:
                if cardCount >= 12:
                    cardCount += 1
                else:
                    cardCount += 10

            if heart2_draw == True:
                cardCount += 2
            if heart3_draw == True:
                cardCount += 3
            if heart4_draw == True:
                cardCount += 4
            if heart5_draw == True:
                cardCount += 5
            if heart6_draw == True:
                cardCount += 6
            if heart7_draw == True:
                cardCount += 7
            if heart8_draw == True:
                cardCount += 8
            if heart9_draw == True:
                cardCount += 9
            if heart10_draw == True:
                cardCount += 10
            if heartJack_draw == True:
                cardCount += 10
            if heartQueen_draw == True:
                cardCount += 10
            if heartKing_draw == True:
                cardCount += 10
            if heartAce_draw == True:
                if cardCount >= 12:
                    cardCount += 1
                else:
                    cardCount += 10
            hit1 = False
            cardreset()
        else:
            bust()
            cardreset()
def cardreset():
    global club2_draw,club3_draw,club4_draw,club5_draw,club6_draw,club7_draw,club8_draw,club9_draw,club10_draw,clubJack_draw,clubQueen_draw,clubKing_draw,clubAce_draw,spade2_draw,spade3_draw,spade4_draw,spade5_draw,spade6_draw,spade7_draw,spade8_draw,spade9_draw,spade10_draw,spadeJack_draw,spadeQueen_draw,spadeKing_draw,spadeAce_draw,diamond2_draw,diamond3_draw,diamond4_draw,diamond5_draw,diamond6_draw,diamond7_draw,diamond8_draw,diamond9_draw,diamond10_draw,diamondJack_draw,diamondQueen_draw,diamondKing_draw,diamondAce_draw,heart2_draw,heart3_draw,heart4_draw,heart5_draw,heart6_draw,heart7_draw,heart8_draw,heart9_draw,heart10_draw,heartJack_draw,heartQueen_draw,heartKing_draw,heartAce_draw
    spade2_draw = False
    spade3_draw = False
    spade4_draw = False
    spade5_draw = False
    spade6_draw = False
    spade7_draw = False
    spade8_draw = False
    spade9_draw = False
    spade10_draw = False
    spadeJack_draw = False
    spadeQueen_draw = False
    spadeKing_draw = False
    spadeAce_draw = False

    club2_draw = False
    club3_draw = False
    club4_draw = False
    club5_draw = False
    club6_draw = False
    club7_draw = False
    club8_draw = False
    club9_draw = False
    club10_draw = False
    clubJack_draw = False
    clubQueen_draw = False
    clubKing_draw = False
    clubAce_draw = False

    diamond2_draw = False
    diamond3_draw = False
    diamond4_draw = False
    diamond5_draw = False
    diamond6_draw = False
    diamond7_draw = False
    diamond8_draw = False
    diamond9_draw = False
    diamond10_draw = False
    diamondJack_draw = False
    diamondQueen_draw = False
    diamondKing_draw = False
    diamondAce_draw = False

    heart2_draw = False
    heart3_draw = False
    heart4_draw = False
    heart5_draw = False
    heart6_draw = False
    heart7_draw = False
    heart8_draw = False
    heart9_draw = False
    heart10_draw = False
    heartJack_draw = False
    heartQueen_draw = False
    heartKing_draw = False
    heartAce_draw = False

def card1reset():
    global spade2_draw1,spade3_draw1,spade4_draw1,spade5_draw1,spade6_draw1,spade7_draw1,spade8_draw1,spade9_draw1,spade10_draw1,spadeJack_draw1,spadeQueen_draw1,spadeKing_draw1,spadeAce_draw1,club2_draw1,club3_draw1,club4_draw1,club5_draw1,club6_draw1,club7_draw1,club8_draw1,club9_draw1,club10_draw1,clubJack_draw1,clubQueen_draw1,clubKing_draw1,clubAce_draw1,diamond2_draw1,diamond3_draw1,diamond4_draw1,diamond5_draw1,diamond6_draw1,diamond7_draw1,diamond8_draw1,diamond9_draw1,diamond10_draw1,diamondJack_draw1,diamondQueen_draw1,diamondKing_draw1,diamondAce_draw1,heart2_draw1,heart3_draw1,heart4_draw1,heart5_draw1,heart6_draw1,heart7_draw1,heart8_draw1,heart9_draw1,heart10_draw1,heartJack_draw1,heartQueen_draw1,heartKing_draw1,heartAce_draw1
    spade2_draw1 = False
    spade3_draw1 = False
    spade4_draw1 = False
    spade5_draw1 = False
    spade6_draw1 = False
    spade7_draw1 = False
    spade8_draw1 = False
    spade9_draw1 = False
    spade10_draw1 = False
    spadeJack_draw1 = False
    spadeQueen_draw1 = False
    spadeKing_draw1 = False
    spadeAce_draw1 = False

    club2_draw1 = False
    club3_draw1 = False
    club4_draw1 = False
    club5_draw1 = False
    club6_draw1 = False
    club7_draw1 = False
    club8_draw1 = False
    club9_draw1 = False
    club10_draw1 = False
    clubJack_draw1 = False
    clubQueen_draw1 = False
    clubKing_draw1 = False
    clubAce_draw1 = False

    diamond2_draw1 = False
    diamond3_draw1 = False
    diamond4_draw1 = False
    diamond5_draw1 = False
    diamond6_draw1 = False
    diamond7_draw1 = False
    diamond8_draw1 = False
    diamond9_draw1 = False
    diamond10_draw1 = False
    diamondJack_draw1 = False
    diamondQueen_draw1 = False
    diamondKing_draw1 = False
    diamondAce_draw1 = False

    heart2_draw1 = False
    heart3_draw1 = False
    heart4_draw1 = False
    heart5_draw1 = False
    heart6_draw1 = False
    heart7_draw1 = False
    heart8_draw1 = False
    heart9_draw1 = False
    heart10_draw1 = False
    heartJack_draw1 = False
    heartQueen_draw1 = False
    heartKing_draw1 = False
    heartAce_draw1 = False

def resetAll():
    global hit1, stand1,botcardCount, cardCount, betAmount, again_draw,stopBet,moneyback1,doubleDown1,doubleDownamount,playerLoose,playerWin1,playerWin2
    cardreset()
    card1reset()
    hit1 = False
    stand1 = False
    botcardCount = 0
    cardCount = 0
    again_draw = False
    betAmount = 0
    stopBet = False
    moneyback1 = False
    doubleDown1 = False
    doubleDownamount = 0
    playerLoose = False
    playerWin2 = False

def on_mouse_down(pos):
    global hit1,hit,stand,stand1,bet2
    if hit.collidepoint(pos):
        hit1 = True
    if stand.collidepoint(pos):
        stand1 = True
    if bet.collidepoint(pos):
        bet1()
        bet2 = True
    if again.collidepoint(pos):
        resetAll()
    if doubledown.collidepoint(pos):
        if doubleDown1 == True:
            doubleDown()

    else:
        print()

def bust():
    if cardCount < 21 and botcardCount > cardCount and botcardCount <= 21:
        playerLose()
    if cardCount <= 21 and botcardCount > 21:
        playerWin()
    if cardCount > 21:
        playerLose()
    if cardCount == botcardCount:
        moneyBack()
    if money <= 0:
        gameOver()
    roundEnd()
def moneyBack():
    global money, betAmount,moneyback1
    money = money + betAmount
    moneyback1 = True
    betAmount = 0
def bet1():
    global money, betAmount, stopBet
    if stopBet == False and money > 9:
        money -= 10
        betAmount += 10
def playerWin():
    global betAmount, money,playerWin2
    betAmount = betAmount * 2
    money = money + betAmount
    betAmount = 0
    playerWin2 = True
def playerLose():
    global betAmount,playerLoose
    playerLoose = True
    betAmount = 0


def roundEnd():
    global gameStart, again_draw
    again_draw = True

def doubleDown():
    global betAmount, doubleDown1,doubleDownamount,money,stopBet,stand1,doubleGenerate1
    if doubleDown1 == True:

        if money >= doubleDownamount:
            doubleGenerate1 = True
            doubleGenerate()
            betAmount += betAmount
            money -= doubleDownamount
            doubleDown1 = False
            stopBet = True

            stand1 = True

def doubleGenerate():
    global hit1,stopBet,doubleDown1,cardCount,doubleGenerate1
    if doubleGenerate1 == True:
        generateCard()
        if spade2_draw == True:
            cardCount += 2
        if spade3_draw == True:
            cardCount += 3
        if spade4_draw == True:
            cardCount += 4
        if spade5_draw == True:
            cardCount += 5
        if spade6_draw == True:
            cardCount += 6
        if spade7_draw == True:
            cardCount += 7
        if spade8_draw == True:
            cardCount += 8
        if spade9_draw == True:
            cardCount += 9
        if spade10_draw == True:
            cardCount += 10
        if spadeJack_draw == True:
            cardCount += 10
        if spadeQueen_draw == True:
            cardCount += 10
        if spadeKing_draw == True:
            cardCount += 10
        if spadeAce_draw == True:
            if cardCount >= 12:
                cardCount += 1
            else:
                cardCount += 10

        if club2_draw == True:
            cardCount += 2
        if club3_draw == True:
            cardCount += 3
        if club4_draw == True:
            cardCount += 4
        if club5_draw == True:
            cardCount += 5
        if club6_draw == True:
            cardCount += 6
        if club7_draw == True:
            cardCount += 7
        if club8_draw == True:
            cardCount += 8
        if club9_draw == True:
            cardCount += 9
        if spade10_draw == True:
            cardCount += 10
        if clubJack_draw == True:
            cardCount += 10
        if clubQueen_draw == True:
            cardCount += 10
        if clubKing_draw == True:
            cardCount += 10
        if clubAce_draw == True:
            if cardCount >= 12:
                cardCount += 1
            else:
                cardCount += 10

        if diamond2_draw == True:
            cardCount += 2
        if diamond3_draw == True:
            cardCount += 3
        if diamond4_draw == True:
            cardCount += 4
        if diamond5_draw == True:
            cardCount += 5
        if diamond6_draw == True:
            cardCount += 6
        if diamond7_draw == True:
            cardCount += 7
        if diamond8_draw == True:
            cardCount += 8
        if diamond9_draw == True:
            cardCount += 9
        if diamond10_draw == True:
            cardCount += 10
        if diamondJack_draw == True:
            cardCount += 10
        if diamondQueen_draw == True:
            cardCount += 10
        if diamondKing_draw == True:
            cardCount += 10
        if diamondAce_draw == True:
            if cardCount >= 12:
                cardCount += 1
            else:
                cardCount += 10

        if heart2_draw == True:
            cardCount += 2
        if heart3_draw == True:
            cardCount += 3
        if heart4_draw == True:
            cardCount += 4
        if heart5_draw == True:
            cardCount += 5
        if heart6_draw == True:
            cardCount += 6
        if heart7_draw == True:
            cardCount += 7
        if heart8_draw == True:
            cardCount += 8
        if heart9_draw == True:
            cardCount += 9
        if heart10_draw == True:
            cardCount += 10
        if heartJack_draw == True:
            cardCount += 10
        if heartQueen_draw == True:
            cardCount += 10
        if heartKing_draw == True:
            cardCount += 10
        if heartAce_draw == True:
            if cardCount >= 12:
                cardCount += 1
            else:
                cardCount += 10
        doubleGenerate1 = False


def cardreset():
    global club2_draw, club3_draw, club4_draw, club5_draw, club6_draw, club7_draw, club8_draw, club9_draw, club10_draw, clubJack_draw, clubQueen_draw, clubKing_draw, clubAce_draw, spade2_draw, spade3_draw, spade4_draw, spade5_draw, spade6_draw, spade7_draw, spade8_draw, spade9_draw, spade10_draw, spadeJack_draw, spadeQueen_draw, spadeKing_draw, spadeAce_draw, diamond2_draw, diamond3_draw, diamond4_draw, diamond5_draw, diamond6_draw, diamond7_draw, diamond8_draw, diamond9_draw, diamond10_draw, diamondJack_draw, diamondQueen_draw, diamondKing_draw, diamondAce_draw, heart2_draw, heart3_draw, heart4_draw, heart5_draw, heart6_draw, heart7_draw, heart8_draw, heart9_draw, heart10_draw, heartJack_draw, heartQueen_draw, heartKing_draw, heartAce_draw
    spade2_draw = False
    spade3_draw = False
    spade4_draw = False
    spade5_draw = False
    spade6_draw = False
    spade7_draw = False
    spade8_draw = False
    spade9_draw = False
    spade10_draw = False
    spadeJack_draw = False
    spadeQueen_draw = False
    spadeKing_draw = False
    spadeAce_draw = False

    club2_draw = False
    club3_draw = False
    club4_draw = False
    club5_draw = False
    club6_draw = False
    club7_draw = False
    club8_draw = False
    club9_draw = False
    club10_draw = False
    clubJack_draw = False
    clubQueen_draw = False
    clubKing_draw = False
    clubAce_draw = False

    diamond2_draw = False
    diamond3_draw = False
    diamond4_draw = False
    diamond5_draw = False
    diamond6_draw = False
    diamond7_draw = False
    diamond8_draw = False
    diamond9_draw = False
    diamond10_draw = False
    diamondJack_draw = False
    diamondQueen_draw = False
    diamondKing_draw = False
    diamondAce_draw = False

    heart2_draw = False
    heart3_draw = False
    heart4_draw = False
    heart5_draw = False
    heart6_draw = False
    heart7_draw = False
    heart8_draw = False
    heart9_draw = False
    heart10_draw = False
    heartJack_draw = False
    heartQueen_draw = False
    heartKing_draw = False
    heartAce_draw = False


def card1reset():
    global spade2_draw1, spade3_draw1, spade4_draw1, spade5_draw1, spade6_draw1, spade7_draw1, spade8_draw1, spade9_draw1, spade10_draw1, spadeJack_draw1, spadeQueen_draw1, spadeKing_draw1, spadeAce_draw1, club2_draw1, club3_draw1, club4_draw1, club5_draw1, club6_draw1, club7_draw1, club8_draw1, club9_draw1, club10_draw1, clubJack_draw1, clubQueen_draw1, clubKing_draw1, clubAce_draw1, diamond2_draw1, diamond3_draw1, diamond4_draw1, diamond5_draw1, diamond6_draw1, diamond7_draw1, diamond8_draw1, diamond9_draw1, diamond10_draw1, diamondJack_draw1, diamondQueen_draw1, diamondKing_draw1, diamondAce_draw1, heart2_draw1, heart3_draw1, heart4_draw1, heart5_draw1, heart6_draw1, heart7_draw1, heart8_draw1, heart9_draw1, heart10_draw1, heartJack_draw1, heartQueen_draw1, heartKing_draw1, heartAce_draw1
    spade2_draw1 = False
    spade3_draw1 = False
    spade4_draw1 = False
    spade5_draw1 = False
    spade6_draw1 = False
    spade7_draw1 = False
    spade8_draw1 = False
    spade9_draw1 = False
    spade10_draw1 = False
    spadeJack_draw1 = False
    spadeQueen_draw1 = False
    spadeKing_draw1 = False
    spadeAce_draw1 = False

    club2_draw1 = False
    club3_draw1 = False
    club4_draw1 = False
    club5_draw1 = False
    club6_draw1 = False
    club7_draw1 = False
    club8_draw1 = False
    club9_draw1 = False
    club10_draw1 = False
    clubJack_draw1 = False
    clubQueen_draw1 = False
    clubKing_draw1 = False
    clubAce_draw1 = False

    diamond2_draw1 = False
    diamond3_draw1 = False
    diamond4_draw1 = False
    diamond5_draw1 = False
    diamond6_draw1 = False
    diamond7_draw1 = False
    diamond8_draw1 = False
    diamond9_draw1 = False
    diamond10_draw1 = False
    diamondJack_draw1 = False
    diamondQueen_draw1 = False
    diamondKing_draw1 = False
    diamondAce_draw1 = False

    heart2_draw1 = False
    heart3_draw1 = False
    heart4_draw1 = False
    heart5_draw1 = False
    heart6_draw1 = False
    heart7_draw1 = False
    heart8_draw1 = False
    heart9_draw1 = False
    heart10_draw1 = False
    heartJack_draw1 = False
    heartQueen_draw1 = False
    heartKing_draw1 = False
    heartAce_draw1 = False


def resetAll():
    global hit1, stand1, botcardCount, cardCount, betAmount, again_draw, stopBet, moneyback1, doubleDown1, doubleDownamount, playerLoose, playerWin1, playerWin2
    cardreset()
    card1reset()
    hit1 = False
    stand1 = False
    botcardCount = 0
    cardCount = 0
    again_draw = False
    betAmount = 0
    stopBet = False
    moneyback1 = False
    doubleDown1 = False
    doubleDownamount = 0
    playerLoose = False
    playerWin2 = False


def on_mouse_down(pos):
    global hit1, hit, stand, stand1, bet2
    if hit.collidepoint(pos):
        hit1 = True
    if stand.collidepoint(pos):
        stand1 = True
    if bet.collidepoint(pos):
        bet1()
        bet2 = True
    if again.collidepoint(pos):
        resetAll()
    if doubledown.collidepoint(pos):
        if doubleDown1 == True:
            doubleDown()

    else:
        print()


def gameOver():
    global gameOver1
    gameOver1 = True


pgzrun.go()