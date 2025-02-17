from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import Twin, TwinProperties

IOTHUB_CONNECTION_STRING = ""

def update_device_tags(registry_manager):
    try:
        devices = registry_manager.get_devices()
        for device in devices:
            twin = registry_manager.get_twin(device.device_id)
            
            if not twin.tags:
                twin.tags = {}
                
            twin.tags["environment"] = "staging"
            registry_manager.update_twin(device.device_id, twin, twin.etag)
            
            print(f"Updated device '{device.device_id}' tags.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    registry_manager = IoTHubRegistryManager(IOTHUB_CONNECTION_STRING)
    update_device_tags(registry_manager)

if __name__ == '__main__':
    main()
