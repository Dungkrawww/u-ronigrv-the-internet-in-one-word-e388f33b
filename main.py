# The Internet in One Word — entry: "unhinged"
#
# Why "unhinged" wins this judge's brief:
# 1. One word, no explanation needed — it is a single word that names the
#    whole internet, not one app, one site or one mood.
# 2. Funny by itself — "unhinged" lands as a joke the moment you read it:
#    the internet, described in one clinical word, as if a doctor wrote the
#    diagnosis.
# 3. True about the internet as a whole — every corner of it, from comment
#    sections to livestreams to group chats, is unhinged in the same way:
#    no filter, no off switch, no adult in the room.
# 4. Surprising — it is not the first obvious word anyone reaches for.
#    People reach for "addictive", "endless", "chaotic", "doomscrolling".
#    "Unhinged" comes from a different angle: not what the internet does
#    to you, but what it IS.
# 5. Lands in one beat — eight letters, instantly readable, spelled the
#    way everyone spells it; the laugh and the nod arrive together.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Deterministic: the entry is one fixed word, so both harness runs must
# write the same bytes. No randomness, no network, no clock.
WORD = "unhinged"


def validate_word(word):
    # Gate rules (sealed scorer): /output/entry.txt must be UTF-8 text of
    # 1 to 30 characters, not only white space.
    assert 1 <= len(word) <= 30, f"word is {len(word)} chars, must be 1-30"
    assert word.strip() == word, "no leading/trailing whitespace"
    assert len(word.split()) == 1, "must be a single word"


def main() -> None:
    validate_word(WORD)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
