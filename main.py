#Football Menager Game
from random import randint
from time import sleep

teamRatingHome = 1.2  # home team odds f.e. from livescore.com

teamRatingAway = 7.1  # away team odds f.e. from livescore.com
teamHomeScore = (10 - teamRatingHome) *3
teamAwayScore = (10 - teamRatingAway) *3
shootChance = 50  #percentage chanc e to hoot
hitChance = 50
shootAttempt = None  # randomize chance to shoot from your position, if > than shootChance then footballer shoots
saveChance = 40  # percentage chance to save a shoot
saveAttempt = None  # randomize chance to save a shoot, if > than saveChance than shoot is saved

matchHalfLenght = 45  #first half time
timeSecondHalf = 45  #second thalf time
teamHome = 'Real Madrid'
teamAway = 'FC Barcelona'
ballPosesion = teamHome
ballNotPossesion = teamAway
playTest = None
extraTime = 0
extraTime2 = 0
pitchZone = [
    'Pole karne '+teamHome, 'Granica pola karnego '+teamHome, 'Połowa '+teamHome, 'Środek boiska',
    'Połowa '+teamAway, 'Granica pola karnego '+teamAway, 'Pole karne '+teamAway
]

timer = 1
ballPosition = 3
playChance = 70
scoreHome = 0
scoreAway = 0
possesionChange = None
goals = []
print('Rozpoczynamy mecz pomiędzy ',teamHome,' a ',teamAway,'!')
print('Spotkanie rozpocznie druzyna gospodarzy')

while matchHalfLenght > 0:


  print('Aktualnie gra toczy się na : ',pitchZone[ballPosition])
  #sleep(0.1)
  playTest = randint(1,100)
  
  if ballPosesion == teamHome:
    teamsRating = teamHomeScore
    ballNotPossesion = teamAway
  else:
    ballNotPossesion = teamHome
    teamsRating = teamAwayScore
  #print(playChance,teamsRating, playTest)
  
                                            #rozgrywka
  
  #print(ballPosition,'                                 POZYCJA')
  if (playChance + teamsRating) >= playTest:
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
    
    if ballPosition == 0 or ballPosition == 6 :
      if (shootChance + teamsRating) >= playTest:
        print(ballPosesion,'Strzela!')
        playTest = randint(1,100)
        if (hitChance + teamsRating) >= playTest:
          playTest = randint(1,100)
          if saveChance >= playTest:
            print('GOOOOOOOL DLA',ballPosesion)
            goal = ballPosesion +'',str(timer)
            goals.append(goal)
            ballPosition = 3
            if ballPosesion == teamHome:
              scoreHome += 1
            else:
              scoreAway += 1
              
            ballPosesion = ballNotPossesion
            print(ballPosesion,' rozpoczyna grę od środka')
            possesionChange = True
              
          else:
            print('Bramkarz drużyny',ballNotPossesion,'Chwyta piłkę')
            print('Bramkarz zaczyna wybiciem od bramki')
            ballPosition = 3
        else:
          print('Piłka nie trafia w światło bramki')
          print('Bramkarz zaczyna wybiciem od bramki')
          ballPosition = 3
            
      else:
        print(ballNotPossesion,' Wybija piłkę!' )
        ballPosition = 3

      
    print(ballPosesion,' przechodzi do strefy',pitchZone[ballPosition])
    playChance -= 20
    playTest = randint(1,100)
  
  else:
    print(ballPosesion,' Traci piłkę')
    ballPosesion = ballNotPossesion
    print('Piłkę przejmuje', ballPosesion)
    possesionChange = True
  
  
  
  print('',timer,'minuta spotkania')
  matchHalfLenght -= 1
  timer += 1
  if timer == 45:
    extraTime = randint(1,5)
    matchHalfLenght += extraTime
    print("Sędzia doliczył ",extraTime,'minuty!')
  if timer == 45+extraTime:
    print('Wynik pierwszej połowy:\n ',teamHome, scoreHome,'\n',teamAway, scoreAway)
    print(goals)
    
    sleep(3)
    print('Rozpoczynamy drugą połowę')
    
    matchHalfLenght = 45
    
    
  if timer == 90:
    extraTime2 = randint(1,5)
    matchHalfLenght += extraTime2
    print("Sędzia doliczył ",extraTime2,'minuty!')
print('Sędzia gwiżdże po raz ostatni!!! Koniec spotkania')
print('Wynik całego meczu:\n ',teamHome, scoreHome,'\n',teamAway, scoreAway)
print(goals)
 

