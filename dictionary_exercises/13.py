#13- Given a dictionary with teams and players, show which players are registered in several teams.
#invert use key team

team_dictionary={
    "chelsea":["juan","peter","harry","pedro"],
    "real madrid":["peter","harry","daniel"],
    "barcelona":["juan","pedro","jose"],
    }
#team_dictionary={
#    "harry": ["chelsea"],
#    "peter":["real madrid"],
#    "daniel":["barcelona","las palmas"],
#    "juan":["las palmas"],
#    "jose":["real madrid","barcelona"],
#    }

player_list=[]

for team,player in team_dictionary.items():

    dictionary_copy= team_dictionary.copy()
    del dictionary_copy[team]

    if player in dictionary_copy.values():
        player_list.append(player)

print(player_list)