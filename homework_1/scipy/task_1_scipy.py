import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def main():
    # Открываем файл для записи результатов
    result_file = open('RESULT.md', 'w')
    result_file.write("# Результаты выполнения задания 1\n\n")
    result_file.write("Метод моментов для нормального распределения с μ=2, σ=4.\n\n")

    def print_and_write(text):
        print(text)
        result_file.write(text + '\n')

    def print_and_write_no_nl(text):
        print(text, end='')

    # Параметры
    mu_true = 2
    sigma_true = 4
    sigma2_true = sigma_true ** 2

    # Размеры выборок
    n1 = 200
    n2 = 1000

    # Генерация выборок с использованием scipy.stats
    np.random.seed(42)
    sample1 = stats.norm.rvs(mu_true, sigma_true, size=n1)
    sample2 = stats.norm.rvs(mu_true, sigma_true, size=n2)

    # Функция для оценок методом моментов
    def method_of_moments_estimates(sample):
        n = len(sample)
        mean_hat = np.mean(sample)
        mean_sq_hat = np.mean(sample ** 2)
        var_hat = mean_sq_hat - mean_hat ** 2
        return mean_hat, var_hat

    # Оценки для n=200 и 1000
    mu_hat1, sigma2_hat1 = method_of_moments_estimates(sample1)
    mu_hat2, sigma2_hat2 = method_of_moments_estimates(sample2)

    print_and_write("## Оценки параметров")
    print_and_write("")
    print_and_write("| Размер выборки | \\hat{μ} | \\hat{σ²} | Истинные μ | Истинные σ² |")
    print_and_write("|-----------------|----------|------------|-------------|--------------|")
    print_and_write(f"| 200             | {mu_hat1:.4f} | {sigma2_hat1:.4f} | {mu_true}        | {sigma2_true}      |")
    print_and_write(f"| 1000            | {mu_hat2:.4f} | {sigma2_hat2:.4f} | {mu_true}        | {sigma2_true}      |")
    print_and_write("")

    # Сравнение
    print_and_write("## Сравнение с истинными значениями")
    print_and_write("")
    print_and_write("| Размер выборки | Ошибка μ | Ошибка σ² |")
    print_and_write("|-----------------|-----------|------------|")
    print_and_write(f"| 200             | {abs(mu_hat1 - mu_true):.4f}    | {abs(sigma2_hat1 - sigma2_true):.4f}     |")
    print_and_write(f"| 1000            | {abs(mu_hat2 - mu_true):.4f}    | {abs(sigma2_hat2 - sigma2_true):.4f}     |")
    print_and_write("")

    # Также вывести в консоль для проверки в процессе отладки
    print(fr"Для n=200: \hat{{μ}} = {mu_hat1:.4f}, \hat{{σ²}} = {sigma2_hat1:.4f}")
    print(f"Истинные: μ = {mu_true}, σ² = {sigma2_true}")
    print(fr"Для n=1000: \hat{{μ}} = {mu_hat2:.4f}, \hat{{σ²}} = {sigma2_hat2:.4f}")
    print(f"Истинные: μ = {mu_true}, σ² = {sigma2_true}")
    print("\nСравнение:")
    print(fr"n=200: |\hat{{μ}} - μ| = {abs(mu_hat1 - mu_true):.4f}, |\hat{{σ²}} - σ²| = {abs(sigma2_hat1 - sigma2_true):.4f}")
    print(fr"n=1000: |\hat{{μ}} - μ| = {abs(mu_hat2 - mu_true):.4f}, |\hat{{σ²}} - σ²| = {abs(sigma2_hat2 - sigma2_true):.4f}")

    # Визуализация
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Для n=200
    axes[0].hist(sample1, bins=30, density=True, alpha=0.7, label='Выборка')
    x = np.linspace(mu_true - 4*sigma_true, mu_true + 4*sigma_true, 100)
    axes[0].plot(x, stats.norm.pdf(x, mu_true, sigma_true), 'r-', label='Истинное')
    axes[0].plot(x, stats.norm.pdf(x, mu_hat1, np.sqrt(sigma2_hat1)), 'g--', label='Оценка')
    axes[0].set_title(f'n=200: μ={mu_hat1:.2f}, σ²={sigma2_hat1:.2f}')
    axes[0].legend()

    # Для n=1000
    axes[1].hist(sample2, bins=30, density=True, alpha=0.7, label='Выборка')
    axes[1].plot(x, stats.norm.pdf(x, mu_true, sigma_true), 'r-', label='Истинное')
    axes[1].plot(x, stats.norm.pdf(x, mu_hat2, np.sqrt(sigma2_hat2)), 'g--', label='Оценка')
    axes[1].set_title(f'n=1000: μ={mu_hat2:.2f}, σ²={sigma2_hat2:.2f}')
    axes[1].legend()

    plt.savefig('task_1_plots.png')

    # Добавляем изображение в файл
    result_file.write("\n## Графики\n\n")
    result_file.write("![Графики](task_1_plots.png)\n")
    result_file.close()

if __name__ == "__main__":
    main()
