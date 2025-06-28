import sys

# Перевірка наявності модуля numpy
if "numpy" not in sys.modules:
    print("Модуль NumPy не встановлений.")
else:
    import numpy
    print("Модуль NumPy знайдено!")
    print("Версія NumPy:", numpy.__version__)
