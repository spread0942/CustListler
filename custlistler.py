#!/bin/python3
import sys
import os


def read_wordlist(wordlist):
    with open(wordlist, 'r') as f:
        return f.readlines()


def customize_list(lines):
    content = set()  # Use a set to avoid duplicates
    
    for line in lines:
        parts = line.split()
        
        if len(parts) == 2:
            first, last = parts
            first_initial = first[0].lower()
            last_initial = last[0].lower()
            
            # Apply your patterns
            content.update([
                f"{first}{last}",      # namelastname
                f"{first_initial}.{last}",  # n.lastname
                f"{first_initial}{last}",   # nlastname
                f"{last_initial}.{first}",  # l.name
                f"{last_initial}{first}",   # lname
                first.lower(),              # name
                first.capitalize(),         # Name
                last.lower(),               # lastname
                last.capitalize()           # Lastname
            ])
        else:
            content.update([
                line.lower(),
                line.capitalize()
            ])
    
    return content


def write_new_wordlist(wordlist, content):
    if os.path.exists(wordlist):
        os.remove(wordlist)
    
    f = open(wordlist, 'a')
    
    for line in content:
        f.write(f'{line.replace("\n", "")}\n')
    
    f.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'[-] Required two arguments: {sys.argv[0]} "LIST TO CUSTOM" "OUTPUT FILE"')
        sys.exit(1)
    
    wordlist = sys.argv[1]
    new_wordlist = sys.argv[2]
    
    print(f'[+] Wordlist to customize: {wordlist}')
        
    # read the wordlist
    lines = read_wordlist(wordlist)
    print('[+] Read wordlist')
    
    content = customize_list(lines)
    print('[+] Customized lines')
    
    # create the new wordlist
    write_new_wordlist(new_wordlist, content)
    print(f'[+] Created new file at {new_wordlist}')
    