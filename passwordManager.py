#! /usr/bin/env python3
#! passwordManager.py - An insecure password locker program.

#This is program allows the user to type the name of an existing account 
#And copy the password to the clipboard.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
            
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python passwordManager.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard.')
else:
    print('There is no account named ' + account)