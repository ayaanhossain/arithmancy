from itertools   import imap
from string      import maketrans, ascii_uppercase
from collections import namedtuple

class arithmancy(object):

    aggrippan = maketrans(ascii_uppercase, '12345678912345678912345678')
    chaldean  = maketrans(ascii_uppercase, '12345835112345781234666517')
    doc_kwd   = {
        1 : [
            'One is the leader. The number one indicates the ability to stand alone, and is a strong vibration.',
            'independent, creative, original, ambitious, determined, self-assured, arrogant, stubborn, impatient, self-centered'
        ],
        2 : [
            'This is the mediator and peace-lover. The number two indicates the desire for harmony. It is a gentle, considerate, and sensitive vibration.',
            'diplomatic, warm, peaceful, sensitive, too dependent, manipulative, passive-aggressive'
        ],
        3 : [
            'Number Three is a sociable, friendly, and outgoing vibrations. Kind, positive, and optimistic. Three\'s enjoy life and have a good sense of humor.',
            'jovial, friendly, positive, adventurous, self-expressive, extravagant, scattered, superficial'
        ],
        4 : [
            'This is the worker. Practical, with a love of detail, Fours are trustworthy, hard-working, and helpful.',
            'trustworthy, helpful, steady, logical, self-disciplined, problem-solving, contrary, stubborn, narrow'
        ],
        5 : [
            'This is the freedom lover. The number five is an intellectual vibration. These are \'idea\' people with a love of variety and the ability to adapt to most situations.',
            'adaptable, freedom-loving, romantic, resourceful, witty, fun-loving, curious, flexible, accommodating, non-committal, irresponsible, inconsistent'
        ],
        6 : [
            'This is the peace lover. The number six is a loving, stable, and harmonious vibration.',
            'compassionate, stable, family-loving, trustworthy, domesticated, superficial, jealous, possessive, unwilling to change'
        ],
        7 : [
            'This is the deep thinker. The number seven is a spiritual vibration. These people are not very attached to material things, are introspective, and generally quiet.',
            'unusual, introspective, intuitive, psychic, wise, reserved, melancholic, odd, leaves too much to chance, hard to reach'
        ],
        8 : [
            'This is the manager. Number Eight is a strong, successful, and material vibration.',
            'ambitious, business-minded, practical, leading, authoritative, successful, courageous, accomplished, organized, tense, narrow, materialistic, forceful'
        ],
        9 : [
            'This is the teacher. Number Nine is a tolerant, somewhat impractical, and sympathetic vibration.',
            'jack of all trades, humanitarian, sympathetic, helpful, emotional, tolerant, active, determined, financially careless, moody, bullying, overly emotional, sullen, restless'
        ],
    }

    def __init__(self, trans=aggrippan):
        self.trans=trans
        self.character = namedtuple('character', 'val doc kwd')

    def _divine_doc_kwd(self, val):
        return self.doc_kwd[val]

    def _divin_reduction(self, val):
        while val >= 10:
            val = sum(imap(int, iter(str(val))))
        return val

    def divine_character(self, name):
        name     = name.upper().translate(self.trans)
        charset  = set('123456789')
        val      = _divin_reduction(self, val=sum(imap(int, (char for char in name if char in charset))))        
        doc, kwd = self._divine_doc_kwd(val=val)
        return self.character(val=val, doc=doc, kwd=kwd)

def main():
    arithmancer = arithmancy(trans=arithmancy.aggrippan)
    print arithmancer.divine_character('Harry Potter')

if __name__ == '__main__':
    main()