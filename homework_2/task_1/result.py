import numpy as np
from scipy import stats

# Данные задачи
sample_data = np.array([12.9, 11.6, 13.5, 13.9, 12.1, 11.9, 13.0])

# Параметры теста
mu_0 = 12.0  # Предполагаемое среднее значение
alpha = 0.05  # Уровень значимости

print("Задача 1: Проверка гипотезы о среднем напряжении батареек")
print(f"Выборка: {sample_data}")
print(f"Предполагаемое среднее значение: {mu_0}")
print(f"Уровень значимости: {alpha}")
print()

# Описательная статистика
n = len(sample_data)
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data, ddof=1)  # Исправленная выборочная дисперсия

print(f"Выборочное среднее: {sample_mean:.4f}")
print(f"Размер выборки: {n}")
print(f"Исправленное стандартное отклонение: {sample_std:.4f}")
print()

# 1. ПРОВЕРКА НОРМАЛЬНОСТИ РАСПРЕДЕЛЕНИЯ
print("1. ПРОВЕРКА НОРМАЛЬНОСТИ РАСПРЕДЕЛЕНИЯ")
print("-" * 50)

# Критерий Шапиро-Уилка
shapiro_stat, shapiro_p = stats.shapiro(sample_data)
print(f"Критерий Шапиро-Уилка:")
print(f"  Статистика: {shapiro_stat:.4f}")
print(f"  P-значение: {shapiro_p:.6f}")

if shapiro_p < alpha:
    print(f"  Вывод: P-значение ({shapiro_p:.6f}) < α ({alpha})")
    print("  Отвергаем гипотезу о нормальности распределения")
    print("  ⚠ t-критерий Стьюдента НЕ применим!")
    print("  Используем непараметрический критерий: знаковый тест")
    
    # Непараметрический знаковый тест
    # H0: медиана = 12
    # H1: медиана ≠ 12
    
    # Подсчитываем положительные и отрицательные разности
    differences = sample_data - mu_0
    positive = np.sum(differences > 0)
    negative = np.sum(differences < 0)
    zero = np.sum(differences == 0)
    
    print(f"  Положительные разности: {positive}")
    print(f"  Отрицательные разности: {negative}")
    print(f"  Нулевые разности: {zero}")
    
    # Биномиальный тест для знаков
    if zero > 0:
        print(f"  Предупреждение: {zero} нулевых разностей исключаются из анализа")
        n_effective = positive + negative
    else:
        n_effective = n
    
    if n_effective > 0:
        # Биномиальный тест
        p_value = 2 * min(stats.binom.cdf(positive, n_effective, 0.5), 
                         1 - stats.binom.cdf(positive - 1, n_effective, 0.5))
        print(f"  Знаковый тест p-значение: {p_value:.6f}")
        
        print("2. РЕЗУЛЬТАТ ЗНАКОВОГО ТЕСТА")
        print("-" * 50)
        if p_value < alpha:
            print(f"P-значение ({p_value:.6f}) < α ({alpha})")
            print("Отвергаем основную гипотезу H₀")
            print("Медиана напряжения статистически отличается от 12 В")
        else:
            print(f"P-значение ({p_value:.6f}) ≥ α ({alpha})")
            print("Нет оснований отвергать основную гипотезу H₀")
            print("Медиану напряжения можно считать равной 12 В")
    else:
        print("Невозможно провести знаковый тест (все разности равны нулю)")
        
else:
    print(f"  Вывод: P-значение ({shapiro_p:.6f}) ≥ α ({alpha})")
    print("  Нет оснований отвергать гипотезу о нормальности распределения")
    print("  ✓ t-критерий Стьюдента применим")

    # 2. ПАРАМЕТРИЧЕСКИЙ Т-ТЕСТ
    print("\n2. T-КРИТЕРИЙ СТЬЮДЕНТА")
    print("-" * 50)
    
    # Выполнение одновыборочного t-теста
    # t_stat - наблюдаемое значение статистики
    # p_value - p-значение
    t_stat, p_value = stats.ttest_1samp(sample_data, mu_0)

    print(f"Наблюдаемое значение t-статистики: {t_stat:.4f}")
    print(f"P-значение: {p_value:.6f}")
    print()

    # Критические значения
    # Для двустороннего теста используем квантили t-распределения
    df = n - 1  # степени свободы
    t_critical_left = stats.t.ppf(alpha/2, df)
    t_critical_right = stats.t.ppf(1 - alpha/2, df)

    print(f"Степени свободы: {df}")
    print(f"Левая критическая точка (t_{alpha/2:.3f}): {t_critical_left:.4f}")
    print(f"Правая критическая точка (t_{1-alpha/2:.3f}): {t_critical_right:.4f}")
    print()

    # Принятие решения
    reject_null = p_value < alpha
    print(f"Результат теста:")
    if reject_null:
        print(f"P-значение ({p_value:.6f}) < α ({alpha})")
        print("Отвергаем основную гипотезу H₀")
        print("Принимаем альтернативную гипотезу H₁: μ ≠ 12")
    else:
        print(f"P-значение ({p_value:.6f}) ≥ α ({alpha})")
        print("Нет оснований отвергать основную гипотезу H₀")
        print("Среднее напряжение можно считать равным 12 В")

    print()
    print("Дополнительно: сравнение с критическими точками")
    if abs(t_stat) > abs(t_critical_right):
        print(f"|tнабл| ({abs(t_stat):.4f}) > |tкр| ({abs(t_critical_right):.4f})")
        print("tнабл попадает в критическую область")
    else:
        print(f"|tнабл| ({abs(t_stat):.4f}) ≤ |tкр| ({abs(t_critical_right):.4f})")
        print("tнабл не попадает в критическую область")

if __name__ == "__main__":
    pass
