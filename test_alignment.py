import flet as ft
print("Flet version:", ft.__version__)
print("Has alignment:", hasattr(ft, 'alignment'))
print("Has Alignment:", hasattr(ft, 'Alignment'))
if hasattr(ft, 'alignment'):
    print("Has alignment.center:", hasattr(ft.alignment, 'center'))
if hasattr(ft, 'alignment'):
    print("Has ft.alignment.center:", hasattr(ft, 'alignment') and hasattr(ft.alignment, 'center'))

try:
    print("ft.alignment.center:", ft.alignment.center)
except AttributeError as e:
    print("Error getting ft.alignment.center:", e)

try:
    print("ft.Alignment(0, 0):", ft.Alignment(0, 0))
except Exception as e:
    print("Error instantiating Alignment:", e)
