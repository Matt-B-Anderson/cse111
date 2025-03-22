import random

def main():
    runs = [[1, "past"], [1, "present"], [1, "future"], [2, "past"], [2, "present"], [2, "future"]]
    for x in runs:
        make_sentences(x[0], x[1])

def make_sentences(quantity, tense):
    print(f'{get_determiner(quantity).capitalize()} {get_noun(quantity)} {get_verb(quantity, tense)} {get_prepositional_phrase(quantity)}.')

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"] 
    word = random.choice(words)
    adject = get_adjective()
    return f'{adject} {word}'

def get_adjective():
    words = ["beautiful","bright","cold","courageous","delightful","elegant","friendly","gentle","happy","heavy","loud","mysterious","quick","quiet","shiny","strong","tall","tiny","warm","wise"]
    return random.choice(words)

def get_verb(quantity, tense):
    words = []
    match tense:
        case "past":
            words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
        case "present":
            if quantity == 1 and tense == "present":
                words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
            else:
                words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
        case "future":
            words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    return random.choice(words)

def get_preprosition():
    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    return random.choice(words)

def get_prepositional_phrase(quantity):
    return f'{get_preprosition()} {get_determiner(quantity)} {get_noun(quantity)}'
main()