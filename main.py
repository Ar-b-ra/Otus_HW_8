import json
import os
import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import BasicProperties, Basic

from resolver.resolver import Resolver


def callback(
    ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes
):
    # Обработка полученного сообщения
    message = body.decode("utf-8")
    resolver.resolve(message)
    print(
        f"Received message: {body = },\n"
        f"{ch = }, {ch}\n"
        f"{method = }, {method.delivery_tag = }\n"
        f"{properties = } {properties.user_id = }"
    )


if __name__ == "__main__":
    # Создание подключения к RabbitMQ
    rabbit_host = os.environ.get("RABBIT_HOST", "localhost")
    rabbit_port = int(os.environ.get("RABBIT_PORT", 5672))
    rabbit_queue = os.environ.get("RABBIT_QUEUE", "my_queue")

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbit_host, port=rabbit_port)
    )
    channel = connection.channel()

    # Создание очереди для получения сообщений
    channel.queue_declare(queue=rabbit_queue)
    resolver = Resolver()
    # Установка callback функции для обработки полученных сообщений
    channel.basic_consume(
        queue=rabbit_queue, on_message_callback=callback, auto_ack=True
    )
    # Запуск бесконечного цикла ожидания сообщений
    print("Waiting for messages...")
    channel.start_consuming()
