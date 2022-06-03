#!/usr/bin/env python3
import argparse
import random

def read_file(filename, type, q):
    if (filename) is None:
        print('File cannot be blank')
        exit()
    with open(filename) as file:
        output = file.readlines()
    if q != True:
        print(f'Read {len(output)} {type} from {filename}')
    return output

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-n', '--nouns', dest='nouns', 
        default='english-nouns.txt', help='name of nouns file (one per line)')
    parser.add_argument('-v', '--verbs', dest='verbs', 
        default='english-verbs.txt', help='name of verbs file (one per line)')
    parser.add_argument('-a', '--adjectives', dest='adjectives', 
        default='english-adjectives.txt', help='name of adjectives file (one per line)')
    parser.add_argument('-q', default=False, action='store_true', help='be quiet')
    args = parser.parse_args()

    adjectives = read_file(args.adjectives, 'adjectives', args.q)
    nouns = read_file(args.nouns, 'nouns', args.q)
    verbs = read_file(args.verbs, 'verbs', args.q)

    name_a = random.choice(adjectives).rstrip().capitalize()
    name_n = random.choice(nouns).rstrip().capitalize()
    name_v = random.choice(verbs).rstrip().capitalize()
    
    # Super basic verb mash-er, we miss loads of rules, but we can parse manually
    if (name_v.endswith('e')):
        name_v = name_v + 'r'
    elif (name_v.endswith('y')):
        name_v = name_v[:-1] + 'ier'
    else:
        name_v = name_v + 'er'

    thing_name = name_a + name_n + name_v
    print(f'ThingName: {thing_name}')

if __name__ == "__main__":
    main()
