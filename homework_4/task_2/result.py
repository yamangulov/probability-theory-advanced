from scipy.stats import spearmanr

def main():
    # Данные из задачи
    jury = [8, 2, 9, 6, 4, 5, 3, 7, 10, 1]
    audience = [10, 7, 8, 2, 5, 1, 6, 3, 9, 4]

    # Коэффициент Спирмена и p-значение
    rho, p = spearmanr(jury, audience)

    print(f"Коэффициент Спирмена ρ: {rho}")
    print(f"p-значение: {p}")

if __name__ == "__main__":
    main()
