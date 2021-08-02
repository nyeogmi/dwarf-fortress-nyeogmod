from random import Random


def chunk(name):
    with open(f"chunks/{name}") as f:
        return f.read() + "\n"


def language_file():
    lang = chunk("language_NYEOGMOD_VAMPBAT.txt")
    lines_2 = []
    vbatwords = vampbat_words(0)
    for line in lang.splitlines():
        if "T_WORD" in line:
            line, _, wordpart = line.rpartition(":")
            lines_2.append(line + ":" + next(vbatwords) + "]")
        else:
            lines_2.append(line)
    return "\n".join(lines_2)


def vampbat_words(seed):
    r = Random(seed)

    words = set()
    while True:
        w = vampbat_word(r)

        if w is None:
            continue

        if w in words:
            continue

        yield w
        words.add(w)


def vampbat_word(r: Random):
    pfx = r.choice([
        "g", "k", "gm", "km", "gn", "kn",
        "gg", "kk",

        "s", "sk", "skr", "skn", "skm",
        "z", "zk", "zkr", "zkn", "zkm",
        "x", "xk", "xkr", "xkn", "xkm",
        "ch",


        "rr", "r",

        "y", "h",
        "n", "m",
    ])

    vwl = r.choice([
        "a", "i", "ee", "o", "u", "eo",
        "yeo",
    ])

    sfx = r.choice([
        "k", "g", "kz", "x",
        "b", "bk",

        "km", "kn",
        "gm", "gn",
        "xm", "xn",
        # "kmi", "gmi", "xmi",
        # "kni", "gni", "xni",
    ])

    w = pfx + vwl + sfx
    w = w.replace("wck", "wk")
    if "yi" in w or "ry" in w or "nig" in w or "uck" in w:
        return None
    if w.endswith("yeogm"):
        w += "i"

    return w


def main(pfx):
    with open(f"{pfx}/creature_nyeogmod_vampbat.txt", "wt") as f:
        f.write(chunk("creature_nyeogmod_vampbat.txt"))

        f.write("\n[CASTE:BAT_MALE]\n")
        f.write(chunk("castes/bat/shared.txt"))
        f.write(chunk("castes/bat/male.txt"))

        f.write("\n[CASTE:BAT_FEMALE]\n")
        f.write(chunk("castes/bat/shared.txt"))
        f.write(chunk("castes/bat/female.txt"))

        for noun in ["dwarf", "elf", "goblin", "human", "kobold"]:
            # no gender for now
            f.write(f"\n[CASTE:{noun.upper()}]\n")
            f.write(chunk(f"castes/{noun}/shared.txt"))

    with open(f"{pfx}/entity_nyeogmod_vampbat.txt", "wt") as f:
        f.write(chunk("entity_nyeogmod_vampbat.txt"))

    with open(f"{pfx}/item_nyeogmod_toy.txt", "wt") as f:
        f.write(chunk("item_nyeogmod_toy.txt"))

    with open(f"{pfx}/item_nyeogmod_trapcomp.txt", "wt") as f:
        f.write(chunk("item_nyeogmod_trapcomp.txt"))

    with open(f"{pfx}/language_NYEOGMOD_VAMPBAT.txt", "wt") as f:
        f.write(language_file())


if __name__ == "__main__":
    main("../raw/objects")
    main("../generated")
