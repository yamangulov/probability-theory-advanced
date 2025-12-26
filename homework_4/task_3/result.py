from scipy.stats import pearsonr, spearmanr, kendalltau

def main():
    # Данные из задачи
    X = [66, 61, 67, 73, 51, 59, 48, 47, 58, 44, 41, 54, 52, 47, 51, 45]
    Y = [38, 31, 36, 43, 29, 33, 28, 25, 36, 26, 21, 30, 20, 27, 28, 26]

    # Случай 1: Пирсон (нормально)
    r, p_pearson = pearsonr(X, Y)
    print(f"Пирсон r: {r}, p: {p_pearson}")

    # Случай 2: Спирмен (ненормально, монотонная)
    rho, p_spearman = spearmanr(X, Y)
    print(f"Спирмен ρ: {rho}, p: {p_spearman}")

    # Случай 3: Кендалл (ненормально, немонотонная)
    tau, p_kendall = kendalltau(X, Y)
    print(f"Кендалл τ: {tau}, p: {p_kendall}")

if __name__ == "__main__":
    main()
