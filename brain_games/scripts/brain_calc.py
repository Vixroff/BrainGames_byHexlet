#!/usr/bin/env python3
from brain_games.logic import play_game
from brain_games.games import play_calc


def main():
    play_game(play_calc)


if __name__ == '__main__':
    main()