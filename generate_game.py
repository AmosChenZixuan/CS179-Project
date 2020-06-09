import random
import numpy as np
def logit(z): return 1./(1.+np.exp(-z))


def generate_players(num_of_players, skill_cap):
    ## returns a list of player's skill
    return [round(random.uniform(0,skill_cap),2) for i in range(num_of_players)]


def generate_games(players,scale,num_of_games, style='pystan'):

    if style == 'pystan':
        
        player1=[]
        player2=[]
        outcome=[]
        for i in range(num_of_games):
            p1,p2 = random.sample(range(len(players)),2)
            win_rate=logit(scale*(players[p1]-players[p2]) )

            ##pystan player id is ONE based
            player1.append(p1+1)
            player2.append(p2+1)
            
            outcome.append(*random.choices([1,0],weights=[win_rate,1-win_rate]))

        return player1,player2,outcome
    
    elif style == 'pygm':
        games=[]
        for i in range(num_of_games):
            p1,p2 = random.sample(range(len(players)),2)
            win_rate=logit(scale*(players[p1]-players[p2]) )
            
            games.append((p1,p2,*random.choices([1,-1],weights=[win_rate,1-win_rate])))
        return games
    
    assert False 


def generate_new_player(skill_cap):
    #returns a double, representing the new player's skill
    return round(random.uniform(0,skill_cap),2)

def generate_new_player_games(players, new_player_id,new_player, scale, num_of_games, style='pystan'):
    if style == 'pystan':
        player1=[]
        player2=[]
        outcome=[]
        for i in range(num_of_games):
            player1.append(new_player_id)
            p2 = random.sample(range(len(players)),1)
            win_rate=logit(scale*(new_player-players[p2]) )
            

            ##pystan player id is ONE based
            player2.append(p2+1)
            outcome.append(*random.choices([1,0],weights=[win_rate,1-win_rate]))

        return player1,player2,outcome
    elif style == 'pygm':
        games=[]
        for i in range(num_of_games):
            p2 = random.sample(range(len(players)),1)
            win_rate=logit(scale*(new_player-players[p2]) )
            
            games.append((new_player_id,p2,*random.choices([1,-1],weights=[win_rate,1-win_rate])))
        return games
    
    assert False 
    

players= generate_players(10,10)

print(players)

print(generate_games(players, 0.3, 10, 'pystan'))

