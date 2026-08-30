import json
from collections import defaultdict

with open('data/1nugs0l/flat.json') as f:
    comments = json.load(f)

real = [c for c in comments if c['body'] not in ('[deleted]', '[removed]') and c['author'] != '[deleted]']

# Cluster definitions:
# 1 = Pro-Rebase / Agreement
# 2 = Pro-Merge / Disagreement  
# 3 = Nuanced / Balanced
# 4 = Practical Workflows
# 5 = Code Review & Collaboration
# 6 = Questions
# 7 = Short Reactions & Humor

cluster_map = {
    # Pro-Rebase / Agreement (1)
    'nh0z9oq': 1, 'nh1ibxn': 1, 'nh1vq9t': 1, 'nh1y4ex': 1, 'nh1yjo7': 1,
    'nh2ile5': 1, 'nh1mo4k': 1, 'nh2nxo3': 1, 'nho0w75': 1, 'ni1212a': 1,
    'nh27zpg': 1, 'nh2fkjy': 1, 'nh7a0b1': 1, 'nh8x97z': 1, 'nh98ltu': 1,
    'nhe51h9': 1, 'nhebuka': 1, 'nhduoc4': 1, 'nh1slo5': 1, 'nh16pva': 1,
    'nh43va8': 1, 'nhbups7': 4, 'nhi20gw': 4, 'nh0yja4': 1, 'nho1c2s': 1,
    'nho223h': 1, 'nho2tql': 1, 'nh1mzvm': 1, 'nh1omy4': 1, 'nhotbz5': 1,
    'nh1xi0h': 1, 'nh2mjad': 1, 'nh2o5d6': 1, 'nh4y9f5': 1, 'nh1t4ou': 1,
    'nh8mwpc': 1, 'nh72bmt': 1, 'nh8ca71': 1, 'nh9ejyu': 1, 'nha5k1o': 1,
    'nhd6yyw': 1, 'nhe77mp': 1, 'nh2qvcc': 2, 'nh2tihx': 4, 'nh13agx': 2,
    'nh1h4h7': 2, 'nh1hoxd': 2, 'nh231fl': 4, 'nh2vv4q': 2, 'nh1g6zk': 6,
    'nh1km07': 2, 'nh23oj2': 4, 'nh25lfz': 2, 'nh3omhf': 2, 'nh1wcf9': 2,
    'nh3di70': 2, 'nh3kwfh': 2, 'nh6kcwz': 2, 'nh1lkzz': 3, 'nh10fa4': 2,
    'nh1uixi': 3, 'nh1y5p9': 2, 'nh2z8ab': 3, 'nh2qs40': 3, 'nh2tw75': 3,
    'nh4z28w': 2, 'nh11fqq': 2, 'nh1fgpq': 3, 'nh1gt6j': 3, 'nh1sa2i': 4,
    'nh2dqzl': 7, 'nh2i2np': 3, 'nh2k3m1': 3, 'nh35uis': 4, 'nh3e57a': 1,
    'nh3x6px': 1, 'nh43qim': 1, 'nh59y4z': 1, 'nh8ccbm': 1, 'nh4jwzm': 2,
    'nh4mbzd': 1, 'nh4rgx8': 4, 'nh4x19e': 2, 'nh4xizv': 2, 'nh5w5wg': 2,
    'nh503kk': 2, 'nh551dq': 2, 'nh57hl0': 1, 'nh5e371': 4, 'nh5tpqk': 3,
    'nh6jlwb': 4, 'nh7k8jz': 7, 'nh7n6xx': 7, 'nh72ktb': 1, 'nh7wtc1': 2,
    'nh7yhfi': 7, 'nh8318p': 4, 'nh8ilec': 7, 'nh9wu5k': 3, 'nhbx4re': 7,
    'nhbyhqy': 7, 'nhbzo5o': 7, 'nhbifnv': 4, 'nhdejat': 5,
    
    # Pro-Merge / Disagreement (2)
    'nh1lx67': 2, 'nh293j2': 6, 'nh68xq9': 6, 'nh6h45s': 7, 'nh9fws4': 7,
    'nh10jm7': 3, 'nh1s6os': 6, 'nh1vpot': 4, 'nh1vyk7': 3, 'nh0xx1i': 2,
    'nh1msez': 7, 'nh3flyz': 6, 'nh1ytmj': 3, 'nh3ksxr': 6, 'nh3n7ll': 7,
    'nh3q4w0': 7, 'nh3s5ip': 7, 'nh0zlvw': 2, 'nh17c48': 2, 'nh18wnk': 2,
    'nh5i6r0': 2, 'nh6my8u': 2, 'nh6o20s': 2, 'nh6tuhu': 2, 'nh694zx': 2,
    'nh762l1': 2, 'nh8gc1u': 2, 'nhmwjdq': 1, 'nh3gaon': 6, 'nh3mvyb': 6,
    'nh3rmuj': 2, 'nh3shis': 6, 'nh46m72': 2, 'nh4wr5k': 7, 'nh4xhp1': 2,
    'ni7mlay': 7, 'nh26yvt': 7, 'nygj3nu': 2, 'nh1f6xk': 2, 'nh12p3p': 3,
    'nh24jr9': 5, 'nh2oahm': 5, 'nh2t3ud': 5, 'nh331up': 5, 'nh33cyw': 5,
    'nhc6yel': 5, 'nh2sfr1': 2, 'nh9el04': 6, 'nh9n2zy': 3, 'nh8xfz7': 2,
    'nh9h8fy': 2, 'nha8g4f': 2, 'nh8x8w4': 2, 'nh53sro': 7, 'nh5436n': 7,
    'nh1fa52': 7, 'nh54e4o': 7, 'nh1gm2k': 7, 'nh25lfz': 2, 'nh3ml8z': 6,
    'nh3omhf': 2, 'nh1tzaq': 3, 'nh2n5s0': 3, 'nh2tgm3': 3, 'nh348lv': 3,
    'nh3fsbh': 3, 'nh55348': 3, 'nh6obgy': 3, 'nh1lkzz': 3, 'nh10fa4': 2,
    'nh1uixi': 3, 'nh1y5p9': 2, 'nh2z8ab': 3, 'nh2qs40': 3, 'nh2tw75': 3,
    'nh4z28w': 2, 'nh11fqq': 2, 'nh1ef6s': 7, 'nh1eque': 7, 'nh1fbfm': 2,
    'nh1j1m5': 7, 'nh1k6na': 7, 'nh2dqzl': 7, 'nh2i2np': 3, 'nh54soh': 7,
    'nh54ue6': 7, 'nh55cr5': 7, 'nh55r0g': 6, 'nh5cut9': 7, 'nh55tkn': 7,
    'nh56fd0': 7, 'nh56iql': 7, 'nh56nmp': 6, 'nh56tpz': 7, 'nh56x4w': 7,
    'nh572pr': 7, 'nh58fqe': 6, 'nh5eio0': 7, 'nh5nssj': 6, 'nh75vn7': 7,
    'nh766bp': 6, 'nh76jp1': 7, 'nh8ilec': 7, 'nhbx4re': 7, 'nhbdhbb': 7,
    'nhbyhqy': 7, 'nhdtftq': 7, 'nhi7ygs': 7, 'nhkdgmy': 2, 'nhimz0w': 2,
    'nhlvehe': 2, 'nhrf3wc': 7, 'nhofu5o': 3, 'nhrgj6g': 7, 'nhomo6i': 2,
    'nhrhfpy': 7, 'nhoyz2w': 3, 'nhrj07g': 7, 'nhr5f58': 3, 'nhx3dnb': 7,
    'nhtabso': 7, 'nh16n9i': 2, 'nh1su3j': 3, 'nh2v65w': 2, 'nh2q1rg': 2,
    'nh1gdap': 3, 'nh534zk': 3, 'nh21k89': 7, 'nh54gpv': 7, 'nh497zu': 2,
    'nh56422': 7, 'nhb4xce': 2, 'nhbxk9a': 7, 'nhcaqj1': 2, 'nhbd8uc': 3,
    'nhbyg96': 7, 'nhcxtoh': 2, 'nhdeota': 2, 'nhdfe94': 3, 'nhdfynm': 7,
    'nhfft1x': 7, 'nhhzewh': 2, 'nhi895z': 7, 'nhiep7f': 2, 'nhin4wm': 7,
    'nhmvwox': 1, 'nhrfh99': 7, 'nhn8jcr': 7, 'nhnffqq': 1, 'nhrfvhk': 7,
    'nhohkku': 6, 'nhohox6': 2, 'nhrhap7': 7, 'nhruvod': 2, 'nhowopd': 4,
    'nhrhsxk': 7, 'nhri20w': 4, 'nhp8znp': 3, 'nhr1ddy': 3, 'ouxn089': 1,
    'nh17p7t': 2, 'nh2876j': 6, 'nh2jljn': 4, 'nh2ot95': 2, 'nh3irs0': 2,
    'nh3t2uj': 2, 'nh4xhhg': 1, 'nh50m98': 3, 'nhddpqu': 2, 'nh11ipj': 7,
    'nh15jmg': 1, 'nh165a2': 3, 'nh1kj4q': 3, 'nh3pz7g': 7, 'nh3tjbe': 2,
    'nh556n0': 7, 'nh14fvn': 5, 'nh2r4zu': 5, 'nh3ikjg': 5, 'nh3tood': 5,
    'nh4ky5i': 5, 'nh6gai6': 5, 'nh189lt': 5, 'nh19x7c': 5, 'nh1h2nj': 5,
    'nh3if9i': 5, 'nh55gjt': 5, 'nh9lr3x': 5, 'nhbf5kd': 5, 'nh130c5': 1,
    'nh1ak9k': 1, 'nh1bd8i': 7, 'nh3i0cn': 2, 'nh6ugb8': 6, 'nh761lb': 7,
    'nh771dn': 3, 'nh7aeow': 7, 'nh7q13g': 1, 'ni93k4r': 7, 'nhi4fjb': 3,
    'ni8wu8p': 7,
}

# Add the missing unassigned comments
cluster_map['nh1jdjo'] = 7  # "This!" - short reaction
cluster_map['nh1uujl'] = 7  # "Thanks for the link! Will read it 👌"
cluster_map['nh20cv2'] = 1  # "100% agree. I like my main branch free from merge commits."
cluster_map['nh20kqr'] = 7  # " 💯!"
cluster_map['nh29pjb'] = 1  # "Agree. And squash is goated"
cluster_map['nh2a46g'] = 7  # "Absolutely 💯"
cluster_map['nh2jhn8'] = 1  # "You mean merging main into feature branch? Yep, this also works, I agree."
cluster_map['nh4zv40'] = 4  # "Squash when merging back into master, and you get just one commit."
cluster_map['nh1gvnt'] = 7  # "Nice workflow! We do almost the same..."
cluster_map['nh1fkdz'] = 7  # "AGREE!"
cluster_map['nh4vwax'] = 2  # "No, you make a statement..."

# Verify all are assigned
unassigned = [c for c in real if c['id'] not in cluster_map]
print(f"Unassigned: {len(unassigned)}")
for c in unassigned:
    print(f"  {c['id']} | {c['author']} | {c['body'][:100]}")

# Count
counts = {i: 0 for i in range(1, 8)}
scores = {i: 0 for i in range(1, 8)}
names = {1: 'Pro-Rebase/Agreement', 2: 'Pro-Merge/Disagreement', 3: 'Nuanced/Balanced', 
         4: 'Practical Workflows', 5: 'Code Review/Collaboration', 6: 'Questions', 7: 'Short Reactions'}

for c in real:
    cl = cluster_map[c['id']]
    counts[cl] += 1
    scores[cl] += c['score']

print("\nCluster distribution:")
total = 0
for i in range(1, 8):
    print(f"  {names[i]}: {counts[i]} comments, {scores[i]} upvotes")
    total += counts[i]
print(f"Total: {total}")
