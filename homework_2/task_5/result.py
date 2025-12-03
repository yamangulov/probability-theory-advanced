import numpy as np
from scipy import stats
from scipy.stats import fisher_exact

# Данные задачи 5
print("Задача 5: Проверка гипотезы о разности долей (вероятностей)")
print("Исследование эффективности лекарства против аллергии")
print()

# Данные таблицы сопряженности
print("Данные:")
print("Группа 1 (принимавшие лекарство):")
print("  Заболели: 3 человека")
print("  Не заболели: 172 человека")
print("  Общий размер: 175 человек")
print()
print("Группа 2 (не принимавшие):")
print("  Заболели: 32 человека")
print("  Не заболели: 168 человек")
print("  Общий размер: 200 человек")
print()

# Конструируем таблицу сопряженности
#            Заболели  Не заболели  Всего
# Группа 1:      3           172      175
# Группа 2:     32           168      200
# Всего:        35           340      375

sick1, not_sick1 = 3, 172
sick2, not_sick2 = 32, 168

n1 = sick1 + not_sick1  # 175
n2 = sick2 + not_sick2  # 200

# Наблюдаемые доли заболевших
p_hat1 = sick1 / n1
p_hat2 = sick2 / n2

print(f"Наблюдаемые доли:")
print(f"Группа 1 (принимавшие): p̂₁ = {p_hat1:.4f} ({p_hat1:.1%})")
print(f"Группа 2 (не принимавшие): p̂₂ = {p_hat2:.4f} ({p_hat2:.1%})")
print(f"Разность: p̂₁ - p̂₂ = {p_hat1 - p_hat2:.4f}")
print()

# Параметры теста
alpha = 0.05

# 1. ПРОВЕРКА УСЛОВИЙ ПРИМЕНИМОСТИ Z-ТЕСТА ДВУХ ДОЛЕЙ
print("1. ПРОВЕРКА УСЛОВИЙ ПРИМЕНИМОСТИ")
print("-" * 50)

# Условия для z-теста двух долей
conditions = {
    "n₁×p̂₁": n1 * p_hat1,
    "n₁×(1-p̂₁)": n1 * (1 - p_hat1),
    "n₂×p̂₂": n2 * p_hat2,
    "n₂×(1-p̂₂)": n2 * (1 - p_hat2)
}

all_satisfied = True
for condition, value in conditions.items():
    satisfied = value >= 5
    status = "✓" if satisfied else "✗"
    print(f"{condition} = {value:.1f} {'≥ 5' if satisfied else '< 5'}: {status}")
    if not satisfied:
        all_satisfied = False

print()
if all_satisfied:
    print("✓ Все условия применимости z-теста выполнены")
else:
    print("✗ Некоторые условия применимости НЕ выполнены")
    print("⚠ z-тест может давать неточные результаты!")
    print("  Рекомендуется использовать точный тест Фишера")

print()

# 2. ФОРМУЛИРОВКА ГИПОТЕЗ
print("2. ФОРМУЛИРОВКА ГИПОТЕЗ")
print("-" * 50)
print("H₀: p₁ = p₂ (лекарство неэффективно, доли заболевших одинаковы)")
print("H₁: p₁ < p₂ (лекарство эффективно, доля заболевших в группе 1 меньше)")
print("Критерий: Левосторонний z-тест для разности долей")
print()

if all_satisfied:
    # 3. Z-ТЕСТ ДЛЯ РАЗНОСТИ ДОЛЕЙ
    print("3. Z-ТЕСТ ДЛЯ РАЗНОСТИ ДОЛЕЙ")
    print("-" * 50)

    # Объединенная оценка доли заболевших
    p_pooled = (sick1 + sick2) / (n1 + n2)
    print(f"Объединенная оценка доли заболевших: p̂об = {p_pooled:.4f}")

    # Стандартная ошибка разности долей при верности H0
    se_diff = np.sqrt(p_pooled * (1 - p_pooled) * (1/n1 + 1/n2))
    print(f"Стандартная ошибка разности: σ₀ = {se_diff:.4f}")

    # Z-статистика
    z_stat = (p_hat1 - p_hat2) / se_diff
    print(f"Z-статистика: zнабл = (p̂₁ - p̂₂)/σ₀ = {z_stat:.4f}")
    print()

    # Критическое значение и P-значение
    z_critical = stats.norm.ppf(alpha)
    p_value = stats.norm.cdf(z_stat)  # Левосторонний тест

    print(f"Критическое значение (α = {alpha}):")
    print(f"Левая критическая точка: z_{alpha} = {z_critical:.3f}")
    print(f"P-значение: {p_value:.6f}")
    print()

    # 4. РЕЗУЛЬТАТ ТЕСТА
    print("4. РЕЗУЛЬТАТ ТЕСТА")
    print("-" * 50)

    reject_null = p_value < alpha

    if reject_null:
        print(f"P-значение ({p_value:.6f}) < α ({alpha})")
        print("Отвергаем основную гипотезу H₀")
        print("Принимаем альтернативную гипотезу H₁")
        print("✓ Лекарство СТАТИСТИЧЕСКИ ЭФФЕКТИВНО")
        print(f"  Доля заболевших снизилась с {p_hat2:.1%} до {p_hat1:.1%}")
        
        # Меры эффекта
        relative_risk = p_hat1 / p_hat2
        odds_ratio = (sick1 * not_sick2) / (sick2 * not_sick1)
        absolute_risk_reduction = p_hat2 - p_hat1
        relative_risk_reduction = (p_hat2 - p_hat1) / p_hat2
        
        print(f"  Относительный риск: {relative_risk:.3f}")
        print(f"  Отношение шансов: {odds_ratio:.3f}")
        print(f"  Абсолютное снижение риска: {absolute_risk_reduction:.1%}")
        print(f"  Относительное снижение риска: {relative_risk_reduction:.1%}")
        
    else:
        print(f"P-значение ({p_value:.6f}) ≥ α ({alpha})")
        print("Нет оснований отвергать основную гипотезу H₀")
        print("✗ Эффективность лекарства статистически не доказана")

    print()
    print("5. ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ")
    print("-" * 50)

    # Сравнение с критическим значением
    if z_stat < z_critical:
        print(f"zнабл ({z_stat:.4f}) < zкр ({z_critical:.4f})")
        print("zнабл попадает в критическую область")
    else:
        print(f"zнабл ({z_stat:.4f}) ≥ zкр ({z_critical:.4f})")
        print("zнабл не попадает в критическую область")

    # Доверительный интервал для разности долей
    se_individual = np.sqrt(p_hat1 * (1 - p_hat1) / n1 + p_hat2 * (1 - p_hat2) / n2)
    diff = p_hat1 - p_hat2
    ci_lower = diff - stats.norm.ppf(1 - alpha/2) * se_individual
    ci_upper = diff + stats.norm.ppf(1 - alpha/2) * se_individual

    print(f"Разность долей (p̂₁ - p̂₂): {diff:.4f}")
    print(f"95% доверительный интервал для разности: [{ci_lower:.4f}, {ci_upper:.4f}]")

else:
    # Точный тест Фишера
    print("3. ТОЧНЫЙ ТЕСТ ФИШЕРА")
    print("-" * 50)
    print("Поскольку условия применимости z-теста не выполнены,")
    print("используем точный тест Фишера")
    print()

    try:
        # Тест Фишера
        odds_ratio, p_value = fisher_exact([[sick1, not_sick1], [sick2, not_sick2]], alternative='less')
        
        print(f"Точный тест Фишера:")
        print(f"Отношение шансов: {odds_ratio:.3f}")
        print(f"P-значение: {p_value:.6f}")
        
        print()
        print("4. РЕЗУЛЬТАТ ТЕСТА")
        print("-" * 50)
        
        reject_null = p_value < alpha
        
        if reject_null:
            print(f"P-значение ({p_value:.6f}) < α ({alpha})")
            print("Отвергаем основную гипотезу H₀")
            print("Принимаем альтернативную гипотезу H₁")
            print("✓ Лекарство СТАТИСТИЧЕСКИ ЭФФЕКТИВНО")
            
            # Меры эффекта
            relative_risk = p_hat1 / p_hat2
            absolute_risk_reduction = p_hat2 - p_hat1
            relative_risk_reduction = (p_hat2 - p_hat1) / p_hat2
            
            print(f"  Доля заболевших снизилась с {p_hat2:.1%} до {p_hat1:.1%}")
            print(f"  Относительный риск: {relative_risk:.3f}")
            print(f"  Отношение шансов: {odds_ratio:.3f}")
            print(f"  Абсолютное снижение риска: {absolute_risk_reduction:.1%}")
            print(f"  Относительное снижение риска: {relative_risk_reduction:.1%}")
            
        else:
            print(f"P-значение ({p_value:.6f}) ≥ α ({alpha})")
            print("Нет оснований отвергать основную гипотезу H₀")
            print("✗ Эффективность лекарства статистически не доказана")
            
    except Exception as e:
        print(f"Ошибка при вычислении теста Фишера: {e}")
        p_value = 1.0

print()
print("6. ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ (если применим z-тест)")
print("-" * 50)
if all_satisfied:
    # Альтернативный тест: точный критерий Фишера (для сравнения)
    odds_ratio_fisher, p_fisher = fisher_exact([[sick1, not_sick1], [sick2, not_sick2]], alternative='less')

    print("Альтернативный тест (точное значение Фишера):")
    print(f"Отношение шансов: {odds_ratio_fisher:.3f}")
    print(f"P-значение (точное): {p_fisher:.6f}")
    print(f"Сравнение p-значений:")
    print(f"  z-тест: {p_value:.6f}")
    print(f"  тест Фишера: {p_fisher:.6f}")
else:
    print("Тест Фишера уже использован как основной метод.")

print()
print("ПРАКТИЧЕСКАЯ ИНТЕРПРЕТАЦИЯ:")
print("-" * 50)
if 'reject_null' in locals() and reject_null:
    print("Лекарство показало статистически значимую эффективность.")
    print(f"Заболеваемость снизилась с {p_hat2:.1%} до {p_hat1:.1%},")
    print(f"что составляет абсолютное снижение риска на {absolute_risk_reduction:.1%}.")
else:
    print("На основании проведенного анализа нельзя сделать вывод")
    print("о статистически значимой эффективности лекарства.")

print()
if all_satisfied:
    print(f"ИСПОЛЬЗОВАННЫЙ МЕТОД: z-тест для разности долей")
else:
    print(f"ИСПОЛЬЗОВАННЫЙ МЕТОД: точный тест Фишера")

if __name__ == "__main__":
    pass
