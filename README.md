# Вычисление числа Фибоначчи с помощью формулы Бине

---

## Описание

### Основной код

#### Функция `fib(n)`:
- **Входные данные**: Целое число `n`.
- **Результат**: Число Фибоначчи, соответствующее индексу `n`.
- **Проверка входных данных**: Если значение `n` выходит за пределы от 1 до 64, выбрасывается ошибка.
- **Алгоритм**: Используется формула Бине для вычисления числа Фибоначчи:
  \[
  F(n) = \frac{{\phi^n - \psi^n}}{\sqrt{5}}
  \]
  где \(\phi = \frac{{1 + \sqrt{5}}}{2}\) и \(\psi = \frac{{1 - \sqrt{5}}}{2}\) — золотые коэффициенты.

#### Замер производительности:
- Используется `time.perf_counter` для измерения времени выполнения функции.

---

### Пример работы

**Входные данные**:
```python
n = 32
```
**Вывод**
```bash
fib(n) = 2178309 
 Таймер 0.000029 c.
```
### Как запустить
1. Сохраните код в файл (например, fib_binet.py).
2. Запустите файл с помощью Python:
```bash
python fib_binet.py
```
3. Измените значение переменной n для вычисления других чисел Фибоначчи.
