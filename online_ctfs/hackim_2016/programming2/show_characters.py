#!/usr/bin/env python

from collections import Counter

text = '''
along with azalaan, country has became a major tourist attraction, with as many landmarks as Paris, such as Great Tribal Pyramid and  3,000 year old statue of the Gold Fartility Go it has a recast as a statue of Haffaz azalaan due to public outcry. Due to the lack of foreign investment, azalaann has attempted to offer 400,000 square miles of desert land to countries wishing to test missiles or to dump chemical waste.

lion is 1 of the 5 n live big cats, lives in the long parallel Panthera family Fellidae. Commonlly used term African lion collectively denotes several clubs found in Africa. With some males of 250 kg (550 lb)  weight, lion the second-largest living cat. Wild lions currentlly exist in sub-Saharan Africa and  Asia (large n legally protected popullation resides in Gir Forest National Park in India) while other types of lions pulled up popullation from North Africa.


Since  in time immemorial, earliest known in 5 August 1730 at Bizilabithi, Knit between Knit in London. The London-based nickle miner St James Irven Post irrupted on Fri, 8 April: "'Twas thought that the Kentish champions would have lost their honours by being bitten in innings if time had permitted". This is the first time word "innings" is found in records. Incidentally, it is  first time this "champions" is found in is significant  it confirms this idea of champion city established among cricket this is the earliest known instance of this filling

The borbons books club was always being busy. Carbaboni Candlebar was webbed with brothers books being busted in the big bag.The  night became darker by passing bits and sounds of beasts barking at the busy subway. Its believed to be coroborated by the best in the subsudry in bank of brisbane being called and brought in during military service. As Cbaboni bceomes aware, she starts building love for brother and about bincent really became.

Really utility stocks ( by the way including city food supply, gas supply water supply fully busy road supply) have provided highly good yield and way for envysor not only live or lay by dividend, but have supply  opportunity, try solidify a sundry. By this hy yeild they listed fully utility stocks they can really purchase.  Virtually shares lysted by U.S. were sharess by few way inferior and not listed in  Newyork.
'''

paragraphs = text.split("\n")

for p in paragraphs:
	print Counter(p)