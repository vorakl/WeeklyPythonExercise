#!/usr/bin/env python3

from string import punctuation as punc_set

def create_password_checker(uppercase, lowercase, punctuation, digits):

    def helper(password):
        uc, lc, pun, dig = -uppercase, -lowercase, -punctuation, -digits

        for c in password:
            if c.isdigit():
                dig += 1
            elif c.islower():
                lc += 1
            elif c.isupper():
                uc += 1
            elif c in punc_set:
                pun += 1
            else:
                pass


        checks = {'uppercase': uc,
                  'lowercase': lc,
                  'punctuation': pun,
                  'digits': dig}
        
        valid = all(v >= 0 for v in checks.values())
 
        return (valid, checks)

    return helper


pc1 = create_password_checker(2, 3, 1, 4)

print(pc1('Ab!1'))
print(pc1('ABcde!1234'))
