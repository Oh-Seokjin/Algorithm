def solution(cards1, cards2, goal):
    cards1.append("")
    cards2.append("")
    for elem in goal:
        if cards1[0] == elem:
            cards1.pop(0)
        elif cards2[0] == elem:
            cards2.pop(0)
        else:
            return "No"            
    return "Yes"