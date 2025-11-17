from RPS import player
from RPS_game import play, quincy, rock_bot, pattern_bot, random_bot

if __name__ == "__main__":
    bots = [quincy, rock_bot, pattern_bot, random_bot]
    for bot in bots:
        print(f"\nPlaying against {bot.__name__}")
        play(player, bot, 1000, verbose=True)
