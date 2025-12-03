import numpy as np
from scipy.optimize import minimize_scalar

def main():
    # Открываем файл для записи результатов
    result_file = open('RESULT_2.md', 'w')
    result_file.write("# Результаты выполнения задания 2\n\n")
    result_file.write("Оценка параметра θ методом максимального правдоподобия для распределения с плотностью:\n\n")
    result_file.write("$$f(x)=\\frac{2x^3}{\\sqrt{2\\pi}} \\cdot e^{-\\frac{(x^4-\\theta)^2}{2}}$$\n\n")

    def print_and_write(text):
        print(text)
        result_file.write(text + '\n')

    # Шаг 0: Функция правдоподобия
    print_and_write("## Шаг 0: Функция правдоподобия")
    print_and_write("")
    print_and_write("$$L(X_1,...,X_n, \\theta)=\\prod_{i=1}^n \\left(\\frac{2x_i^3}{\\sqrt{2\\pi}} \\cdot e^{-\\frac{(x_i^4-\\theta)^2}{2}}\\right)$$")
    print_and_write("")

    # Шаг 1: Упростить функцию правдоподобия
    print_and_write("## Шаг 1: Упростить функцию правдоподобия")
    print_and_write("")
    print_and_write("$$L(\\theta) = \\left(\\frac{2}{\\sqrt{2\\pi}}\\right)^n \\cdot \\prod_{i=1}^n x_i^3 \\cdot \\exp\\left(-\\frac{1}{2} \\sum_{i=1}^n (x_i^4 - \\theta)^2\\right)$$")
    print_and_write("")

    # Шаг 2: Прологарифмировать функцию правдоподобия
    print_and_write("## Шаг 2: Прологарифмировать функцию правдоподобия")
    print_and_write("")
    print_and_write("$$\\ell(\\theta) = n \\ln\\left(\\frac{2}{\\sqrt{2\\pi}}\\right) + 3 \\sum_{i=1}^n \\ln x_i - \\frac{1}{2} \\sum_{i=1}^n (x_i^4 - \\theta)^2$$")
    print_and_write("")
    print_and_write("Раскрывая сумму:")
    print_and_write("$$\\ell(\\theta) = n \\ln\\left(\\frac{2}{\\sqrt{2\\pi}}\\right) + 3 \\sum_{i=1}^n \\ln x_i - \\frac{1}{2} \\sum_{i=1}^n x_i^8 + \\theta \\sum_{i=1}^n x_i^4 - \\frac{n}{2} \\theta^2$$")
    print_and_write("")

    # Шаг 3: Найти частную производную относительно θ
    print_and_write("## Шаг 3: Найти частную производную относительно θ")
    print_and_write("")
    print_and_write("$$\\frac{\\partial \\ell(\\theta)}{\\partial \\theta} = \\sum_{i=1}^n x_i^4 - n \\theta$$")
    print_and_write("")

    # Шаг 4: Приравнять производную к нулю
    print_and_write("## Шаг 4: Приравнять производную к нулю")
    print_and_write("")
    print_and_write("$$\\sum_{i=1}^n x_i^4 - n \\theta = 0$$")
    print_and_write("")
    print_and_write("$$\\theta = \\frac{1}{n} \\sum_{i=1}^n x_i^4$$")
    print_and_write("")
    print_and_write("**Оценка максимального правдоподобия: $\\hat{\\theta} = \\frac{1}{n} \\sum_{i=1}^n X_i^4$**")

    # Теперь используем SciPy для численной проверки
    print_and_write("## Численная проверка с использованием SciPy")
    print_and_write("")
    # Генерируем тестовую выборку (предположим, что распределение определено, но для демонстрации используем случайные данные)
    # Поскольку плотность нестандартная, для демонстрации сгенерируем выборку из нормального распределения и применим MLE
    np.random.seed(42)
    sample = np.random.normal(0, 1, 100)  # Примерная выборка

    def negative_log_likelihood(theta):
        # Лог-плотность: log(2*x^3 / sqrt(2*pi)) - (x^4 - theta)^2 / 2
        log_f = np.log(2 * sample**3 / np.sqrt(2 * np.pi)) - (sample**4 - theta)**2 / 2
        return -np.sum(log_f)  # Отрицательная сумма для минимизации

    # Минимизируем отрицательную лог-правдоподобие
    result_opt = minimize_scalar(negative_log_likelihood)
    theta_hat_scipy = result_opt.x

    print_and_write(f"Численная оценка θ с использованием scipy.optimize: {theta_hat_scipy:.4f}")
    print_and_write("")
    print_and_write("Аналитическая оценка для этой выборки: " + str(np.mean(sample**4)))
    print_and_write("")

    result_file.close()

if __name__ == "__main__":

    main()
