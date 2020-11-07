import pandas
wiki = pandas.read_html('https://en.wikipedia.org/wiki/2020_United_States_presidential_election')
election = wiki[4]
candidate_1 = election[1]
cand_1_name = candidate_1[1]
cand_1_votes = candidate_1[5]
cand_1_popular = candidate_1[7]

candidate_2 = election[2]
cand_2_name = candidate_2[1]
cand_2_votes = candidate_2[5]
cand_2_popular = candidate_2[7]

if cand_1_votes > cand_2_votes:
    print(cand_1_name, 'winner')
else:
    print(cand_2_name, 'winner')