# Результаты выполнения задания 2

Оценка параметра θ методом максимального правдоподобия для распределения с плотностью:

$$f(x)=\frac{2x^3}{\sqrt{2\pi}} \cdot e^{-\frac{(x^4-\theta)^2}{2}}$$

## Шаг 0: Функция правдоподобия

### Итоговый результат

$$L(X_1,...,X_n, \theta)=\prod_{i=1}^n p(x_i, \theta) = \prod_{i=1}^n \left(\frac{2x_i^3}{\sqrt{2\pi}} \cdot e^{-\frac{(x_i^4-\theta)^2}{2}}\right)$$

## Шаг 1: Упростить функцию правдоподобия

Выносим общие множители:
$$L(\theta) = \prod_{i=1}^n \left(\frac{2x_i^3}{\sqrt{2\pi}}\right) \cdot \prod_{i=1}^n e^{-\frac{(x_i^4-\theta)^2}{2}}$$

$$L(\theta) = \left(\frac{2}{\sqrt{2\pi}}\right)^n \cdot \prod_{i=1}^n x_i^3 \cdot \exp\left(-\frac{1}{2} \sum_{i=1}^n (x_i^4 - \theta)^2\right)$$

### Итоговый результат

$$L(\theta) = \left(\frac{2}{\sqrt{2\pi}}\right)^n \cdot \prod_{i=1}^n x_i^3 \cdot \exp\left(-\frac{1}{2} \sum_{i=1}^n (x_i^4 - \theta)^2\right)$$

## Шаг 2: Прологарифмировать функцию правдоподобия

$$\ell(\theta) = \ln L(\theta) = \ln \left[ \left(\frac{2}{\sqrt{2\pi}}\right)^n \cdot \prod_{i=1}^n x_i^3 \cdot \exp\left(-\frac{1}{2} \sum_{i=1}^n (x_i^4 - \theta)^2\right) \right]$$

Используя свойства логарифма:
$$\ell(\theta) = n \ln\left(\frac{2}{\sqrt{2\pi}}\right) + \sum_{i=1}^n \ln(x_i^3) + \ln\left( \exp\left(-\frac{1}{2} \sum_{i=1}^n (x_i^4 - \theta)^2\right) \right)$$

$$\ell(\theta) = n \ln\left(\frac{2}{\sqrt{2\pi}}\right) + 3 \sum_{i=1}^n \ln x_i - \frac{1}{2} \sum_{i=1}^n (x_i^4 - \theta)^2$$

Раскрываем сумму:
$$(x_i^4 - \theta)^2 = x_i^8 - 2\theta x_i^4 + \theta^2$$

$$\sum_{i=1}^n (x_i^4 - \theta)^2 = \sum_{i=1}^n x_i^8 - 2\theta \sum_{i=1}^n x_i^4 + \theta^2 \sum_{i=1}^n 1 = \sum_{i=1}^n x_i^8 - 2\theta \sum_{i=1}^n x_i^4 + n \theta^2$$

$$\ell(\theta) = n \ln\left(\frac{2}{\sqrt{2\pi}}\right) + 3 \sum_{i=1}^n \ln x_i - \frac{1}{2} \left( \sum_{i=1}^n x_i^8 - 2\theta \sum_{i=1}^n x_i^4 + n \theta^2 \right)$$

$$\ell(\theta) = n \ln\left(\frac{2}{\sqrt{2\pi}}\right) + 3 \sum_{i=1}^n \ln x_i - \frac{1}{2} \sum_{i=1}^n x_i^8 + \theta \sum_{i=1}^n x_i^4 - \frac{n}{2} \theta^2$$

### Итоговый результат

$$\ell(\theta) = n \ln\left(\frac{2}{\sqrt{2\pi}}\right) + 3 \sum_{i=1}^n \ln x_i - \frac{1}{2} \sum_{i=1}^n x_i^8 + \theta \sum_{i=1}^n x_i^4 - \frac{n}{2} \theta^2$$
## Шаг 3: Найти частную производную относительно θ

Дифференцируем по θ:
$$\frac{\partial \ell(\theta)}{\partial \theta} = \frac{\partial}{\partial \theta} \left( \theta \sum_{i=1}^n x_i^4 - \frac{n}{2} \theta^2 \right) = \sum_{i=1}^n x_i^4 - n \theta$$

### Итоговый результат

$$\frac{\partial \ell(\theta)}{\partial \theta} = \sum_{i=1}^n x_i^4 - n \theta$$

## Шаг 4: Приравнять производную к нулю

$$\frac{\partial \ell(\theta)}{\partial \theta} = 0 \Rightarrow \sum_{i=1}^n x_i^4 - n \theta = 0$$

$$n \theta = \sum_{i=1}^n x_i^4$$

$$\theta = \frac{1}{n} \sum_{i=1}^n x_i^4$$

### Оценка максимального правдоподобия

$$\hat{\theta} = \frac{1}{n} \sum_{i=1}^n X_i^4$$
