"""
Задача 2. Анализ корреляций между дозировкой лекарства, временем действия и продолжительностью эффекта
Визуализация результатов корреляционного анализа
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import warnings
warnings.filterwarnings('ignore')

# Настройка отображения для кириллицы
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

def analyze_and_visualize_correlations():
    """
    Анализ и визуализация корреляций между дозировкой лекарства, временем действия и продолжительностью эффекта.
    
    Функция выполняет полный корреляционный анализ трех переменных:
    - X: дозировка лекарства (мг)
    - Y: время до действия лекарства (мин)  
    - Z: продолжительность действия лекарства (ч)
    
    Вычисляет и визуализирует:
    - Матрицу корреляций в виде тепловой карты
    - Диаграммы рассеяния для всех пар переменных с линиями тренда
    - Коэффициенты корреляции Пирсона и их статистическую значимость
    - Основные статистики (среднее и стандартное отклонение)
    
    Выводит результаты в консоль и создает визуализации.
    """
    
    print("=" * 80)
    print("ЗАДАЧА 2. АНАЛИЗ И ВИЗУАЛИЗАЦИЯ КОРРЕЛЯЦИЙ МЕЖДУ ДОЗИРОВКОЙ ЛЕКАРСТВА,")
    print("ВРЕМЕНЕМ ДЕЙСТВИЯ И ПРОДОЛЖИТЕЛЬНОСТЬЮ ЭФФЕКТА")
    print("=" * 80)
    print()
    
    # Исходные данные
    print("ИСХОДНЫЕ ДАННЫЕ:")
    print("-" * 40)
    patient_numbers = np.arange(1, 11)
    X = np.array([3.0, 3.5, 4.0, 5.0, 6.0, 6.5, 7.0, 8.0, 8.5, 9.0])  # Дозировка (мг)
    Y = np.array([17, 22, 14, 17, 15, 12, 11, 9, 8, 6])  # Время до действия (мин)
    Z = np.array([9.1, 5.5, 12.3, 9.2, 14.2, 16.8, 22.0, 18.3, 24.5, 22.7])  # Продолжительность (ч)
    
    print(f"Пациенты:           {patient_numbers}")
    print(f"X (дозировка, мг):  {X}")
    print(f"Y (время до действия, мин): {Y}")
    print(f"Z (продолжительность, ч):   {Z}")
    print()
    
    # Создание DataFrame для удобства работы
    data = pd.DataFrame({
        'Пациент': patient_numbers,
        'X_Дозировка_мг': X,
        'Y_Время_до_действия_мин': Y,
        'Z_Продолжительность_действия_ч': Z
    })
    
    # Основные статистики
    print("ОСНОВНЫЕ СТАТИСТИКИ:")
    print("-" * 40)
    variables = ['X_Дозировка_мг', 'Y_Время_до_действия_мин', 'Z_Продолжительность_действия_ч']
    variable_names = {
        'X_Дозировка_мг': 'X (дозировка)',
        'Y_Время_до_действия_мин': 'Y (время до действия)', 
        'Z_Продолжительность_действия_ч': 'Z (продолжительность)'
    }
    
    for var in variables:
        name = variable_names[var]
        mean_val = data[var].mean()
        std_val = data[var].std()
        print(f"{name:25} μ = {mean_val:6.2f}, σ = {std_val:6.2f}")
    print()
    
    # Вычисление матрицы корреляций
    print("МАТРИЦА ВЫБОРОЧНЫХ КОРРЕЛЯЦИЙ:")
    print("-" * 40)
    correlation_matrix = data[variables].corr()
    
    # Форматированный вывод матрицы корреляций
    print(f"{'Переменная':<30}", end="")
    for var in variables:
        short_name = var.split('_')[0]
        print(f"{short_name:>10}", end="")
    print()
    
    for i, var in enumerate(variables):
        short_name = var.split('_')[0]
        print(f"{short_name:30}", end="")
        for j, other_var in enumerate(variables):
            corr_value = correlation_matrix.iloc[i, j]
            print(f"{corr_value:10.4f}", end="")
        print()
    print()
    
    # Создание визуализаций
    create_correlation_visualizations(data, correlation_matrix)
    
    # Детальный анализ корреляций между парами
    print("ДЕТАЛЬНЫЙ АНАЛИЗ КОРРЕЛЯЦИЙ:")
    print("-" * 40)
    
    pairs = [
        ('X_Дозировка_мг', 'Y_Время_до_действия_мин', 'X и Y', 'дозировка и время до действия'),
        ('Y_Время_до_действия_мин', 'Z_Продолжительность_действия_ч', 'Y и Z', 'время до действия и продолжительность'),
        ('X_Дозировка_мг', 'Z_Продолжительность_действия_ч', 'X и Z', 'дозировка и продолжительность')
    ]
    
    correlation_results = {}
    
    for var1, var2, pair_name, description in pairs:
        # Коэффициент корреляции Пирсона
        corr_coef, p_value = pearsonr(data[var1], data[var2])
        
        # Статистическая значимость
        alpha = 0.05
        is_significant = p_value < alpha
        
        correlation_results[pair_name] = {
            'correlation': corr_coef,
            'p_value': p_value,
            'significant': is_significant
        }
        
        # Интерпретация силы корреляции
        abs_corr = abs(corr_coef)
        if abs_corr < 0.1:
            strength = "пренебрежимо малая"
        elif abs_corr < 0.3:
            strength = "слабая"
        elif abs_corr < 0.5:
            strength = "умеренная"
        elif abs_corr < 0.7:
            strength = "сильная"
        else:
            strength = "очень сильная"
        
        direction = "положительная" if corr_coef > 0 else "отрицательная"
        
        print(f"Пара {pair_name} ({description}):")
        print(f"  Коэффициент корреляции:    r = {corr_coef:.4f}")
        print(f"  p-значение:                {p_value:.4f}")
        print(f"  Статистически значима:     {'Да' if is_significant else 'Нет'} (α = 0.05)")
        print(f"  Интерпретация:             {strength} {direction} корреляция")
        print()
    
    # Общие выводы
    print("ОБЩИЕ ВЫВОДЫ:")
    print("-" * 40)
    print("Анализ показывает следующие закономерности:")
    print()
    
    for pair_name, results in correlation_results.items():
        corr = results['correlation']
        significant = results['significant']
        
        if significant:
            if corr > 0:
                trend = "положительная связь - при увеличении одной переменной другая также увеличивается"
            else:
                trend = "отрицательная связь - при увеличении одной переменной другая уменьшается"
        else:
            trend = "статистически незначимая связь"
        
        print(f"• {pair_name}: {trend}")
    
    print()
    print("ПРАКТИЧЕСКАЯ ИНТЕРПРЕТАЦИЯ:")
    print("-" * 40)
    print("• Дозировка лекарства (X) и время до действия (Y): отрицательная корреляция")
    print("  - Чем больше дозировка, тем быстрее наступает эффект (меньше время ожидания)")
    print()
    print("• Время до действия (Y) и продолжительность (Z): отрицательная корреляция")
    print("  - Чем быстрее наступает эффект, тем дольше он длится")
    print()
    print("• Дозировка лекарства (X) и продолжительность (Z): положительная корреляция")
    print("  - Большая дозировка приводит к более длительному эффекту")
    print()
    
    print("ЗНАЧИМОСТЬ КОРРЕЛЯЦИЙ:")
    print("-" * 40)
    print("*** - p < 0.05")
    for pair_name, results in correlation_results.items():
        var1, var2 = pair_name.split(' и ')
        corr = results['correlation']
        significant = "***" if results['significant'] else ""
        print(f"• {var1}-{var2}: r = {corr:.3f}{significant}")
    
    print()
    print("Визуализации сохранены в файл: correlation_analysis.png")
    print()
    print("=" * 80)
    print("АНАЛИЗ И ВИЗУАЛИЗАЦИЯ ЗАВЕРШЕНЫ")
    print("=" * 80)

def create_correlation_visualizations(data, correlation_matrix):
    """Создание визуализаций корреляционного анализа"""
    
    # Настройка размера фигуры
    fig = plt.figure(figsize=(16, 12))
    
    # 1. Тепловая карта корреляций
    plt.subplot(2, 3, 1)
    sns.heatmap(correlation_matrix, 
                annot=True, 
                cmap='RdBu_r', 
                center=0,
                square=True,
                fmt='.3f',
                cbar_kws={'label': 'Коэффициент корреляции'})
    plt.title('Матрица корреляций', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    # 2-4. Scatter plots для каждой пары
    pairs_data = [
        ('X_Дозировка_мг', 'Y_Время_до_действия_мин', 'Дозировка (мг)', 'Время до действия (мин)'),
        ('Y_Время_до_действия_мин', 'Z_Продолжительность_действия_ч', 'Время до действия (мин)', 'Продолжительность (ч)'),
        ('X_Дозировка_мг', 'Z_Продолжительность_действия_ч', 'Дозировка (мг)', 'Продолжительность (ч)')
    ]
    
    for i, (x_var, y_var, x_label, y_label) in enumerate(pairs_data, 2):
        plt.subplot(2, 3, i)
        
        # Scatter plot
        plt.scatter(data[x_var], data[y_var], alpha=0.7, s=80, color=f'C{i-2}')
        
        # Линия тренда
        z = np.polyfit(data[x_var], data[y_var], 1)
        p = np.poly1d(z)
        plt.plot(data[x_var], p(data[x_var]), "r--", alpha=0.8, linewidth=2)
        
        # Вычисление корреляции для заголовка
        corr_coef, _ = pearsonr(data[x_var], data[y_var])
        
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(f'{x_label} vs {y_label}\nr = {corr_coef:.3f}', fontweight='bold')
        plt.grid(True, alpha=0.3)
    
    # 5. Обзорная диаграмма рассеяния (pair plot)
    plt.subplot(2, 3, 5)
    
    # Создаем упрощенную версий pair plot
    variables = ['X_Дозировка_мг', 'Y_Время_до_действия_мин', 'Z_Продолжительность_действия_ч']
    labels = ['Дозировка', 'Время до\nдействия', 'Продолжительность']
    
    # Создаем корреляционную матрицу для отображения
    corr_data = data[variables].corr().values
    
    # Тепловая карта для обзора
    sns.heatmap(corr_data, 
                annot=True, 
                xticklabels=labels,
                yticklabels=labels,
                cmap='RdBu_r', 
                center=0,
                square=True,
                fmt='.3f')
    plt.title('Корреляционная матрица\n(обзор)', fontweight='bold')
    
    # 6. Статистические характеристики
    plt.subplot(2, 3, 6)
    plt.axis('off')
    
    # Создание текстового блока с основной статистикой
    stats_text = "ОСНОВНЫЕ СТАТИСТИКИ:\n\n"
    
    for var in variables:
        var_short = var.split('_')[0]
        mean_val = data[var].mean()
        std_val = data[var].std()
        stats_text += f"{var_short}: μ = {mean_val:.2f}, σ = {std_val:.2f}\n"
    
    stats_text += "\nКОРРЕЛЯЦИИ:\n"
    for i, var1 in enumerate(variables):
        for j, var2 in enumerate(variables):
            if i < j:  # Только верхний треугольник
                corr_val = correlation_matrix.iloc[i, j]
                var1_short = var1.split('_')[0]
                var2_short = var2.split('_')[0]
                stats_text += f"{var1_short}-{var2_short}: r = {corr_val:.3f}\n"
    
    plt.text(0.1, 0.9, stats_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top', fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('correlation_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Основная функция"""
    analyze_and_visualize_correlations()

if __name__ == "__main__":
    main()
