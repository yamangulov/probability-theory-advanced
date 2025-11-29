import math
from scipy import stats

def main():
    # Открываем файл для записи результатов
    result_file = open('RESULT_3.md', 'w')
    result_file.write("# Результаты выполнения задания 3\n\n")
    result_file.write("Строим точный доверительный интервал для среднего μ с надёжностью 0.95.\n\n")
    result_file.write("Дано: генеральная совокупность распределена нормально со средним квадратическим отклонением σ=5, выборочная средняя x̄=24.15, объём выборки n=100.\n\n")

    def print_and_write(text):
        print(text)
        result_file.write(text + '\n')

    # Шаг 1: Выбрать подходящую формулу доверительного интервала
    print_and_write("## Шаг 1: Выбрать подходящую формулу доверительного интервала")
    print_and_write("")
    print_and_write("Поскольку дисперсия генеральной совокупности известна (σ=5), используем точный доверительный интервал для среднего при известной дисперсии:")
    print_and_write("")
    print_and_write("$$P \\left( \\bar{x} - z_{1-\\frac{\\alpha}{2}} \\cdot \\frac{\\sigma}{\\sqrt{n}} \\leq \\mu \\leq \\bar{x} + z_{1-\\frac{\\alpha}{2}} \\cdot \\frac{\\sigma}{\\sqrt{n}} \\right) = 1-\\alpha$$")
    print_and_write("")
    print_and_write("Где α=0.05, 1-α=0.95.")
    print_and_write("")

    # Шаг 2: Применить формулу для доверительного интервала
    print_and_write("## Шаг 2: Применить формулу для доверительного интервала")
    print_and_write("")
    print_and_write("Используем scipy.stats для вычисления доверительного интервала.")
    print_and_write("")
    x_bar = 24.15
    sigma = 5
    n = 100
    alpha = 0.05

    # Вычисление доверительного интервала с использованием scipy.stats.norm.interval
    # Для известной дисперсии, loc = x_bar, scale = sigma / sqrt(n)
    ci = stats.norm.interval(1 - alpha, loc=x_bar, scale=sigma / math.sqrt(n))

    print_and_write(f"Доверительный интервал с использованием scipy.stats.norm.interval: {ci}")
    print_and_write("")
    print_and_write("Нижняя граница: " + str(ci[0]))
    print_and_write("")
    print_and_write("Верхняя граница: " + str(ci[1]))
    print_and_write("")

    # Шаг 3: Получить конкретный доверительный интервал для среднего
    print_and_write("## Шаг 3: Получить конкретный доверительный интервал для среднего")
    print_and_write("")
    print_and_write("Доверительный интервал с надёжностью 0.95:")
    print_and_write("")
    print_and_write(f"$$ {ci[0]:.2f} \\leq \\mu \\leq {ci[1]:.2f} $$")
    print_and_write("")
    print_and_write("Или в интервальной форме: (" + str(ci[0]) + ", " + str(ci[1]) + ")")

    result_file.close()

if __name__ == "__main__":
    main()
