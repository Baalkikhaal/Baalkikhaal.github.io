# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:48:12 2022

@author: fubar
"""

class Joker:
    name = 'The Joker'
    quotes = ['Why so serious?',
              'I just doooo things.',
              'Do I look like I am man with a plan?'
             ]
    def random_quote(self):
        n_quotes = len(self.quotes)
        from random import randint
        quote = self.quotes[randint(0, n_quotes-1)]
        return quote
        
class ReelJoker:
    name = 'The Joker'
    quotes = ['Why so serious?',
              'I doooo things.',
              'Do I look like I am man with a plan?'
             ]
    def __init__(self, age, director, actor):
        self.version = dict(	age=age,
					director=director,
					actor=actor
				)
    def tell_random_quote(self):
        n_quotes = len(self.quotes)
        from random import randint
        quote = self.quotes[randint(0, n_quotes-1)]
        return quote


class InheritedJoker(Joker):
    def __init__(self, age, director, actor):
        self.version = dict(	age=age,
					director=director,
					actor=actor
				)


print(Joker.name)
print(Joker.random_quote(Joker))

joker_golden = ReelJoker("golden", "Tim Burton", "Jack Nicholson")
joker_silver = ReelJoker("silver", "Christopher Nolan", "Heath Ledger")
joker_modern = ReelJoker("modern", "Todd Phillips", "Joachim Phoenix")

golden_age_actor = joker_golden.version.get('actor')
silver_age_director = joker_silver.version.get('director')

print(f'{joker_golden.name} of the golden age was played by {golden_age_actor}.')
print(f'{joker_silver.name} of the silver age was directed by {silver_age_director}.')

inherited_joker_golden = InheritedJoker("golden", "Tim Burton", "Jack Nicholson")

inherited_golden_age_actor = inherited_joker_golden.version.get('actor')
print(f'{inherited_joker_golden.name} of the golden age was played by {inherited_golden_age_actor}.')

print(ReelJoker.name == joker_golden.name)

#print(ReelJoker.version)

variable = Joker()

def test():
    pass

variable1 = test