import random
import time

#Create a list of voters
people = []

#Create a list of candidates
candidates = [["A",0], ["B",0], ["C",0], ["D",0], ["E",0]]
averages = []
totalAverage = 0
hate_averages=[]
hateTotalAverage=0
#---------------------------------------------------------------------------------------
#print votes in graph form
def print_votes(votes, candidates, numberOfVoters):
  total_votes = 0
  for i in range(len(votes)):
    total_votes += votes[i]
  for i in range(len(candidates)):
    graph = int(votes[i] / (total_votes/100))*("-")
    print(candidates[i][0]+":"+graph)
  print()

#create new candidates   
def newcandidates():
  for i in range(5):
    candidates[i][1] = random.randint(1, 15)
  for i in range(len(candidates)): #This is to make sure two candidates aren't the same
    for j in range(len(candidates)):
      if(candidates[i][0] != candidates[j][0]):
        if(candidates[i][1] == candidates[j][1]):
          candidates[j][1] = random.randint(1,10)

#calculate the average happiness of the voters  
def calcHappiness(winner, numberOfVoters):
  print()
  winningCandidateNum = candidates[winner][1]
  averageDifference = 0
  for i in range(numberOfVoters):
    difference = abs(people[i]-winningCandidateNum)
    averageDifference += difference
  averageDifference = averageDifference/numberOfVoters
  print("Average Difference: " + str(round(averageDifference,2)))
  if averageDifference < 2:
    print("The voters are extremely happy with their leader!")
  elif 2>= averageDifference <3:
    print("The voters are very happy with their leader!")
  elif averageDifference >=3 and averageDifference<4:
    print("The voters are happy with their leader!")
  elif averageDifference >= 4 and averageDifference<5: 
    print("The voters are ok with their leader.")
  elif averageDifference <= 5 and averageDifference<6:
    print("The voters are unhappy with their leader.")
  elif averageDifference <= 6 and averageDifference<7:
    print("The voters are very uhappy with their leader")
  elif averageDifference >= 7:
    print("The voters are extremely unhappy with their leader")
  return averageDifference

#calculate the percentage of the population that is very unhappy with the leader
def calcHate(winner, numberOfVoters):
  winningCandidateNum = candidates[winner][1]
  numberofhaters = 0
  for i in range(numberOfVoters):
    difference = abs(people[i] - winningCandidateNum)
    if difference >= 7:
      numberofhaters += 1
  hatePercentage = (numberofhaters/numberOfVoters)*100
  print(str(round(hatePercentage,2))+"% of the population is extremely unhappy with their leader.")
  return hatePercentage
  
  
#-------------------------------------------------------------------------------------
#First Past the Post System: 
#vote for 1, winner takes all
def firstpastthepost(numberOfVoters):
  
  print("Generating voters...\n")
  for i in range(numberOfVoters):
    people.append(random.randint(1, 15))
  
  print("\nCounting votes for First past the post...\n")
  votes_for_candidates = [0,0,0,0,0,0,0,0,0,0]
  myVote = 0
  for i in range(numberOfVoters): #Each 'i' is a voter
    leastDifference = 10
    myVote = 0
    for j in range(len(candidates)): #Each 'j' is a candidate
      
      #Finds the difference between the voter and candidate
      difference = abs(people[i] - candidates[j][1]) 
      
      if difference < leastDifference:
        placeholder = j
        leastDifference = difference      
    
    myVote = placeholder
    votes_for_candidates[myVote] += 1

  maximum = 0
  for i in range(len(votes_for_candidates)):
    if votes_for_candidates[i] > maximum:
      maximum = votes_for_candidates[i]
      winner = i
  
  print_votes(votes_for_candidates, candidates, numberOfVoters)
  print(candidates[winner][0] + " has won the election!")
  votes_for_candidates = [0,0,0,0,0,0,0,0,0,0]
  print()
  a = calcHappiness(winner,numberOfVoters)
  averages.append(a)
  h = calcHate(winner,numberOfVoters)
  hate_averages.append(h)
  people.clear()

#---------------------------------------------------------------------------------------
#Two Round System:
#vote for 1, top 2 candidates go to a second round
def tworoundsystem(numberOfVoters):
  print("Generating voters...\n")
  for i in range(numberOfVoters):
    people.append(random.randint(1, 15))
  
  print("\nCounting votes for Two round system...\n")
  votes_for_candidates = [0,0,0,0,0,0,0,0,0,0]
  myVote = 0
  for i in range(numberOfVoters):
    leastDifference = 10
    myVote = 0
    for j in range(len(candidates)):
      difference = abs(people[i] - candidates[j][1])
      
      if(difference < leastDifference):
        placeholder = j
        leastDifference = difference
        
    
    myVote = placeholder
    votes_for_candidates[myVote] += 1

  firstPlace = 0;
  secondPlace = 0;
  firstplace_index = 0
  for i in range(len(votes_for_candidates)):
    if(votes_for_candidates[i] > secondPlace):
      if(votes_for_candidates[i] > firstPlace):
        secondPlace = firstPlace
        almostwinner = firstplace_index
        firstPlace = votes_for_candidates[i]
        firstplace_index = i
        winner = i
        
      else:
        secondPlace = votes_for_candidates[i]
        almostwinner = i
  print_votes(votes_for_candidates, candidates, numberOfVoters)
  print(candidates[winner][0] + " has won the first election!")
  print(candidates[almostwinner][0] + " got second place in the first election!")
  
  secondroundcandidates = [candidates[winner],candidates[almostwinner]]
  votes_for_candidates = [0,0]
  myVote = 0
  for i in range(int(numberOfVoters*0.95)):
    leastDifference = 10
    myVote = 0
    for j in range(len(secondroundcandidates)):
      difference = abs(people[i] - secondroundcandidates[j][1])
      
      if difference < leastDifference:
        placeholder = j
        leastDifference = difference
        
    
    myVote = placeholder
    votes_for_candidates[myVote] += 1
  maximum2 = 0
  for i in range(len(votes_for_candidates)):
    if(votes_for_candidates[i] > maximum2):
      maximum2 = votes_for_candidates[i]
      winner = i

  print_votes(votes_for_candidates,secondroundcandidates,numberOfVoters)
  print(secondroundcandidates[winner][0] + " has won the election!\n")
  print("But, only 95% of the population voted in the second election.")
  a = calcHappiness(winner, numberOfVoters)
  averages.append(a)
  h = calcHate(winner,numberOfVoters)
  hate_averages.append(h)
  people.clear()
#--------------------------------------------------------------------------------------
#Approval voting:
#vote for as many as you want
def approval(numberOfVoters,vote_range):
  print("Generating voters...\n")
  for i in range(numberOfVoters):
    people.append(random.randint(1, 15))
  
  print("\nCounting votes for Approval voting...\n")
  votes_for_candidates = [0,0,0,0,0,0,0,0,0,0]
  myVote = 0

  for i in range(numberOfVoters):
    for j in range(len(candidates)):
      difference = abs(people[i]-candidates[j][1])
      
      if difference < vote_range:
        votes_for_candidates[j] += 1
        
        
   
  print_votes(votes_for_candidates, candidates, numberOfVoters)  

  maximum = 0
  for i in range(len(votes_for_candidates)):
    if votes_for_candidates[i] > maximum:
      maximum = votes_for_candidates[i]
      winner = i
  print(candidates[winner][0] + " has won the election!")
  votes_for_candidates = [0,0,0,0,0,0,0,0,0,0]
  print()
  a = calcHappiness(winner, numberOfVoters)
  averages.append(a)
  h = calcHate(winner,numberOfVoters)
  hate_averages.append(h)
  people.clear()
      
#-------------------------------------------------------------------------------------
#Borda Count:
#rank all candidates, candidates get points depending on their rank, most points wins
def bordacount(numberOfVoters):
  print("Generating voters...\n")
  for i in range(numberOfVoters):
    people.append(random.randint(1, 15))
  
  print("\nCounting votes for Borda count...\n")
  differences = []
  votes_for_candidates = [0,0,0,0,0,0,0,0,0,0]

  for i in range(numberOfVoters):
    differences = []

    for j in range(len(candidates)):
      difference = abs(people[i] - candidates[j][1])
      candidate = [difference, candidates[j][0]]
      differences.append(candidate)
    differences=sorted(differences)
    n = 1

    for k in range(len(differences)):
      for a in range(len(candidates)):
        if differences[k][1] == candidates[a][0]:
          votes_for_candidates[a] += 10-n
      n+=1
      
  print_votes(votes_for_candidates, candidates, numberOfVoters)
  maximum = 0
  for i in range(len(votes_for_candidates)):      
    if votes_for_candidates[i] > maximum:
      maximum = votes_for_candidates[i]
      winner = i
  print(candidates[winner][0] + " has won the election!")
  a = calcHappiness(winner, numberOfVoters)
  averages.append(a)
  h = calcHate(winner, numberOfVoters)
  hate_averages.append(h)
  people.clear()
#--------------------------------------------------------------------------------------
#Elimination
#vote least favorite, one candidate gets eliminated every round, go until one left
def elimination(numberOfVoters):
  print("Generating voters...\n")
  for i in range(numberOfVoters):
    people.append(random.randint(1, 15))
  
  print("\nCounting votes for elimination...\n")
  copyCandidates = candidates.copy()
  votes_for_candidates = [0,0,0,0,0,0,0,0,0,0]
  rounds=1
  while len(copyCandidates) > 1:
    myVote=0

    for i in range(int(numberOfVoters*rounds)):
      mostDifference = 0
      myVote=0
      for j in range(len(copyCandidates)):
        difference = abs(people[i] - copyCandidates[j][1])
        
        if difference > mostDifference:
          placeholder = j
          mostDifference = difference      
      
      myVote = placeholder
      votes_for_candidates[myVote] += 1

    maximum=0
    for i in range(len(votes_for_candidates)):
      if votes_for_candidates[i] > maximum:
        maximum = votes_for_candidates[i]
        loser = i
    rounds-=0.15
    print_votes(votes_for_candidates, copyCandidates,numberOfVoters)
    print(copyCandidates[loser][0]+ " has been eliminated!")
    print("But, only "+str(round(rounds*100,1))+"% of the population voted.")
    
    votes_for_candidates.remove(maximum)
    
    copyCandidates.remove(copyCandidates[loser])
    

  for i in range(len(candidates)):
    if(copyCandidates[0][0] == candidates[i][0]):
      winner = i
  votes_for_candidates = [0,0,0,0,0,0,0,0,0,0]
  print()
  print(candidates[winner][0] + " has won the election!")
  a = calcHappiness(winner, numberOfVoters)
  averages.append(a)
  h = calcHate(winner, numberOfVoters)
  hate_averages.append(h)
  people.clear()
#-------------------------------------------------------------------------------------
#Main Loop
q=False
while not(q):
  answer = input("Which voting system do you want to test:\n 1: 1st Past the Post\n 2: Two Round System \n 3: Approval Voting\n 4: Borda Count\n 5: Elimination\n(Type q to quit)\n(Type h for help)\n(Type a for analysis)\n")
  if answer == "q":
    q = True
    break
  if answer=="h":
    print("This is a program that allows you to simulate different voting systems in elections!")
    print("This program currently supports these 5 voting systems:")
    print("First past the post: Vote for 1 candidate, top candidate wins.")
    print("Two round system: Vote for 1 candidate, top 2 candidates go to a runoff.")
    print("Approval voting: Vote for as many as you want, top candidate wins.")
    print("Borda count: Rank all candidates, candidates get points depending on your rankings, top candidate wins.")
    print("Elimination: Vote for worst candidate, worst candidate gets eliminated, keep going until only one candidate left.")
    print("After you choose the voting system, you can choose how many people are going to vote in the election. Maximum is 1 million so that it does not take too long to run the simulation.")
    print("After that, the simulation will run. After every election occurs, a graph will appear, showing the candidates and using lines to represent how many votes they got. Longer line, more votes.")
    print("After the graph, you will see who won the election. After that, it will display the average difference between the voters and the candidate. The higher the difference, the farther away the candidate is from the voter in terms of political views. Lower average difference means the population will overall be happier. Then, it will display the percentage of the population that is extremely unhappy with their leader. These are the voters that had a difference of 7 or more from the candidate. Lower percentage is better, because it means less people that really hate the leader. Finally, after all of the elections are over, it will show you the total average difference across all elections, the total average hate across all elections, and the general happiness or unhappiness of the voters across all elections based on the average difference.")
    print("And that's it! We hope you enjoy, and have fun :) (Press Enter to Reset)")
    input()
    q=True
    break
  if answer=="a":
    print("The worst voting method is first past the post.")
    print("It has high average differences and high percentages of hate. Especially with many candidates, it only represents a small percentage of the population. It's only advantage is that it is simple.")
    print("\nSimilar to first past the post is the two round system.")
    print("It is basically first past the post with an added runoff election. This can vary the results a little bit, sometimes it is better, but sometimes it is worse, but also not all of the population votes in the runoff election, which is worse. Overall, it is similar to first past the post, but still far inferior to the other 3 voting methods.")
    print("\nElimination is the third best voting method, and approval voting is the second best. Elimination actually has significantly lower average differences and average hate percentage, but, unfortuantly, elimation has one major flaw. You have to vote in many, many elections to get the final result. This means that the voting population is very low, and in the real world, it would probably be even lower. People don't want to vote in 10 different elections just to decide one leader. When people see that only 20% of the population is voting in the election, that makes them not want to vote. This is why approval voting is better than elimination. But, both of these voting methods had much better results than first past the post and the two round system all")
    print("\nBorda Count is the best out of all of the voting methods, with the lowest average political difference between voters, the lowest unhappiness, and a 100% voter turnout. Borda Count is the undeniable winner of these 5 voting methods.")
    print()
    print("Here are the statistics from our simulations, but you are free to try as much as you like.")
    print("All of these are 100 elections, with 100k voters in each.")
    print()
    print("First past the post: \nAverage difference: 4.63\nAverage hate: 28.21% of the population\nVoting: Perfect\nThe voters are ok with their leader.")
    print()
    print("Two round system: \nAverage difference: 4.96\nAverage hate: 31.73% of the population\nVoting: Almost perfect\nThe voters are ok with their leader. ")
    print()
    print("Approval voting: \nAverage difference : 4.34\nAverage hate: 24.63% of the population\nVoting: Perfect\nThe voters are ok with their leader.")
    print()
    print("Elimination: \nAverage difference: 4.07\nAverage hate: 20.06% of the population\nVoting: Low\nThe voters are ok with their leader.")
    print()
    print("Borda count: \nAverage difference: 3.92\nAverage hate: 16.66% of the population\nVoting: Perfect\nThe voters are happy with their leader.")
    print()
    print("Press enter to reset.")
    input()
    break
  num = input("How many people are participating in the election?(maximum 1 million)")
  num = int(num)
  times = int(input("How many elections do you want to simulate? "))
  for i in range(times):

    if answer == "1":
      newcandidates()
      firstpastthepost(num)
    elif answer == "2":
      newcandidates()
      tworoundsystem(num)
    elif answer == "3":
      newcandidates()
      approval(num, 3)
    elif answer== "4" :
      newcandidates()
      bordacount(num)
    elif answer == "5":
      newcandidates()
      elimination(num)
  for j in range(len(averages)):
    totalAverage += averages[j]
  totalAverage = totalAverage/times
  for k in range(len(hate_averages)):
    hateTotalAverage += hate_averages[k]
  hateTotalAverage = hateTotalAverage/times
  print()
  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
  time.sleep(0.5)
  print("Total average difference: "+str(round(totalAverage,2)))
  time.sleep(0.5)
  if totalAverage<2:
    print("The voters are extremely happy with their leader!")
  elif totalAverage>=2 and totalAverage<3:
    print("The voters are very happy with their leader!")
  elif totalAverage>=3 and totalAverage<4:
    print("The voters are happy with their leader!")
  elif totalAverage>=4 and totalAverage<=5:
    print("The voters are ok with their leader.")
  elif totalAverage>=5 and totalAverage<6:
    print("The voters are unhappy with their leader.")
  elif totalAverage>=6 and totalAverage<7:
    print("The voters are very unhappy with their leader")
  elif totalAverage>7:
    print("The voters are extremely unhappy with their leader")
  time.sleep(0.5)
  print("Total average hate: "+str(round(hateTotalAverage,2))+"% of the population.")
  time.sleep(0.5)
  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
  print()
  averages = []
  totalAverage = 0
  hate_averages=[]
  hateTotalAverage=0
  time.sleep(2)
#--------------------------------------------------------------------------------------
