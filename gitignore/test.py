import concurrent.futures
import requests
import time

URL = "http://127.0.0.1:8080"
TOTAL_REQUESTS = 200
CONCURRENT_USERS = 5


def send_request(req_id):
    try:
        start_time = time.time()
        response = requests.get(URL, timeout=2)
        latency = time.time() - start_time
        return response.status_code, latency
    except Exception as e:
        return "ERROR", 0


if __name__ == "__main__":
    print(f"Запуск теста: {TOTAL_REQUESTS} запросов в {CONCURRENT_USERS} потоков...")

    start_test = time.time()
    success_count = 0
    error_count = 0
    latencies = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENT_USERS) as executor:
        results = executor.map(send_request, range(TOTAL_REQUESTS))

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

    print("\n=== РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ ===")
    print(f"Общее время теста: {total_time:.2f} сек")
    print(f"Успешных запросов (200 OK): {success_count}")
    print(f"Ошибок/Отказов: {error_count}")
    print(f"Среднее время ответа (Latency): {avg_latency * 1000:.1f} мс")
    print(f"Производительность (RPS): {rps:.1f} запросов/сек")