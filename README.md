![logo file](logo.png)

# MSE PROJECT
-------------------------------------

# ENCRYPTION BY MUTILPLE SUBTITUTION
-------------------------------------
Chiffrement par subtitution multiple

projet sur un programme de chiffrement par subtitution multiple,
pour but de créer des messages codés avec des phrases courtes.

pratique pour:
    créer des énigmes complexes
    hacher un mot de passe
    **aprendre la cryptographie et la cryptanalyse !**

pas pratique pour:
    **sécurisé ces données**

**Normalement il faut avoir les clés de chiffrement pour pouvoir déchiffrer les messages de quelqu'un d'autre, normalement ! (Tentez de décoder les messages sans le programme !)**

**Attention si vous perdez vos clés, tous les messages que vous avez chiffrées précédemment seront plus possible à déchiffrer (comme si vous perdez vous bitcoin à jamais !**

Tous est facilement paramétrable dans le fichier [parametre.py](https://github.com/flowlord/encryption-by-mutilple-subtitution/blob/main/parametre.py)
---------------------------------------

# REQUIS !
-------------------------------------
Pour copier le message automatiquement vous devez installez le module [pyperclip](https://pypi.org/project/pyperclip/)

	> pip install pyperclip
	
[pyAesCrypt](https://pypi.org/project/pyAesCrypt/) pour chiffrer et envoyer vos clés de chiffrement

	> pip install pyAesCrypt

	
-------------------------------------

**le fichier keylib.py sont vous clés de chiffrement, gardez les secret à tous prix !**
Elle est générer lorsque vous chiffrer votre premier message
**Ne tantez pas d'ouvrir le fichier keylib.py ou initpat.txt, cela risque de faire bugger votre IDE**

pour régénérer vos clés de chiffrement supprimer le fichier keylib.py

-------------------------------------

    INPUT --> A --> B --> C --> output
--------------------------------------------------------------------------
    I) Bloc A
        Le texte est légèrement modifié.
--------------------------------------------------------------------------
    II) Bloc B
        Chaque caractère est substitué.
--------------------------------------------------------------------------
    II) Bloc C
        Complexifie le code après la substitution.


# Usage
---------------------------
	main.py (cipher | c) "message"
	
	main.py (decipher | d) (le message est automatiquement colé)


# Exemples:
---------------------------
	$ python main.py c "meeting tonight for speak"
	
	> 쓗턞🃅὎꾋⦏넲糀뀅獀㬶㜹킹껥⩞刍鲵鴇ꁺ樈蓅𒉗ﳀ𝌐㏘⠹楨ꎷ䤁ዚ㬙譆귘鷛堘籉뫴됺𒀀뀤넵⤯頨ꍪ扰𓋊Ჷ휏鹃𓃖農挘ᎇچめⶴ 㥅셋וֹ꿮뛋巭
	
	$ python main.py decipher
	
	> meeting tonight for speak


# Remarque:
Vous devez copier le message secret avant de le déchiffrer

# Astuces
---------------------------

Si le programme a du mal
à déchiffrer un mot que sa soit en français ou
en anglais vérifier l'orthographe de ce mot et/ou qui est présent dans le fichier word_lst.txt

utiliser la fonction encrypt_keylib dans tools.py pour chiffrer et envoyer vos clés de chiffrement

modifier les caractères du fichier initpat.txt
Mettez ce que vous voulez sauf les caractères
que vous souhaitez remplacer.

Modifier la longueur des caractères générés.

Remplacer la liste de mots, par une liste
mot de votre langue ou inventez des mots.

modifier la liste des lettres spéciaux

Cette méthode de chiffrement reste vulnérable
aux attaques, ne chiffrer pas vos données personel avec cette méthode !

pensez à mélanger les caractères du fichier initpat.txt à l'aide de la fonction mixeur.

-----------------------------------
le monde merveilleux des secrets, des lettres et des
chiffres !

-----------------------
Autre version 1: [SlotBorderCut](https://github.com/flowlord/MSE-SlotBorderCut)

Autre version 2: [GRUYERE CHEESE](https://github.com/flowlord/MSE-GRUYERE-CHEESE)

---------------------------------------
---------------------------------------


[Serveur Discord officiel ](https://discord.gg/YQCufGwwwt)
![demo file](demo/demo.jpg)
![demo file 2](demo/cap_ex.png)
![demo file 3](demo/cap_ex2.png)


