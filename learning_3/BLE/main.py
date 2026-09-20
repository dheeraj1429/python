import asyncio
from bleak import BleakScanner, BLEDevice, BleakClient
from typing import Optional

SERVICE_UUID: str = "f0165585-6058-4c5d-a4b7-412dc08e9d8b"
CHAR_UUID: str = "9417b329-5d1c-4ee7-9dc7-000387134cf1"
ACK_BYTE = 0x06
NAK_BYTE = 0x15

disconnect_event = asyncio.Event()
ack_received_event = asyncio.Event()

# Device: TMR-01 | Address: D747B14F-8A6B-E22D-1B45-C8DEAFA206F0
# async def scan() -> list[BLEDevice]:
#   print("Scanning for BLE devices...")
#   devices = await BleakScanner.discover()
#   for device in devices:
#     print(f"Device: {device.name or "Unknown"} | Address: {device.address}")
#   return devices
# asyncio.run(scan())

def on_disconnect(client: BleakClient):
  print("\n[!] Device disconnected! Reconnecting....")
  disconnect_event.set()

def parsed_nak_ack_notification(data: bytearray):
  if ACK_BYTE in data:
    print("Received ACK response from the ble device")
  elif NAK_BYTE in data:
    print("Received NAK response from the ble device")

def handle_notification(sender: int, data: bytearray):
  raw_hex = data.hex()

  try:
    decoded_text = data.decode("utf-8")
    parsed_nak_ack_notification(data=data)
    print(f"[Data Received] text: {decoded_text}")
  except UnicodeDecodeError as e:
    print(f"[Data Received] Raw Bytes: {list(data)} | Hex: 0x{raw_hex} | Error: {e}")

async def send_command(client: BleakClient, command: Optional[str] = None, raw_bytes: Optional[bytes] = None):
  try:
    if raw_bytes != None:
      print(f"Sending raw bytes: {raw_bytes}")
      await client.write_gatt_char(CHAR_UUID, raw_bytes, response=True)
    else:
      print(f"Sending command: {command}...")
      hex_command = f"1B{command.encode('utf-8').hex()}04"
      _raw_bytes = bytes.fromhex(hex_command)
      print(f"Hex Command:    {hex_command}")
    
      await client.write_gatt_char(CHAR_UUID, _raw_bytes, response=True)
  except Exception as e:
    print(f"Error during send command: {e}")

async def connect_to_device(deviceAddress: str):
  print(f"Wait for finding the device with address: {deviceAddress}...")
  device = await BleakScanner.find_device_by_address(deviceAddress)
  if not device:
    print(f"Device with address {deviceAddress} not found...")
    return

  print(f"Found {device.name} [{device.address}]. Connecting...")

  try:
    disconnect_event.clear()
    ack_received_event.clear()
    async with BleakClient(device, disconnected_callback=on_disconnect) as client:
      if client.is_connected:
        print(f"Connected {client.is_connected}")

        # Discover the ble device services
        for service in client.services:
          print(f"[Service] {service.uuid} ({service.description})")

        # Discover the ble device characteristics
          for char in service.characteristics:
            print(f"  └── [Characteristic] {char.uuid} | Properties: {','.join(char.properties)}")
  
            # Step 2: Subscribe to notifications
            if char.uuid == CHAR_UUID:
              print(f"Connected! Subscribing to notifications on {CHAR_UUID}...")
              await client.start_notify(CHAR_UUID, handle_notification)

      await asyncio.sleep(2.0)
      # await send_command(client=client, command="GB")
      # await send_command(client=client, command="Sl10")
      await send_command(client=client, raw_bytes=bytes([0x05]))

      # Keep open the connection until the ble device is disconnected
      while client.is_connected:
        try:
          await asyncio.wait_for(disconnect_event.wait(), timeout=1.0)
        except asyncio.TimeoutError:
          pass

      # Clean up subscription on disconnect
      await client.stop_notify(CHAR_UUID)

      await asyncio.sleep(3.0)

  except Exception as e:
    print(f"Error: {e}")

asyncio.run(connect_to_device(deviceAddress="D747B14F-8A6B-E22D-1B45-C8DEAFA206F0"))