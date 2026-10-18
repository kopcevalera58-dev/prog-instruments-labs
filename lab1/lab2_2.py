import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

a = 0
n = 4
sigma2 = 9
sigma = np.sqrt(sigma2)
N = 550
gamma = 0.94
# пункт 1
print("пункт 1")
sample_2_1 = stats.norm.rvs(a, sigma, n)
x_bar_2_1 = np.mean(sample_2_1)
S = np.std(sample_2_1, ddof=1)

print("выборка =", sample_2_1)
print("выборочная средняя =", x_bar_2_1)
print("исправленное стандартное отклонение S =", S)

# способ 1
t_gamma = stats.t.ppf((1 + gamma) / 2, df=n - 1)
delta_2_1 = t_gamma * S / np.sqrt(n)
L1_2_1 = x_bar_2_1 - delta_2_1
R1_2_1 = x_bar_2_1 + delta_2_1

print("t_gamma =", t_gamma)
print("delta =", delta_2_1)
print("доверительный интервал (способ 1) =", (L1_2_1, R1_2_1))
print("длина интервала =", R1_2_1 - L1_2_1)

# способ 2
L2_2_1, R2_2_1 = stats.t.interval(gamma, df=n - 1, loc=x_bar_2_1, scale=S / np.sqrt(n))

print("доверительный интервал (способ 2) =", (L2_2_1, R2_2_1))
print("длина интервала =", R2_2_1 - L2_2_1)

# пункт 2
gammas = np.linspace(0.01, 0.99, 200)
t_gammas = stats.t.ppf((1 + gammas) / 2, df=n - 1)
lengths = 2 * t_gammas * S / np.sqrt(n)

plt.plot(gammas, lengths, color="purple")
plt.xlabel("надежность gamma")
plt.ylabel("длина доверительного интервала")
plt.title("Зависимость длины интервала от надежности ")
plt.grid()
plt.show()

# пункт 3
nn = np.zeros(98)
ln = np.zeros(98)
for i in range(2, 100):
    sample_3 = stats.norm.rvs(a, sigma, n)
    x_bar_3 = np.mean(sample_3)
    S_3 = np.std(sample_3, ddof=1)
    L3_i, R3_i = stats.t.interval(gamma, df=i - 1, loc=x_bar_3, scale=S_3 / np.sqrt(i))
    ln[i - 2] = R3_i - L3_i
    nn[i - 2] = i
plt.plot(nn, ln, color="pink")
plt.xlabel("объем выборки")
plt.ylabel("длина доверительного интервал")
plt.title("Зависимость длины интервала от объема выборки")
plt.grid()
plt.show()
# пункт 4
print("пункт 4")
cnt = 0
for _ in range(N):
    sample_i = stats.norm.rvs(a, sigma, n)
    x_bar_i = np.mean(sample_i)
    S_i = np.std(sample_i, ddof=1)
    L_i, R_i = stats.t.interval(gamma, df=n - 1, loc=x_bar_i, scale=S_i / np.sqrt(n))
    if L_i < a < R_i:
        cnt += 1
percent = (cnt / N) * 100
print("t_gamma =", t_gamma)
print("число накрытий =", cnt, "из", N)
print("процент накрытий =", percent, "%")
print("ожидаемый процент =", gamma * 100, "%")

# пункт 5
print("пункт 5")
S2 = np.zeros(N)
for i in range(N):
    sample_i2 = stats.norm.rvs(a, sigma, n)
    S2[i] = np.var(sample_i2, ddof=1)
print("S2(первые 10) = ", S2[:10])
# пункт 6
plt.hist(S2, bins=20, density=True)
x_min = min(S2)
x_max = max(S2)
shag = 0.1
x = np.arange(x_min, x_max, shag)
y = stats.chi2.pdf(x, df=n - 1, scale=sigma2 / (n - 1))

plt.plot(x, y, color="red")
plt.title("Гистограмма S^2 и теоретическая кривая")
plt.xlabel("S^2")
plt.ylabel("плотность")
plt.grid()
plt.show()

# пункт 7
print("пункт 7")
plt.boxplot(S2, vert=False)
plt.title("Boxplot выборки")
plt.xlabel("Значения")
plt.grid()
plt.show()

S2_25 = np.percentile(S2, 25)
S2_50 = np.percentile(S2, 50)
S2_75 = np.percentile(S2, 75)

IQR = S2_75 - S2_25

lev_us = S2_25 - 1.5 * IQR
prav_us = S2_75 + 1.5 * IQR

print("x_25=", S2_25)
print("x_50=", S2_50)
print("x_75=", S2_75)
print("lev_us=", lev_us)
print("prav_us=", prav_us)

outliers = S2[(S2 < lev_us) | (S2 > prav_us)]
print("число выбросов =", len(outliers))
print("процент выбросов =", len(outliers) / len(S2) * 100, "%")

# пункт 8
print("пункт 8")
cnt_2 = 0
for i in range(len(S2)):
    if S2[i] < sigma2:
        cnt_2 += 1
ppercent_s2 = cnt_2 / len(S2) * 100

print("процент значений S2 < sigma2 =", ppercent_s2)

# пункт 9
print("пункт 9")
sample_9 = stats.norm.rvs(a, sigma, n)
S2_9 = np.var(sample_9, ddof=1)

z_gamma = stats.norm.ppf((1 + gamma) / 2)
delta = z_gamma * sigma2 / np.sqrt(n)
L_chi, R_chi = stats.chi2.interval(gamma, df=n - 1)

L_9 = (n - 1) * S2_9 / R_chi
R_9 = (n - 1) * S2_9 / L_chi

print("выборка 9 =", sample_9)
print("S2_9 =", S2_9)
print("доверительный интервал для sigma^2 =", (L_9, R_9))

print("контроольные вопросы")
print("выборочное среднее S^2 =", np.mean(S2))
print("выборочная дисперсия S^2 =", np.var(S2, ddof=1))
