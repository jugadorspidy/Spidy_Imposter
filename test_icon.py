import flet as ft
import inspect

print("Flet version:", ft.__version__)

try:
    print("Signature of ft.Icon.__init__:")
    print(inspect.signature(ft.Icon.__init__))
except Exception as e:
    print(e)
    
try:
    print("\nTesting keyword:")
    icon = ft.Icon(name="mobile_screen_share")
    print("Keyword ok")
except Exception as e:
    print("Keyword err:", e)

try:
    print("\nTesting positional:")
    icon = ft.Icon("mobile_screen_share")
    print("Positional ok")
except Exception as e:
    print("Positional err:", e)
