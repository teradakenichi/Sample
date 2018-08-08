"""
軌跡付きの放物運動のアニメーション
Animation with a locus
"""

import matplotlib.pyplot as plt
%matplotlib nbagg  # Jupyter-notebookでアニメーションを表示する場合に付け加える
from matplotlib.animation import ArtistAnimation # アニメーション作成のためのメソッドをインポート
import numpy as np

fig = plt.figure()

anim = [] #アニメーション用に描くパラパラ図のデータを格納するためのリスト
tt = np.arange(0,15,0.5) # 描画するための時間設定: t=0から15までの0.5刻み。

x_all=[] # 全てのx位置のデータを格納するためのリスト
y_all=[] # 全てのy位置のデータを格納するためのリスト

#初期条件の設定
V0 =100 # 初速度の大きさ: 100 m/s
theta=np.pi/4
x0=0 # 初期位置: x＝０
y0=0 #初期位置: y = 0
g=9.8 # 重力定数 [m/s^2]

for t in tt:
    x= [V0*np.cos(theta)*t+x0]  # x(t)の記述
    y = [-( g/2)*t**2+V0*np.sin(theta)*t+y0] # y(t)の記述
    x_all.append(x[0]) # xの時々刻々データを格納
    y_all.append(y[0]) # yの時々刻々データを格納

    # 時刻tにおける質点と，時刻tに至るまでの運動の軌跡の二つの絵を作成し， アニメーション用のリストに格納する。
    im=plt.plot(x,y,'o', x_all,y_all, '--', color='red',markersize=10, linewidth = 2, aa=True)
    anim.append(im)


anim = ArtistAnimation(fig, anim) # アニメーション作成

# 描画のカスタマイズ
plt.xlabel('X',fontsize=18) # 
plt.ylabel('Y',fontsize=18)
plt.xlim(0, 1100)
plt.ylim(-10,300)
plt.hlines([0], 0, 2000, linestyles="-")  # y=0に線を描く。

fig.show() 
anim.save("t.gif", writer='imagemagick')   #アニメーションをt.gifという名前で保存し，gifアニメーションファイルを作成する。
