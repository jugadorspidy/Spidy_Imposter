import flet as ft
print("Flet version:", ft.__version__)
print("Has colors:", hasattr(ft, 'colors'))
print("Has Colors:", hasattr(ft, 'Colors'))
if hasattr(ft, 'Colors'):
    print("Example color:", getattr(ft.Colors, 'RED_400', 'Not found'))
