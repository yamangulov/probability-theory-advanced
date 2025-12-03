import numpy as np
from scipy import stats
import warnings

print("Задача 2: Проверка гипотезы о равенстве средних для парных наблюдений")
print("Сравнение двух методов определения процентного содержания жира в мясе")
print()

# Реальные данные из таблицы
method1_data = np.array([23.1, 23.2, 26.5, 26.6, 27.1, 48.3, 40.5, 25.0, 38.4, 23.5])
method2_data = np.array([22.7, 23.6, 27.1, 27.4, 27.4, 46.8, 40.4, 24.9, 38.1, 23.8])

print(f"Метод I: {method1_data}")
print(f"Метод II: {method2_data}")
print(f"Размер выборки: {len(method1_data)} пар")
print()

# Вычисление разностей
differences = method1_data - method2_data
n = len(differences)

print(f"Разности (Метод I - Метод II): {differences}")
print(f"Среднее разностей: {np.mean(differences):.4f}")
print(f"Стандартное отклонение разностей: {np.std(differences, ddof=1):.4f}")
print()

# Параметры теста
alpha = 0.05  # Уровень значимости

# 1. ПРОВЕРКА НОРМАЛЬНОСТИ РАСПРЕДЕЛЕНИЯ РАЗНОСТЕЙ
print("1. ПРОВЕРКА НОРМАЛЬНОСТИ РАСПРЕДЕЛЕНИЯ РАЗНОСТЕЙ")
print("-" * 50)

# Критерий Шапиро-Уилка
shapiro_stat, shapiro_p = stats.shapiro(differences)
print(f"Критерий Шапиро-Уилка:")
print(f"  Статистика: {shapiro_stat:.4f}")
print(f"  P-значение: {shapiro_p:.6f}")

if shapiro_p < alpha:
    print(f"  Вывод: P-значение ({shapiro_p:.6f}) < α ({alpha})")
    print("  Отвергаем гипотезу о нормальности распределения")
    print("  ⚠ t-критерий для парных наблюдений НЕ применим!")
    print("  Используем непараметрический критерий: критерий Уилкоксона")
    
    # Непараметрический критерий Уилкоксона для парных выборок
    # H0: медиана разностей = 0
    # H1: медиана разностей ≠ 0
    
    # Подсчитываем ранги абсолютных разностей
    abs_diff = np.abs(differences)
    ranks = stats.rankdata(abs_diff)
    
    # Суммируем ранги положительных разностей
    positive_ranks = ranks[differences > 0]
    negative_ranks = ranks[differences < 0]
    
    W_plus = np.sum(positive_ranks)
    W_minus = np.sum(negative_ranks)
    W = min(W_plus, W_minus)
    
    print(f"  Сумма рангов положительных разностей: {W_plus}")
    print(f"  Сумма рангов отрицательных разностей: {W_minus}")
    print(f"  Статистика критерия Уилкоксона: W = {W}")
    
    # Для n=10 используем точное распределение
    try:
        # scipy.stats.wilcoxon автоматически выберет точный или асимптотический тест
        wilcoxon_stat, p_value = stats.wilcoxon(method1_data, method2_data, alternative='two-sided')
        print(f"  P-значение (критерий Уилкоксона): {p_value:.6f}")
    except:
        print("  Ошибка при вычислении критерия Уилкоксона")
        p_value = 1.0
        
    print("2. РЕЗУЛЬТАТ КРИТЕРИЯ УИЛКОКСОНА")
    print("-" * 50)
    if p_value < alpha:
        print(f"P-значение ({p_value:.6f}) < α ({alpha})")
        print("Отвергаем основную гипотезу H₀")
        print("Медиана разностей статистически отличается от нуля")
        print("Методы дают статистически разные результаты")
    else:
        print(f"P-значение ({p_value:.6f}) ≥ α ({alpha})")
        print("Нет оснований отвергать основную гипотезу H₀")
        print("Медиана разностей не отличается от нуля")
        print("Методы дают статистически одинаковые результаты")
        
else:
    print(f"  Вывод: P-значение ({shapiro_p:.6f}) ≥ α ({alpha})")
    print("  Нет оснований отвергать гипотезу о нормальности распределения")
    print("  ✓ t-критерий для парных наблюдений применим")

    # 2. ПАРАМЕТРИЧЕСКИЙ ПАРНЫЙ T-ТЕСТ
    print("\n2. ПАРНЫЙ T-КРИТЕРИЙ")
    print("-" * 50)

    # Выполнение парного t-теста
    # H0: μ_d = 0 (разность средних равна нулю)
    # H1: μ_d ≠ 0 (разность средних не равна нулю)
    t_stat, p_value = stats.ttest_rel(method1_data, method2_data)

    print(f"Наблюдаемое значение t-статистики: {t_stat:.4f}")
    print(f"P-значение: {p_value:.6f}")
    print()

    # Критические значения
    df = n - 1  # степени свободы
    t_critical_left = stats.t.ppf(alpha/2, df)
    t_critical_right = stats.t.ppf(1 - alpha/2, df)

    print(f"Степени свободы: {df}")
    print(f"Левая критическая точка (t_{alpha/2:.3f}): {t_critical_left:.4f}")
    print(f"Правая критическая точка (t_{1-alpha/2:.3f}): {t_critical_right:.4f}")
    print()

    # Принятие решения
    reject_null = p_value < alpha
    print("3. РЕЗУЛЬТАТ ТЕСТА")
    print("-" * 50)
    print("Формулировка гипотез:")
    print("H₀: μ_d = 0 (методы дают одинаковые результаты)")
    print("H₁: μ_d ≠ 0 (методы дают разные результаты)")
    print()

    if reject_null:
        print(f"P-значение ({p_value:.6f}) < α ({alpha})")
        print("Отвергаем основную гипотезу H₀")
        print("Принимаем альтернативную гипотезу H₁")
        if t_stat > 0:
            print("Метод I дает в среднем БОЛЬШИЕ показания, чем метод II")
        else:
            print("Метод I дает в среднем МЕНЬШИЕ показания, чем метод II")
    else:
        print(f"P-значение ({p_value:.6f}) ≥ α ({alpha})")
        print("Нет оснований отвергать основную гипотезу H₀")
        print("Методы дают статистически одинаковые результаты")

    print()
    print("4. ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ")
    print("-" * 50)
    print(f"Сравнение с критическими точками:")
    if abs(t_stat) > abs(t_critical_right):
        print(f"|tнабл| ({abs(t_stat):.4f}) > |tкр| ({abs(t_critical_right):.4f})")
        print("tнабл попадает в критическую область")
    else:
        print(f"|tнабл| ({abs(t_stat):.4f}) ≤ |tкр| ({abs(t_critical_right):.4f})")
        print("tнабл не попадает в критическую область")

    # Доверительный интервал для средней разности
    se = np.std(differences, ddof=1) / np.sqrt(n)
    ci_lower = np.mean(differences) - stats.t.ppf(1 - alpha/2, df) * se
    ci_upper = np.mean(differences) + stats.t.ppf(1 - alpha/2, df) * se
    print(f"95% доверительный интервал для средней разности: [{ci_lower:.4f}, {ci_upper:.4f}]")

if __name__ == "__main__":
    pass
