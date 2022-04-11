import re
import urllib.request

import matplotlib.pyplot as plt
import numpy as np

teams = ['ATL', 'BOS', 'NJN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA',
         'MIL', 'MIN', 'NOH', 'NYK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']


def stats(team, player):
    url = ''
    if player == 'KOBE':
        url = 'https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&match=game&year_min=1997&year_max=2016&is_playoffs=E&age_min=0&age_max=99&opp_id=' \
              + team + '&season_start=1&season_end=-1&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&player_id=bryanko01&c1stat=mp&c1comp=gt&c1val=10&order_by=pts'
    elif player == 'LBJ':
        url = 'https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&match=game&year_min=2004&year_max=2019&is_playoffs=E&age_min=0&age_max=99&opp_id=' \
              + team + '&season_start=1&season_end=-1&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&player_id=jamesle01&order_by=ast'
    elif player == 'MJ':
        url = 'https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&match=game&year_min=1985&year_max=2003&is_playoffs=E&age_min=0&age_max=99&opp_id=' \
              + team + '&season_start=1&season_end=-1&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&player_id=jordami01&order_by=pts'

    if player == 'KOBE' and team == 'LAL':
        return [0], [0], [0], [0], [0], [0], [0], [0], [0]
    print(team + '\n')

    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read().decode('utf-8')

    pts = re.findall('"pts" >(\d+)<\/td>', respData)
    pts.sort(reverse=True, key=int)
    # print('Points \nCareer high: {0} \nCareer low: {1}'.format(pts[0],pts[-1]))
    for i in range(len(pts)):
        pts[i] = int(pts[i])
    # print('Career average: {0:.2f}\n'.format(sum(pts)/len(pts)))

    ast = re.findall('"ast" >(\d+)<\/td>', respData)
    ast.sort(reverse=True, key=int)
    # print('Assists \nCareer high: {0} \nCareer low: {1}'.format(ast[0],ast[-1]))
    for i in range(len(ast)):
        ast[i] = int(ast[i])
    # print('Career average: {0:.2f}\n'.format(sum(ast)/len(ast)))

    reb = re.findall('"trb" >(\d+)<\/td>', respData)
    reb.sort(reverse=True, key=int)
    # print('Rebounds \nCareer high: {0} \nCareer low: {1}'.format(reb[0],reb[-1]))
    for i in range(len(reb)):
        reb[i] = int(reb[i])
    # print('Career average: {0:.2f}\n'.format(sum(reb)/len(reb)))

    game_score = re.findall('"game_score" >(\d+\.\d)<\/td>', respData)
    game_score.sort(reverse=True, key=float)
    # print('Game score \nCareer high: {0} \nCareer low: {1}'.format(game_score[0],game_score[-1]))
    for i in range(len(game_score)):
        game_score[i] = float(game_score[i])
    # print('Career average: {0:.2f}\n'.format(sum(game_score)/len(game_score)))

    # print("Total games: {0}\n".format(len(pts)))

    return pts, ast, reb, game_score, float("{0:.2f}".format(sum(pts) / len(pts))), float(
        "{0:.2f}".format(sum(ast) / len(ast))), float("{0:.2f}".format(sum(reb) / len(reb))), float(
        "{0:.2f}".format(sum(game_score) / len(game_score))), len(pts)


LBJpts_career_highs = []
KOBEpts_career_highs = []
MJpts_career_highs = []
ast_career_highs = []
reb_career_highs = []
game_score_career_highs = []

pts_career_avg = []
ast_career_avg = []
reb_career_avg = []
game_score_career_avg = []

pts_career_lows = []
ast_career_lows = []
reb_career_lows = []
game_score_career_lows = []

games = []

# stats('LAL','KOBE')[0][0]

for i in range(len(teams)):
    # stats(teams[i],'KOBE')
    KOBEpts_career_highs.append(stats(teams[i], 'KOBE')[0][0])
    LBJpts_career_highs.append(stats(teams[i], 'LBJ')[0][0])
    MJpts_career_highs.append(stats(teams[i], 'MJ')[0][0])
    # ast_career_highs.append(stats(teams[i])[1][0])
    # reb_career_highs.append(stats(teams[i])[2][0])
    # game_score_career_highs.append(stats(teams[i])[3][0])
    # pts_career_avg.append(stats(teams[i])[4])
    # ast_career_avg.append(stats(teams[i])[5])
    # reb_career_avg.append(stats(teams[i])[6])
    # game_score_career_avg.append(stats(teams[i])[7])
    # pts_career_lows.append(stats(teams[i])[0][-1])
    # ast_career_lows.append(stats(teams[i])[1][-1])
    # reb_career_lows.append(stats(teams[i])[2][-1])
    # game_score_career_lows.append(stats(teams[i])[3][-1])
    # games.append(stats(teams[i])[8])

w = 0.2
ind = np.arange(len(teams))

plt.title('Career highs in points')
ax = plt.subplot(111)
ax.bar(ind - w, KOBEpts_career_highs, width=w, color='y', align='center', label='Kobe')
ax.bar(ind, LBJpts_career_highs, width=w, color='b', align='center', label='LeBron')
ax.bar(ind + w, MJpts_career_highs, width=w, color='r', align='center', label='MJ')
ax.set_xticks(ind)
ax.set_xticklabels(teams)
plt.legend()
# plt.title('Career highs in assists')
# plt.bar(teams,ast_career_highs)
# plt.title('Career highs in rebounds')
# plt.bar(teams,reb_career_highs)
# plt.title('Career highs in game score')
# plt.bar(teams,game_score_career_highs)
# plt.title('Career averages in points')
# plt.bar(teams,pts_career_avg)
# plt.title('Career averages in assists')
# plt.bar(teams,ast_career_avg)
# plt.title('Career averages in rebounds')
# plt.bar(teams,reb_career_avg)
# plt.title('Career averages in game score')
# plt.bar(teams,game_score_career_avg)
# plt.title('Career lows in points')
# plt.bar(teams,pts_career_lows)
# plt.title('Career lows in game score')
# plt.bar(teams,game_score_career_lows)
# plt.title('Career games')
# plt.bar(teams,games)

plt.show()
