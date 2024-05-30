def parse_trie(trie):
    # trie -> 5 red
    tt = trie.strip().split(" ")

    return tt[1], int(tt[0])


def parse_set(st):
    # set -> 5 red, 1 green, 1 blue
    tries = st.strip().split(",")

    return dict([parse_trie(t) for t in tries])


def parse_line(line):
    # line -> Game 36: 10 red; 5 red, 1 green, 1 blue; 2 green, 8 red; 9 red, 2 green; 1 blue, 10 red; 6 red, 1 green, 1 blue
    parts = line.split(":")
    game = int(parts[0].split(" ")[1])
    # sets -> 10 red; 5 red, 1 green, 1 blue; 2 green, 8 red; 9 red, 2 green; 1 blue, 10 red; 6 red, 1 green, 1 blue
    sets = parts[1].strip().split(";")
    parsed_sets = [parse_set(st) for st in sets]
    return {"game": game, "sets": parsed_sets}


with open("day2b.txt") as fin:
    parsed_data = [parse_line(line) for line in fin.readlines()]


def valid_set(st):
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    valid_colors = set(["red", "green", "blue"])
    print(st)
    if not set(st.keys()).issubset(valid_colors):
        return False
    return (
        st.get("red", 0) <= 12 and st.get("green", 0) <= 13 and st.get("blue", 0) <= 14
    )


def valid_game(game):
    return all(valid_set(s) for s in game["sets"])


print(sum(game["game"] for game in parsed_data if valid_game(game)))


def game_power(game):
    import functools

    min_colors = {"red": 0, "green": 0, "blue": 0}
    for s in game["sets"]:
        for color, count in s.items():
            min_colors[color] = max(min_colors[color], count)
    return functools.reduce(lambda a, b: a * b, min_colors.values())

print(sum(game_power(game) for game in parsed_data))