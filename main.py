import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/communicate")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Received:{data}")
    except WebSocketDisconnect:
        await websocket.send_text("Bye!!!")


if __name__ == '__main__':
    uvicorn.run()