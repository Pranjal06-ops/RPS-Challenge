import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    beats = {"R": "P", "P": "S", "S": "R"}
    if not opponent_history:
        return random.choice(["R", "P", "S"])
    counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        counts[move] += 1
    most_common = max(counts, key=counts.get)
    next_move = beats[most_common]
    if len(opponent_history) > 4:
        for length in [3, 2]:
            pattern = ''.join(opponent_history[-length:])
            for i in range(len(opponent_history) - length):
                if ''.join(opponent_history[i:i+length]) == pattern:
                    if i + length < len(opponent_history):
                        predicted = opponent_history[i + length]
                        next_move = beats[predicted]
                        break
    if random.random() < 0.1:
        next_move = random.choice(["R", "P", "S"])
    return next_move
