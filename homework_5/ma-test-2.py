import pandas as pd
import matplotlib
from numpy.ma.core import squeeze
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings
from concurrent.futures import ProcessPoolExecutor
import os

# Suppress warnings
warnings.filterwarnings("ignore")


def train_and_plot(q, train_data, test_data, df):
    """
    Функция для обучения модели и построения графика в отдельном процессе.
    """
    print(f"Building MA({q})...", flush=True)
    try:
        # Построение модели MA(q) -> ARIMA(0, 0, q)
        model = ARIMA(train_data, order=(0, 0, q))
        res = model.fit()

        # Прогноз на тестовую выборку
        start = test_data.index[0]
        end = test_data.index[-1]
        predictions = res.predict(start=start, end=end)

        # Расчет MSE
        mse = ((predictions - test_data) ** 2).mean()

        # Построение графика
        # Используем объектный интерфейс matplotlib для безопасности в процессах
        fig, ax = plt.subplots(figsize=(12, 6))
        # Ограничение графика данными с 2003 по 2007 год
        filtered_df = df.loc['2003':'2007']
        ax.plot(filtered_df.index, filtered_df, label='Real (2003-2007)', color='blue')
        ax.plot(test_data.index, predictions, label=f'MA({q}) Prediction', color='red')
        ax.set_title(f'MA({q}) Model Comparison')
        ax.legend()
        ax.grid(True)

        # Сохранение графика
        plot_filename = f'ma-test_{q}_plot.png'
        # Путь сохранения относительно текущей директории запуска.
        # Если запускаем из корня, сохраняем в homework_5/.
        # Но чтобы было универсально, проверим, где мы.
        if os.path.exists('homework_5'):
            save_path = f'homework_5/{plot_filename}'
        else:
            save_path = plot_filename

        fig.savefig(save_path)
        plt.close(fig)

        description = ""
        if q == 1:
            description = "Модель MA(1) учитывает только одну предыдущую ошибку. График, вероятно, будет слабо повторять динамику, сглаживая ряд.\n\n"
        elif q == 100:
            description = "Модель MA(100) учитывает множество прошлых ошибок. Это может привести к переобучению или, наоборот, к лучшему улавливанию долгих зависимостей, но график может быть шумным или слишком инертным.\n\n"

        return {
            'q': q,
            'mse': mse,
            'plot_filename': plot_filename,
            'description': description,
            'success': True
        }
    except Exception as e:
        print(f"Error in MA({q}): {e}", flush=True)
        return {
            'q': q,
            'error': str(e),
            'success': False
        }


def main():
    # 1. Загрузка данных
    file_path = 'homework_5/FedFunds.csv'
    # Проверка пути
    if not os.path.exists(file_path):
        if os.path.exists('FedFunds.csv'):
            file_path = 'FedFunds.csv'
        else:
            print("Error: Data file not found.")
            return

    # df = pd.read_csv(file_path, parse_dates=['DATE'], index_col='DATE')
    # параметр squeeze устарел, теперь это метод
    df = pd.read_csv(file_path, header=0, index_col=0, parse_dates=True).squeeze()

    # 2. Фильтрация данных до 2008 года
    # df = df[df.index < '2008-01-01']
    df = df[:'2007']

    # 3. Разбиение на тренировочную и тестовую части
    # split_date = '2003-01-01'
    # train = df[df.index < split_date]['FEDFUNDS']
    # test = df[df.index >= split_date]['FEDFUNDS']

    # этот вариант разбиения работать не будет, так как вызовет ошибку "'numpy.ndarray' object has no attribute 'index'"  из-за того, что в коде переменные train и test являются numpy массивами (полученными через df.values), а не pandas Series с индексом. В функции train_and_plot код пытается получить test_data.index[0] и test_data.index[-1], но numpy массивы не имеют атрибута index.
    # X = df.values
    # train, test = X[:len(X) - 7], X[len(X) - 7:]

    train, test = df[:-7], df[-7:]

    # Список моделей MA(q)
    qs = [1, 2, 4, 40, 100]

    # альтернативное тестирование
    model = ARIMA(train, order=(0, 0, 1))
    model_fit = model.fit()
    predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1, dynamic=False)
    plt.plot(test, label='Тестовые данные')
    plt.plot(predictions)
    plt.grid()
    plt.legend()
    plt.savefig('ma-test-2.png')

    # Параллельное выполнение
    results = []
    # Используем ProcessPoolExecutor для распараллеливания CPU-intensive задач
    # with ProcessPoolExecutor() as executor:
        # map возвращает результаты в том же порядке, что и входные аргументы
        # futures = executor.map(train_and_plot, qs, [train] * len(qs), [test] * len(qs), [df] * len(qs))
        # results = list(futures)

    # # Запись результатов в файл
    # # Определяем путь к RESULT.md
    # result_path = 'homework_5/RESULT_TEST_2.md' if os.path.exists('homework_5') else 'RESULT_TEST_2.md'
    #
    # with open(result_path, 'w', encoding='utf-8') as f:
    #     f.write("# Результаты моделирования MA-процессов\n\n")
    #     f.write("Данные ограничены периодом до 2008 года.\n")
    #     f.write(f"Разбиение на тренировочную и тестовую выборки по дате: до 2008 года\n\n")

        # for res in results:
        #     if res['success']:
        #         q = res['q']
        #         f.write(f"## Модель MA({q})\n\n")
        #         f.write(f"График прогнозных значений против реальных:\n\n")
        #         f.write(f"![MA({q})]({res['plot_filename']})\n\n")
        #         f.write(f"MSE: {res['mse']:.4f}\n\n")
        #         f.write(res['description'])
        #         # Принудительно сбрасываем буфер
        #         f.flush()
        #     else:
        #         f.write(f"## Модель MA({res['q']})\n\n")
        #         f.write(f"Ошибка при построении: {res.get('error')}\n\n")
        #
        # f.write("## Общие выводы\n\n")
        # f.write("С увеличением порядка q модель получает больше информации о прошлых шоках (ошибках).\n")
        # f.write(
        #     "Ожидается, что при увеличении q качество подгонки может улучшаться до определенного момента, но слишком большое q может усложнить модель.\n")
        # f.write("Визуально нужно оценить, насколько красная линия близка к синей.\n")


if __name__ == '__main__':
    main()
