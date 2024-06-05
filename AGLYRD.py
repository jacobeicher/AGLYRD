#AGLYRD
import pygame, sys, time, random
from pygame.locals import *

pygame.init()

#player spawn
x = 200
y = 200
FPS = 100 # frames per second setting
fpsClock = pygame.time.Clock()
losstime = 0
#Background music 
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(0,0.0)

DS = pygame.display.set_mode((400, 400))
DS = pygame.display.set_mode((400, 400))
pygame.display.set_caption('AGLYRD')

BLUE  = (  0,   255, 255)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
YELLOW = (  255, 255,  0)
BLACK = (0, 0, 0)
Color = (0, 91, 222)
loopruns = 0
def Delete(loopruns, FPS):
    if loopruns >= FPS*.5:
        return random.randint(1, 100)
def ChangeLoop(loopruns, FPS):
    if loopruns >= FPS*.5:
        return 0
    else:
        return loopruns
def groundbreak():
    sound = pygame.mixer.Sound('GlassBreaking.wav')
    #sound.play()
score = 0
safe1 = 0
safe2 = 0
safe3 = 0
safe4 = 0
safe5 = 0
safe6 = 0
safe7 = 0
safe8 = 0
safe9 = 0
safe10 = 0
safe11 = 0
safe12 = 0
safe13 = 0
safe14 = 0
safe15 = 0
safe16 = 0
safe17 = 0
safe18 = 0
safe19 = 0
safe20 = 0
safe21 = 0
safe22 = 0
safe23 = 0
safe24 = 0
safe25 = 0
safe26 = 0
safe27 = 0
safe28 = 0
safe29 = 0
safe30 = 0
safe31 = 0
safe32 = 0
safe33 = 0
safe34 = 0
safe35 = 0
safe36 = 0
safe37 = 0
safe38 = 0
safe39 = 0
safe40 = 0
safe41 = 0
safe42 = 0
safe43 = 0
safe44 = 0
safe45 = 0
safe46 = 0
safe47 = 0
safe48 = 0
safe49 = 0
safe50 = 0
safe51 = 0
safe52 = 0
safe53 = 0
safe54 = 0
safe55 = 0
safe56 = 0
safe57 = 0
safe58 = 0
safe59 = 0
safe60 = 0
safe61 = 0
safe62 = 0
safe63 = 0
safe64 = 0
safe65 = 0
safe66 = 0
safe67 = 0
safe68 = 0
safe69 = 0
safe70 = 0
safe71 = 0
safe72 = 0
safe73 = 0
safe74 = 0
safe75 = 0
safe76 = 0
safe77 = 0
safe78 = 0
safe79 = 0
safe80 = 0
safe81 = 0
safe82 = 0
safe83 = 0
safe84 = 0
safe85 = 0
safe86 = 0
safe87 = 0
safe88 = 0
safe89 = 0
safe90 = 0
safe91 = 0
safe92 = 0
safe93 = 0
safe94 = 0
safe95 = 0
safe96 = 0
safe97 = 0
safe98 = 0
safe99 = 0
safe100 = 0
 #separater  
grid1 = 0
grid2 = 0
grid3 = 0
grid4 = 0
grid5 = 0
grid6 = 0
grid7 = 0
grid8 = 0
grid9 = 0
grid10 = 0
grid11 = 0
grid12 = 0
grid13 = 0
grid14 = 0
grid15 = 0
grid16 = 0
grid17 = 0
grid18 = 0
grid19 = 0
grid20 = 0
grid21 = 0
grid22 = 0
grid23 = 0
grid24 = 0
grid25 = 0
grid26 = 0
grid27 = 0
grid28 = 0
grid29 = 0
grid30 = 0
grid31 = 0
grid32 = 0
grid33 = 0
grid34 = 0
grid35 = 0
grid36 = 0
grid37 = 0
grid38 = 0
grid39 = 0
grid40 = 0
grid41 = 0
grid42 = 0
grid43 = 0
grid44 = 0
grid45 = 0
grid46 = 0
grid47 = 0
grid48 = 0
grid49 = 0
grid50 = 0
grid51 = 0
grid52 = 0
grid53 = 0
grid54 = 0
grid55 = 0
grid56 = 0
grid57 = 0
grid58 = 0
grid59 = 0
grid60 = 0
grid61 = 0
grid62 = 0
grid63 = 0
grid64 = 0
grid65 = 0
grid66 = 0
grid67 = 0
grid68 = 0
grid69 = 0
grid70 = 0
grid71 = 0
grid72 = 0
grid73 = 0
grid74 = 0
grid75 = 0
grid76 = 0
grid77 = 0
grid78 = 0
grid79 = 0
grid80 = 0
grid81 = 0
grid82 = 0
grid83 = 0
grid84 = 0
grid85 = 0
grid86 = 0
grid87 = 0
grid88 = 0
grid89 = 0
grid90 = 0
grid91 = 0
grid92 = 0
grid93 = 0
grid94 = 0
grid95 = 0
grid96 = 0
grid97 = 0
grid98 = 0
grid99 = 0
grid100 = 0




while True:
    if pygame.key.get_pressed()[K_0] !=0:
        v = 1
        while v == 1:
            if pygame.key.get_pressed()[K_9] !=0:
                v = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            fpsClock.tick(FPS)
    DS.fill(Color)
    if pygame.key.get_pressed()[K_s] !=0 :
        y = y + 2
        if y > 390:
            y = 390
    if pygame.key.get_pressed()[K_w] !=0:
        y = y - 2
        if y < 1:
            y = 1
    if pygame.key.get_pressed()[K_d] !=0:
        x = x + 2
        if x > 390:
            x = 390
    if pygame.key.get_pressed()[K_a] !=0:
        x = x - 2
        if x < 1:
            x = 1

    if pygame.key.get_pressed()[K_DOWN] !=0:
        y = y + 2
        if y > 390:
            y = 390
    if pygame.key.get_pressed()[K_UP] !=0:
        y = y - 2
        if y < 1:
            y = 1
    if pygame.key.get_pressed()[K_RIGHT] !=0:
        x = x + 2
        if x > 390:
            x = 390
    if pygame.key.get_pressed()[K_LEFT] !=0:
        x = x - 2
        if x < 1:
            x = 1


    f = 1
    while f == 1:
        c = 0
        SqrToDel = Delete(loopruns, FPS)
        if SqrToDel == 1 and safe1<= 2: 
            grid1= 1
            grid1_1 = 0
            safe1+= 1
            c = 1
        if SqrToDel == 2 and safe2<= 2: 
            grid2= 1
            grid2_1 = 0
            safe2+= 1
            c = 1
        if SqrToDel == 3 and safe3<= 2: 
            grid3= 1
            grid3_1 = 0
            safe3+= 1
            c = 1
        if SqrToDel == 4 and safe4<= 2: 
            grid4= 1
            grid4_1 = 0
            safe4+= 1
            c = 1
        if SqrToDel == 5 and safe5<= 2: 
            grid5= 1
            grid5_1 = 0
            safe5+= 1
            c = 1
        if SqrToDel == 6 and safe6<= 2: 
            grid6= 1
            grid6_1 = 0
            safe6+= 1
            c = 1
        if SqrToDel == 7 and safe7<= 2: 
            grid7= 1
            grid7_1 = 0
            safe7+= 1
            c = 1
        if SqrToDel == 8 and safe8<= 2: 
            grid8= 1
            grid8_1 = 0
            safe8+= 1
            c = 1
        if SqrToDel == 9 and safe9<= 2: 
            grid9= 1
            grid9_1 = 0
            safe9+= 1
            c = 1
        if SqrToDel == 10 and safe10<= 2: 
            grid10= 1
            grid10_1 = 0
            safe10+= 1
            c = 1
        if SqrToDel == 11 and safe11<= 2: 
            grid11= 1
            grid11_1 = 0
            safe11+= 1
            c = 1
        if SqrToDel == 12 and safe12<= 2: 
            grid12= 1
            grid12_1 = 0
            safe12+= 1
            c = 1
        if SqrToDel == 13 and safe13<= 2: 
            grid13= 1
            grid13_1 = 0
            safe13+= 1
            c = 1
        if SqrToDel == 14 and safe14<= 2: 
            grid14= 1
            grid14_1 = 0
            safe14+= 1
            c = 1
        if SqrToDel == 15 and safe15<= 2: 
            grid15= 1
            grid15_1 = 0
            safe15+= 1
            c = 1
        if SqrToDel == 16 and safe16<= 2: 
            grid16= 1
            grid16_1 = 0
            safe16+= 1
            c = 1
        if SqrToDel == 17 and safe17<= 2: 
            grid17= 1
            grid17_1 = 0
            safe17+= 1
            c = 1
        if SqrToDel == 18 and safe18<= 2: 
            grid18= 1
            grid18_1 = 0
            safe18+= 1
            c = 1
        if SqrToDel == 19 and safe19<= 2: 
            grid19= 1
            grid19_1 = 0
            safe19+= 1
            c = 1
        if SqrToDel == 20 and safe20<= 2: 
            grid20= 1
            grid20_1 = 0
            safe20+= 1
            c = 1
        if SqrToDel == 21 and safe21<= 2: 
            grid21= 1
            grid21_1 = 0
            safe21+= 1
            c = 1
        if SqrToDel == 22 and safe22<= 2: 
            grid22= 1
            grid22_1 = 0
            safe22+= 1
            c = 1
        if SqrToDel == 23 and safe23<= 2: 
            grid23= 1
            grid23_1 = 0
            safe23+= 1
            c = 1
        if SqrToDel == 24 and safe24<= 2: 
            grid24= 1
            grid24_1 = 0
            safe24+= 1
            c = 1
        if SqrToDel == 25 and safe25<= 2: 
            grid25= 1
            grid25_1 = 0
            safe25+= 1
            c = 1
        if SqrToDel == 26 and safe26<= 2: 
            grid26= 1
            grid26_1 = 0
            safe26+= 1
            c = 1
        if SqrToDel == 27 and safe27<= 2: 
            grid27= 1
            grid27_1 = 0
            safe27+= 1
            c = 1
        if SqrToDel == 28 and safe28<= 2: 
            grid28= 1
            grid28_1 = 0
            safe28+= 1
            c = 1
        if SqrToDel == 29 and safe29<= 2: 
            grid29= 1
            grid29_1 = 0
            safe29+= 1
            c = 1
        if SqrToDel == 30 and safe30<= 2: 
            grid30= 1
            grid30_1 = 0
            safe30+= 1
            c = 1
        if SqrToDel == 31 and safe31<= 2: 
            grid31= 1
            grid31_1 = 0
            safe31+= 1
            c = 1
        if SqrToDel == 32 and safe32<= 2: 
            grid32= 1
            grid32_1 = 0
            safe32+= 1
            c = 1
        if SqrToDel == 33 and safe33<= 2: 
            grid33= 1
            grid33_1 = 0
            safe33+= 1
            c = 1
        if SqrToDel == 34 and safe34<= 2: 
            grid34= 1
            grid34_1 = 0
            safe34+= 1
            c = 1
        if SqrToDel == 35 and safe35<= 2: 
            grid35= 1
            grid35_1 = 0
            safe35+= 1
            c = 1
        if SqrToDel == 36 and safe36<= 2: 
            grid36= 1
            grid36_1 = 0
            safe36+= 1
            c = 1
        if SqrToDel == 37 and safe37<= 2: 
            grid37= 1
            grid37_1 = 0
            safe37+= 1
            c = 1
        if SqrToDel == 38 and safe38<= 2: 
            grid38= 1
            grid38_1 = 0
            safe38+= 1
            c = 1
        if SqrToDel == 39 and safe39<= 2: 
            grid39= 1
            grid39_1 = 0
            safe39+= 1
            c = 1
        if SqrToDel == 40 and safe40<= 2: 
            grid40= 1
            grid40_1 = 0
            safe40+= 1
            c = 1
        if SqrToDel == 41 and safe41<= 2: 
            grid41= 1
            grid41_1 = 0
            safe41+= 1
            c = 1
        if SqrToDel == 42 and safe42<= 2: 
            grid42= 1
            grid42_1 = 0
            safe42+= 1
            c = 1
        if SqrToDel == 43 and safe43<= 2: 
            grid43= 1
            grid43_1 = 0
            safe43+= 1
            c = 1
        if SqrToDel == 44 and safe44<= 2: 
            grid44= 1
            grid44_1 = 0
            safe44+= 1
            c = 1
        if SqrToDel == 45 and safe45<= 2: 
            grid45= 1
            grid45_1 = 0
            safe45+= 1
            c = 1
        if SqrToDel == 46 and safe46<= 2: 
            grid46= 1
            grid46_1 = 0
            safe46+= 1
            c = 1
        if SqrToDel == 47 and safe47<= 2: 
            grid47= 1
            grid47_1 = 0
            safe47+= 1
            c = 1
        if SqrToDel == 48 and safe48<= 2: 
            grid48= 1
            grid48_1 = 0
            safe48+= 1
            c = 1
        if SqrToDel == 49 and safe49<= 2: 
            grid49= 1
            grid49_1 = 0
            safe49+= 1
            c = 1
        if SqrToDel == 50 and safe50<= 2: 
            grid50= 1
            grid50_1 = 0
            safe50+= 1
            c = 1
        if SqrToDel == 51 and safe51<= 2: 
            grid51= 1
            grid51_1 = 0
            safe51+= 1
            c = 1
        if SqrToDel == 52 and safe52<= 2: 
            grid52= 1
            grid52_1 = 0
            safe52+= 1
            c = 1
        if SqrToDel == 53 and safe53<= 2: 
            grid53= 1
            grid53_1 = 0
            safe53+= 1
            c = 1
        if SqrToDel == 54 and safe54<= 2: 
            grid54= 1
            grid54_1 = 0
            safe54+= 1
            c = 1
        if SqrToDel == 55 and safe55<= 2: 
            grid55= 1
            grid55_1 = 0
            safe55+= 1
            c = 1
        if SqrToDel == 56 and safe56<= 2: 
            grid56= 1
            grid56_1 = 0
            safe56+= 1
            c = 1
        if SqrToDel == 57 and safe57<= 2: 
            grid57= 1
            grid57_1 = 0
            safe57+= 1
            c = 1
        if SqrToDel == 58 and safe58<= 2: 
            grid58= 1
            grid58_1 = 0
            safe58+= 1
            c = 1
        if SqrToDel == 59 and safe59<= 2: 
            grid59= 1
            grid59_1 = 0
            safe59+= 1
            c = 1
        if SqrToDel == 60 and safe60<= 2: 
            grid60= 1
            grid60_1 = 0
            safe60+= 1
            c = 1
        if SqrToDel == 61 and safe61<= 2: 
            grid61= 1
            grid61_1 = 0
            safe61+= 1
            c = 1
        if SqrToDel == 62 and safe62<= 2: 
            grid62= 1
            grid62_1 = 0
            safe62+= 1
            c = 1
        if SqrToDel == 63 and safe63<= 2: 
            grid63= 1
            grid63_1 = 0
            safe63+= 1
            c = 1
        if SqrToDel == 64 and safe64<= 2: 
            grid64= 1
            grid64_1 = 0
            safe64+= 1
            c = 1
        if SqrToDel == 65 and safe65<= 2: 
            grid65= 1
            grid65_1 = 0
            safe65+= 1
            c = 1
        if SqrToDel == 66 and safe66<= 2: 
            grid66= 1
            grid66_1 = 0
            safe66+= 1
            c = 1
        if SqrToDel == 67 and safe67<= 2: 
            grid67= 1
            grid67_1 = 0
            safe67+= 1
            c = 1
        if SqrToDel == 68 and safe68<= 2: 
            grid68= 1
            grid68_1 = 0
            safe68+= 1
            c = 1
        if SqrToDel == 69 and safe69<= 2: 
            grid69= 1
            grid69_1 = 0
            safe69+= 1
            c = 1
        if SqrToDel == 70 and safe70<= 2: 
            grid70= 1
            grid70_1 = 0
            safe70+= 1
            c = 1
        if SqrToDel == 71 and safe71<= 2: 
            grid71= 1
            grid71_1 = 0
            safe71+= 1
            c = 1
        if SqrToDel == 72 and safe72<= 2: 
            grid72= 1
            grid72_1 = 0
            safe72+= 1
            c = 1
        if SqrToDel == 73 and safe73<= 2: 
            grid73= 1
            grid73_1 = 0
            safe73+= 1
            c = 1
        if SqrToDel == 74 and safe74<= 2: 
            grid74= 1
            grid74_1 = 0
            safe74+= 1
            c = 1
        if SqrToDel == 75 and safe75<= 2: 
            grid75= 1
            grid75_1 = 0
            safe75+= 1
            c = 1
        if SqrToDel == 76 and safe76<= 2: 
            grid76= 1
            grid76_1 = 0
            safe76+= 1
            c = 1
        if SqrToDel == 77 and safe77<= 2: 
            grid77= 1
            grid77_1 = 0
            safe77+= 1
            c = 1
        if SqrToDel == 78 and safe78<= 2: 
            grid78= 1
            grid78_1 = 0
            safe78+= 1
            c = 1
        if SqrToDel == 79 and safe79<= 2: 
            grid79= 1
            grid79_1 = 0
            safe79+= 1
            c = 1
        if SqrToDel == 80 and safe80<= 2: 
            grid80= 1
            grid80_1 = 0
            safe80+= 1
            c = 1
        if SqrToDel == 81 and safe81<= 2: 
            grid81= 1
            grid81_1 = 0
            safe81+= 1
            c = 1
        if SqrToDel == 82 and safe82<= 2: 
            grid82= 1
            grid82_1 = 0
            safe82+= 1
            c = 1
        if SqrToDel == 83 and safe83<= 2: 
            grid83= 1
            grid83_1 = 0
            safe83+= 1
            c = 1
        if SqrToDel == 84 and safe84<= 2: 
            grid84= 1
            grid84_1 = 0
            safe84+= 1
            c = 1
        if SqrToDel == 85 and safe85<= 2: 
            grid85= 1
            grid85_1 = 0
            safe85+= 1
            c = 1
        if SqrToDel == 86 and safe86<= 2: 
            grid86= 1
            grid86_1 = 0
            safe86+= 1
            c = 1
        if SqrToDel == 87 and safe87<= 2: 
            grid87= 1
            grid87_1 = 0
            safe87+= 1
            c = 1
        if SqrToDel == 88 and safe88<= 2: 
            grid88= 1
            grid88_1 = 0
            safe88+= 1
            c = 1
        if SqrToDel == 89 and safe89<= 2: 
            grid89= 1
            grid89_1 = 0
            safe89+= 1
            c = 1
        if SqrToDel == 90 and safe90<= 2: 
            grid90= 1
            grid90_1 = 0
            safe90+= 1
            c = 1
        if SqrToDel == 91 and safe91<= 2: 
            grid91= 1
            grid91_1 = 0
            safe91+= 1
            c = 1
        if SqrToDel == 92 and safe92<= 2: 
            grid92= 1
            grid92_1 = 0
            safe92+= 1
            c = 1
        if SqrToDel == 93 and safe93<= 2: 
            grid93= 1
            grid93_1 = 0
            safe93+= 1
            c = 1
        if SqrToDel == 94 and safe94<= 2: 
            grid94= 1
            grid94_1 = 0
            safe94+= 1
            c = 1
        if SqrToDel == 95 and safe95<= 2: 
            grid95= 1
            grid95_1 = 0
            safe95+= 1
            c = 1
        if SqrToDel == 96 and safe96<= 2: 
            grid96= 1
            grid96_1 = 0
            safe96+= 1
            c = 1
        if SqrToDel == 97 and safe97<= 2: 
            grid97= 1
            grid97_1 = 0
            safe97+= 1
            c = 1
        if SqrToDel == 98 and safe98<= 2: 
            grid98= 1
            grid98_1 = 0
            safe98+= 1
            c = 1
        if SqrToDel == 99 and safe99<= 2: 
            grid99= 1
            grid99_1 = 0
            safe99+= 1
            c = 1
        if SqrToDel == 100 and safe100<= 2: 
            grid100= 1
            grid100_1 = 0
            safe100+= 1
            c = 1
        if c == 1 or SqrToDel == None:
            f = 0
    if c == 1:
        groundbreak()
    if grid1 == 1:
        if grid1_1 < FPS*.5:
            grid1_1 += 1
            pygame.draw.rect(DS, BLUE, (1, 1, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (1, 1, 40, 40), 0)
            if x <= 40 and y <= 40 and x >= -9 and y >= -9:
                break
    if grid2 == 1:
        if grid2_1 < FPS*.5:
            grid2_1 += 1
            pygame.draw.rect(DS, BLUE, (41, 1, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (41, 1, 40, 40), 0)
            if x <= 80 and y <= 40 and x >= 31 and y >= -9:
                break
    if grid3 == 1:
        if grid3_1 < FPS*.5:
            grid3_1 += 1
            pygame.draw.rect(DS, BLUE, (81, 1, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (81, 1, 40, 40), 0)
            if x <= 120 and y <= 40 and x >= 71 and y >= -9:
                break
    if grid4 == 1:
        if grid4_1 < FPS*.5:
            grid4_1 += 1
            pygame.draw.rect(DS, BLUE, (121, 1, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (121, 1, 40, 40), 0)
            if x <= 160 and y <= 40 and x >= 111 and y >= -9:
                break
    if grid5 == 1:
        if grid5_1 < FPS*.5:
            grid5_1 += 1
            pygame.draw.rect(DS, BLUE, (161, 1, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (161, 1, 40, 40), 0)
            if x <= 200 and y <= 40 and x >= 151 and y >= -9:
                break
    if grid6 == 1:
        if grid6_1 < FPS*.5:
            grid6_1 += 1
            pygame.draw.rect(DS, BLUE, (201, 1, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (201, 1, 40, 40), 0)
            if x <= 240 and y <= 40 and x >= 191 and y >= -9:
                break
    if grid7 == 1:
        if grid7_1 < FPS*.5:
            grid7_1 += 1
            pygame.draw.rect(DS, BLUE, (241, 1, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (241, 1, 40, 40), 0)
            if x <= 280 and y <= 40 and x >= 231 and y >= -9:
                break
    if grid8 == 1:
        if grid8_1 < FPS*.5:
            grid8_1 += 1
            pygame.draw.rect(DS, BLUE, (281, 1, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (281, 1, 40, 40), 0)
            if x <= 320 and y <= 40 and x >= 271 and y >= -9:
                break
    if grid9 == 1:
        if grid9_1 < FPS*.5:
            grid9_1 += 1
            pygame.draw.rect(DS, BLUE, (321, 1, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (321, 1, 40, 40), 0)
            if x <= 360 and y <= 40 and x >= 311 and y >= -9:
                break
    if grid10 == 1:
        if grid10_1 < FPS*.5:
            grid10_1 += 1
            pygame.draw.rect(DS, BLUE, (361, 1, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (361, 1, 40, 40), 0)
            if x <= 400 and y <= 40 and x >= 351 and y >= -9:
                break
    if grid11 == 1:
        if grid11_1 < FPS*.5:
            grid11_1 += 1
            pygame.draw.rect(DS, BLUE, (1, 41, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (1, 41, 40, 40), 0)
            if x <= 40 and y <= 80 and x >= -9 and y >= 31:
                break
    if grid12 == 1:
        if grid12_1 < FPS*.5:
            grid12_1 += 1
            pygame.draw.rect(DS, BLUE, (41, 41, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (41, 41, 40, 40), 0)
            if x <= 80 and y <= 80 and x >= 31 and y >= 31:
                break
    if grid13 == 1:
        if grid13_1 < FPS*.5:
            grid13_1 += 1
            pygame.draw.rect(DS, BLUE, (81, 41, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (81, 41, 40, 40), 0)
            if x <= 120 and y <= 80 and x >= 71 and y >= 31:
                break
    if grid14 == 1:
        if grid14_1 < FPS*.5:
            grid14_1 += 1
            pygame.draw.rect(DS, BLUE, (121, 41, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (121, 41, 40, 40), 0)
            if x <= 160 and y <= 80 and x >= 111 and y >= 31:
                break
    if grid15 == 1:
        if grid15_1 < FPS*.5:
            grid15_1 += 1
            pygame.draw.rect(DS, BLUE, (161, 41, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (161, 41, 40, 40), 0)
            if x <= 200 and y <= 80 and x >= 151 and y >= 31:
                break
    if grid16 == 1:
        if grid16_1 < FPS*.5:
            grid16_1 += 1
            pygame.draw.rect(DS, BLUE, (201, 41, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (201, 41, 40, 40), 0)
            if x <= 240 and y <= 80 and x >= 191 and y >= 31:
                break
    if grid17 == 1:
        if grid17_1 < FPS*.5:
            grid17_1 += 1
            pygame.draw.rect(DS, BLUE, (241, 41, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (241, 41, 40, 40), 0)
            if x <= 280 and y <= 80 and x >= 231 and y >= 31:
                break
    if grid18 == 1:
        if grid18_1 < FPS*.5:
            grid18_1 += 1
            pygame.draw.rect(DS, BLUE, (281, 41, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (281, 41, 40, 40), 0)
            if x <= 320 and y <= 80 and x >= 271 and y >= 31:
                break
    if grid19 == 1:
        if grid19_1 < FPS*.5:
            grid19_1 += 1
            pygame.draw.rect(DS, BLUE, (321, 41, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (321, 41, 40, 40), 0)
            if x <= 360 and y <= 80 and x >= 311 and y >= 31:
                break
    if grid20 == 1:
        if grid20_1 < FPS*.5:
            grid20_1 += 1
            pygame.draw.rect(DS, BLUE, (361, 41, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (361, 41, 40, 40), 0)
            if x <= 400 and y <= 80 and x >= 351 and y >= 31:
                break
    if grid21 == 1:
        if grid21_1 < FPS*.5:
            grid21_1 += 1
            pygame.draw.rect(DS, BLUE, (1, 81, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (1, 81, 40, 40), 0)
            if x <= 40 and y <= 120 and x >= -9 and y >= 71:
                break
    if grid22 == 1:
        if grid22_1 < FPS*.5:
            grid22_1 += 1
            pygame.draw.rect(DS, BLUE, (41, 81, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (41, 81, 40, 40), 0)
            if x <= 80 and y <= 120 and x >= 31 and y >= 71:
                break
    if grid23 == 1:
        if grid23_1 < FPS*.5:
            grid23_1 += 1
            pygame.draw.rect(DS, BLUE, (81, 81, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (81, 81, 40, 40), 0)
            if x <= 120 and y <= 120 and x >= 71 and y >= 71:
                break
    if grid24 == 1:
        if grid24_1 < FPS*.5:
            grid24_1 += 1
            pygame.draw.rect(DS, BLUE, (121, 81, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (121, 81, 40, 40), 0)
            if x <= 160 and y <= 120 and x >= 111 and y >= 71:
                break
    if grid25 == 1:
        if grid25_1 < FPS*.5:
            grid25_1 += 1
            pygame.draw.rect(DS, BLUE, (161, 81, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (161, 81, 40, 40), 0)
            if x <= 200 and y <= 120 and x >= 151 and y >= 71:
                break
    if grid26 == 1:
        if grid26_1 < FPS*.5:
            grid26_1 += 1
            pygame.draw.rect(DS, BLUE, (201, 81, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (201, 81, 40, 40), 0)
            if x <= 240 and y <= 120 and x >= 191 and y >= 71:
                break
    if grid27 == 1:
        if grid27_1 < FPS*.5:
            grid27_1 += 1
            pygame.draw.rect(DS, BLUE, (241, 81, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (241, 81, 40, 40), 0)
            if x <= 280 and y <= 120 and x >= 231 and y >= 71:
                break
    if grid28 == 1:
        if grid28_1 < FPS*.5:
            grid28_1 += 1
            pygame.draw.rect(DS, BLUE, (281, 81, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (281, 81, 40, 40), 0)
            if x <= 320 and y <= 120 and x >= 271 and y >= 71:
                break
    if grid29 == 1:
        if grid29_1 < FPS*.5:
            grid29_1 += 1
            pygame.draw.rect(DS, BLUE, (321, 81, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (321, 81, 40, 40), 0)
            if x <= 360 and y <= 120 and x >= 311 and y >= 71:
                break
    if grid30 == 1:
        if grid30_1 < FPS*.5:
            grid30_1 += 1
            pygame.draw.rect(DS, BLUE, (361, 81, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (361, 81, 40, 40), 0)
            if x <= 400 and y <= 120 and x >= 351 and y >= 71:
                break
    if grid31 == 1:
        if grid31_1 < FPS*.5:
            grid31_1 += 1
            pygame.draw.rect(DS, BLUE, (1, 121, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (1, 121, 40, 40), 0)
            if x <= 40 and y <= 160 and x >= -9 and y >= 111:
                break
    if grid32 == 1:
        if grid32_1 < FPS*.5:
            grid32_1 += 1
            pygame.draw.rect(DS, BLUE, (41, 121, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (41, 121, 40, 40), 0)
            if x <= 80 and y <= 160 and x >= 31 and y >= 111:
                break
    if grid33 == 1:
        if grid33_1 < FPS*.5:
            grid33_1 += 1
            pygame.draw.rect(DS, BLUE, (81, 121, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (81, 121, 40, 40), 0)
            if x <= 120 and y <= 160 and x >= 71 and y >= 111:
                break
    if grid34 == 1:
        if grid34_1 < FPS*.5:
            grid34_1 += 1
            pygame.draw.rect(DS, BLUE, (121, 121, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (121, 121, 40, 40), 0)
            if x <= 160 and y <= 160 and x >= 111 and y >= 111:
                break
    if grid35 == 1:
        if grid35_1 < FPS*.5:
            grid35_1 += 1
            pygame.draw.rect(DS, BLUE, (161, 121, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (161, 121, 40, 40), 0)
            if x <= 200 and y <= 160 and x >= 151 and y >= 111:
                break
    if grid36 == 1:
        if grid36_1 < FPS*.5:
            grid36_1 += 1
            pygame.draw.rect(DS, BLUE, (201, 121, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (201, 121, 40, 40), 0)
            if x <= 240 and y <= 160 and x >= 191 and y >= 111:
                break
    if grid37 == 1:
        if grid37_1 < FPS*.5:
            grid37_1 += 1
            pygame.draw.rect(DS, BLUE, (241, 121, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (241, 121, 40, 40), 0)
            if x <= 280 and y <= 160 and x >= 231 and y >= 111:
                break
    if grid38 == 1:
        if grid38_1 < FPS*.5:
            grid38_1 += 1
            pygame.draw.rect(DS, BLUE, (281, 121, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (281, 121, 40, 40), 0)
            if x <= 320 and y <= 160 and x >= 271 and y >= 111:
                break
    if grid39 == 1:
        if grid39_1 < FPS*.5:
            grid39_1 += 1
            pygame.draw.rect(DS, BLUE, (321, 121, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (321, 121, 40, 40), 0)
            if x <= 360 and y <= 160 and x >= 311 and y >= 111:
                break
    if grid40 == 1:
        if grid40_1 < FPS*.5:
            grid40_1 += 1
            pygame.draw.rect(DS, BLUE, (361, 121, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (361, 121, 40, 40), 0)
            if x <= 400 and y <= 160 and x >= 351 and y >= 111:
                break
    if grid41 == 1:
        if grid41_1 < FPS*.5:
            grid41_1 += 1
            pygame.draw.rect(DS, BLUE, (1, 161, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (1, 161, 40, 40), 0)
            if x <= 40 and y <= 200 and x >= -9 and y >= 151:
                break
    if grid42 == 1:
        if grid42_1 < FPS*.5:
            grid42_1 += 1
            pygame.draw.rect(DS, BLUE, (41, 161, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (41, 161, 40, 40), 0)
            if x <= 80 and y <= 200 and x >= 31 and y >= 151:
                break
    if grid43 == 1:
        if grid43_1 < FPS*.5:
            grid43_1 += 1
            pygame.draw.rect(DS, BLUE, (81, 161, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (81, 161, 40, 40), 0)
            if x <= 120 and y <= 200 and x >= 71 and y >= 151:
                break
    if grid44 == 1:
        if grid44_1 < FPS*.5:
            grid44_1 += 1
            pygame.draw.rect(DS, BLUE, (121, 161, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (121, 161, 40, 40), 0)
            if x <= 160 and y <= 200 and x >= 111 and y >= 151:
                break
    if grid45 == 1:
        if grid45_1 < FPS*.5:
            grid45_1 += 1
            pygame.draw.rect(DS, BLUE, (161, 161, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (161, 161, 40, 40), 0)
            if x <= 200 and y <= 200 and x >= 151 and y >= 151:
                break
    if grid46 == 1:
        if grid46_1 < FPS*.5:
            grid46_1 += 1
            pygame.draw.rect(DS, BLUE, (201, 161, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (201, 161, 40, 40), 0)
            if x <= 240 and y <= 200 and x >= 191 and y >= 151:
                break
    if grid47 == 1:
        if grid47_1 < FPS*.5:
            grid47_1 += 1
            pygame.draw.rect(DS, BLUE, (241, 161, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (241, 161, 40, 40), 0)
            if x <= 280 and y <= 200 and x >= 231 and y >= 151:
                break
    if grid48 == 1:
        if grid48_1 < FPS*.5:
            grid48_1 += 1
            pygame.draw.rect(DS, BLUE, (281, 161, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (281, 161, 40, 40), 0)
            if x <= 320 and y <= 200 and x >= 271 and y >= 151:
                break
    if grid49 == 1:
        if grid49_1 < FPS*.5:
            grid49_1 += 1
            pygame.draw.rect(DS, BLUE, (321, 161, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (321, 161, 40, 40), 0)
            if x <= 360 and y <= 200 and x >= 311 and y >= 151:
                break
    if grid50 == 1:
        if grid50_1 < FPS*.5:
            grid50_1 += 1
            pygame.draw.rect(DS, BLUE, (361, 161, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (361, 161, 40, 40), 0)
            if x <= 400 and y <= 200 and x >= 351 and y >= 151:
                break
    if grid51 == 1:
        if grid51_1 < FPS*.5:
            grid51_1 += 1
            pygame.draw.rect(DS, BLUE, (1, 201, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (1, 201, 40, 40), 0)
            if x <= 40 and y <= 240 and x >= -9 and y >= 191:
                break
    if grid52 == 1:
        if grid52_1 < FPS*.5:
            grid52_1 += 1
            pygame.draw.rect(DS, BLUE, (41, 201, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (41, 201, 40, 40), 0)
            if x <= 80 and y <= 240 and x >= 31 and y >= 191:
                break
    if grid53 == 1:
        if grid53_1 < FPS*.5:
            grid53_1 += 1
            pygame.draw.rect(DS, BLUE, (81, 201, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (81, 201, 40, 40), 0)
            if x <= 120 and y <= 240 and x >= 71 and y >= 191:
                break
    if grid54 == 1:
        if grid54_1 < FPS*.5:
            grid54_1 += 1
            pygame.draw.rect(DS, BLUE, (121, 201, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (121, 201, 40, 40), 0)
            if x <= 160 and y <= 240 and x >= 111 and y >= 191:
                break
    if grid55 == 1:
        if grid55_1 < FPS*.5:
            grid55_1 += 1
            pygame.draw.rect(DS, BLUE, (161, 201, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (161, 201, 40, 40), 0)
            if x <= 200 and y <= 240 and x >= 151 and y >= 191:
                break
    if grid56 == 1:
        if grid56_1 < FPS*.5:
            grid56_1 += 1
            pygame.draw.rect(DS, BLUE, (201, 201, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (201, 201, 40, 40), 0)
            if x <= 240 and y <= 240 and x >= 191 and y >= 191:
                break
    if grid57 == 1:
        if grid57_1 < FPS*.5:
            grid57_1 += 1
            pygame.draw.rect(DS, BLUE, (241, 201, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (241, 201, 40, 40), 0)
            if x <= 280 and y <= 240 and x >= 231 and y >= 191:
                break
    if grid58 == 1:
        if grid58_1 < FPS*.5:
            grid58_1 += 1
            pygame.draw.rect(DS, BLUE, (281, 201, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (281, 201, 40, 40), 0)
            if x <= 320 and y <= 240 and x >= 271 and y >= 191:
                break
    if grid59 == 1:
        if grid59_1 < FPS*.5:
            grid59_1 += 1
            pygame.draw.rect(DS, BLUE, (321, 201, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (321, 201, 40, 40), 0)
            if x <= 360 and y <= 240 and x >= 311 and y >= 191:
                break
    if grid60 == 1:
        if grid60_1 < FPS*.5:
            grid60_1 += 1
            pygame.draw.rect(DS, BLUE, (361, 201, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (361, 201, 40, 40), 0)
            if x <= 400 and y <= 240 and x >= 351 and y >= 191:
                break
    if grid61 == 1:
        if grid61_1 < FPS*.5:
            grid61_1 += 1
            pygame.draw.rect(DS, BLUE, (1, 241, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (1, 241, 40, 40), 0)
            if x <= 40 and y <= 280 and x >= -9 and y >= 231:
                break
    if grid62 == 1:
        if grid62_1 < FPS*.5:
            grid62_1 += 1
            pygame.draw.rect(DS, BLUE, (41, 241, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (41, 241, 40, 40), 0)
            if x <= 80 and y <= 280 and x >= 31 and y >= 231:
                break
    if grid63 == 1:
        if grid63_1 < FPS*.5:
            grid63_1 += 1
            pygame.draw.rect(DS, BLUE, (81, 241, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (81, 241, 40, 40), 0)
            if x <= 120 and y <= 280 and x >= 71 and y >= 231:
                break
    if grid64 == 1:
        if grid64_1 < FPS*.5:
            grid64_1 += 1
            pygame.draw.rect(DS, BLUE, (121, 241, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (121, 241, 40, 40), 0)
            if x <= 160 and y <= 280 and x >= 111 and y >= 231:
                break
    if grid65 == 1:
        if grid65_1 < FPS*.5:
            grid65_1 += 1
            pygame.draw.rect(DS, BLUE, (161, 241, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (161, 241, 40, 40), 0)
            if x <= 200 and y <= 280 and x >= 151 and y >= 231:
                break
    if grid66 == 1:
        if grid66_1 < FPS*.5:
            grid66_1 += 1
            pygame.draw.rect(DS, BLUE, (201, 241, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (201, 241, 40, 40), 0)
            if x <= 240 and y <= 280 and x >= 191 and y >= 231:
                break
    if grid67 == 1:
        if grid67_1 < FPS*.5:
            grid67_1 += 1
            pygame.draw.rect(DS, BLUE, (241, 241, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (241, 241, 40, 40), 0)
            if x <= 280 and y <= 280 and x >= 231 and y >= 231:
                break
    if grid68 == 1:
        if grid68_1 < FPS*.5:
            grid68_1 += 1
            pygame.draw.rect(DS, BLUE, (281, 241, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (281, 241, 40, 40), 0)
            if x <= 320 and y <= 280 and x >= 271 and y >= 231:
                break
    if grid69 == 1:
        if grid69_1 < FPS*.5:
            grid69_1 += 1
            pygame.draw.rect(DS, BLUE, (321, 241, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (321, 241, 40, 40), 0)
            if x <= 360 and y <= 280 and x >= 311 and y >= 231:
                break
    if grid70 == 1:
        if grid70_1 < FPS*.5:
            grid70_1 += 1
            pygame.draw.rect(DS, BLUE, (361, 241, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (361, 241, 40, 40), 0)
            if x <= 400 and y <= 280 and x >= 351 and y >= 231:
                break
    if grid71 == 1:
        if grid71_1 < FPS*.5:
            grid71_1 += 1
            pygame.draw.rect(DS, BLUE, (1, 281, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (1, 281, 40, 40), 0)
            if x <= 40 and y <= 320 and x >= -9 and y >= 271:
                break
    if grid72 == 1:
        if grid72_1 < FPS*.5:
            grid72_1 += 1
            pygame.draw.rect(DS, BLUE, (41, 281, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (41, 281, 40, 40), 0)
            if x <= 80 and y <= 320 and x >= 31 and y >= 271:
                break
    if grid73 == 1:
        if grid73_1 < FPS*.5:
            grid73_1 += 1
            pygame.draw.rect(DS, BLUE, (81, 281, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (81, 281, 40, 40), 0)
            if x <= 120 and y <= 320 and x >= 71 and y >= 271:
                break
    if grid74 == 1:
        if grid74_1 < FPS*.5:
            grid74_1 += 1
            pygame.draw.rect(DS, BLUE, (121, 281, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (121, 281, 40, 40), 0)
            if x <= 160 and y <= 320 and x >= 111 and y >= 271:
                break
    if grid75 == 1:
        if grid75_1 < FPS*.5:
            grid75_1 += 1
            pygame.draw.rect(DS, BLUE, (161, 281, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (161, 281, 40, 40), 0)
            if x <= 200 and y <= 320 and x >= 151 and y >= 271:
                break
    if grid76 == 1:
        if grid76_1 < FPS*.5:
            grid76_1 += 1
            pygame.draw.rect(DS, BLUE, (201, 281, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (201, 281, 40, 40), 0)
            if x <= 240 and y <= 320 and x >= 191 and y >= 271:
                break
    if grid77 == 1:
        if grid77_1 < FPS*.5:
            grid77_1 += 1
            pygame.draw.rect(DS, BLUE, (241, 281, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (241, 281, 40, 40), 0)
            if x <= 280 and y <= 320 and x >= 231 and y >= 271:
                break
    if grid78 == 1:
        if grid78_1 < FPS*.5:
            grid78_1 += 1
            pygame.draw.rect(DS, BLUE, (281, 281, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (281, 281, 40, 40), 0)
            if x <= 320 and y <= 320 and x >= 271 and y >= 271:
                break
    if grid79 == 1:
        if grid79_1 < FPS*.5:
            grid79_1 += 1
            pygame.draw.rect(DS, BLUE, (321, 281, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (321, 281, 40, 40), 0)
            if x <= 360 and y <= 320 and x >= 311 and y >= 271:
                break
    if grid80 == 1:
        if grid80_1 < FPS*.5:
            grid80_1 += 1
            pygame.draw.rect(DS, BLUE, (361, 281, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (361, 281, 40, 40), 0)
            if x <= 400 and y <= 320 and x >= 351 and y >= 271:
                break
    if grid81 == 1:
        if grid81_1 < FPS*.5:
            grid81_1 += 1
            pygame.draw.rect(DS, BLUE, (1, 321, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (1, 321, 40, 40), 0)
            if x <= 40 and y <= 360 and x >= -9 and y >= 311:
                break
    if grid82 == 1:
        if grid82_1 < FPS*.5:
            grid82_1 += 1
            pygame.draw.rect(DS, BLUE, (41, 321, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (41, 321, 40, 40), 0)
            if x <= 80 and y <= 360 and x >= 31 and y >= 311:
                break
    if grid83 == 1:
        if grid83_1 < FPS*.5:
            grid83_1 += 1
            pygame.draw.rect(DS, BLUE, (81, 321, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (81, 321, 40, 40), 0)
            if x <= 120 and y <= 360 and x >= 71 and y >= 311:
                break
    if grid84 == 1:
        if grid84_1 < FPS*.5:
            grid84_1 += 1
            pygame.draw.rect(DS, BLUE, (121, 321, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (121, 321, 40, 40), 0)
            if x <= 160 and y <= 360 and x >= 111 and y >= 311:
                break
    if grid85 == 1:
        if grid85_1 < FPS*.5:
            grid85_1 += 1
            pygame.draw.rect(DS, BLUE, (161, 321, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (161, 321, 40, 40), 0)
            if x <= 200 and y <= 360 and x >= 151 and y >= 311:
                break
    if grid86 == 1:
        if grid86_1 < FPS*.5:
            grid86_1 += 1
            pygame.draw.rect(DS, BLUE, (201, 321, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (201, 321, 40, 40), 0)
            if x <= 240 and y <= 360 and x >= 191 and y >= 311:
                break
    if grid87 == 1:
        if grid87_1 < FPS*.5:
            grid87_1 += 1
            pygame.draw.rect(DS, BLUE, (241, 321, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (241, 321, 40, 40), 0)
            if x <= 280 and y <= 360 and x >= 231 and y >= 311:
                break
    if grid88 == 1:
        if grid88_1 < FPS*.5:
            grid88_1 += 1
            pygame.draw.rect(DS, BLUE, (281, 321, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (281, 321, 40, 40), 0)
            if x <= 320 and y <= 360 and x >= 271 and y >= 311:
                break
    if grid89 == 1:
        if grid89_1 < FPS*.5:
            grid89_1 += 1
            pygame.draw.rect(DS, BLUE, (321, 321, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (321, 321, 40, 40), 0)
            if x <= 360 and y <= 360 and x >= 311 and y >= 311:
                break
    if grid90 == 1:
        if grid90_1 < FPS*.5:
            grid90_1 += 1
            pygame.draw.rect(DS, BLUE, (361, 321, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (361, 321, 40, 40), 0)
            if x <= 400 and y <= 360 and x >= 351 and y >= 311:
                break
    if grid91 == 1:
        if grid91_1 < FPS*.5:
            grid91_1 += 1
            pygame.draw.rect(DS, BLUE, (1, 361, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (1, 361, 40, 40), 0)
            if x <= 40 and y <= 400 and x >= -9 and y >= 351:
                break
    if grid92 == 1:
        if grid92_1 < FPS*.5:
            grid92_1 += 1
            pygame.draw.rect(DS, BLUE, (41, 361, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (41, 361, 40, 40), 0)
            if x <= 80 and y <= 400 and x >= 31 and y >= 351:
                break
    if grid93 == 1:
        if grid93_1 < FPS*.5:
            grid93_1 += 1
            pygame.draw.rect(DS, BLUE, (81, 361, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (81, 361, 40, 40), 0)
            if x <= 120 and y <= 400 and x >= 71 and y >= 351:
                break
    if grid94 == 1:
        if grid94_1 < FPS*.5:
            grid94_1 += 1
            pygame.draw.rect(DS, BLUE, (121, 361, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (121, 361, 40, 40), 0)
            if x <= 160 and y <= 400 and x >= 111 and y >= 351:
                break
    if grid95 == 1:
        if grid95_1 < FPS*.5:
            grid95_1 += 1
            pygame.draw.rect(DS, BLUE, (161, 361, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (161, 361, 40, 40), 0)
            if x <= 200 and y <= 400 and x >= 151 and y >= 351:
                break
    if grid96 == 1:
        if grid96_1 < FPS*.5:
            grid96_1 += 1
            pygame.draw.rect(DS, BLUE, (201, 361, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (201, 361, 40, 40), 0)
            if x <= 240 and y <= 400 and x >= 191 and y >= 351:
                break
    if grid97 == 1:
        if grid97_1 < FPS*.5:
            grid97_1 += 1
            pygame.draw.rect(DS, BLUE, (241, 361, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (241, 361, 40, 40), 0)
            if x <= 280 and y <= 400 and x >= 231 and y >= 351:
                break
    if grid98 == 1:
        if grid98_1 < FPS*.5:
            grid98_1 += 1
            pygame.draw.rect(DS, BLUE, (281, 361, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (281, 361, 40, 40), 0)
            if x <= 320 and y <= 400 and x >= 271 and y >= 351:
                break
    if grid99 == 1:
        if grid99_1 < FPS*.5:
            grid99_1 += 1
            pygame.draw.rect(DS, BLUE, (321, 361, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (321, 361, 40, 40), 0)
            if x <= 360 and y <= 400 and x >= 311 and y >= 351:
                break
    if grid100 == 1:
        if grid100_1 < FPS*.5:
            grid100_1 += 1
            pygame.draw.rect(DS, BLUE, (361, 361, 40, 40), 0)
        else:
            pygame.draw.rect(DS, RED, (361, 361, 40, 40), 0)
            if x <= 400 and y <= 400 and x >= 351 and y >= 351:
                break



    loopruns = ChangeLoop(loopruns, FPS)

    loopruns+=1
    pygame.draw.rect(DS, YELLOW, (x, y, 10, 10), 0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
FPS = 4
if grid1 == 1:
    score += 1
if grid2 == 1:
    score += 1
if grid3 == 1:
    score += 1
if grid4 == 1:
    score += 1
if grid5 == 1:
    score += 1
if grid6 == 1:
    score += 1
if grid7 == 1:
    score += 1
if grid8 == 1:
    score += 1
if grid9 == 1:
    score += 1
if grid10 == 1:
    score += 1
if grid11 == 1:
    score += 1
if grid12 == 1:
    score += 1
if grid13 == 1:
    score += 1
if grid14 == 1:
    score += 1
if grid15 == 1:
    score += 1
if grid16 == 1:
    score += 1
if grid17 == 1:
    score += 1
if grid18 == 1:
    score += 1
if grid19 == 1:
    score += 1
if grid20 == 1:
    score += 1
if grid21 == 1:
    score += 1
if grid22 == 1:
    score += 1
if grid23 == 1:
    score += 1
if grid24 == 1:
    score += 1
if grid25 == 1:
    score += 1
if grid26 == 1:
    score += 1
if grid27 == 1:
    score += 1
if grid28 == 1:
    score += 1
if grid29 == 1:
    score += 1
if grid30 == 1:
    score += 1
if grid31 == 1:
    score += 1
if grid32 == 1:
    score += 1
if grid33 == 1:
    score += 1
if grid34 == 1:
    score += 1
if grid35 == 1:
    score += 1
if grid36 == 1:
    score += 1
if grid37 == 1:
    score += 1
if grid38 == 1:
    score += 1
if grid39 == 1:
    score += 1
if grid40 == 1:
    score += 1
if grid41 == 1:
    score += 1
if grid42 == 1:
    score += 1
if grid43 == 1:
    score += 1
if grid44 == 1:
    score += 1
if grid45 == 1:
    score += 1
if grid46 == 1:
    score += 1
if grid47 == 1:
    score += 1
if grid48 == 1:
    score += 1
if grid49 == 1:
    score += 1
if grid50 == 1:
    score += 1
if grid51 == 1:
    score += 1
if grid52 == 1:
    score += 1
if grid53 == 1:
    score += 1
if grid54 == 1:
    score += 1
if grid55 == 1:
    score += 1
if grid56 == 1:
    score += 1
if grid57 == 1:
    score += 1
if grid58 == 1:
    score += 1
if grid59 == 1:
    score += 1
if grid60 == 1:
    score += 1
if grid61 == 1:
    score += 1
if grid62 == 1:
    score += 1
if grid63 == 1:
    score += 1
if grid64 == 1:
    score += 1
if grid65 == 1:
    score += 1
if grid66 == 1:
    score += 1
if grid67 == 1:
    score += 1
if grid68 == 1:
    score += 1
if grid69 == 1:
    score += 1
if grid70 == 1:
    score += 1
if grid71 == 1:
    score += 1
if grid72 == 1:
    score += 1
if grid73 == 1:
    score += 1
if grid74 == 1:
    score += 1
if grid75 == 1:
    score += 1
if grid76 == 1:
    score += 1
if grid77 == 1:
    score += 1
if grid78 == 1:
    score += 1
if grid79 == 1:
    score += 1
if grid80 == 1:
    score += 1
if grid81 == 1:
    score += 1
if grid82 == 1:
    score += 1
if grid83 == 1:
    score += 1
if grid84 == 1:
    score += 1
if grid85 == 1:
    score += 1
if grid86 == 1:
    score += 1
if grid87 == 1:
    score += 1
if grid88 == 1:
    score += 1
if grid89 == 1:
    score += 1
if grid90 == 1:
    score += 1
if grid91 == 1:
    score += 1
if grid92 == 1:
    score += 1
if grid93 == 1:
    score += 1
if grid94 == 1:
    score += 1
if grid95 == 1:
    score += 1
if grid96 == 1:
    score += 1
if grid97 == 1:
    score += 1
if grid98 == 1:
    score += 1
if grid99 == 1:
    score += 1
if grid100 == 1:
    score += 1
pygame.mixer.music.load('Lost.wav')
pygame.mixer.music.play(-1, 0.0)
while losstime < (FPS*3.5):
    DS.fill(Color)
    pygame.display.set_caption('AGLYRD')
    if grid1 == 1:
        pygame.draw.rect(DS, BLUE, (1, 1, 40, 40), 0)
    if grid2 == 1:
        pygame.draw.rect(DS, BLUE, (41, 1, 40, 40), 0)
    if grid3 == 1:
        pygame.draw.rect(DS, BLUE, (81, 1, 40, 40), 0)
    if grid4 == 1:
        pygame.draw.rect(DS, BLUE, (121, 1, 40, 40), 0)
    if grid5 == 1:
        pygame.draw.rect(DS, BLUE, (161, 1, 40, 40), 0)
    if grid6 == 1:
        pygame.draw.rect(DS, BLUE, (201, 1, 40, 40), 0)
    if grid7 == 1:
        pygame.draw.rect(DS, BLUE, (241, 1, 40, 40), 0)
    if grid8 == 1:
        pygame.draw.rect(DS, BLUE, (281, 1, 40, 40), 0)
    if grid9 == 1:
        pygame.draw.rect(DS, BLUE, (321, 1, 40, 40), 0)
    if grid10 == 1:
        pygame.draw.rect(DS, BLUE, (361, 1, 40, 40), 0)
    if grid11 == 1:
        pygame.draw.rect(DS, BLUE, (1, 41, 40, 40), 0)
    if grid12 == 1:
        pygame.draw.rect(DS, BLUE, (41, 41, 40, 40), 0)
    if grid13 == 1:
        pygame.draw.rect(DS, BLUE, (81, 41, 40, 40), 0)
    if grid14 == 1:
        pygame.draw.rect(DS, BLUE, (121, 41, 40, 40), 0)
    if grid15 == 1:
        pygame.draw.rect(DS, BLUE, (161, 41, 40, 40), 0)
    if grid16 == 1:
        pygame.draw.rect(DS, BLUE, (201, 41, 40, 40), 0)
    if grid17 == 1:
        pygame.draw.rect(DS, BLUE, (241, 41, 40, 40), 0)
    if grid18 == 1:
        pygame.draw.rect(DS, BLUE, (281, 41, 40, 40), 0)
    if grid19 == 1:
        pygame.draw.rect(DS, BLUE, (321, 41, 40, 40), 0)
    if grid20 == 1:
        pygame.draw.rect(DS, BLUE, (361, 41, 40, 40), 0)
    if grid21 == 1:
        pygame.draw.rect(DS, BLUE, (1, 81, 40, 40), 0)
    if grid22 == 1:
        pygame.draw.rect(DS, BLUE, (41, 81, 40, 40), 0)
    if grid23 == 1:
        pygame.draw.rect(DS, BLUE, (81, 81, 40, 40), 0)
    if grid24 == 1:
        pygame.draw.rect(DS, BLUE, (121, 81, 40, 40), 0)
    if grid25 == 1:
        pygame.draw.rect(DS, BLUE, (161, 81, 40, 40), 0)
    if grid26 == 1:
        pygame.draw.rect(DS, BLUE, (201, 81, 40, 40), 0)
    if grid27 == 1:
        pygame.draw.rect(DS, BLUE, (241, 81, 40, 40), 0)
    if grid28 == 1:
        pygame.draw.rect(DS, BLUE, (281, 81, 40, 40), 0)
    if grid29 == 1:
        pygame.draw.rect(DS, BLUE, (321, 81, 40, 40), 0)
    if grid30 == 1:
        pygame.draw.rect(DS, BLUE, (361, 81, 40, 40), 0)
    if grid31 == 1:
        pygame.draw.rect(DS, BLUE, (1, 121, 40, 40), 0)
    if grid32 == 1:
        pygame.draw.rect(DS, BLUE, (41, 121, 40, 40), 0)
    if grid33 == 1:
        pygame.draw.rect(DS, BLUE, (81, 121, 40, 40), 0)
    if grid34 == 1:
        pygame.draw.rect(DS, BLUE, (121, 121, 40, 40), 0)
    if grid35 == 1:
        pygame.draw.rect(DS, BLUE, (161, 121, 40, 40), 0)
    if grid36 == 1:
        pygame.draw.rect(DS, BLUE, (201, 121, 40, 40), 0)
    if grid37 == 1:
        pygame.draw.rect(DS, BLUE, (241, 121, 40, 40), 0)
    if grid38 == 1:
        pygame.draw.rect(DS, BLUE, (281, 121, 40, 40), 0)
    if grid39 == 1:
        pygame.draw.rect(DS, BLUE, (321, 121, 40, 40), 0)
    if grid40 == 1:
        pygame.draw.rect(DS, BLUE, (361, 121, 40, 40), 0)
    if grid41 == 1:
        pygame.draw.rect(DS, BLUE, (1, 161, 40, 40), 0)
    if grid42 == 1:
        pygame.draw.rect(DS, BLUE, (41, 161, 40, 40), 0)
    if grid43 == 1:
        pygame.draw.rect(DS, BLUE, (81, 161, 40, 40), 0)
    if grid44 == 1:
        pygame.draw.rect(DS, BLUE, (121, 161, 40, 40), 0)
    if grid45 == 1:
        pygame.draw.rect(DS, BLUE, (161, 161, 40, 40), 0)
    if grid46 == 1:
        pygame.draw.rect(DS, BLUE, (201, 161, 40, 40), 0)
    if grid47 == 1:
        pygame.draw.rect(DS, BLUE, (241, 161, 40, 40), 0)
    if grid48 == 1:
        pygame.draw.rect(DS, BLUE, (281, 161, 40, 40), 0)
    if grid49 == 1:
        pygame.draw.rect(DS, BLUE, (321, 161, 40, 40), 0)
    if grid50 == 1:
        pygame.draw.rect(DS, BLUE, (361, 161, 40, 40), 0)
    if grid51 == 1:
        pygame.draw.rect(DS, BLUE, (1, 201, 40, 40), 0)
    if grid52 == 1:
        pygame.draw.rect(DS, BLUE, (41, 201, 40, 40), 0)
    if grid53 == 1:
        pygame.draw.rect(DS, BLUE, (81, 201, 40, 40), 0)
    if grid54 == 1:
        pygame.draw.rect(DS, BLUE, (121, 201, 40, 40), 0)
    if grid55 == 1:
        pygame.draw.rect(DS, BLUE, (161, 201, 40, 40), 0)
    if grid56 == 1:
        pygame.draw.rect(DS, BLUE, (201, 201, 40, 40), 0)
    if grid57 == 1:
        pygame.draw.rect(DS, BLUE, (241, 201, 40, 40), 0)
    if grid58 == 1:
        pygame.draw.rect(DS, BLUE, (281, 201, 40, 40), 0)
    if grid59 == 1:
        pygame.draw.rect(DS, BLUE, (321, 201, 40, 40), 0)
    if grid60 == 1:
        pygame.draw.rect(DS, BLUE, (361, 201, 40, 40), 0)
    if grid61 == 1:
        pygame.draw.rect(DS, BLUE, (1, 241, 40, 40), 0)
    if grid62 == 1:
        pygame.draw.rect(DS, BLUE, (41, 241, 40, 40), 0)
    if grid63 == 1:
        pygame.draw.rect(DS, BLUE, (81, 241, 40, 40), 0)
    if grid64 == 1:
        pygame.draw.rect(DS, BLUE, (121, 241, 40, 40), 0)
    if grid65 == 1:
        pygame.draw.rect(DS, BLUE, (161, 241, 40, 40), 0)
    if grid66 == 1:
        pygame.draw.rect(DS, BLUE, (201, 241, 40, 40), 0)
    if grid67 == 1:
        pygame.draw.rect(DS, BLUE, (241, 241, 40, 40), 0)
    if grid68 == 1:
        pygame.draw.rect(DS, BLUE, (281, 241, 40, 40), 0)
    if grid69 == 1:
        pygame.draw.rect(DS, BLUE, (321, 241, 40, 40), 0)
    if grid70 == 1:
        pygame.draw.rect(DS, BLUE, (361, 241, 40, 40), 0)
    if grid71 == 1:
        pygame.draw.rect(DS, BLUE, (1, 281, 40, 40), 0)
    if grid72 == 1:
        pygame.draw.rect(DS, BLUE, (41, 281, 40, 40), 0)
    if grid73 == 1:
        pygame.draw.rect(DS, BLUE, (81, 281, 40, 40), 0)
    if grid74 == 1:
        pygame.draw.rect(DS, BLUE, (121, 281, 40, 40), 0)
    if grid75 == 1:
        pygame.draw.rect(DS, BLUE, (161, 281, 40, 40), 0)
    if grid76 == 1:
        pygame.draw.rect(DS, BLUE, (201, 281, 40, 40), 0)
    if grid77 == 1:
        pygame.draw.rect(DS, BLUE, (241, 281, 40, 40), 0)
    if grid78 == 1:
        pygame.draw.rect(DS, BLUE, (281, 281, 40, 40), 0)
    if grid79 == 1:
        pygame.draw.rect(DS, BLUE, (321, 281, 40, 40), 0)
    if grid80 == 1:
        pygame.draw.rect(DS, BLUE, (361, 281, 40, 40), 0)
    if grid81 == 1:
        pygame.draw.rect(DS, BLUE, (1, 321, 40, 40), 0)
    if grid82 == 1:
        pygame.draw.rect(DS, BLUE, (41, 321, 40, 40), 0)
    if grid83 == 1:
        pygame.draw.rect(DS, BLUE, (81, 321, 40, 40), 0)
    if grid84 == 1:
        pygame.draw.rect(DS, BLUE, (121, 321, 40, 40), 0)
    if grid85 == 1:
        pygame.draw.rect(DS, BLUE, (161, 321, 40, 40), 0)
    if grid86 == 1:
        pygame.draw.rect(DS, BLUE, (201, 321, 40, 40), 0)
    if grid87 == 1:
        pygame.draw.rect(DS, BLUE, (241, 321, 40, 40), 0)
    if grid88 == 1:
        pygame.draw.rect(DS, BLUE, (281, 321, 40, 40), 0)
    if grid89 == 1:
        pygame.draw.rect(DS, BLUE, (321, 321, 40, 40), 0)
    if grid90 == 1:
        pygame.draw.rect(DS, BLUE, (361, 321, 40, 40), 0)
    if grid91 == 1:
        pygame.draw.rect(DS, BLUE, (1, 361, 40, 40), 0)
    if grid92 == 1:
        pygame.draw.rect(DS, BLUE, (41, 361, 40, 40), 0)
    if grid93 == 1:
        pygame.draw.rect(DS, BLUE, (81, 361, 40, 40), 0)
    if grid94 == 1:
        pygame.draw.rect(DS, BLUE, (121, 361, 40, 40), 0)
    if grid95 == 1:
        pygame.draw.rect(DS, BLUE, (161, 361, 40, 40), 0)
    if grid96 == 1:
        pygame.draw.rect(DS, BLUE, (201, 361, 40, 40), 0)
    if grid97 == 1:
        pygame.draw.rect(DS, BLUE, (241, 361, 40, 40), 0)
    if grid98 == 1:
        pygame.draw.rect(DS, BLUE, (281, 361, 40, 40), 0)
    if grid99 == 1:
        pygame.draw.rect(DS, BLUE, (321, 361, 40, 40), 0)
    if grid100 == 1:
        pygame.draw.rect(DS, BLUE, (361, 361, 40, 40), 0)
    pygame.draw.rect(DS, YELLOW, (x, y, 10, 10), 0)
    pygame.display.update()
    losstime += 1
    fpsClock.tick(FPS)
    DS.fill(Color)
    pygame.display.set_caption('AGLYRD - YOU LOSE - SCORE:' + str(score))
    if grid1 == 1:
        pygame.draw.rect(DS, RED, (1, 1, 40, 40), 0)
    if grid2 == 1:
        pygame.draw.rect(DS, RED, (41, 1, 40, 40), 0)
    if grid3 == 1:
        pygame.draw.rect(DS, RED, (81, 1, 40, 40), 0)
    if grid4 == 1:
        pygame.draw.rect(DS, RED, (121, 1, 40, 40), 0)
    if grid5 == 1:
        pygame.draw.rect(DS, RED, (161, 1, 40, 40), 0)
    if grid6 == 1:
        pygame.draw.rect(DS, RED, (201, 1, 40, 40), 0)
    if grid7 == 1:
        pygame.draw.rect(DS, RED, (241, 1, 40, 40), 0)
    if grid8 == 1:
        pygame.draw.rect(DS, RED, (281, 1, 40, 40), 0)
    if grid9 == 1:
        pygame.draw.rect(DS, RED, (321, 1, 40, 40), 0)
    if grid10 == 1:
        pygame.draw.rect(DS, RED, (361, 1, 40, 40), 0)
    if grid11 == 1:
        pygame.draw.rect(DS, RED, (1, 41, 40, 40), 0)
    if grid12 == 1:
        pygame.draw.rect(DS, RED, (41, 41, 40, 40), 0)
    if grid13 == 1:
        pygame.draw.rect(DS, RED, (81, 41, 40, 40), 0)
    if grid14 == 1:
        pygame.draw.rect(DS, RED, (121, 41, 40, 40), 0)
    if grid15 == 1:
        pygame.draw.rect(DS, RED, (161, 41, 40, 40), 0)
    if grid16 == 1:
        pygame.draw.rect(DS, RED, (201, 41, 40, 40), 0)
    if grid17 == 1:
        pygame.draw.rect(DS, RED, (241, 41, 40, 40), 0)
    if grid18 == 1:
        pygame.draw.rect(DS, RED, (281, 41, 40, 40), 0)
    if grid19 == 1:
        pygame.draw.rect(DS, RED, (321, 41, 40, 40), 0)
    if grid20 == 1:
        pygame.draw.rect(DS, RED, (361, 41, 40, 40), 0)
    if grid21 == 1:
        pygame.draw.rect(DS, RED, (1, 81, 40, 40), 0)
    if grid22 == 1:
        pygame.draw.rect(DS, RED, (41, 81, 40, 40), 0)
    if grid23 == 1:
        pygame.draw.rect(DS, RED, (81, 81, 40, 40), 0)
    if grid24 == 1:
        pygame.draw.rect(DS, RED, (121, 81, 40, 40), 0)
    if grid25 == 1:
        pygame.draw.rect(DS, RED, (161, 81, 40, 40), 0)
    if grid26 == 1:
        pygame.draw.rect(DS, RED, (201, 81, 40, 40), 0)
    if grid27 == 1:
        pygame.draw.rect(DS, RED, (241, 81, 40, 40), 0)
    if grid28 == 1:
        pygame.draw.rect(DS, RED, (281, 81, 40, 40), 0)
    if grid29 == 1:
        pygame.draw.rect(DS, RED, (321, 81, 40, 40), 0)
    if grid30 == 1:
        pygame.draw.rect(DS, RED, (361, 81, 40, 40), 0)
    if grid31 == 1:
        pygame.draw.rect(DS, RED, (1, 121, 40, 40), 0)
    if grid32 == 1:
        pygame.draw.rect(DS, RED, (41, 121, 40, 40), 0)
    if grid33 == 1:
        pygame.draw.rect(DS, RED, (81, 121, 40, 40), 0)
    if grid34 == 1:
        pygame.draw.rect(DS, RED, (121, 121, 40, 40), 0)
    if grid35 == 1:
        pygame.draw.rect(DS, RED, (161, 121, 40, 40), 0)
    if grid36 == 1:
        pygame.draw.rect(DS, RED, (201, 121, 40, 40), 0)
    if grid37 == 1:
        pygame.draw.rect(DS, RED, (241, 121, 40, 40), 0)
    if grid38 == 1:
        pygame.draw.rect(DS, RED, (281, 121, 40, 40), 0)
    if grid39 == 1:
        pygame.draw.rect(DS, RED, (321, 121, 40, 40), 0)
    if grid40 == 1:
        pygame.draw.rect(DS, RED, (361, 121, 40, 40), 0)
    if grid41 == 1:
        pygame.draw.rect(DS, RED, (1, 161, 40, 40), 0)
    if grid42 == 1:
        pygame.draw.rect(DS, RED, (41, 161, 40, 40), 0)
    if grid43 == 1:
        pygame.draw.rect(DS, RED, (81, 161, 40, 40), 0)
    if grid44 == 1:
        pygame.draw.rect(DS, RED, (121, 161, 40, 40), 0)
    if grid45 == 1:
        pygame.draw.rect(DS, RED, (161, 161, 40, 40), 0)
    if grid46 == 1:
        pygame.draw.rect(DS, RED, (201, 161, 40, 40), 0)
    if grid47 == 1:
        pygame.draw.rect(DS, RED, (241, 161, 40, 40), 0)
    if grid48 == 1:
        pygame.draw.rect(DS, RED, (281, 161, 40, 40), 0)
    if grid49 == 1:
        pygame.draw.rect(DS, RED, (321, 161, 40, 40), 0)
    if grid50 == 1:
        pygame.draw.rect(DS, RED, (361, 161, 40, 40), 0)
    if grid51 == 1:
        pygame.draw.rect(DS, RED, (1, 201, 40, 40), 0)
    if grid52 == 1:
        pygame.draw.rect(DS, RED, (41, 201, 40, 40), 0)
    if grid53 == 1:
        pygame.draw.rect(DS, RED, (81, 201, 40, 40), 0)
    if grid54 == 1:
        pygame.draw.rect(DS, RED, (121, 201, 40, 40), 0)
    if grid55 == 1:
        pygame.draw.rect(DS, RED, (161, 201, 40, 40), 0)
    if grid56 == 1:
        pygame.draw.rect(DS, RED, (201, 201, 40, 40), 0)
    if grid57 == 1:
        pygame.draw.rect(DS, RED, (241, 201, 40, 40), 0)
    if grid58 == 1:
        pygame.draw.rect(DS, RED, (281, 201, 40, 40), 0)
    if grid59 == 1:
        pygame.draw.rect(DS, RED, (321, 201, 40, 40), 0)
    if grid60 == 1:
        pygame.draw.rect(DS, RED, (361, 201, 40, 40), 0)
    if grid61 == 1:
        pygame.draw.rect(DS, RED, (1, 241, 40, 40), 0)
    if grid62 == 1:
        pygame.draw.rect(DS, RED, (41, 241, 40, 40), 0)
    if grid63 == 1:
        pygame.draw.rect(DS, RED, (81, 241, 40, 40), 0)
    if grid64 == 1:
        pygame.draw.rect(DS, RED, (121, 241, 40, 40), 0)
    if grid65 == 1:
        pygame.draw.rect(DS, RED, (161, 241, 40, 40), 0)
    if grid66 == 1:
        pygame.draw.rect(DS, RED, (201, 241, 40, 40), 0)
    if grid67 == 1:
        pygame.draw.rect(DS, RED, (241, 241, 40, 40), 0)
    if grid68 == 1:
        pygame.draw.rect(DS, RED, (281, 241, 40, 40), 0)
    if grid69 == 1:
        pygame.draw.rect(DS, RED, (321, 241, 40, 40), 0)
    if grid70 == 1:
        pygame.draw.rect(DS, RED, (361, 241, 40, 40), 0)
    if grid71 == 1:
        pygame.draw.rect(DS, RED, (1, 281, 40, 40), 0)
    if grid72 == 1:
        pygame.draw.rect(DS, RED, (41, 281, 40, 40), 0)
    if grid73 == 1:
        pygame.draw.rect(DS, RED, (81, 281, 40, 40), 0)
    if grid74 == 1:
        pygame.draw.rect(DS, RED, (121, 281, 40, 40), 0)
    if grid75 == 1:
        pygame.draw.rect(DS, RED, (161, 281, 40, 40), 0)
    if grid76 == 1:
        pygame.draw.rect(DS, RED, (201, 281, 40, 40), 0)
    if grid77 == 1:
        pygame.draw.rect(DS, RED, (241, 281, 40, 40), 0)
    if grid78 == 1:
        pygame.draw.rect(DS, RED, (281, 281, 40, 40), 0)
    if grid79 == 1:
        pygame.draw.rect(DS, RED, (321, 281, 40, 40), 0)
    if grid80 == 1:
        pygame.draw.rect(DS, RED, (361, 281, 40, 40), 0)
    if grid81 == 1:
        pygame.draw.rect(DS, RED, (1, 321, 40, 40), 0)
    if grid82 == 1:
        pygame.draw.rect(DS, RED, (41, 321, 40, 40), 0)
    if grid83 == 1:
        pygame.draw.rect(DS, RED, (81, 321, 40, 40), 0)
    if grid84 == 1:
        pygame.draw.rect(DS, RED, (121, 321, 40, 40), 0)
    if grid85 == 1:
        pygame.draw.rect(DS, RED, (161, 321, 40, 40), 0)
    if grid86 == 1:
        pygame.draw.rect(DS, RED, (201, 321, 40, 40), 0)
    if grid87 == 1:
        pygame.draw.rect(DS, RED, (241, 321, 40, 40), 0)
    if grid88 == 1:
        pygame.draw.rect(DS, RED, (281, 321, 40, 40), 0)
    if grid89 == 1:
        pygame.draw.rect(DS, RED, (321, 321, 40, 40), 0)
    if grid90 == 1:
        pygame.draw.rect(DS, RED, (361, 321, 40, 40), 0)
    if grid91 == 1:
        pygame.draw.rect(DS, RED, (1, 361, 40, 40), 0)
    if grid92 == 1:
        pygame.draw.rect(DS, RED, (41, 361, 40, 40), 0)
    if grid93 == 1:
        pygame.draw.rect(DS, RED, (81, 361, 40, 40), 0)
    if grid94 == 1:
        pygame.draw.rect(DS, RED, (121, 361, 40, 40), 0)
    if grid95 == 1:
        pygame.draw.rect(DS, RED, (161, 361, 40, 40), 0)
    if grid96 == 1:
        pygame.draw.rect(DS, RED, (201, 361, 40, 40), 0)
    if grid97 == 1:
        pygame.draw.rect(DS, RED, (241, 361, 40, 40), 0)
    if grid98 == 1:
        pygame.draw.rect(DS, RED, (281, 361, 40, 40), 0)
    if grid99 == 1:
        pygame.draw.rect(DS, RED, (321, 361, 40, 40), 0)
    if grid100 == 1:
        pygame.draw.rect(DS, RED, (361, 361, 40, 40), 0)
    #pygame.draw.rect(DS, YELLOW, (x, y, 10, 10), 0)
    pygame.display.update()
    losstime += 1
    fpsClock.tick(FPS)
print(str(score)) 
pygame.quit()
sys.exit()
