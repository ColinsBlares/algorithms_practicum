# 1.5. Определение четности n-го большого числа Фибоначчи

---

## Описание

### Основной код

#### Функция `fib_eo(n)`:
- **Входные данные**: Целое число `n`, где 1≤n≤10<sup>6</sup> 
 .
- **Результат**: Строка `"even"` (чётное) или `"odd"` (нечётное).
- **Проверка входных данных**: Если значение `n` выходит за пределы, выбрасывается ошибка.
- **Алгоритм**: Итеративный расчёт последней цифры числа Фибоначчи с использованием операции остатка от деления (`%`), что делает алгоритм оптимальным по времени и памяти.

#### Замер производительности:
- Используется `time.perf_counter` для измерения времени выполнения функции.

---

### Пример работы
**Входные данные**:
```python
n = 841645
```
Вывод:
```bash
fib(n) = odd 
Таймер 0.000012 c.
```

## Как запустить

1. Сохраните код в файл (например, `fib_big_even_odd.py`).
2. Запустите файл с помощью Python:
   ```bash
   python fib_big_even_odd.py
   ```
3.Измените значение переменной n для тестирования других позиций в последовательности Фибоначчи.
