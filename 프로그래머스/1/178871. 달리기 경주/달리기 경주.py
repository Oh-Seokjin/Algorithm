def solution(players, callings):
    ranking = {player: i for i, player in enumerate(players)}
    for call in callings:
        idx = ranking[call]
        ranking[call] -= 1
        ranking[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players