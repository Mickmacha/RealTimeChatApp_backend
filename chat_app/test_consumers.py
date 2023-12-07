import json
from channels.testing import WebsocketCommunicator
from chat_app.consumers import ChatConsumer

async def test_chat_consumer():
    communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "/ws/chat/")
    connected, _ = await communicator.connect()

    assert connected

    message = {"message": "Hello, world!"}
    await communicator.send_json_to(message)

    response = await communicator.receive_json_from()

    assert response == message

    await communicator.disconnect()