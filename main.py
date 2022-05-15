#Football Menager Game
from random import randint
from time import sleep
from os import system, name
teamRatingHome = 0  # home team odds f.e. from livescore.com

teamRatingAway = 15  # away team odds f.e. from livescore.com
teamHomeScore = (15 - teamRatingHome) *2
teamAwayScore = (15 - teamRatingAway) *2
shootChance = 50  #percentage chanc e to hoot
hitChance = 50
shootAttempt = None  # randomize chance to shoot from your position, if > than shootChance then footballer shoots
saveChance = 40  # percentage chance to save a shoot
saveAttempt = None  # randomize chance to save a shoot, if > than saveChance than shoot is saved
textWhere = ''
textZone = ''
text3 = ''
textTimer = ''
text = 0
ballMove = 5
matchHalfLenght = 45  #first half time
timeSecondHalf = 45  #second thalf time
teamHome = 'Real Madryt'
teamAway = 'Liverpol FC'
ballPosesion = teamHome
ballNotPossesion = teamAway
playTest = None
extraTime = randint(2,4)
extraTime2 = randint(3,8)
pitchZone = [
    'Pole karne '+teamHome, 'Granica pola karnego '+teamHome, 'Połowa '+teamHome, 'Środek boiska',
    'Połowa '+teamAway, 'Granica pola karnego '+teamAway, 'Pole karne '+teamAway
]
firstHalf = True
secondHalf = False
timer = 0
ballPosition = 3
playChance = 85
scoreHome = 0
scoreAway = 0
possesionChange = None
goalScored = False
goals = [] 
ballGraph = '@'
skipSomeIf = False # this variable helps to skip loops after goal
skipFirstIf = False
print('Rozpoczynamy mecz pomiędzy ',teamHome,' a ',teamAway,'!')
print('Spotkanie rozpocznie druzyna gospodarzy')
sleep(2)
def clear():
  _ = system('clear')
clear()
def time():
  global timer, matchHalfLenght
  
  #sleep(1)
  timer += 1
  #clear()
  matchHalfLenght -= 1



line1 =  ('------------------------------------------------------------------------------------')
line2 =  ('|                                        |                                         |')
line3 =  ('|                                        |                                         |')
line4 =  ('|----------                              |                               ----------|')
line5 =  ('|         |                            --|--                             |         |')
line6 =  ('|         |                          -   |    -                          |         |')
line7 =  ('|-        |-                       -     |      -                       -|        -|')
line8 =  ('| |       | -                    -       |        -                    - |       | |')
line9 =  ('| |       |  -                  -        o         -                  -  |       | |')
line10 = ('| |       | -                    -       |        -                    - |       | |')
line11 = ('|-        |-                       -     |      -                       -|        -|')
line12 = ('|         |                          -   |    -                          |         |')
line13 = ('|         |                            --|--                             |         |')
line14 = ('|----------                              |                               ----------|')
line15 = ('|                                        |                                         |')
line16 = ('|                                        |                                         |')
line17 = ('------------------------------------------------------------------------------------')


xMin = 41
xMax = 41
yMin = 9
yMax = 9
goalkeeperCatched = False
while matchHalfLenght > 0:
  skipSomeIf = False # means that no goal yet
  
  
 

  
  
  
  
  #sleep(0.8)
  playTest = randint(1,100)
  
  if ballPosesion == teamHome:
    teamsRating = teamHomeScore
    ballNotPossesion = teamAway
  else:
    ballNotPossesion = teamHome
    teamsRating = teamAwayScore
  #print(playChance,teamsRating, playTest)
  
                                            #rozgrywka

 
  if goalScored is True:
    print(ballPosesion,' rozpoczyna grę od środka')
    possesionChange = True
    goalScored = False
    skipFirstIf = True
    skipSomeIf = True
    time()
  #print(ballPosition,'                                 POZYCJA')
  if (ballPosition == 0 and ballPosesion == teamAway) or (ballPosition == 6 and ballPosesion == teamHome) and skipFirstIf is False:
      if (shootChance + teamsRating) >= playTest:
        print(ballPosesion,'Strzela!')
        playTest = randint(1,100)
        if (hitChance + teamsRating) >= playTest:
          playTest = randint(1,100)
          
          if ballPosesion == teamHome :
            saveChance += teamHomeScore
          else:
            saveChance += teamAwayScore
          print('jeśli ',saveChance,' jest większe od ',playTest,' to gol')
          if saveChance >= playTest:
            print('GOOOOOOOL DLA',ballPosesion)
            goal = ballPosesion +'',str(timer)
            
            goals.append(goal)
            goalScored = True
            ballPosition = 3
            skipSomeIf = True # skips next if's from 120 line
            saveChance = 40
            if ballPosesion == teamHome:
              scoreHome += 1
             
            else:
              scoreAway += 1
              
            sleep(2)
            ballPosesion = ballNotPossesion
            
            
            
            time()
            
              
          else:
            print('Bramkarz drużyny',ballNotPossesion,'Chwyta piłkę')
            print('Bramkarz zaczyna wybiciem od bramki')
            sleep(3)
            goalkeeperCatched = True
            ballPosition = 3
            skipSomeIf = True
            time()
        else:
          print('Piłka nie trafia w światło bramki')
          print('Bramkarz zaczyna wybiciem od bramki')
          sleep(3)
          ballPosition = 3
          skipSomeIf = True
          time()
          
            
      else:
        playTest = randint(1,100)
        if playTest > 50 :
          text3 = (ballNotPossesion,' Wybija piłkę!' )
          ballPosition = 3
        elif playTest <= 50 :
          textZone = (ballPosesion,'traci piłkę, przejmuję ją',ballNotPossesion)
          ballPosesion = ballNotPossesion
          
          
          possesionChange = True
          skipSomeIf = True
          playChance = 85 
          
          time()
  #print(teamsRating+playChance, teamHomeScore, teamAwayScore)
  clear()
  if (playChance + teamsRating) >= playTest and skipSomeIf is False and skipFirstIf is False:
    if ballPosition == 3:
      playChance = 85
    elif ballPosition == 2 or ballPosition == 4:
      playChance = 65
    elif ballPosition == 1 or ballPosition == 5:
      playChance = 40
    elif possesionChange is True:
      playChance = 70
    possesionChange = False
    if ballPosesion == teamAway:
      ballPosition -= 1
    else:
      ballPosition += 1
    
    

      
    textZone = (ballPosesion,'przechodzi do strefy',pitchZone[ballPosition])
    playChance -= 20
    playTest = randint(1,100)
    time()
  
  else :
    if skipSomeIf is False:
      textZone = (ballPosesion,'traci piłkę, przejmuję ją',ballNotPossesion)
      ballPosesion = ballNotPossesion
      
      
      possesionChange = True
      playChance = 85
      time()
  
  
  

  

  while ballMove > 1:
    
    if ballPosition == 3 :
      xMin = 35
      xMax = 47
    elif ballPosition == 2:
      xMin = 20
      xMax = 35
    elif ballPosition == 1:
      xMin = 11
      xMax = 20
    elif ballPosition == 0:
      xMin = 3
      xMax = 11
    elif ballPosition == 4:
      xMin = 45
      xMax = 62
    elif ballPosition == 5:
      xMin = 63
      xMax = 73
    elif ballPosition == 6:
      xMin = 74
      xMax = 78
    if ballMove == 5:
      xx = randint(xMin,xMax)
      yy = randint(yMin,yMax)
    if goalScored is True or secondHalf:
      x = 41
      y = 9
    else:
      x = randint(xx-1,xx+1)
      y = randint(yy-1,yy+1)
    
      
    
    if y > 17: 
      y = 15
    if y < 2:
      y = 3
  
    
    if goalkeeperCatched == True :
      x = 80
      y = 9
  
  
  
    if y == 2:
      line2 = line2[:x] + ballGraph + line2[x+1:]
    elif y == 3:
      line3 = line3[:x] + ballGraph + line3[x+1:]
    elif y == 4:
      line4 = line4[:x] + ballGraph + line4[x+1:]
    elif y == 5:
      line5 = line5[:x] + ballGraph + line5[x+1:]
    elif y == 6:
      line6 = line6[:x] + ballGraph + line6[x+1:]
    elif y == 7:
      line7 = line7[:x] + ballGraph + line7[x+1:]
    elif y == 8:
      line8 = line8[:x] + ballGraph + line8[x+1:]
    elif y == 9:
      line9 = line9[:x] + ballGraph + line9[x+1:]
    elif y == 10:
      line10 = line10[:x] + ballGraph + line10[x+1:]
    elif y == 11:
      line11 = line11[:x] + ballGraph + line11[x+1:]
    elif y == 12:
      line12 = line12[:x] + ballGraph + line12[x+1:]
    elif y == 13:
      line13 = line13[:x] + ballGraph + line13[x+1:]
    elif y == 14:
      line14 = line14[:x] + ballGraph + line14[x+1:]
    elif y == 15:
      line15 = line15[:x] + ballGraph + line15[x+1:]
    elif y == 16:
      line16 = line16[:x] + ballGraph + line16[x+1:]
    ballMove -= 1
    print ('                 ',teamHome, scoreHome,'          :        ',scoreAway, teamAway)
    if ballPosesion == teamHome:
      print('                  =============')
    else:
      print('                                                    ==============')
    print('                                    ',timer,'minuta')
    print(line1)       #football pitch
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
    print(line8)
    print(line9)
    print(line10)
    print(line11)
    print(line12)
    print(line13)
    print(line14)
    print(line15)
    print(line16)
    print(line17)
    if goalScored is True:
      print(ballPosesion,'rozpocznie grę z środka boiska')
    if timer == 45 and firstHalf:
    
      matchHalfLenght += extraTime
      print("Sędzia doliczył ",extraTime-1,'minuty!')
    if timer == 45+extraTime and firstHalf:
      print('Wynik pierwszej połowy:\n ',teamHome, scoreHome,'\n',teamAway, scoreAway)
      print(goals)
      sleep(3)
      print('Rozpoczynamy drugą połowę')
      secondHalf = True
      firstHalf = False
      timer = 45
      matchHalfLenght = 45
    
    
    if timer == 90:
      matchHalfLenght += extraTime2
      print("Sędzia doliczył ",extraTime2-1,'minuty!')
    
    if goalkeeperCatched is False and goalScored is False and skipFirstIf is False:
      print(' '.join(textZone))
    if skipFirstIf is False and goalScored is False:
      print('Piłka znajduje się w:',pitchZone[ballPosition])
    print(' '.join(text3))
    if timer == 0:
      print(teamHome,'rozpoczyna spotkanie z środka boiska')
    sleep(1)
    
    line1 =  ('------------------------------------------------------------------------------------')
    line2 =  ('|                                        |                                         |')
    line3 =  ('|                                        |                                         |')
    line4 =  ('|----------                              |                               ----------|')
    line5 =  ('|         |                            --|--                             |         |')
    line6 =  ('|         |                          -   |    -                          |         |')
    line7 =  ('|-        |-                       -     |      -                       -|        -|')
    line8 =  ('| |       | -                    -       |        -                    - |       | |')
    line9 =  ('| |       |  -                  -        o         -                  -  |       | |')
    line10 = ('| |       | -                    -       |        -                    - |       | |')
    line11 = ('|-        |-                       -     |      -                       -|        -|')
    line12 = ('|         |                          -   |    -                          |         |')
    line13 = ('|         |                            --|--                             |         |')
    line14 = ('|----------                              |                               ----------|')
    line15 = ('|                                        |                                         |')
    line16 = ('|                                        |                                         |')
    line17 = ('------------------------------------------------------------------------------------')
    if ballMove != 1:
      clear()
  ballMove = 5
  text3 = ''
  goalkeeperCatched = False
  skipFirstIf = False
  
  
print(line1)       #football pitch
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
print(line8)
print(line9)
print(line10)
print(line11)
print(line12)
print(line13)
print(line14)
print(line15)
print(line16)
print(line17)   
print('Sędzia gwiżdże po raz ostatni!!! Koniec spotkania')
print('Wynik całego meczu:\n ',teamHome, scoreHome,'\n',teamAway, scoreAway)
print(goals)
 

