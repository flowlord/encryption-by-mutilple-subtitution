"""
    II) Bloc C
        Complexifie le code après la subtitution.
    
    m = chaos('hello world',10)
	print(m)
	> h녓♲ell臥o w腢o⪙rﲸld킙碹蘛᪙

"""

from configs.parametre import*
from random import choice,randint

def chaos(plain_text,x):
    """
        Ajoute de manière aléatoire un caractère du groupe_b
        dans le code dans une position au hazard x fois.
    """
    plain_text = list(plain_text)
    
    for _ in range(x):
        get_rand_carac = choice(groupe_b)
        position = randint(0,len(plain_text))
        
        plain_text.insert(position, get_rand_carac)

    plain_text = ''.join(plain_text)
    return plain_text


def dechaos(code):
    """
    Enlève les carcatères du groupe b
    """
    
    new_text = ""
    for element in code:
        if element not in groupe_b:
            new_text = new_text + element  
    return new_text


