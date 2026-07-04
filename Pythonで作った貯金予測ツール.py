import time

def 文字表示(text, delay=0.03):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

文字表示("貯金シュミレーションスタート！")

文字表示("あなたの今の貯金は何円ですか？: ")
貯金 = int(input())

文字表示("あなたの目標金額を教えてください: ")
目標 = int(input())
if 目標 <= 0:
    print("目標は1円以上にしてね")
    input("\nEnterキーで終了")
    exit()

文字表示("あなたの月の収入はいくらですか？")
収入 = int(input())

文字表示("お年玉は何円貰いますか？（臨時収入とかボーナスでもOK）")
お年玉 = int(input())

文字表示("クリスマスプレゼントは何円貰いますか？（臨時収入とかボーナスでもOK）")
クリプレ = int(input())

文字表示("誕生日にお金は何円貰いますか？（臨時収入とかボーナスでもOK）")
誕プレ = int(input())

文字表示("あなたの買いたいものはなんですか？")
欲しいもの = input()

年間ボーナス = お年玉 + クリプレ + 誕プレ

文字表示("何か月シミュレーションしますか？: ")
毎月 = int(input())
if 毎月 >= 120:
    step = 12
else:
    step = 3
現在 = 貯金
履歴 = []

for 月 in range(毎月):
    現在 += 収入

    if (月 + 1) % 12 == 0:
        現在 += 年間ボーナス

    履歴.append((月 + 1, 現在))
現在2 = 貯金
経過月数 = 0

while 現在2 < 目標:
    現在2 += 収入
    経過月数 += 1

    if 経過月数 % 12 == 0:
        現在2 += 年間ボーナス
print("\n計算ログを表示するよ...\n")
time.sleep(0.5)

for i in range(0, len(履歴), step):
    月, 金額 = 履歴[i]
    print(f"{月:3}ヶ月目 | {金額:,}円")
    time.sleep(0.03)

最終金額 = 履歴[-1][1]

if 目標 > 0:
    達成率 = 最終金額 * 100 // 目標
else:
    達成率 = 0

if 最終金額 >= 目標:
    余り = 最終金額 - 目標
    print(f"{最終金額:,}円貯まったね！高級な{欲しいもの}も視野に入るかも！")
    print(f"余り：{余り:,}円")
else:
    不足 = 目標 - 最終金額
    print(f"{最終金額:,}円ならまだ足りないかも！")
    print(f"不足分：{不足:,}円")

print(f"達成率：{達成率}%")
print(f"目標達成予測：{経過月数}ヶ月")
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Meiryo"
月 = [x[0] for x in 履歴]
金額 = [x[1] for x in 履歴]
plt.plot(月, 金額)
plt.title("貯金シミュレーション")
plt.xlabel("月")
plt.ylabel("貯金額")
plt.show()

input("\nEnterキーで終了")