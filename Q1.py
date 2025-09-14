#import itertools

def find_mafia(matrix):
    n = len(matrix)
    mafia_count = n // 3
    players = range(n)

    def is_valid(roles):
        for i in range(n):
            speaker_is_citizen = roles[i] == 1
            for j in range(n):
                claim = matrix[i][j]
                if claim == 0:
                    continue
                target = roles[j]
                if speaker_is_citizen:
                    if claim == 1 and target != 1:
                        return False
                    if claim == -1 and target != 0:
                        return False
                else:  # mafia always lies
                    if claim == 1 and target == 1:
                        return False
                    if claim == -1 and target == 0:
                        return False
        return True

    # بهینه‌سازی: فقط تا پیدا شدن اولین جواب می‌گردیم
    for mafia in itertools.combinations(players, mafia_count):
        roles = [1] * n
        for m
