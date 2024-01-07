import pika


def callback(ch, method, properties, body):
    # Обработка полученного сообщения
    print("Received message:", body, ch, method, properties)


if __name__ == "__main__":
    # Создание подключения к RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost", port=5672)
    )
    channel = connection.channel()

    # Создание очереди для получения сообщений
    channel.queue_declare(queue="my_queue")

    # Установка callback функции для обработки полученных сообщений
    channel.basic_consume(queue="my_queue", on_message_callback=callback, auto_ack=True)

    # Запуск бесконечного цикла ожидания сообщений
    print("Waiting for messages...")
    channel.start_consuming()
