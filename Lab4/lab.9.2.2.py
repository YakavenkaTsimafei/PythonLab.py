import pyautogui

# Создание скриншота рабочего стола
screenshot = pyautogui.screenshot()

# Сохранение скриншота в файл
screenshot.save("desktop_screenshot.png")

print("Скриншот рабочего стола сохранен в файл 'desktop_screenshot.png'")