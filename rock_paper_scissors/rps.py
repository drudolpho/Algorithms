#!/usr/bin/python

import sys



def rock_paper_scissors(n):

    # Base cases
    if n == 0:
        return [[]]

    if n == 1:
        return [["rock"], ["paper"], ["scissors"]]

    answer = []

    for i in rock_paper_scissors(n - 1):
        temp_rock = i + ["rock"]
        temp_paper = i + ["paper"]
        temp_scissors = i + ["scissors"]
        answer.append(temp_rock)
        answer.append(temp_paper)
        answer.append(temp_scissors)

    return answer


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
