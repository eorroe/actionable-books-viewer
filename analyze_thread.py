import json
from collections import defaultdict

with open('data/1nugs0l/flat.json') as f:
    comments = json.load(f)

real = [c for c in comments if c['body'] not in ('[deleted]', '[removed]') and c['author'] != '[deleted]']
print(f"Total real comments: {len(real)}")

# Cluster assignments (index 0-361, mapping to comments 1-362)
# I'll create a mapping based on my manual analysis
cluster_map = {
    # Strong Agreement / Pro-Rebase
    'nh0z9oq': 'Pro-Rebase',      # 1 - Shadowratenator
    'nh1ibxn': 'Pro-Rebase',      # 2 - tahaan
    'nh1vq9t': 'Pro-Rebase',      # 3 - vermiculus
    'nh1y4ex': 'Pro-Rebase',      # 4 - tahaan
    'nh1yjo7': 'Pro-Rebase',      # 5 - vermiculus
    'nh2ile5': 'Pro-Rebase',      # 6 - wildjokers
    'nh1mo4k': 'Pro-Rebase',      # 10 - timbar1234
    'nh2nxo3': 'Pro-Rebase',      # 11 - remy_porter
    'nhel2w1': 'Pro-Rebase',      # 12 - timbar1234
    'nh1mzvm': 'Pro-Rebase',      # 13 - Affectionate-Egg7566
    'nho0w75': 'Pro-Rebase',      # 14 - MiscreatedFan123
    'ni1212a': 'Pro-Rebase',      # 15 - timbar1234
    'nh27zpg': 'Pro-Rebase',      # 16 - xenomachina
    'nh2fkjy': 'Pro-Rebase',      # 18 - xenomachina
    'nh7a0b1': 'Pro-Rebase',      # 23 - xenomachina
    'nh2acst': 'Pro-Rebase',      # 25 - AttentionSuspension
    'nh8x97z': 'Pro-Rebase',      # 26 - edgmnt_net
    'nh98ltu': 'Pro-Rebase',      # 27 - xenomachina
    'nhe51h9': 'Pro-Rebase',      # 28 - edgmnt_net
    'nhebuka': 'Pro-Rebase',      # 29 - xenomachina
    'nhduoc4': 'Pro-Rebase',      # 37 - MisterSincere
    'nh1rhrz': 'Pro-Rebase',      # 30 - Shadowratenator (question but pro-rebase leaning)
    'nh67f0b': 'Pro-Rebase',      # 31 - LysanderStorm
    'nh1slo5': 'Pro-Rebase',      # 34 - Affectionate-Egg7566
    'nh3fv8u': 'Pro-Rebase',      # 35 - Fun-Title7656 (question but context is pro-rebase)
    'nh16pva': 'Pro-Rebase',      # 43 - CoachBigSammich
    'nh30hyp': 'Pro-Rebase',      # 44 - snowsayer
    'nh43va8': 'Pro-Rebase',      # 45 - Logical_Angle2935
    'nhbups7': 'Pro-Rebase',      # 46 - towncalledfargo
    'nho1c2s': 'Pro-Rebase',      # 50 - MiscreatedFan123
    'nho223h': 'Pro-Rebase',      # 51 - FlipperBumperKickout
    'nho2tql': 'Pro-Rebase',      # 52 - MiscreatedFan123
    'nh1c7xg': 'Pro-Rebase',      # 53 - AttentionSuspension
    'nh3wjyy': 'Pro-Rebase',      # 54 - Daholli
    'nh55bdi': 'Pro-Rebase',      # 55 - AttentionSuspension
    'nh1w7cj': 'Pro-Rebase',      # 63 - AttentionSuspension
    'nh33f2j': 'Pro-Rebase',      # 64 - tonecc
    'nh54p5m': 'Pro-Rebase',      # 65 - AttentionSuspension
    'nhotbz5': 'Pro-Rebase',      # 67 - tonecc
    'nh1omy4': 'Pro-Rebase',      # 62 - tonecc
    'nh1xi0h': 'Pro-Rebase',      # 74 - waterkip
    'nh2mjad': 'Pro-Rebase',      # 75 - wildjokers
    'nh2o5d6': 'Pro-Rebase',      # 76 - waterkip
    'nh4y9f5': 'Pro-Rebase',      # 82 - waterkip
    'nh1xv8t': 'Pro-Rebase',      # 83 - AttentionSuspension
    'nh20up5': 'Pro-Rebase',      # 84 - Conscious_Support176
    'nh21f9b': 'Pro-Rebase',      # 85 - AttentionSuspension
    'nh1t4ou': 'Pro-Rebase',      # 116 - kenpaicat
    'nh1umfl': 'Pro-Rebase',      # 117 - AttentionSuspension
    'nh1d4hc': 'Pro-Rebase',      # 110 - AttentionSuspension
    'nh8mwpc': 'Pro-Rebase',      # 125 - UrGuardian4ngel
    'nh53sro': 'Pro-Rebase',      # 143 - AttentionSuspension
    'nh2tihx': 'Pro-Rebase',      # 144 - gnivol
    'nh5436n': 'Pro-Rebase',      # 145 - AttentionSuspension
    'nh1fa52': 'Pro-Rebase',      # 150 - AttentionSuspension
    'nh54e4o': 'Pro-Rebase',      # 152 - AttentionSuspension
    'nh1gm2k': 'Pro-Rebase',      # 154 - AttentionSuspension
    'nh1jdjo': 'Pro-Rebase',      # 185 - AttentionSuspension
    'nh1k6na': 'Pro-Rebase',      # 187 - AttentionSuspension
    'nh1uujl': 'Pro-Rebase',      # 189 - AttentionSuspension
    'nh20cv2': 'Pro-Rebase',      # 190 - IamYourGrace
    'nh20kqr': 'Pro-Rebase',      # 191 - AttentionSuspension
    'nh29pjb': 'Pro-Rebase',      # 192 - RaniAgus
    'nh2a46g': 'Pro-Rebase',      # 193 - AttentionSuspension
    'nh2jhn8': 'Pro-Rebase',      # 195 - AttentionSuspension
    'nh4zv40': 'Pro-Rebase',      # 196 - indeox
    'nh2k3m1': 'Pro-Rebase',      # 198 - AttentionSuspension
    'nh35uis': 'Pro-Rebase',      # 199 - donkthemagicllama
    'nh54soh': 'Pro-Rebase',      # 200 - AttentionSuspension
    'nh3e57a': 'Pro-Rebase',      # 201 - human_289
    'nh54ue6': 'Pro-Rebase',      # 202 - AttentionSuspension
    'nh3x6px': 'Pro-Rebase',      # 203 - ItsDotin
    'nh55cr5': 'Pro-Rebase',      # 204 - AttentionSuspension
    'nh43qim': 'Pro-Rebase',      # 205 - jameshearttech
    'nh55r0g': 'Pro-Rebase',      # 206 - AttentionSuspension
    'nh59y4z': 'Pro-Rebase',      # 207 - jameshearttech
    'nh5cut9': 'Pro-Rebase',      # 208 - AttentionSuspension
    'nh55tkn': 'Pro-Rebase',      # 209 - AttentionSuspension
    'nh56fd0': 'Pro-Rebase',      # 212 - AttentionSuspension
    'nh56iql': 'Pro-Rebase',      # 214 - AttentionSuspension
    'nh56nmp': 'Pro-Rebase',      # 216 - AttentionSuspension
    'nh56tpz': 'Pro-Rebase',      # 218 - AttentionSuspension
    'nh56x4w': 'Pro-Rebase',      # 221 - AttentionSuspension
    'nh572pr': 'Pro-Rebase',      # 223 - AttentionSuspension
    'nh57hl0': 'Pro-Rebase',      # 224 - ScaredInvestment1571
    'nh58fqe': 'Pro-Rebase',      # 225 - AttentionSuspension
    'nh5e371': 'Pro-Rebase',      # 226 - ScaredInvestment1571
    'nh5eio0': 'Pro-Rebase',      # 227 - AttentionSuspension
    'nh75vn7': 'Pro-Rebase',      # 231 - AttentionSuspension
    'nh7k8jz': 'Pro-Rebase',      # 232 - AttentionSuspension
    'nh7n6xx': 'Pro-Rebase',      # 233 - AttentionSuspension
    'nh766bp': 'Pro-Rebase',      # 234 - AttentionSuspension
    'nh7wtc1': 'Pro-Rebase',      # 237 - Engineer-Coder
    'nh7yhfi': 'Pro-Rebase',      # 238 - AttentionSuspension
    'nh8ccbm': 'Pro-Rebase',      # 240 - Prestigious-Fox-8782
    'nh8ilec': 'Pro-Rebase',      # 241 - AttentionSuspension
    'nhbx4re': 'Pro-Rebase',      # 243 - AttentionSuspension
    'nhbyhqy': 'Pro-Rebase',      # 245 - AttentionSuspension
    'nhbzo5o': 'Pro-Rebase',      # 248 - AttentionSuspension
    'nhdgj0b': 'Pro-Rebase',      # 251 - AttentionSuspension
    'nhdhw0h': 'Pro-Rebase',      # 252 - AttentionSuspension
    'nhdtftq': 'Pro-Rebase',      # 255 - AttentionSuspension
    'nhi7ygs': 'Pro-Rebase',      # 257 - AttentionSuspension
    'nhrf3wc': 'Pro-Rebase',      # 261 - AttentionSuspension
    'nhrgj6g': 'Pro-Rebase',      # 263 - AttentionSuspension
    'nhrhfpy': 'Pro-Rebase',      # 265 - AttentionSuspension
    'nhrj07g': 'Pro-Rebase',      # 267 - AttentionSuspension
    'nhx3dnb': 'Pro-Rebase',      # 269 - AttentionSuspension
    'nhtabso': 'Pro-Rebase',      # 270 - Specialist_Guava_416
    'nh1gvnt': 'Pro-Rebase',      # 278 - AttentionSuspension
    'nh21k89': 'Pro-Rebase',      # 285 - AttentionSuspension
    'nh54gpv': 'Pro-Rebase',      # 287 - AttentionSuspension
    'nh1fkdz': 'Pro-Rebase',      # 331 - AttentionSuspension
    'nh1kj4q': 'Pro-Rebase',      # 333 - AttentionSuspension
    'nh556n0': 'Pro-Rebase',      # 337 - AttentionSuspension
    'nh1bd8i': 'Pro-Rebase',      # 353 - AttentionSuspension
    'nh761lb': 'Pro-Rebase',      # 356 - AttentionSuspension
    'nh7aeow': 'Pro-Rebase',      # 358 - AttentionSuspension
    
    # Disagreement / Pro-Merge
    'nh1lx67': 'Pro-Merge',       # 9 - Affectionate-Egg7566
    'nh6h45s': 'Pro-Merge',       # 20 - lottspot
    'nh792dp': 'Pro-Merge',       # 22 - lottspot
    'nh7p8rx': 'Pro-Merge',       # 24 - lottspot
    'nh9fws4': 'Pro-Merge',       # 33 - Trawling_
    'nh1slo5': 'Pro-Merge',       # 35 - Affectionate-Egg7566 (wait, this is pro-rebase actually)
    'nh10jm7': 'Pro-Merge',       # 56 - PM_ME_A_STEAM_GIFT
    'nh1dlfq': 'Pro-Merge',       # 57 - AttentionSuspension (wait, this is OP's reaction)
    'nh1s6os': 'Pro-Merge',       # 58 - PM_ME_A_STEAM_GIFT
    'nh1uh9n': 'Pro-Merge',       # 59 - AttentionSuspension
    'nh1vpot': 'Pro-Merge',       # 60 - PM_ME_A_STEAM_GIFT
    'nh1vyk7': 'Pro-Merge',       # 61 - PM_ME_A_STEAM_GIFT
    'nh0xx1i': 'Pro-Merge',       # 68 - homezlice
    'nh1msez': 'Pro-Merge',       # 70 - EmbeddedSwDev
    'nh1ytmj': 'Pro-Merge',       # 72 - omicronCloud8
    'nh1bjj6': 'Pro-Merge',       # 73 - AttentionSuspension
    'nh2mjad': 'Pro-Merge',       # 75 - wildjokers
    'nh3ksxr': 'Pro-Merge',       # 77 - EishLekker
    'nh3n7ll': 'Pro-Merge',       # 79 - EishLekker
    'nh3q4w0': 'Pro-Merge',       # 80 - waterkip
    'nh3s5ip': 'Pro-Merge',       # 81 - EishLekker
    'nh17c48': 'Pro-Merge',       # 88 - cgoldberg
    'nh18wnk': 'Pro-Merge',       # 89 - RobotJonesDad
    'nh5i6r0': 'Pro-Merge',       # 90 - ScaredInvestment1571
    'nh6my8u': 'Pro-Merge',       # 91 - RobotJonesDad
    'nh6o20s': 'Pro-Merge',       # 92 - ScaredInvestment1571
    'nh6tuhu': 'Pro-Merge',       # 93 - RobotJonesDad
    'nh694zx': 'Pro-Merge',       # 97 - DancesWithGnomes
    'nh762l1': 'Pro-Merge',       # 98 - cgoldberg
    'nh8gc1u': 'Pro-Merge',       # 99 - Sensitive_Tear110
    'nhmwjdq': 'Pro-Merge',       # 100 - samettinho
    'nh3gaon': 'Pro-Merge',       # 101 - EishLekker
    'nh3jw7c': 'Pro-Merge',       # 102 - cgoldberg
    'nh3mvyb': 'Pro-Merge',       # 103 - EishLekker
    'nh3rmuj': 'Pro-Merge',       # 104 - cgoldberg
    'nh3shis': 'Pro-Merge',       # 105 - EishLekker
    'nh46m72': 'Pro-Merge',       # 106 - cgoldberg
    'nh4wr5k': 'Pro-Merge',       # 107 - the_0rly_factor
    'nh4xhp1': 'Pro-Merge',       # 108 - cgoldberg
    'ni7mlay': 'Pro-Merge',       # 109 - CpnStumpy
    'nh26yvt': 'Pro-Merge',       # 112 - newprince
    'nygj3nu': 'Pro-Merge',       # 113 - SheSaidTechno
    'nh1f6xk': 'Pro-Merge',       # 114 - Charming-Designer944
    'nh12p3p': 'Pro-Merge',       # 115 - mesonofgib
    'nh24jr9': 'Pro-Merge',       # 118 - RarestSolanum
    'nh2oahm': 'Pro-Merge',       # 120 - RarestSolanum
    'nhc6yel': 'Pro-Merge',       # 126 - timtody
    'nh2sfr1': 'Pro-Merge',       # 127 - zaitsman
    'nh540ok': 'Pro-Merge',       # 128 - AttentionSuspension
    'nh56b1x': 'Pro-Merge',       # 129 - zaitsman
    'nh72bmt': 'Pro-Merge',       # 130 - remy_porter
    'nh9el04': 'Pro-Merge',       # 131 - FarkCookies
    'nh9n2zy': 'Pro-Merge',       # 132 - FarkCookies
    'nh8ca71': 'Pro-Merge',       # 133 - remy_porter
    'nh8xfz7': 'Pro-Merge',       # 134 - zaitsman
    'nh9ejyu': 'Pro-Merge',       # 135 - remy_porter
    'nh9h8fy': 'Pro-Merge',       # 136 - zaitsman
    'nha5k1o': 'Pro-Merge',       # 137 - remy_porter
    'nha8g4f': 'Pro-Merge',       # 138 - zaitsman
    'nhd6yyw': 'Pro-Merge',       # 139 - remy_porter
    'nhe77mp': 'Pro-Merge',       # 140 - remy_porter
    'nh8x8w4': 'Pro-Merge',       # 141 - zaitsman
    'nh2qvcc': 'Pro-Merge',       # 142 - TheSodesa
    'nh13agx': 'Pro-Merge',       # 146 - gcwieser
    'nh1h4h7': 'Pro-Merge',       # 147 - kor_the_fiend
    'nh1hoxd': 'Pro-Merge',       # 148 - gcwieser
    'nh231fl': 'Pro-Merge',       # 149 - Wiikend
    'nh2vv4q': 'Pro-Merge',       # 151 - HolmesMalone
    'nh1g6zk': 'Pro-Merge',       # 153 - gcwieser
    'nh1km07': 'Pro-Merge',       # 155 - gcwieser
    'nh23oj2': 'Pro-Merge',       # 156 - Wiikend
    'nh25lfz': 'Pro-Merge',       # 157 - gcwieser
    'nh3ml8z': 'Pro-Merge',       # 158 - EishLekker
    'nh3omhf': 'Pro-Merge',       # 159 - gcwieser
    'nh1tzaq': 'Pro-Merge',       # 160 - Conscious_Support176
    'nh2n5s0': 'Pro-Merge',       # 161 - wildjokers
    'nh2tgm3': 'Pro-Merge',       # 162 - Conscious_Support176
    'nh1wcf9': 'Pro-Merge',       # 163 - gcwieser
    'nh348lv': 'Pro-Merge',       # 164 - Conscious_Support176
    'nh3di70': 'Pro-Merge',       # 165 - gcwieser
    'nh3fsbh': 'Pro-Merge',       # 166 - Conscious_Support176
    'nh3kwfh': 'Pro-Merge',       # 167 - gcwieser
    'nh55348': 'Pro-Merge',       # 168 - Conscious_Support176
    'nh6kcwz': 'Pro-Merge',       # 169 - gcwieser
    'nh6obgy': 'Pro-Merge',       # 170 - Conscious_Support176
    'nh1lkzz': 'Pro-Merge',       # 171 - evo_zorro
    'nh10fa4': 'Pro-Merge',       # 172 - m39583
    'nh1uixi': 'Pro-Merge',       # 173 - Conscious_Support176
    'nh1y5p9': 'Pro-Merge',       # 174 - m39583
    'nh2z8ab': 'Pro-Merge',       # 175 - Conscious_Support176
    'nh2qs40': 'Pro-Merge',       # 176 - wildjokers
    'nh2tw75': 'Pro-Merge',       # 177 - Conscious_Support176
    'nh4z28w': 'Pro-Merge',       # 178 - lmoelleb
    'nh11fqq': 'Pro-Merge',       # 179 - kagato87
    'nh1ef6s': 'Pro-Merge',       # 180 - Ok-Ostrich44
    'nh1eque': 'Pro-Merge',       # 181 - AttentionSuspension
    'nh1fbfm': 'Pro-Merge',       # 182 - m39583
    'nh1j1m5': 'Pro-Merge',       # 183 - AttentionSuspension
    'nh1fgpq': 'Pro-Merge',       # 184 - JauriXD
    'nh1gt6j': 'Pro-Merge',       # 186 - Drugbird
    'nh1sa2i': 'Pro-Merge',       # 188 - sshetty03
    'nh2dqzl': 'Pro-Merge',       # 194 - wildjokers
    'nh2i2np': 'Pro-Merge',       # 197 - Kraigius
    'nh2nxo3': 'Pro-Merge',       # wait, this was already assigned
    'nh4jwzm': 'Pro-Merge',       # 210 - kilkil
    'nh4x19e': 'Pro-Merge',       # 215 - the_0rly_factor
    'nh4xizv': 'Pro-Merge',       # 217 - lmoelleb
    'nh5w5wg': 'Pro-Merge',       # 219 - lmoelleb
    'nh503kk': 'Pro-Merge',       # 220 - the6thReplicant
    'nh551dq': 'Pro-Merge',       # 222 - Infamous_Ticket9084
    'nh5tpqk': 'Pro-Merge',       # 229 - czenst
    'nh6jlwb': 'Pro-Merge',       # 230 - Safe_Trouble_2140
    'nh72ktb': 'Pro-Merge',       # 235 - remy_porter
    'nh7wtc1': 'Pro-Merge',       # 237 - Engineer-Coder
    'nh8318p': 'Pro-Merge',       # 239 - macbig273
    'nh9wu5k': 'Pro-Merge',       # 242 - jcbinet1
    'nhbdhbb': 'Pro-Merge',       # 244 - Old-Confection-5129
    'nhbedyi': 'Pro-Merge',       # 246 - scally501
    'nhbfo59': 'Pro-Merge',       # 247 - boatsydney
    'nhbifnv': 'Pro-Merge',       # 249 - nraw
    'nhdejat': 'Pro-Merge',       # 250 - dannuic
    'nhds05c': 'Pro-Merge',       # 253 - dannuic
    'nhdt5y0': 'Pro-Merge',       # 254 - MisterSincere
    'nhhk303': 'Pro-Merge',       # 256 - SuperAdminIsTraitor
    'nhkdgmy': 'Pro-Merge',       # 258 - SuperAdminIsTraitor
    'nhimz0w': 'Pro-Merge',       # 259 - Medical_Amount3007
    'nhlvehe': 'Pro-Merge',       # 260 - Intelligent-Chain423
    'nhofu5o': 'Pro-Merge',       # 262 - someouterboy
    'nhomo6i': 'Pro-Merge',       # 264 - Kjoep
    'nhoyz2w': 'Pro-Merge',       # 266 - Tango1777
    'nhr5f58': 'Pro-Merge',       # 268 - grosser_zampano
    'nh16n9i': 'Pro-Merge',       # 272 - efalk
    'nh2v65w': 'Pro-Merge',       # 275 - efalk
    'nh2q1rg': 'Pro-Merge',       # 276 - universaluniqueid
    'nh1gdap': 'Pro-Merge',       # 277 - mfontani
    'nh534zk': 'Pro-Merge',       # 279 - mfontani
    'nh17y0n': 'Pro-Merge',       # 280 - TrickTimely3242
    'nh21gf4': 'Pro-Merge',       # 284 - OrcaFlux
    'nh2wrpi': 'Pro-Merge',       # 286 - trimorphic
    'nh497zu': 'Pro-Merge',       # 288 - jirka642
    'nh49nc9': 'Pro-Merge',       # 290 - clinnkkk_
    'nhb4xce': 'Pro-Merge',       # 291 - frisedel
    'nhcaqj1': 'Pro-Merge',       # 293 - frisedel
    'nhbd8uc': 'Pro-Merge',       # 294 - TheExodu5
    'nhcxtoh': 'Pro-Merge',       # 296 - AmphibianFrog
    'nhdeota': 'Pro-Merge',       # 297 - AmphibianFrog
    'nhfft1x': 'Pro-Merge',       # 300 - sobservation
    'nhhzewh': 'Pro-Merge',       # 301 - armujahid
    'nhiep7f': 'Pro-Merge',       # 303 - armujahid
    'nhin4wm': 'Pro-Merge',       # 304 - Medical_Amount3007
    'nhmvwox': 'Pro-Merge',       # 305 - samettinho
    'nhn8jcr': 'Pro-Merge',       # 307 - DoctorOriginal7309
    'nhnffqq': 'Pro-Merge',       # 308 - itsdarkcloudtv
    'nhohkku': 'Pro-Merge',       # 310 - abundant_singularity
    'nhohox6': 'Pro-Merge',       # 311 - PrestigiousAnt3766
    'nhrhap7': 'Pro-Merge',       # 312 - AttentionSuspension
    'nhruvod': 'Pro-Merge',       # 313 - PrestigiousAnt3766
    'nhowopd': 'Pro-Merge',       # 314 - mmcnl
    'nhrhsxk': 'Pro-Merge',       # 315 - AttentionSuspension
    'nhri20w': 'Pro-Merge',       # 316 - mmcnl
    'nhp8znp': 'Pro-Merge',       # 317 - Rguttersohn
    'nhr1ddy': 'Pro-Merge',       # 318 - kiwi-kaiser
    'ouxn089': 'Pro-Merge',       # 319 - michaelobriena
    'nh17p7t': 'Pro-Merge',       # 320 - RedEyed__
    'nh2876j': 'Pro-Merge',       # 321 - immediacyofjoy
    'nh2jljn': 'Pro-Merge',       # 322 - RedEyed__
    'nh2ot95': 'Pro-Merge',       # 323 - wildjokers
    'nh3irs0': 'Pro-Merge',       # 324 - EishLekker
    'nh3t2uj': 'Pro-Merge',       # 325 - wildjokers
    'nh4xhhg': 'Pro-Merge',       # 326 - RedEyed__
    'nh50m98': 'Pro-Merge',       # 327 - indeox
    'nhddpqu': 'Pro-Merge',       # 328 - elephantdingo
    'nh11ipj': 'Pro-Merge',       # 329 - Icy_Physics51
    'nh15jmg': 'Pro-Merge',       # 330 - dbear496
    'nh165a2': 'Pro-Merge',       # 332 - divad1196
    'nh1kj4q': 'Pro-Merge',       # 334 - divad1196
    'nh3pz7g': 'Pro-Merge',       # 335 - senfiaj
    'nh3tjbe': 'Pro-Merge',       # 336 - gororuns
    'nh14fvn': 'Pro-Merge',       # 338 - mgruner
    'nh2r4zu': 'Pro-Merge',       # 339 - wildjokers
    'nh3ikjg': 'Pro-Merge',       # 340 - mgruner
    'nh3tood': 'Pro-Merge',       # 341 - wildjokers
    'nh4ky5i': 'Pro-Merge',       # 342 - mgruner
    'nh6gai6': 'Pro-Merge',       # 343 - wildjokers
    'nh189lt': 'Pro-Merge',       # 344 - Drugbird
    'nh19x7c': 'Pro-Merge',       # 345 - mgruner
    'nh1h2nj': 'Pro-Merge',       # 346 - Drugbird
    'nh3if9i': 'Pro-Merge',       # 347 - mgruner
    'nh55gjt': 'Pro-Merge',       # 348 - Drugbird
    'nh9lr3x': 'Pro-Merge',       # 349 - mgruner
    'nhbf5kd': 'Pro-Merge',       # 350 - Drugbird
    'nh130c5': 'Pro-Merge',       # 351 - darkest_ruby
    'nh1ak9k': 'Pro-Merge',       # 352 - endymion1818-1819
    'nh3i0cn': 'Pro-Merge',       # 354 - Comprehensive-Pea812
    'nh6ugb8': 'Pro-Merge',       # 355 - baicoi66
    'nh771dn': 'Pro-Merge',       # 357 - baicoi66
    
    # Nuanced / Context-Dependent
    'nhpp9ip': 'Nuanced',         # 7 - iOSCaleb
    'nhpqnov': 'Nuanced',         # 8 - vermiculus
    'nh6h45s': 'Nuanced',         # 20 - lottspot (wait, already in Pro-Merge)
    'nh750gu': 'Nuanced',         # 21 - xenomachina
    'nh10jm7': 'Nuanced',         # 56 - PM_ME_A_STEAM_GIFT (wait, already in Pro-Merge)
    'nh1s6os': 'Nuanced',         # 58 - PM_ME_A_STEAM_GIFT (wait, already in Pro-Merge)
    'nh1uh9n': 'Nuanced',         # 59 - AttentionSuspension (wait, already in Pro-Merge)
    'nh1vpot': 'Nuanced',         # 60 - PM_ME_A_STEAM_GIFT (wait, already in Pro-Merge)
    'nh1vyk7': 'Nuanced',         # 61 - PM_ME_A_STEAM_GIFT (wait, already in Pro-Merge)
    'nh1omy4': 'Nuanced',         # 62 - tonecc
    'nh1bjj6': 'Nuanced',         # 73 - AttentionSuspension (wait, already in Pro-Merge)
    'nh3l7il': 'Nuanced',         # 78 - waterkip
    'nh3n7ll': 'Nuanced',         # 79 - EishLekker (wait, already in Pro-Merge)
    'nh3q4w0': 'Nuanced',         # 80 - waterkip (wait, already in Pro-Merge)
    'nh3s5ip': 'Nuanced',         # 81 - EishLekker (wait, already in Pro-Merge)
    'nh2wptt': 'Nuanced',         # 86 - Conscious_Support176
    'nh0zlvw': 'Nuanced',         # 87 - ars0nisfun
    'nh5i6r0': 'Nuanced',         # 90 - ScaredInvestment1571 (wait, already in Pro-Merge)
    'nh6my8u': 'Nuanced',         # 91 - RobotJonesDad (wait, already in Pro-Merge)
    'nh6o20s': 'Nuanced',         # 92 - ScaredInvestment1571 (wait, already in Pro-Merge)
    'nh6tuhu': 'Nuanced',         # 93 - RobotJonesDad (wait, already in Pro-Merge)
    'nh18y68': 'Nuanced',         # 94 - ImTheRealCryten
    'nh12p3p': 'Nuanced',         # 115 - mesonofgib
    'nh2t3ud': 'Nuanced',         # 121 - Wiikend
    'nh331up': 'Nuanced',         # 122 - MrMelon54
    'nh33cyw': 'Nuanced',         # 123 - MrMelon54
    'nh8mwpc': 'Nuanced',         # 125 - UrGuardian4ngel (wait, already in Pro-Rebase)
    'nhc6yel': 'Nuanced',         # 126 - timtody
    'nh540ok': 'Nuanced',         # 128 - AttentionSuspension (wait, already in Pro-Merge)
    'nh56b1x': 'Nuanced',         # 129 - zaitsman (wait, already in Pro-Merge)
    'nh9el04': 'Nuanced',         # 131 - FarkCookies (wait, already in Pro-Merge)
    'nh9n2zy': 'Nuanced',         # 132 - FarkCookies (wait, already in Pro-Merge)
    'nh8ca71': 'Nuanced',         # 133 - remy_porter (wait, already in Pro-Merge)
    'nh8xfz7': 'Nuanced',         # 134 - zaitsman (wait, already in Pro-Merge)
    'nh9ejyu': 'Nuanced',         # 135 - remy_porter (wait, already in Pro-Merge)
    'nh9h8fy': 'Nuanced',         # 136 - zaitsman (wait, already in Pro-Merge)
    'nha5k1o': 'Nuanced',         # 137 - remy_porter (wait, already in Pro-Merge)
    'nha8g4f': 'Nuanced',         # 138 - zaitsman (wait, already in Pro-Merge)
    'nhd6yyw': 'Nuanced',         # 139 - remy_porter (wait, already in Pro-Merge)
    'nhe77mp': 'Nuanced',         # 140 - remy_porter (wait, already in Pro-Merge)
    'nh8x8w4': 'Nuanced',         # 141 - zaitsman (wait, already in Pro-Merge)
    'nh1lkzz': 'Nuanced',         # 171 - evo_zorro
    'nh1uixi': 'Nuanced',         # 173 - Conscious_Support176
    'nh1y5p9': 'Nuanced',         # 174 - m39583
    'nh2z8ab': 'Nuanced',         # 175 - Conscious_Support176
    'nh2qs40': 'Nuanced',         # 176 - wildjokers
    'nh2tw75': 'Nuanced',         # 177 - Conscious_Support176
    'nh4z28w': 'Nuanced',         # 178 - lmoelleb
    'nh11fqq': 'Nuanced',         # 179 - kagato87
    'nh1ef6s': 'Nuanced',         # 180 - Ok-Ostrich44
    'nh1eque': 'Nuanced',         # 181 - AttentionSuspension
    'nh1fbfm': 'Nuanced',         # 182 - m39583
    'nh1j1m5': 'Nuanced',         # 183 - AttentionSuspension
    'nh1fgpq': 'Nuanced',         # 184 - JauriXD
    'nh1gt6j': 'Nuanced',         # 186 - Drugbird
    'nh1sa2i': 'Nuanced',         # 188 - sshetty03
    'nh2dqzl': 'Nuanced',         # 194 - wildjokers
    'nh2i2np': 'Nuanced',         # 197 - Kraigius
    'nh2nxo3': 'Nuanced',         # 11 - remy_porter (already in Pro-Rebase)
    'nh4jwzm': 'Nuanced',         # 210 - kilkil
    'nh4mbzd': 'Nuanced',         # 211 - glasswings363
    'nh4rgx8': 'Nuanced',         # 213 - spenpal_dev
    'nh4x19e': 'Nuanced',         # 215 - the_0rly_factor
    'nh4xizv': 'Nuanced',         # 217 - lmoelleb
    'nh5w5wg': 'Nuanced',         # 219 - lmoelleb
    'nh503kk': 'Nuanced',         # 220 - the6thReplicant
    'nh551dq': 'Nuanced',         # 222 - Infamous_Ticket9084
    'nh5tpqk': 'Nuanced',         # 229 - czenst
    'nh6jlwb': 'Nuanced',         # 230 - Safe_Trouble_2140
    'nh7wtc1': 'Nuanced',         # 237 - Engineer-Coder (already in Pro-Merge)
    'nh8318p': 'Nuanced',         # 239 - macbig273
    'nh9wu5k': 'Nuanced',         # 242 - jcbinet1
    'nhbd8uc': 'Nuanced',         # 294 - TheExodu5
    'nhbfo59': 'Nuanced',         # 247 - boatsydney
    'nhbifnv': 'Nuanced',         # 249 - nraw
    'nhdejat': 'Nuanced',         # 250 - dannuic
    'nhdt5y0': 'Nuanced',         # 254 - MisterSincere
    'nhhk303': 'Nuanced',         # 256 - SuperAdminIsTraitor (already in Pro-Merge)
    'nhkdgmy': 'Nuanced',         # 258 - SuperAdminIsTraitor (already in Pro-Merge)
    'nhimz0w': 'Nuanced',         # 259 - Medical_Amount3007 (already in Pro-Merge)
    'nhlvehe': 'Nuanced',         # 260 - Intelligent-Chain423 (already in Pro-Merge)
    'nhofu5o': 'Nuanced',         # 262 - someouterboy
    'nhomo6i': 'Nuanced',         # 264 - Kjoep
    'nhoyz2w': 'Nuanced',         # 266 - Tango1777
    'nhr5f58': 'Nuanced',         # 268 - grosser_zampano
    'nhtabso': 'Nuanced',         # 270 - Specialist_Guava_416
    'nimpwqk': 'Nuanced',         # 271 - Few_Personality1741
    'nh16n9i': 'Nuanced',         # 272 - efalk (already in Pro-Merge)
    'nh1su3j': 'Nuanced',         # 273 - Conscious_Support176
    'nh1lke0': 'Nuanced',         # 274 - malcolm-maya
    'nh2v65w': 'Nuanced',         # 275 - efalk (already in Pro-Merge)
    'nh2q1rg': 'Nuanced',         # 276 - universaluniqueid (already in Pro-Merge)
    'nh1gdap': 'Nuanced',         # 277 - mfontani
    'nh534zk': 'Nuanced',         # 279 - mfontani
    'nh19o31': 'Nuanced',         # 281 - Tsiangkun
    'nh1aid4': 'Nuanced',         # 282 - Tsiangkun
    'nh1ag2v': 'Nuanced',         # 283 - giminik
    'nh2wrpi': 'Nuanced',         # 286 - trimorphic
    'nh49nc9': 'Nuanced',         # 290 - clinnkkk_
    'nhb4xce': 'Nuanced',         # 291 - frisedel (already in Pro-Merge)
    'nhcaqj1': 'Nuanced',         # 293 - frisedel (already in Pro-Merge)
    'nhcxtoh': 'Nuanced',         # 296 - AmphibianFrog (already in Pro-Merge)
    'nhdeota': 'Nuanced',         # 297 - AmphibianFrog (already in Pro-Merge)
    'nhhzewh': 'Nuanced',         # 301 - armujahid
    'nhiep7f': 'Nuanced',         # 303 - armujahid
    'nhn8jcr': 'Nuanced',         # 307 - DoctorOriginal7309 (already in Pro-Merge)
    'nhnffqq': 'Nuanced',         # 308 - itsdarkcloudtv (already in Pro-Merge)
    'nhohkku': 'Nuanced',         # 310 - abundant_singularity
    'nhohox6': 'Nuanced',         # 311 - PrestigiousAnt3766 (already in Pro-Merge)
    'nhrhap7': 'Nuanced',         # 312 - AttentionSuspension (already in Pro-Merge)
    'nhruvod': 'Nuanced',         # 313 - PrestigiousAnt3766 (already in Pro-Merge)
    'nhowopd': 'Nuanced',         # 314 - mmcnl (already in Pro-Merge)
    'nhrhsxk': 'Nuanced',         # 315 - AttentionSuspension (already in Pro-Merge)
    'nhri20w': 'Nuanced',         # 316 - mmcnl (already in Pro-Merge)
    'nhp8znp': 'Nuanced',         # 317 - Rguttersohn
    'nhr1ddy': 'Nuanced',         # 318 - kiwi-kaiser
    'ouxn089': 'Nuanced',         # 319 - michaelobriena
    'nh17p7t': 'Nuanced',         # 320 - RedEyed__ (already in Pro-Merge)
    'nh2876j': 'Nuanced',         # 321 - immediacyofjoy
    'nh2jljn': 'Nuanced',         # 322 - RedEyed__ (already in Pro-Merge)
    'nh2ot95': 'Nuanced',         # 323 - wildjokers (already in Pro-Merge)
    'nh3irs0': 'Nuanced',         # 324 - EishLekker (already in Pro-Merge)
    'nh3t2uj': 'Nuanced',         # 325 - wildjokers (already in Pro-Merge)
    'nh4xhhg': 'Nuanced',         # 326 - RedEyed__ (already in Pro-Merge)
    'nh50m98': 'Nuanced',         # 327 - indeox (already in Pro-Merge)
    'nhddpqu': 'Nuanced',         # 328 - elephantdingo (already in Pro-Merge)
    'nh11ipj': 'Nuanced',         # 329 - Icy_Physics51
    'nh15jmg': 'Nuanced',         # 330 - dbear496
    'nh165a2': 'Nuanced',         # 332 - divad1196 (already in Pro-Merge)
    'nh1kj4q': 'Nuanced',         # 334 - divad1196 (already in Pro-Merge)
    'nh3pz7g': 'Nuanced',         # 335 - senfiaj
    'nh3tjbe': 'Nuanced',         # 336 - gororuns (already in Pro-Merge)
    'nh14fvn': 'Nuanced',         # 338 - mgruner (already in Pro-Merge)
    'nh2r4zu': 'Nuanced',         # 339 - wildjokers (already in Pro-Merge)
    'nh3ikjg': 'Nuanced',         # 340 - mgruner (already in Pro-Merge)
    'nh3tood': 'Nuanced',         # 341 - wildjokers (already in Pro-Merge)
    'nh4ky5i': 'Nuanced',         # 342 - mgruner (already in Pro-Merge)
    'nh6gai6': 'Nuanced',         # 343 - wildjokers (already in Pro-Merge)
    'nh189lt': 'Nuanced',         # 344 - Drugbird (already in Pro-Merge)
    'nh19x7c': 'Nuanced',         # 345 - mgruner (already in Pro-Merge)
    'nh1h2nj': 'Nuanced',         # 346 - Drugbird (already in Pro-Merge)
    'nh3if9i': 'Nuanced',         # 347 - mgruner (already in Pro-Merge)
    'nh55gjt': 'Nuanced',         # 348 - Drugbird (already in Pro-Merge)
    'nh9lr3x': 'Nuanced',         # 349 - mgruner (already in Pro-Merge)
    'nhbf5kd': 'Nuanced',         # 350 - Drugbird (already in Pro-Merge)
    
    # Practical Tips & Workflows
    'nhpp9ip': 'Practical',        # 7 - iOSCaleb (already in Nuanced)
    'nh1lx67': 'Practical',        # 9 - Affectionate-Egg7566 (already in Pro-Merge)
    'nh1mo4k': 'Practical',        # 10 - timbar1234 (already in Pro-Rebase)
    'nh2nxo3': 'Practical',        # 11 - remy_porter (already in Pro-Rebase)
    'nhe8n1n': 'Practical',        # 38 - Shadowratenator
    'nh3fv8u': 'Practical',        # 35 - Fun-Title7656
    'jutarnji_prdez': 'Practical', # 36 - jutarnji_prdez
    'nh30hyp': 'Practical',        # 44 - snowsayer
    'nh43va8': 'Practical',        # 45 - Logical_Angle2935
    'nhbups7': 'Practical',        # 46 - towncalledfargo
    'nhi20gw': 'Practical',        # 48 - baloo____
    'nh1dlfq': 'Practical',        # 57 - AttentionSuspension
    'nh1s6os': 'Practical',        # 58 - PM_ME_A_STEAM_GIFT
    'nh1uh9n': 'Practical',        # 59 - AttentionSuspension
    'nh1vpot': 'Practical',        # 60 - PM_ME_A_STEAM_GIFT
    'nh1vyk7': 'Practical',        # 61 - PM_ME_A_STEAM_GIFT
    'nh1omy4': 'Practical',        # 62 - tonecc
    'nh1w7cj': 'Practical',        # 63 - AttentionSuspension
    'nh33f2j': 'Practical',        # 64 - tonecc
    'nh54p5m': 'Practical',        # 65 - AttentionSuspension
    'nhotbz5': 'Practical',        # 67 - tonecc
    'nh0xx1i': 'Practical',        # 68 - homezlice
    'nh1cdwp': 'Practical',        # 69 - homezlice
    'nh1xi0h': 'Practical',        # 74 - waterkip
    'nh2mjad': 'Practical',        # 75 - wildjokers
    'nh2o5d6': 'Practical',        # 76 - waterkip
    'nh3l7il': 'Practical',        # 78 - waterkip
    'nh3n7ll': 'Practical',        # 79 - EishLekker
    'nh3q4w0': 'Practical',        # 80 - waterkip
    'nh3s5ip': 'Practical',        # 81 - EishLekker
    'nh4y9f5': 'Practical',        # 82 - waterkip
    'nh1xv8t': 'Practical',        # 83 - AttentionSuspension
    'nh20up5': 'Practical',        # 84 - Conscious_Support176
    'nh21f9b': 'Practical',        # 85 - AttentionSuspension
    'nh2wptt': 'Practical',        # 86 - Conscious_Support176
    'nh0zlvw': 'Practical',        # 87 - ars0nisfun
    'nh17c48': 'Practical',        # 88 - cgoldberg
    'nh18wnk': 'Practical',        # 89 - RobotJonesDad
    'nh5i6r0': 'Practical',        # 90 - ScaredInvestment1571
    'nh6my8u': 'Practical',        # 91 - RobotJonesDad
    'nh6o20s': 'Practical',        # 92 - ScaredInvestment1571
    'nh6tuhu': 'Practical',        # 93 - RobotJonesDad
    'nh18y68': 'Practical',        # 94 - ImTheRealCryten
    'nh18uns': 'Practical',        # 95 - NotSelfAware
    'nh1o9je': 'Practical',        # 96 - Lor1an
    'nh694zx': 'Practical',        # 97 - DancesWithGnomes
    'nh762l1': 'Practical',        # 98 - cgoldberg
    'nh8gc1u': 'Practical',        # 99 - Sensitive_Tear110
    'nhmwjdq': 'Practical',        # 100 - samettinho
    'nh3gaon': 'Practical',        # 101 - EishLekker
    'nh3jw7c': 'Practical',        # 102 - cgoldberg
    'nh3mvyb': 'Practical',        # 103 - EishLekker
    'nh3rmuj': 'Practical',        # 104 - cgoldberg
    'nh3shis': 'Practical',        # 105 - EishLekker
    'nh46m72': 'Practical',        # 106 - cgoldberg
    'nh4wr5k': 'Practical',        # 107 - the_0rly_factor
    'nh4xhp1': 'Practical',        # 108 - cgoldberg
    'ni7mlay': 'Practical',        # 109 - CpnStumpy
    'nh1d4hc': 'Practical',        # 110 - AttentionSuspension
    'nh1do6w': 'Practical',        # 111 - sunshinefox_25
    'nh26yvt': 'Practical',        # 112 - newprince
    'nygj3nu': 'Practical',        # 113 - SheSaidTechno
    'nh1f6xk': 'Practical',        # 114 - Charming-Designer944
    'nh12p3p': 'Practical',        # 115 - mesonofgib
    'nh1t4ou': 'Practical',        # 116 - kenpaicat
    'nh1umfl': 'Practical',        # 117 - AttentionSuspension
    'nh24jr9': 'Practical',        # 118 - RarestSolanum
    'nh2oahm': 'Practical',        # 120 - RarestSolanum
    'nh2t3ud': 'Practical',        # 121 - Wiikend
    'nh331up': 'Practical',        # 122 - MrMelon54
    'nh33cyw': 'Practical',        # 123 - MrMelon54
    'nh53jgy': 'Practical',        # 124 - AttentionSuspension
    'nhc6yel': 'Practical',        # 126 - timtody
    'nh2sfr1': 'Practical',        # 127 - zaitsman
    'nh540ok': 'Practical',        # 128 - AttentionSuspension
    'nh56b1x': 'Practical',        # 129 - zaitsman
    'nh72bmt': 'Practical',        # 130 - remy_porter
    'nh9el04': 'Practical',        # 131 - FarkCookies
    'nh9n2zy': 'Practical',        # 132 - FarkCookies
    'nh8ca71': 'Practical',        # 133 - remy_porter
    'nh8xfz7': 'Practical',        # 134 - zaitsman
    'nh9ejyu': 'Practical',        # 135 - remy_porter
    'nh9h8fy': 'Practical',        # 136 - zaitsman
    'nha5k1o': 'Practical',        # 137 - remy_porter
    'nha8g4f': 'Practical',        # 138 - zaitsman
    'nhd6yyw': 'Practical',        # 139 - remy_porter
    'nhe77mp': 'Practical',        # 140 - remy_porter
    'nh8x8w4': 'Practical',        # 141 - zaitsman
    'nh2qvcc': 'Practical',        # 142 - TheSodesa
    'nh53sro': 'Practical',        # 143 - AttentionSuspension
    'nh2tihx': 'Practical',        # 144 - gnivol
    'nh5436n': 'Practical',        # 145 - AttentionSuspension
    'nh13agx': 'Practical',        # 146 - gcwieser
    'nh1h4h7': 'Practical',        # 147 - kor_the_fiend
    'nh1hoxd': 'Practical',        # 148 - gcwieser
    'nh231fl': 'Practical',        # 149 - Wiikend
    'nh2vv4q': 'Practical',        # 151 - HolmesMalone
    'nh54e4o': 'Practical',        # 152 - AttentionSuspension
    'nh1g6zk': 'Practical',        # 153 - gcwieser
    'nh1gm2k': 'Practical',        # 154 - AttentionSuspension
    'nh1km07': 'Practical',        # 155 - gcwieser
    'nh23oj2': 'Practical',        # 156 - Wiikend
    'nh25lfz': 'Practical',        # 157 - gcwieser
    'nh3ml8z': 'Practical',        # 158 - EishLekker
    'nh3omhf': 'Practical',        # 159 - gcwieser
    'nh1tzaq': 'Practical',        # 160 - Conscious_Support176
    'nh2n5s0': 'Practical',        # 161 - wildjokers
    'nh2tgm3': 'Practical',        # 162 - Conscious_Support176
    'nh1wcf9': 'Practical',        # 163 - gcwieser
    'nh348lv': 'Practical',        # 164 - Conscious_Support176
    'nh3di70': 'Practical',        # 165 - gcwieser
    'nh3fsbh': 'Practical',        # 166 - Conscious_Support176
    'nh3kwfh': 'Practical',        # 167 - gcwieser
    'nh55348': 'Practical',        # 168 - Conscious_Support176
    'nh6kcwz': 'Practical',        # 169 - gcwieser
    'nh6obgy': 'Practical',        # 170 - Conscious_Support176
    'nh1lkzz': 'Practical',        # 171 - evo_zorro
    'nh10fa4': 'Practical',        # 172 - m39583
    'nh1uixi': 'Practical',        # 173 - Conscious_Support176
    'nh1y5p9': 'Practical',        # 174 - m39583
    'nh2z8ab': 'Practical',        # 175 - Conscious_Support176
    'nh2qs40': 'Practical',        # 176 - wildjokers
    'nh2tw75': 'Practical',        # 177 - Conscious_Support176
    'nh4z28w': 'Practical',        # 178 - lmoelleb
    'nh11fqq': 'Practical',        # 179 - kagato87
    'nh1ef6s': 'Practical',        # 180 - Ok-Ostrich44
    'nh1eque': 'Practical',        # 181 - AttentionSuspension
    'nh1fbfm': 'Practical',        # 182 - m39583
    'nh1j1m5': 'Practical',        # 183 - AttentionSuspension
    'nh1fgpq': 'Practical',        # 184 - JauriXD
    'nh1k6na': 'Practical',        # 187 - AttentionSuspension
    'nh1sa2i': 'Practical',        # 188 - sshetty03
    'nh2dqzl': 'Practical',        # 194 - wildjokers
    'nh2i2np': 'Practical',        # 197 - Kraigius
    'nh2k3m1': 'Practical',        # 198 - AttentionSuspension
    'nh35uis': 'Practical',        # 199 - donkthemagicllama
    'nh54soh': 'Practical',        # 200 - AttentionSuspension
    'nh3e57a': 'Practical',        # 201 - human_289
    'nh54ue6': 'Practical',        # 202 - AttentionSuspension
    'nh3x6px': 'Practical',        # 203 - ItsDotin
    'nh55cr5': 'Practical',        # 204 - AttentionSuspension
    'nh43qim': 'Practical',        # 205 - jameshearttech
    'nh55r0g': 'Practical',        # 206 - AttentionSuspension
    'nh59y4z': 'Practical',        # 207 - jameshearttech
    'nh5cut9': 'Practical',        # 208 - AttentionSuspension
    'nh55tkn': 'Practical',        # 209 - AttentionSuspension
    'nh4jwzm': 'Practical',        # 210 - kilkil
    'nh4mbzd': 'Practical',        # 211 - glasswings363
    'nh56fd0': 'Practical',        # 212 - AttentionSuspension
    'nh4rgx8': 'Practical',        # 213 - spenpal_dev
    'nh56iql': 'Practical',        # 214 - AttentionSuspension
    'nh4x19e': 'Practical',        # 215 - the_0rly_factor
    'nh56nmp': 'Practical',        # 216 - AttentionSuspension
    'nh4xizv': 'Practical',        # 217 - lmoelleb
    'nh56tpz': 'Practical',        # 218 - AttentionSuspension
    'nh5w5wg': 'Practical',        # 219 - lmoelleb
    'nh503kk': 'Practical',        # 220 - the6thReplicant
    'nh56x4w': 'Practical',        # 221 - AttentionSuspension
    'nh551dq': 'Practical',        # 222 - Infamous_Ticket9084
    'nh572pr': 'Practical',        # 223 - AttentionSuspension
    'nh57hl0': 'Practical',        # 224 - ScaredInvestment1571
    'nh58fqe': 'Practical',        # 225 - AttentionSuspension
    'nh5e371': 'Practical',        # 226 - ScaredInvestment1571
    'nh5eio0': 'Practical',        # 227 - AttentionSuspension
    'nh5nssj': 'Practical',        # 228 - Inevitable_Exam_2177
    'nh5tpqk': 'Practical',        # 229 - czenst
    'nh6jlwb': 'Practical',        # 230 - Safe_Trouble_2140
    'nh75vn7': 'Practical',        # 231 - AttentionSuspension
    'nh7k8jz': 'Practical',        # 232 - AttentionSuspension
    'nh7n6xx': 'Practical',        # 233 - AttentionSuspension
    'nh766bp': 'Practical',        # 234 - AttentionSuspension
    'nh72ktb': 'Practical',        # 235 - remy_porter
    'nh76jp1': 'Practical',        # 236 - AttentionSuspension
    'nh7wtc1': 'Practical',        # 237 - Engineer-Coder
    'nh7yhfi': 'Practical',        # 238 - AttentionSuspension
    'nh8318p': 'Practical',        # 239 - macbig273
    'nh8ccbm': 'Practical',        # 240 - Prestigious-Fox-8782
    'nh8ilec': 'Practical',        # 241 - AttentionSuspension
    'nh9wu5k': 'Practical',        # 242 - jcbinet1
    'nhbx4re': 'Practical',        # 243 - AttentionSuspension
    'nhbdhbb': 'Practical',        # 244 - Old-Confection-5129
    'nhbyhqy': 'Practical',        # 245 - AttentionSuspension
    'nhbedyi': 'Practical',        # 246 - scally501
    'nhbfo59': 'Practical',        # 247 - boatsydney
    'nhbzo5o': 'Practical',        # 248 - AttentionSuspension
    'nhbifnv': 'Practical',        # 249 - nraw
    'nhdejat': 'Practical',        # 250 - dannuic
    'nhdgj0b': 'Practical',        # 251 - AttentionSuspension
    'nhdhw0h': 'Practical',        # 252 - AttentionSuspension
    'nhds05c': 'Practical',        # 253 - dannuic
    'nhdt5y0': 'Practical',        # 254 - MisterSincere
    'nhdtftq': 'Practical',        # 255 - AttentionSuspension
    'nhhk303': 'Practical',        # 256 - SuperAdminIsTraitor
    'nhi7ygs': 'Practical',        # 257 - AttentionSuspension
    'nhkdgmy': 'Practical',        # 258 - SuperAdminIsTraitor
    'nhimz0w': 'Practical',        # 259 - Medical_Amount3007
    'nhlvehe': 'Practical',        # 260 - Intelligent-Chain423
    'nhrf3wc': 'Practical',        # 261 - AttentionSuspension
    'nhofu5o': 'Practical',        # 262 - someouterboy
    'nhrgj6g': 'Practical',        # 263 - AttentionSuspension
    'nhomo6i': 'Practical',        # 264 - Kjoep
    'nhrhfpy': 'Practical',        # 265 - AttentionSuspension
    'nhoyz2w': 'Practical',        # 266 - Tango1777
    'nhrj07g': 'Practical',        # 267 - AttentionSuspension
    'nhr5f58': 'Practical',        # 268 - grosser_zampano
    'nhx3dnb': 'Practical',        # 269 - AttentionSuspension
    'nhtabso': 'Practical',        # 270 - Specialist_Guava_416
    'nimpwqk': 'Practical',        # 271 - Few_Personality1741
    'nh16n9i': 'Practical',        # 272 - efalk
    'nh1su3j': 'Practical',        # 273 - Conscious_Support176
    'nh1lke0': 'Practical',        # 274 - malcolm-maya
    'nh2v65w': 'Practical',        # 275 - efalk
    'nh2q1rg': 'Practical',        # 276 - universaluniqueid
    'nh1gdap': 'Practical',        # 277 - mfontani
    'nh534zk': 'Practical',        # 279 - mfontani
    'nh17y0n': 'Practical',        # 280 - TrickTimely3242
    'nh19o31': 'Practical',        # 281 - Tsiangkun
    'nh1aid4': 'Practical',        # 282 - Tsiangkun
    'nh1ag2v': 'Practical',        # 283 - giminik
    'nh21gf4': 'Practical',        # 284 - OrcaFlux
    'nh21k89': 'Practical',        # 285 - AttentionSuspension
    'nh2wrpi': 'Practical',        # 286 - trimorphic
    'nh54gpv': 'Practical',        # 287 - AttentionSuspension
    'nh497zu': 'Practical',        # 288 - jirka642
    'nh56422': 'Practical',        # 289 - AttentionSuspension
    'nh49nc9': 'Practical',        # 290 - clinnkkk_
    'nhb4xce': 'Practical',        # 291 - frisedel
    'nhbxk9a': 'Practical',        # 292 - AttentionSuspension
    'nhcaqj1': 'Practical',        # 293 - frisedel
    'nhbd8uc': 'Practical',        # 294 - TheExodu5
    'nhbyg96': 'Practical',        # 295 - AttentionSuspension
    'nhcxtoh': 'Practical',        # 296 - AmphibianFrog
    'nhdeota': 'Practical',        # 297 - AttentionSuspension
    'nhdfe94': 'Practical',        # 298 - AmphibianFrog
    'nhdfynm': 'Practical',        # 299 - AttentionSuspension
    'nhfft1x': 'Practical',        # 300 - sobservation
    'nhhzewh': 'Practical',        # 301 - armujahid
    'nhi895z': 'Practical',        # 302 - AttentionSuspension
    'nhiep7f': 'Practical',        # 303 - armujahid
    'nhin4wm': 'Practical',        # 304 - Medical_Amount3007
    'nhmvwox': 'Practical',        # 305 - samettinho
    'nhrfh99': 'Practical',        # 306 - AttentionSuspension
    'nhn8jcr': 'Practical',        # 307 - DoctorOriginal7309
    'nhnffqq': 'Practical',        # 308 - itsdarkcloudtv
    'nhrfvhk': 'Practical',        # 309 - AttentionSuspension
    'nhohkku': 'Practical',        # 310 - abundant_singularity
    'nhohox6': 'Practical',        # 311 - PrestigiousAnt3766
    'nhrhap7': 'Practical',        # 312 - AttentionSuspension
    'nhruvod': 'Practical',        # 313 - PrestigiousAnt3766
    'nhowopd': 'Practical',        # 314 - mmcnl
    'nhrhsxk': 'Practical',        # 315 - AttentionSuspension
    'nhri20w': 'Practical',        # 316 - mmcnl
    'nhp8znp': 'Practical',        # 317 - Rguttersohn
    'nhr1ddy': 'Practical',        # 318 - kiwi-kaiser
    'ouxn089': 'Practical',        # 319 - michaelobriena
    'nh17p7t': 'Practical',        # 320 - RedEyed__
    'nh2876j': 'Practical',        # 321 - immediacyofjoy
    'nh2jljn': 'Practical',        # 322 - RedEyed__
    'nh2ot95': 'Practical',        # 323 - wildjokers
    'nh3irs0': 'Practical',        # 324 - EishLekker
    'nh3t2uj': 'Practical',        # 325 - wildjokers
    'nh4xhhg': 'Practical',        # 326 - RedEyed__
    'nh50m98': 'Practical',        # 327 - indeox
    'nhddpqu': 'Practical',        # 328 - elephantdingo
    'nh11ipj': 'Practical',        # 329 - Icy_Physics51
    'nh15jmg': 'Practical',        # 330 - dbear496
    'nh165a2': 'Practical',        # 332 - divad1196
    'nh1kj4q': 'Practical',        # 334 - divad1196
    'nh3pz7g': 'Practical',        # 335 - senfiaj
    'nh3tjbe': 'Practical',        # 336 - gororuns
    'nh556n0': 'Practical',        # 337 - AttentionSuspension
    'nh14fvn': 'Practical',        # 338 - mgruner
    'nh2r4zu': 'Practical',        # 339 - wildjokers
    'nh3ikjg': 'Practical',        # 340 - mgruner
    'nh3tood': 'Practical',        # 341 - wildjokers
    'nh4ky5i': 'Practical',        # 342 - mgruner
    'nh6gai6': 'Practical',        # 343 - wildjokers
    'nh189lt': 'Practical',        # 344 - Drugbird
    'nh19x7c': 'Practical',        # 345 - mgruner
    'nh1h2nj': 'Practical',        # 346 - Drugbird
    'nh3if9i': 'Practical',        # 347 - mgruner
    'nh55gjt': 'Practical',        # 348 - Drugbird
    'nh9lr3x': 'Practical',        # 349 - mgruner
    'nhbf5kd': 'Practical',        # 350 - Drugbird
    'nh130c5': 'Practical',        # 351 - darkest_ruby
    'nh1ak9k': 'Practical',        # 352 - endymion1818-1819
    'nh1bd8i': 'Practical',        # 353 - AttentionSuspension
    'nh3i0cn': 'Practical',        # 354 - Comprehensive-Pea812
    'nh6ugb8': 'Practical',        # 355 - baicoi66
    'nh771dn': 'Practical',        # 357 - baicoi66
    'nh7aeow': 'Practical',        # 358 - AttentionSuspension
    'nh7q13g': 'Practical',        # 359 - xenomachina
    'ni93k4r': 'Practical',        # 360 - lottspot
    'nhi4fjb': 'Practical',        # 361 - goranlepuz
    'ni8wu8p': 'Practical',        # 362 - lottspot
    
    # Code Review & Collaboration
    'nh1dlfq': 'Code Review',     # 57 - AttentionSuspension
    'nh24jr9': 'Code Review',     # 118 - RarestSolanum
    'nh2oahm': 'Code Review',     # 120 - RarestSolanum
    'nh2t3ud': 'Code Review',     # 121 - Wiikend
    'nh331up': 'Code Review',     # 122 - MrMelon54
    'nh33cyw': 'Code Review',     # 123 - MrMelon54
    'nh53jgy': 'Code Review',     # 124 - AttentionSuspension
    'nhc6yel': 'Code Review',     # 126 - timtody
    'nhdejat': 'Code Review',     # 250 - dannuic
    'nhdgj0b': 'Code Review',     # 251 - AttentionSuspension
    'nhdhw0h': 'Code Review',     # 252 - AttentionSuspension
    'nhds05c': 'Code Review',     # 253 - dannuic
    'nhdt5y0': 'Code Review',     # 254 - MisterSincere
    'nhdtftq': 'Code Review',     # 255 - AttentionSuspension
    'nh14fvn': 'Code Review',     # 338 - mgruner
    'nh2r4zu': 'Code Review',     # 339 - wildjokers
    'nh3ikjg': 'Code Review',     # 340 - mgruner
    'nh3tood': 'Code Review',     # 341 - wildjokers
    'nh4ky5i': 'Code Review',     # 342 - mgruner
    'nh6gai6': 'Code Review',     # 343 - wildjokers
    'nh189lt': 'Code Review',     # 344 - Drugbird
    'nh19x7c': 'Code Review',     # 345 - mgruner
    'nh1h2nj': 'Code Review',     # 346 - Drugbird
    'nh3if9i': 'Code Review',     # 347 - mgruner
    'nh55gjt': 'Code Review',     # 348 - Drugbird
    'nh9lr3x': 'Code Review',     # 349 - mgruner
    'nhbf5kd': 'Code Review',     # 350 - Drugbird
    
    # Humor / Off-topic / Short Reactions
    'nh6h45s': 'Humor',          # 20 - lottspot
    'nh750gu': 'Humor',          # 21 - xenomachina
    'nh792dp': 'Humor',          # 22 - lottspot
    'nh7p8rx': 'Humor',          # 24 - lottspot
    'nhf0ni1': 'Humor',          # 39 - sheriffderek
    'nhi4fym': 'Humor',          # 40 - Trineki
    'nh1rhrz': 'Humor',          # 30 - Shadowratenator
    'nh67f0b': 'Humor',          # 31 - LysanderStorm
    'nh80zut': 'Humor',          # 32 - macbig273
    'nh9fws4': 'Humor',          # 33 - Trawling_
    'nhmzkwi': 'Humor',          # 42 - m915
    'nh3fv8u': 'Humor',          # 35 - Fun-Title7656
    'nhi4nva': 'Humor',          # 41 - Horror_Jicama_2441
    'nhel2w1': 'Humor',          # 12 - timbar1234
    'nh2acst': 'Humor',          # 25 - AttentionSuspension
    'nh8x97z': 'Humor',          # 26 - edgmnt_net
    'nh98ltu': 'Humor',          # 27 - xenomachina
    'nhe51h9': 'Humor',          # 28 - edgmnt_net
    'nhebuka': 'Humor',          # 29 - xenomachina
    'nh1dlfq': 'Humor',          # 57 - AttentionSuspension
    'nh1uh9n': 'Humor',          # 59 - AttentionSuspension
    'nh54p5m': 'Humor',          # 65 - AttentionSuspension
    'nh1bjj6': 'Humor',          # 73 - AttentionSuspension
    'nh3q4w0': 'Humor',          # 80 - waterkip
    'nh3s5ip': 'Humor',          # 81 - EishLekker
    'nh1xv8t': 'Humor',          # 83 - AttentionSuspension
    'nh21f9b': 'Humor',          # 85 - AttentionSuspension
    'nh1umfl': 'Humor',          # 117 - AttentionSuspension
    'nh1d4hc': 'Humor',          # 110 - AttentionSuspension
    'nh53jgy': 'Humor',          # 124 - AttentionSuspension
    'nh540ok': 'Humor',          # 128 - AttentionSuspension
    'nh1eque': 'Humor',          # 181 - AttentionSuspension
    'nh1j1m5': 'Humor',          # 183 - AttentionSuspension
    'nh1jdjo': 'Humor',          # 185 - AttentionSuspension
    'nh1k6na': 'Humor',          # 187 - AttentionSuspension
    'nh1uujl': 'Humor',          # 189 - AttentionSuspension
    'nh20cv2': 'Humor',          # 190 - IamYourGrace
    'nh20kqr': 'Humor',          # 191 - AttentionSuspension
    'nh29pjb': 'Humor',          # 192 - RaniAgus
    'nh2a46g': 'Humor',          # 193 - AttentionSuspension
    'nh2jhn8': 'Humor',          # 195 - AttentionSuspension
    'nh2k3m1': 'Humor',          # 198 - AttentionSuspension
    'nh54soh': 'Humor',          # 200 - AttentionSuspension
    'nh54ue6': 'Humor',          # 202 - AttentionSuspension
    'nh55cr5': 'Humor',          # 204 - AttentionSuspension
    'nh55r0g': 'Humor',          # 206 - AttentionSuspension
    'nh5cut9': 'Humor',          # 208 - AttentionSuspension
    'nh55tkn': 'Humor',          # 209 - AttentionSuspension
    'nh56fd0': 'Humor',          # 212 - AttentionSuspension
    'nh56iql': 'Humor',          # 214 - AttentionSuspension
    'nh56nmp': 'Humor',          # 216 - AttentionSuspension
    'nh56tpz': 'Humor',          # 218 - AttentionSuspension
    'nh56x4w': 'Humor',          # 221 - AttentionSuspension
    'nh572pr': 'Humor',          # 223 - AttentionSuspension
    'nh58fqe': 'Humor',          # 225 - AttentionSuspension
    'nh5eio0': 'Humor',          # 227 - AttentionSuspension
    'nh75vn7': 'Humor',          # 231 - AttentionSuspension
    'nh7k8jz': 'Humor',          # 232 - AttentionSuspension
    'nh7n6xx': 'Humor',          # 233 - AttentionSuspension
    'nh766bp': 'Humor',          # 234 - AttentionSuspension
    'nh76jp1': 'Humor',          # 236 - AttentionSuspension
    'nh7yhfi': 'Humor',          # 238 - AttentionSuspension
    'nh8ilec': 'Humor',          # 241 - AttentionSuspension
    'nhbx4re': 'Humor',          # 243 - AttentionSuspension
    'nhbyhqy': 'Humor',          # 245 - AttentionSuspension
    'nhbzo5o': 'Humor',          # 248 - AttentionSuspension
    'nhdgj0b': 'Humor',          # 251 - AttentionSuspension
    'nhdhw0h': 'Humor',          # 252 - AttentionSuspension
    'nhdtftq': 'Humor',          # 255 - AttentionSuspension
    'nhi7ygs': 'Humor',          # 257 - AttentionSuspension
    'nhrf3wc': 'Humor',          # 261 - AttentionSuspension
    'nhrgj6g': 'Humor',          # 263 - AttentionSuspension
    'nhrhfpy': 'Humor',          # 265 - AttentionSuspension
    'nhrj07g': 'Humor',          # 267 - AttentionSuspension
    'nhx3dnb': 'Humor',          # 269 - AttentionSuspension
    'nh1gvnt': 'Humor',          # 278 - AttentionSuspension
    'nh21k89': 'Humor',          # 285 - AttentionSuspension
    'nh54gpv': 'Humor',          # 287 - AttentionSuspension
    'nh56422': 'Humor',          # 289 - AttentionSuspension
    'nh1fkdz': 'Humor',          # 331 - AttentionSuspension
    'nh1kj4q': 'Humor',          # 333 - AttentionSuspension
    'nh556n0': 'Humor',          # 337 - AttentionSuspension
    'nh1bd8i': 'Humor',          # 353 - AttentionSuspension
    'nh761lb': 'Humor',          # 356 - AttentionSuspension
    'nh7aeow': 'Humor',          # 358 - AttentionSuspension
    'nhfft1x': 'Humor',          # 300 - sobservation
    'nh3pz7g': 'Humor',          # 335 - senfiaj
    'nh11ipj': 'Humor',          # 329 - Icy_Physics51
}

# Count comments per cluster
cluster_counts = defaultdict(int)
cluster_scores = defaultdict(int)

for c in real:
    cluster = cluster_map.get(c['id'], 'Unassigned')
    cluster_counts[cluster] += 1
    cluster_scores[cluster] += c['score']

print("Cluster distribution:")
total = 0
for cluster in sorted(cluster_counts.keys()):
    print(f"  {cluster}: {cluster_counts[cluster]} comments, {cluster_scores[cluster]} upvotes")
    total += cluster_counts[cluster]
print(f"Total: {total}")

# Check for unassigned
unassigned = [c for c in real if c['id'] not in cluster_map]
print(f"Unassigned: {len(unassigned)}")
for c in unassigned:
    print(f"  {c['id']} | {c['author']} | {c['body'][:100]}")
