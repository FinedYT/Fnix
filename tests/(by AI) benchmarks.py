import concurrent.futures
import requests
import time

URL = "http://127.0.0.1:8080"  # Твой порт Fnix
TOTAL_REQUESTS = 2000
CONCURRENT_USERS = 50

# Создаем заголовки, как у настоящего Chrome
FAKE_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'close'  # Просим сервер сразу закрыть сокет после ответа
}


def run_integration_tests():
    print("=== 1. ЗАПУСК ИНТЕГРАЦИОННЫХ ТЕСТОВ ===")

    # Тест 1: Проверка главной страницы
    try:
        r_main = requests.get(f"{URL}/benchmark", headers=FAKE_HEADERS, timeout=2)
        print(f"[OK] Главная страница '/': Статус {r_main.status_code}")
    except Exception as e:
        print(f"[FAIL] Главная страница '/': Ошибка {e}")

def send_stress_request(req_id):
    target = "/benchmark"
    try:
        start_time = time.time()
        # Передаем фейковые заголовки браузера во время стресс-теста
        response = requests.get(f"{URL}{target}", headers=FAKE_HEADERS, timeout=2)
        return response.status_code, time.time() - start_time
    except Exception:
        return "ERROR", 0

def run_stress_test():
    print("\n=== 2. ЗАПУСК СТРЕСС-ТЕСТА РОУТЕРА ===")
    print(f"Отправка {TOTAL_REQUESTS} запросов в {CONCURRENT_USERS} параллельных потоков...")

    start_test = time.time()
    success_count = 0
    error_count = 0
    latencies = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENT_USERS) as executor:
        results = executor.map(send_stress_request, range(TOTAL_REQUESTS))

        for status, latency in results:
            if status == 200:
                success_count += 1
                latencies.append(latency)
            else:
                error_count += 1

    end_test = time.time()
    total_time = end_test - start_test

    rps = success_count / total_time if total_time > 0 else 0
    avg_latency = sum(latencies) / len(latencies) if latencies else 0

    print("\n=== РЕЗУЛЬТАТЫ СТРЕСС-ТЕСТА ===")
    print(f"Время выполнения: {total_time:.2f} сек")
    print(f"Успешно обработано Роутером (200 OK): {success_count}")
    print(f"Ошибок соединения/таймаутов: {error_count}")
    print(f"Средняя задержка Роутера (Latency): {avg_latency * 1000:.1f} мс")
    print(f"Итоговая скорость (RPS): {rps:.1f} запр/сек")


if __name__ == "__main__":
    try:
        # Проверяем, жив ли сервер вообще перед стартом
        requests.get(URL, timeout=1)
        run_integration_tests()
        run_stress_test()
    except requests.exceptions.ConnectionError as er:
        print(er)
        print(f"[CRITICAL] Не удалось подключиться к Fnix на {URL}. Запусти сервер!")