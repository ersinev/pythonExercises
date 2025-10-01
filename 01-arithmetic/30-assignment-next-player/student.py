# write your code here

def next_player(player, player_count):

    player_going_to_play = (player+1) % player_count
    return player_going_to_play