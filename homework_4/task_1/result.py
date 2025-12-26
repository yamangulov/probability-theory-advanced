import numpy as np
from scipy.stats import chi2_contingency

def main():
    # Данные из задачи
    observed = np.array([[197, 158], [102, 221]])

    # Хи-квадрат тест
    chi2, p, dof, expected = chi2_contingency(observed)

    print(f"Хи-квадрат статистика: {chi2}")
    print(f"p-значение: {p}")
    print(f"Степени свободы: {dof}")

    # Коэффициент Крамера V
    n = np.sum(observed)
    min_dim = min(observed.shape) - 1
    v = np.sqrt(chi2 / (n * min_dim))
    print(f"Коэффициент Крамера V: {v}")

    # Коэффициент Пирсона C
    c = np.sqrt(chi2 / (chi2 + n))
    print(f"Коэффициент Пирсона C: {c}")

if __name__ == "__main__":
    main()
