import asyncio
from src.websocket_client import WebSocketClient
from src.camera_manager import CameraManager
from src.command_manager import CommandManager
from src.ui_manager import UiManager 
import configs

class App:
  async def exec(self):
    self.websocket_client = WebSocketClient(uri=configs.websocket_uri)
    self.camera_manager = CameraManager(event_loop=asyncio.get_event_loop(), websocket_client=self.websocket_client)
    self.command_manager = CommandManager(websocket_client=self.websocket_client, camera_manager=self.camera_manager)
    self.ui_manager = UiManager(event_loop=asyncio.get_event_loop(), command_manager=self.command_manager)
    self.camera_manager.set_ui_manager(ui_manager=self.ui_manager)
    await self.ui_manager.show()

if __name__ == "__main__":
  try:
    asyncio.run(App().exec())
  except KeyboardInterrupt:
    print("KeyboardInterrupt: Stopping the program.")