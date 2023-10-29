import numpy as np
import matplotlib.pyplot as plt
from data import data
from functions import get_main_points, get_main_plot, graph_list, get_graph, get_axs, get_data

[paa, sak, saq, saj, sat, sa9, sa8, sa7, sa6, sa5, sa4, sa3, sa2,
 oak, pkk, skq, skj, skt, sk9, sk8, sk7, sk6, sk5, sk4, sk3, sk2,
 oaq, okq, pqq, sqj, sqt, sq9, sq8, sq7, sq6, sq5, sq4, sq3, sq2,
 oaj, okj, oqj, pjj, sjt, sj9, sj8, sj7, sj6, sj5, sj4, sj3, sj2,
 oat, okt, oqt, ojt, ptt, st9, st8, st7, st6, st5, st4, st3, st2,
 oa9, ok9, oq9, oj9, ot9, p99, s98, s97, s96, s95, s94, s93, s92,
 oa8, ok8, oq8, oj8, ot8, o98, p88, s87, s86, s85, s84, s83, s82,
 oa7, ok7, oq7, oj7, ot7, o97, o87, p77, s76, s75, s74, s73, s72,
 oa6, ok6, oq6, oj6, ot6, o96, o86, o76, p66, s65, s64, s63, s62,
 oa5, ok5, oq5, oj5, ot5, o95, o85, o75, o65, p55, s54, s53, s52,
 oa4, ok4, oq4, oj4, ot4, o94, o84, o74, o64, o54, p44, s43, s42,
 oa3, ok3, oq3, oj3, ot3, o93, o83, o73, o63, o53, o43, p33, s32,
 oa2, ok2, oq2, oj2, ot2, o92, o82, o72, o62, o52, o42, o32, p22] = [list(i) for i in zip(*data)]

hands = [paa, sak, saq, saj, sat, sa9, sa8, sa7, sa6, sa5, sa4, sa3, sa2,
         oak, pkk, skq, skj, skt, sk9, sk8, sk7, sk6, sk5, sk4, sk3, sk2,
         oaq, okq, pqq, sqj, sqt, sq9, sq8, sq7, sq6, sq5, sq4, sq3, sq2,
         oaj, okj, oqj, pjj, sjt, sj9, sj8, sj7, sj6, sj5, sj4, sj3, sj2,
         oat, okt, oqt, ojt, ptt, st9, st8, st7, st6, st5, st4, st3, st2,
         oa9, ok9, oq9, oj9, ot9, p99, s98, s97, s96, s95, s94, s93, s92,
         oa8, ok8, oq8, oj8, ot8, o98, p88, s87, s86, s85, s84, s83, s82,
         oa7, ok7, oq7, oj7, ot7, o97, o87, p77, s76, s75, s74, s73, s72,
         oa6, ok6, oq6, oj6, ot6, o96, o86, o76, p66, s65, s64, s63, s62,
         oa5, ok5, oq5, oj5, ot5, o95, o85, o75, o65, p55, s54, s53, s52,
         oa4, ok4, oq4, oj4, ot4, o94, o84, o74, o64, o54, p44, s43, s42,
         oa3, ok3, oq3, oj3, ot3, o93, o83, o73, o63, o53, o43, p33, s32,
         oa2, ok2, oq2, oj2, ot2, o92, o82, o72, o62, o52, o42, o32, p22]

players = [2, 3, 4, 5, 6, 7, 8, 9, 10]

x, y = get_main_points(hands, players)

get_main_plot(x, y)
graph_list(hands, "black", "All Hands")
get_graph("All Hands")

get_main_plot(x, y)
bpp = [paa, pkk, pqq, pjj, ptt]
spp = [p99, p88, p77, p66, p55, p44, p33, p22]
graph_list(bpp, "red", "Big Pocket Pairs")
graph_list(spp, "orange", "Small Pocket Pairs")
get_graph("Pocket Pairs")

get_main_plot(x, y)
sc = [sak, skq, sqj, sjt, st9, s98, s87, s76, s65, s54, s43, s32]
s1 = [saq, skj, sqt, sj9, st8, s97, s86, s75, s64, s53, s42]
s2 = [saj, skt, sq9, sj8, st7, s96, s85, s74, s63, s52]
s3 = [sat, sk9, sq8, sj7, st6, s95, s84, s73, s62]
graph_list(sc, "red", "Suited Connectors")
graph_list(s1, "orange", "Suited One-Gappers")
graph_list(s2, "yellow", "Suited Two-Gappers")
graph_list(s3, "green", "Suited Three-Gappers")
get_graph("Suited Connectors")

get_main_plot(x, y)
oc = [oak, okq, oqj, ojt, ot9, o98, o87, o76, o65, o54, o43, o32]
o1 = [oaq, okj, oqt, oj9, ot8, o97, o86, o75, o64, o53, o42]
o2 = [oaj, okt, oq9, oj8, ot7, o96, o85, o74, o63, o52]
o3 = [oat, ok9, oq8, oj7, ot6, o95, o84, o73, o62]
graph_list(oc, "red", "Unsuited Connectors")
graph_list(o1, "orange", "Unsuited One-Gappers")
graph_list(o2, "yellow", "Unsuited Two-Gappers")
graph_list(o3, "green", "Unsuited Three-Gappers")
get_graph("Unsuited Connectors")

get_main_plot(x, y)
sa = [sak, saq, saj, sat, sa9, sa8, sa7, sa6, sa5, sa4, sa3, sa2]
sk = [skq, skj, skt, sk9, sk8, sk7, sk6, sk5, sk4, sk3, sk2]
sq = [sqj, sqt, sq9, sq8, sq7, sq6, sq5, sq4, sq3, sq2]
sj = [sjt, sj9, sj8, sj7, sj6, sj5, sj4, sj3, sj2]
st = [st9, st8, st7, st6, st5, st4, st3, st2]
graph_list(sa, "red", "Suited Aces")
graph_list(sk, "orange", "Suited Kings")
graph_list(sq, "yellow", "Suited Queens")
graph_list(sj, "green", "Suited Jacks")
graph_list(st, "blue", "Suited Tens")
get_graph("Suited Big Cards")

get_main_plot(x, y)
oa = [oak, oaq, oaj, oat, oa9, oa8, oa7, oa6, oa5, oa4, oa3, oa2]
ok = [okq, okj, okt, ok9, ok8, ok7, ok6, ok5, ok4, ok3, ok2]
oq = [oqj, oqt, oq9, oq8, oq7, oq6, oq5, oq4, oq3, oq2]
oj = [ojt, oj9, oj8, oj7, oj6, oj5, oj4, oj3, oj2]
ot = [ot9, ot8, ot7, ot6, ot5, ot4, ot3, ot2]
graph_list(oa, "red", "Unsuited Aces")
graph_list(ok, "orange", "Unsuited Kings")
graph_list(oq, "yellow", "Unsuited Queens")
graph_list(oj, "green", "Unsuited Jacks")
graph_list(ot, "blue", "Unsuited Tens")
get_graph("Unsuited Big Cards")

get_main_plot(x, y)
sbc = [sak, saq, saj, sat, skq, skj, skt, sqj, sqt, sjt]
smc = [sa9, sa8, sa7, sa6, sa5, sa4, sa3, sa2, sk9, sk8, sk7, sk6, sk5, sk4, sk3, sk2,
       sq9, sq8, sq7, sq6, sq5, sq4, sq3, sq2, sj9, sj8, sj7, sj6, sj5, sj4, sj3, sj2,
       st9, st8, st7, st6, st5, st4, st3, st2]
ssc = [s98, s97, s96, s95, s94, s93, s92, s87, s86, s85, s84, s83, s82, s76, s75, s74, s73, s72, s65, s64, s63, s62,
       s54, s53, s52, s43, s42, s32]
graph_list(sbc, "red", "Suited Big Cards")
graph_list(smc, "orange", "Suited Medium Cards")
graph_list(ssc, "yellow", "Suited Small Cards")
get_graph("Suited Cards")

get_main_plot(x, y)
obc = [oak, oaq, oaj, oat, okq, okj, okt, oqj, oqt, ojt]
omc = [oa9, oa8, oa7, oa6, oa5, oa4, oa3, oa2, ok9, ok8, ok7, ok6, ok5, ok4, ok3, ok2,
       oq9, oq8, oq7, oq6, oq5, oq4, oq3, oq2, oj9, oj8, oj7, oj6, oj5, oj4, oj3, oj2,
       ot9, ot8, ot7, ot6, ot5, ot4, ot3, ot2]
osc = [o98, o97, o96, o95, o94, o93, o92, o87, o86, o85, o84, o83, o82, o76, o75, o74, o73, o72, o65, o64, o63, o62,
       o54, o53, o52, o43, o42, o32]
graph_list(obc, "red", "Unsuited Big Cards")
graph_list(omc, "orange", "Unsuited Medium Cards")
graph_list(osc, "yellow", "Unsuited Small Cards")
get_graph("Unsuited Cards")

p2 = np.array([i[0] for i in hands]).reshape(13, 13)
p3 = np.array([i[1] for i in hands]).reshape(13, 13)
p4 = np.array([i[2] for i in hands]).reshape(13, 13)
p5 = np.array([i[3] for i in hands]).reshape(13, 13)
p6 = np.array([i[4] for i in hands]).reshape(13, 13)
p7 = np.array([i[5] for i in hands]).reshape(13, 13)
p8 = np.array([i[6] for i in hands]).reshape(13, 13)
p9 = np.array([i[7] for i in hands]).reshape(13, 13)
pt = np.array([i[8] for i in hands]).reshape(13, 13)

fig, axs = plt.subplots(3, 3)

get_axs(axs[0, 0], p2, "2")
get_axs(axs[0, 1], p3, "3")
get_axs(axs[0, 2], p4, "4")
get_axs(axs[1, 0], p5, "5")
get_axs(axs[1, 1], p6, "6")
get_axs(axs[1, 2], p7, "7")
get_axs(axs[2, 0], p8, "8")
get_axs(axs[2, 1], p9, "9")
get_axs(axs[2, 2], pt, "10")
fig.suptitle("Equity per Players")
plt.show()

fig, axs = plt.subplots(1, 2)
get_axs(axs[0], np.array(x).reshape(13, 13), "log(α) (Normalized [0-Player] Equity)")
get_axs(axs[1], np.array(y).reshape(13, 13), "β (Equity Retention)")
fig.suptitle("Equity Coefficients")
plt.show()

get_data(hands)
