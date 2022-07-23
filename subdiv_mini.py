"""

Je reprend une petite partie du code issu du projet: https://github.com/flowlord/subdiv8

SUBDIV MINI
-----------
Principe et fonctionnement

abcde --> ab | cd | e (impair)
abcd --> ab | cd (pair)

C = combinaison

C1: abcde --> ab | cd | e --> change le sens -->c de ab
C1_inv: fait l'inverse

C2: abcd --> ab | cd --> change le sens --> cdab
C2_inv: fait l'inverse

"""


def milieu(char):
    """
    abcd --> nombre de carcatères --> 4 --> 4/2 ---> 2
    """
    return int(len(char)/2)


def C1(t):
    m = milieu(t)
    start = t[:m]
    middle = t[m:-1]
    end = t[-1]
    return middle+end+start

def C1_inv(t):
    m = milieu(t)
    start = t[m+1:]
    middle = t[:m]
    end = t[m]
    return start+middle+end




def C2(t):
    m = milieu(t)
    start = t[:m]
    end = t[m:]
    return end+start
    
def C2_inv(t):
    m = milieu(t)
    start = t[m:]
    end = t[:m]
    return start+end



def inverser_mot(word):
    n = len(word)
    
    if n == 1:
        return word
    elif n%2 == 0:
        return C2(word)
    else:
        return C1(word)


def remettre_mot(word):
    n = len(word)
    
    if n == 1:
        return word
    elif n%2 == 0:
        return C2_inv(word)
    else:
        return C1_inv(word)


def remettre_phrase(code):
    code = code.split(' ')
    msg = ''
    
    for word in code:
        msg = msg + remettre_mot(word) + ' '
    
    return msg[:-1]


def inverser_phrase(msg):
    msg = msg.split(' ')
    code = ''
    
    for word in msg:
        code = code + inverser_mot(word) + ' '
    
    return code[:-1]





