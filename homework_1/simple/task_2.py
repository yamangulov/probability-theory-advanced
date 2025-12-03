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
    print_and_write("### Итоговый результат")
    print_and_write("")
    print_and_write("$$L(X_1,...,X_n, \\theta)=\\prod_{i=1}^n p(x_i, \\theta) = \\prod_{i=1}^n \\left(\\frac{2x_i^3}{\\sqrt{2\\pi}} \\cdot e^{-\\frac{(x_i^4-\\theta)^2}{2}}\\right)$$")
    print_and_write("")

    # Шаг 1: Упростить функцию правдоподобия
    print_and_write("## Шаг 1: Упростить функцию правдоподобия")
    print_and_write("")
    print_and_write("Выносим общие множители:")
    print_and_write("$$L(\\theta) = \\prod_{i=1}^n \\left(\\frac{2x_i^3}{\\sqrt{2\\pi}}\\right) \\cdot \\prod_{i=1}^n e^{-\\frac{(x_i^4-\\theta)^2}{2}}$$")
    print_and_write("")
    print_and_write("$$L(\\theta) = \\left(\\frac{2}{\\sqrt{2\\pi}}\\right)^n \\cdot \\prod_{i=1}^n x_i^3 \\cdot \\exp\\left(-\\frac{1}{2} \\sum_{i=1}^n (x_i^4 - \\theta)^2\\right)$$")
    print_and_write("")
    print_and_write("### Итоговый результат")
    print_and_write("")
    print_and_write("$$L(\\theta) = \\left(\\frac{2}{\\sqrt{2\\pi}}\\right)^n \\cdot \\prod_{i=1}^n x_i^3 \\cdot \\exp\\left(-\\frac{1}{2} \\sum_{i=1}^n (x_i^4 - \\theta)^2\\right)$$")
    print_and_write("")

    # Шаг 2: Прологарифмировать функцию правдоподобия
    print_and_write("## Шаг 2: Прологарифмировать функцию правдоподобия")
    print_and_write("")
    print_and_write("$$\\ell(\\theta) = \\ln L(\\theta) = \\ln \\left[ \\left(\\frac{2}{\\sqrt{2\\pi}}\\right)^n \\cdot \\prod_{i=1}^n x_i^3 \\cdot \\exp\\left(-\\frac{1}{2} \\sum_{i=1}^n (x_i^4 - \\theta)^2\\right) \\right]$$")
    print_and_write("")
    print_and_write("Используя свойства логарифма:")
    print_and_write("$$\\ell(\\theta) = n \\ln\\left(\\frac{2}{\\sqrt{2\\pi}}\\right) + \\sum_{i=1}^n \\ln(x_i^3) + \\ln\\left( \\exp\\left(-\\frac{1}{2} \\sum_{i=1}^n (x_i^4 - \\theta)^2\\right) \\right)$$")
    print_and_write("")
    print_and_write("$$\\ell(\\theta) = n \\ln\\left(\\frac{2}{\\sqrt{2\\pi}}\\right) + 3 \\sum_{i=1}^n \\ln x_i - \\frac{1}{2} \\sum_{i=1}^n (x_i^4 - \\theta)^2$$")
    print_and_write("")
    print_and_write("Раскрываем сумму:")
    print_and_write("$$(x_i^4 - \\theta)^2 = x_i^8 - 2\\theta x_i^4 + \\theta^2$$")
    print_and_write("")
    print_and_write("$$\\sum_{i=1}^n (x_i^4 - \\theta)^2 = \\sum_{i=1}^n x_i^8 - 2\\theta \\sum_{i=1}^n x_i^4 + \\theta^2 \\sum_{i=1}^n 1 = \\sum_{i=1}^n x_i^8 - 2\\theta \\sum_{i=1}^n x_i^4 + n \\theta^2$$")
    print_and_write("")
    print_and_write("$$\\ell(\\theta) = n \\ln\\left(\\frac{2}{\\sqrt{2\\pi}}\\right) + 3 \\sum_{i=1}^n \\ln x_i - \\frac{1}{2} \\left( \\sum_{i=1}^n x_i^8 - 2\\theta \\sum_{i=1}^n x_i^4 + n \\theta^2 \\right)$$")
    print_and_write("")
    print_and_write("$$\\ell(\\theta) = n \\ln\\left(\\frac{2}{\\sqrt{2\\pi}}\\right) + 3 \\sum_{i=1}^n \\ln x_i - \\frac{1}{2} \\sum_{i=1}^n x_i^8 + \\theta \\sum_{i=1}^n x_i^4 - \\frac{n}{2} \\theta^2$$")
    print_and_write("")
    print_and_write("### Итоговый результат")
    print_and_write("")
    print_and_write("$$\\ell(\\theta) = n \\ln\\left(\\frac{2}{\\sqrt{2\\pi}}\\right) + 3 \\sum_{i=1}^n \\ln x_i - \\frac{1}{2} \\sum_{i=1}^n x_i^8 + \\theta \\sum_{i=1}^n x_i^4 - \\frac{n}{2} \\theta^2$$")


    # Шаг 3: Найти частную производную относительно θ
    print_and_write("## Шаг 3: Найти частную производную относительно θ")
    print_and_write("")
    print_and_write("Дифференцируем по θ:")
    print_and_write("$$\\frac{\\partial \\ell(\\theta)}{\\partial \\theta} = \\frac{\\partial}{\\partial \\theta} \\left( \\theta \\sum_{i=1}^n x_i^4 - \\frac{n}{2} \\theta^2 \\right) = \\sum_{i=1}^n x_i^4 - n \\theta$$")
    print_and_write("")
    print_and_write("### Итоговый результат")
    print_and_write("")
    print_and_write("$$\\frac{\\partial \\ell(\\theta)}{\\partial \\theta} = \\sum_{i=1}^n x_i^4 - n \\theta$$")
    print_and_write("")

    # Шаг 4: Приравнять производную к нулю
    print_and_write("## Шаг 4: Приравнять производную к нулю")
    print_and_write("")
    print_and_write("$$\\frac{\\partial \\ell(\\theta)}{\\partial \\theta} = 0 \\Rightarrow \\sum_{i=1}^n x_i^4 - n \\theta = 0$$")
    print_and_write("")
    print_and_write("$$n \\theta = \\sum_{i=1}^n x_i^4$$")
    print_and_write("")
    print_and_write("$$\\theta = \\frac{1}{n} \\sum_{i=1}^n x_i^4$$")
    print_and_write("")
    print_and_write("### Оценка максимального правдоподобия")
    print_and_write("")
    print_and_write("$$\\hat{\\theta} = \\frac{1}{n} \\sum_{i=1}^n X_i^4$$")

    result_file.close()

if __name__ == "__main__":
    main()
