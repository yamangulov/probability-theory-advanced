import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Данные задачи 3
print("Задача 3: Проверка гипотезы о равенстве средних для независимых наблюдений")
print("Сравнение артериального давления у горожан и селян")
print()

# Выборки
city_residents = np.array([132, 111, 119, 138, 200, 131, 138, 170, 159, 140])
rural_residents = np.array([115, 190, 127, 155, 148, 121, 116, 121, 197])

n1 = len(city_residents)
n2 = len(rural_residents)

print("Данные:")
print(f"Горожане: {city_residents}")
print(f"Селяне: {rural_residents}")
print(f"Размер выборки: n₁ = {n1}, n₂ = {n2}")
print()

# Параметры теста
alpha = 0.05

# Выборочные характеристики
mean1 = np.mean(city_residents)
mean2 = np.mean(rural_residents)
std1 = np.std(city_residents, ddof=1)
std2 = np.std(rural_residents, ddof=1)

print(f"Выборочные характеристики:")
print(f"Горожане: x̄₁ = {mean1:.2f}, s₁ = {std1:.2f}")
print(f"Селяне:   x̄₂ = {mean2:.2f}, s₂ = {std2:.2f}")
print()

# 1. ПРОВЕРКА НОРМАЛЬНОСТИ РАСПРЕДЕЛЕНИЯ В ОБЕИХ ВЫБОРКАХ
print("1. ПРОВЕРКА НОРМАЛЬНОСТИ РАСПРЕДЕЛЕНИЯ")
print("-" * 50)

# Критерий Шапиро-Уилка для каждой выборки
shapiro1_stat, shapiro1_p = stats.shapiro(city_residents)
shapiro2_stat, shapiro2_p = stats.shapiro(rural_residents)

print(f"Критерий Шапиро-Уилка для горожан:")
print(f"  Статистика: {shapiro1_stat:.4f}")
print(f"  P-значение: {shapiro1_p:.6f}")

print(f"Критерий Шапиро-Уилка для селян:")
print(f"  Статистика: {shapiro2_stat:.4f}")
print(f"  P-значение: {shapiro2_p:.6f}")

# Проверка нормальности
both_normal = shapiro1_p >= alpha and shapiro2_p >= alpha
city_normal = shapiro1_p >= alpha
rural_normal = shapiro2_p >= alpha

print(f"Результат проверки нормальности:")
print(f"Горожане: {'✓ нормально' if city_normal else '✗ не нормально'}")
print(f"Селяне: {'✓ нормально' if rural_normal else '✗ не нормально'}")

if not both_normal:
    print("⚠ Одна или обе выборки не имеют нормального распределения")
    print("⚠ t-критерий Стьюдента может быть неприменим!")
    print("→ Используем непараметрический критерий Манна-Уитни")

    # Непараметрический критерий Манна-Уитни для независимых выборок
    # H0: медианы равны
    # H1: медиана горожан > медианы селян
    
    # Проверяем также равенство дисперсий для информации
    levene_stat, levene_p = stats.levene(city_residents, rural_residents)
    print(f"\nТест Левена (для информации): p = {levene_p:.6f}")
    
    # Критерий Манна-Уитни
    try:
        # one-sided тест: проверяем, что горожане имеют большее давление
        mannwhitney_stat, p_value = stats.mannwhitneyu(
            city_residents, rural_residents, 
            alternative='greater'  # H1: μ1 > μ2
        )
        
        print(f"\n2. КРИТЕРИЙ МАННА-УИТНИ")
        print("-" * 50)
        print(f"Формулировка гипотез:")
        print(f"H₀: медианы равны (горожане и селяне имеют одинаковое давление)")
        print(f"H₁: M₁ > M₂ (горожане имеют большее давление, чем селяне)")
        print(f"Статистика Манна-Уитни: {mannwhitney_stat:.4f}")
        print(f"P-значение: {p_value:.6f}")
        
        # Критическое значение (асимптотический)
        z_critical = stats.norm.ppf(1 - alpha)
        print(f"Критическое значение (нормальное приближение): z₀.₉₅ = {z_critical:.4f}")
        
        print(f"\n3. РЕЗУЛЬТАТ ТЕСТА")
        print("-" * 50)
        if p_value < alpha:
            print(f"P-значение ({p_value:.6f}) < α ({alpha})")
            print("Отвергаем основную гипотезу H₀")
            print("✓ Горожане имеют статистически значимо БОЛЬШЕЕ давление")
        else:
            print(f"P-значение ({p_value:.6f}) ≥ α ({alpha})")
            print("Нет оснований отвергать основную гипотезу H₀")
            print("✗ Нельзя считать верной гипотезу о большем давлении у горожан")
            
    except Exception as e:
        print(f"Ошибка при вычислении критерия Манна-Уитни: {e}")
        p_value = 1.0
        
else:
    print("✓ Обе выборки имеют нормальное распределение")
    print("✓ t-критерий Стьюдента применим")

    # 2. ПРОВЕРКА РАВЕНСТВА ДИСПЕРСИЙ
    print("\n2. ПРОВЕРКА РАВЕНСТВА ДИСПЕРСИЙ")
    print("-" * 50)

    # Тест Левена (более устойчивый к ненормальности)
    levene_stat, levene_p = stats.levene(city_residents, rural_residents)
    print(f"Тест Левена:")
    print(f"  Статистика: {levene_stat:.4f}")
    print(f"  P-значение: {levene_p:.6f}")

    equal_var = levene_p >= alpha
    print(f"Результат:")
    if equal_var:
        print("✓ Дисперсии можно считать равными (равные дисперсии)")
        test_type = "t-критерий Стьюдента (равные дисперсии)"
    else:
        print("✗ Дисперсии статистически различны (неравные дисперсии)")
        test_type = "Критерий Уэлча (неравные дисперсии)"

    # 3. ПАРАМЕТРИЧЕСКИЙ T-ТЕСТ
    print("\n3. ДВУХВЫБОРОЧНЫЙ T-ТЕСТ")
    print("-" * 50)

    print(f"Формулировка гипотез:")
    print(f"H₀: μ₁ = μ₂ (горожане и селяне имеют одинаковое среднее давление)")
    print(f"H₁: μ₁ > μ₂ (горожане имеют более высокое давление, чем селяне)")
    print(f"Тест: {test_type}")
    print()

    # Выполнение теста
    if equal_var:
        # t-критерий Стьюдента с равными дисперсиями
        t_stat, p_value = stats.ttest_ind(city_residents, rural_residents, equal_var=True)
    else:
        # Критерий Уэлча (неравные дисперсии)
        t_stat, p_value = stats.ttest_ind(city_residents, rural_residents, equal_var=False)

    print(f"Наблюдаемое значение статистики: {t_stat:.4f}")
    print(f"P-значение: {p_value:.6f}")

    # Степени свободы
    if equal_var:
        df = n1 + n2 - 2
        df_description = "n₁ + n₂ - 2"
    else:
        # Для критерия Уэлча
        s1_sq = std1**2
        s2_sq = std2**2
        df = (s1_sq/n1 + s2_sq/n2)**2 / ((s1_sq/n1)**2/(n1-1) + (s2_sq/n2)**2/(n2-1))
        df_description = "Уэлча (приближенно)"

    print(f"Степени свободы: {df:.1f} (формула: {df_description})")
    print()

    # Критическое значение
    t_critical = stats.t.ppf(1 - alpha, df)
    print(f"Критическое значение (t_{1-alpha:.2f}): {t_critical:.4f}")
    print()

    # 4. Принятие решения
    print("4. РЕЗУЛЬТАТ ТЕСТА")
    print("-" * 50)

    reject_null = p_value < alpha

    if reject_null:
        print(f"P-значение ({p_value:.6f}) < α ({alpha})")
        print("Отвергаем основную гипотезу H₀")
        print("Принимаем альтернативную гипотезу H₁")
        print("✓ Горожане имеют статистически значимо БОЛЬШЕЕ давление, чем селяне")
    else:
        print(f"P-значение ({p_value:.6f}) ≥ α ({alpha})")
        print("Нет оснований отвергать основную гипотезу H₀")
        print("✗ Нельзя считать верной гипотезу о том, что горожане имеют")
        print("  большее давление, чем селяне")

    print()
    print("5. ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ")
    print("-" * 50)

    # Сравнение с критическим значением
    if t_stat > t_critical:
        print(f"tнабл ({t_stat:.4f}) > tкр ({t_critical:.4f})")
        print("Наблюдаемое значение попадает в критическую область")
    else:
        print(f"tнабл ({t_stat:.4f}) ≤ tкр ({t_critical:.4f})")
        print("Наблюдаемое значение не попадает в критическую область")

    # Доверительный интервал для разности средних
    if equal_var:
        pooled_var = ((n1-1)*std1**2 + (n2-1)*std2**2) / (n1 + n2 - 2)
        se_diff = np.sqrt(pooled_var * (1/n1 + 1/n2))
    else:
        se_diff = np.sqrt(std1**2/n1 + std2**2/n2)

    diff_mean = mean1 - mean2
    ci_lower = diff_mean - stats.t.ppf(1 - alpha/2, df) * se_diff
    ci_upper = diff_mean + stats.t.ppf(1 - alpha/2, df) * se_diff

    print(f"Разность средних (x̄₁ - x̄₂): {diff_mean:.2f}")
    print(f"95% доверительный интервал для разности: [{ci_lower:.2f}, {ci_upper:.2f}]")

# 6. ПРАКТИЧЕСКАЯ ИНТЕРПРЕТАЦИЯ
print()
print("ПРАКТИЧЕСКАЯ ИНТЕРПРЕТАЦИЯ:")
print("-" * 50)
if not both_normal:
    print("Поскольку данные не имеют нормального распределения,")
    print("использован непараметрический критерий Манна-Уитни.")
    print("Этот тест сравнивает медианы, а не средние значения.")

if 'reject_null' in locals():
    if not reject_null:
        print("Разность в давлении между горожанами и селянами не является")
        print("статистически значимой на уровне 5%.")
    else:
        if both_normal:
            print(f"Разность в давлении статистически значима. Среднее давление")
            print(f"у горожан выше на {diff_mean:.1f} мм рт.ст. по сравнению с селянами.")
        else:
            print("Разность в давлении статистически значима согласно")
            print("непараметрическому критерию Манна-Уитни.")

if __name__ == "__main__":
    pass
