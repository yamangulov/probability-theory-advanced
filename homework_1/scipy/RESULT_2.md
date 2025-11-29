# Результаты выполнения задания 2

Оценка параметра θ методом максимального правдоподобия для распределения с плотностью:

$$f(x)=\frac{2x^3}{\sqrt{2\pi}} \cdot e^{-\frac{(x^4-\theta)^2}{2}}$$

## Шаг 0: Функция правдоподобия

$$L(X_1,...,X_n, \theta)=\prod_{i=1}^n \left(\frac{2x_i^3}{\sqrt{2\pi}} \cdot e^{-\frac{(x_i^4-\theta)^2}{2}}\right)$$

## Шаг 1: Упростить функцию правдоподобия

$$L(\theta) = \left(\frac{2}{\sqrt{2\pi}}\right)^n \cdot \prod_{i=1}^n x_i^3 \cdot \exp\left(-\frac{1}{2} \sum_{i=1}^n (x_i^4 - \theta)^2\right)$$

## Шаг 2: Прологарифмировать функцию правдоподобия

$$\ell(\theta) = n \ln\left(\frac{2}{\sqrt{2\pi}}\right) + 3 \sum_{i=1}^n \ln x_i - \frac{1}{2} \sum_{i=1}^n (x_i^4 - \theta)^2$$

Раскрывая сумму:
$$\ell(\theta) = n \ln\left(\frac{2}{\sqrt{2\pi}}\right) + 3 \sum_{i=1}^n \ln x_i - \frac{1}{2} \sum_{i=1}^n x_i^8 + \theta \sum_{i=1}^n x_i^4 - \frac{n}{2} \theta^2$$

## Шаг 3: Найти частную производную относительно θ

$$\frac{\partial \ell(\theta)}{\partial \theta} = \sum_{i=1}^n x_i^4 - n \theta$$

## Шаг 4: Приравнять производную к нулю

$$\sum_{i=1}^n x_i^4 - n \theta = 0$$

$$\theta = \frac{1}{n} \sum_{i=1}^n x_i^4$$

**Оценка максимального правдоподобия: $\hat{\theta} = \frac{1}{n} \sum_{i=1}^n X_i^4$**
## Численная проверка с использованием SciPy

Численная оценка θ с использованием scipy.optimize: nan

Аналитическая оценка для этой выборки: 2.003181150402443

