from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def toggle_sound():
    # Получаем все аудиоустройства
    devices = AudioUtilities.GetSpeakers()
    
    # Получаем интерфейс управления громкостью
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Проверяем текущее состояние устройства
    current_volume = volume.GetMasterVolumeLevelScalar()  # Значение от 0.0 до 1.0
    if current_volume == 0.0:
        print("Устройство отключено. Включение...")
        volume.SetMasterVolumeLevelScalar(0.1, None)  # Включаем устройство
    else:
        print("Устройство уже включено.")

if __name__ == "__main__":
    toggle_sound()
