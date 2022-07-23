"""
    I) Bloc A
        Serie d'opération sur une chaine de caractère
        servant à modifier légèrement le text entré
"""
from subdiv_mini import inverser_phrase,remettre_phrase

def complexi(plain_text):
    """
        example:
            hello word ---> rowdl lehol
    """
    plain_text =  plain_text[::-1]
    plain_text = inverser_phrase(plain_text)
    return plain_text

def decomplex(coded_text):
    """ 
        Remet le text dans me bon sens
        example:
            rowdl lehol ---> hello world
    """
    coded_text = remettre_phrase(coded_text)
    coded_text =  coded_text[::-1]
    return coded_text


"""
Test
-----------
m = complex('Salut sava tu tfk quoi ?')
>> ? uqio ftk tu asav laStu

print(decomplex(m))
>> Salut sava tu tfk quoi ?

"""



