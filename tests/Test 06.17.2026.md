### Fnix\tests\(by AI) benchmarks.py

## En
# === 1. STARTING INTEGRATION TESTS ===
[OK] Homepage '/': Status 200
[OK] Routing '/about': Status 200
[OK] Error 404 is handled correctly (Status 404)

# === 2. STARTING ROUTER STRESS TEST ===
Sending 300 requests in 10 parallel threads...

# === STRESS TEST RESULTS ===
Execution time: 0.35 sec
Successfully handled by the router (200 OK): 300
Connection errors/timeouts: 0
Average router latency (latency): 11.3 ms
Total throughput (RPS): 852.7 request/sec

Process finished with exit code 0

## Ru
# === 1. ЗАПУСК ИНТЕГРАЦИОННЫХ ТЕСТОВ ===
[OK] Главная страница '/': Статус 200
[OK] Роутинг '/about': Статус 200
[OK] Ошибка 404 обрабатывается корректно (Статус 404)

# === 2. ЗАПУСК СТРЕСС-ТЕСТА РОУТЕРА ===
Отправка 300 запросов в 10 параллельных потоков...

# === РЕЗУЛЬТАТЫ СТРЕСС-ТЕСТА ===
Время выполнения: 0.35 сек
Успешно обработано Роутером (200 OK): 300
Ошибок соединения/таймаутов: 0
Средняя задержка Роутера (Latency): 11.3 мс
Итоговая скорость (RPS): 852.7 запр/сек

Process finished with exit code 0