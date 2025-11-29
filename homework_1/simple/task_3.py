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
    print_and_write("Подставим известные значения:")
    print_and_write("")
    print_and_write("α = 0.05")
    print_and_write("")
    print_and_write("1-α = 0.95")
    print_and_write("")
    print_and_write("z_{1-α/2} = z_{0.975} ≈ 1.96")
    print_and_write("")
    print_and_write("σ = 5")
    print_and_write("")
    print_and_write("x̄ = 24.15")
    print_and_write("")
    print_and_write("n = 100")
    print_and_write("")
    print_and_write("Сначала вычислим стандартную ошибку среднего:")
    print_and_write("")
    print_and_write("$$\\frac{\\sigma}{\\sqrt{n}} = \\frac{5}{\\sqrt{100}} = \\frac{5}{10} = 0.5$$")
    print_and_write("")
    print_and_write("Теперь вычислим границы интервала:")
    print_and_write("")
    print_and_write("Нижняя граница:")
    print_and_write("")
    print_and_write("$$\\bar{x} - z_{1-\\frac{\\alpha}{2}} \\cdot \\frac{\\sigma}{\\sqrt{n}} = 24.15 - 1.96 \\cdot 0.5 = 24.15 - 0.98 = 23.17$$")
    print_and_write("")
    print_and_write("Верхняя граница:")
    print_and_write("")
    print_and_write("$$\\bar{x} + z_{1-\\frac{\\alpha}{2}} \\cdot \\frac{\\sigma}{\\sqrt{n}} = 24.15 + 1.96 \\cdot 0.5 = 24.15 + 0.98 = 25.13$$")
    print_and_write("")

    # Шаг 3: Получить конкретный доверительный интервал для среднего
    print_and_write("## Шаг 3: Получить конкретный доверительный интервал для среднего")
    print_and_write("")
    print_and_write("Доверительный интервал с надёжностью 0.95:")
    print_and_write("")
    print_and_write("$$23.17 \\leq \\mu \\leq 25.13$$")
    print_and_write("")
    print_and_write("Или в интервальной форме: (23.17, 25.13)")

    result_file.close()

if __name__ == "__main__":
    main()
