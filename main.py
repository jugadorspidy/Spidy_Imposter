import flet as ft
import random
import json
import os
from datetime import datetime

# ─── Categories ────────────────────────────────────────────────────────────────
CATEGORIES = {
    "Food": ["Pizza", "Burger", "Pasta", "Sushi", "Sandwich", "Tacos", "Biryani",
             "Salad", "Soup", "Steak", "Donut", "Ice Cream", "Noodles", "Fried Rice",
             "Pancakes", "Waffles", "Hotdog", "Curry", "Dumplings", "Burrito", "Lasagna", "Chocolate"],
    "Electronics": ["Smartphone", "Laptop", "Tablet", "Smartwatch", "Headphones", "Camera",
                    "Drone", "TV", "Microwave", "Refrigerator", "Keyboard", "Mouse", "Speaker",
                    "Router", "Printer", "Game Console", "Monitor", "Power Bank", "USB Drive",
                    "Projector", "AirPods"],
    "Nature": ["Mountain", "River", "Ocean", "Desert", "Forest", "Volcano", "Waterfall",
               "Lake", "Island", "Canyon", "Glacier", "Rainforest", "Cliff", "Valley",
               "Cave", "Meadow", "Hill", "Reef", "Beach", "Jungle", "Oasis"],
    "Animals": ["Lion", "Tiger", "Elephant", "Dog", "Cat", "Horse", "Monkey", "Giraffe",
                "Zebra", "Bear", "Panda", "Kangaroo", "Dolphin", "Shark", "Eagle", "Snake",
                "Rabbit", "Fox", "Wolf", "Owl", "Turtle"],
    "Sports": ["Football", "Basketball", "Cricket", "Tennis", "Baseball", "Volleyball",
               "Rugby", "Badminton", "Golf", "Swimming", "Boxing", "Wrestling", "Cycling",
               "Running", "Skiing", "Ice Hockey", "Table Tennis", "Archery", "Fencing",
               "Skateboarding", "Surfing"],
    "Movies": ["Inception", "Avatar", "Titanic", "The Matrix", "Interstellar",
               "The Godfather", "Avengers", "Jurassic Park", "Star Wars", "Harry Potter",
               "Frozen", "Toy Story", "The Dark Knight", "Spider-Man", "Iron Man",
               "Shrek", "Gladiator", "Joker", "Black Panther", "Finding Nemo", "Up"],
    "Countries": ["India", "USA", "Spain", "France", "Germany", "Italy", "Japan", "China",
                  "Brazil", "Canada", "Australia", "Russia", "Mexico", "UK", "South Korea",
                  "Argentina", "Egypt", "Turkey", "Thailand", "South Africa", "UAE"],
    "Occupations": ["Doctor", "Engineer", "Teacher", "Chef", "Pilot", "Police Officer",
                    "Firefighter", "Lawyer", "Nurse", "Scientist", "Farmer", "Artist",
                    "Musician", "Actor", "Driver", "Architect", "Plumber", "Electrician",
                    "Writer", "Photographer", "Designer"],
    "Vehicles": ["Car", "Bike", "Bus", "Train", "Airplane", "Helicopter", "Boat", "Ship",
                 "Scooter", "Truck", "Tractor", "Submarine", "Bicycle", "Van", "Jet",
                 "Yacht", "Tram", "Taxi", "Race Car", "Hot Air Balloon", "Spaceship"],
    "Clothing": ["Shirt", "Pants", "Jacket", "Sweater", "Dress", "Skirt", "Shorts",
                 "Hat", "Cap", "Shoes", "Sandals", "Boots", "Scarf", "Gloves", "Socks",
                 "Tie", "Belt", "Hoodie", "Coat", "Blazer", "Sunglasses"],
    "Drinks": ["Water", "Coffee", "Tea", "Juice", "Soda", "Milkshake", "Smoothie",
               "Lemonade", "Hot Chocolate", "Beer", "Wine", "Whiskey", "Latte",
               "Espresso", "Mojito", "Cola", "Energy Drink", "Coconut Water",
               "Iced Tea", "Milk", "Orange Juice"],
    "Musical Instruments": ["Guitar", "Piano", "Violin", "Drums", "Flute", "Saxophone",
                            "Trumpet", "Harp", "Cello", "Keyboard", "Clarinet",
                            "Tambourine", "Ukulele", "Bass Guitar", "Harmonica",
                            "Oboe", "Tuba", "Xylophone", "Banjo", "Recorder", "Synthesizer"],
    "Furniture": ["Chair", "Table", "Sofa", "Bed", "Desk", "Cupboard", "Shelf",
                  "Wardrobe", "Stool", "Bench", "Couch", "Dresser", "Nightstand",
                  "Bookshelf", "Cabinet", "Recliner", "Ottoman", "Coffee Table",
                  "Dining Table", "TV Stand", "Drawer"],
    "Apps & Websites": ["Instagram", "YouTube", "TikTok", "Facebook", "Twitter",
                        "Snapchat", "WhatsApp", "Gmail", "Google Maps", "Spotify",
                        "Netflix", "Amazon", "Reddit", "Discord", "LinkedIn",
                        "Pinterest", "Zoom", "Uber", "Airbnb", "Twitch", "Chrome"],
    "School Subjects": ["Math", "Science", "English", "History", "Geography", "Physics",
                        "Chemistry", "Biology", "Computer Science", "Economics", "Art",
                        "Music", "PE", "Literature", "Civics", "Algebra", "Geometry",
                        "Calculus", "Sociology", "Psychology", "Business"],
    "Colors": ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Black",
               "White", "Brown", "Grey", "Cyan", "Magenta", "Gold", "Silver", "Teal",
               "Navy", "Maroon", "Beige", "Lavender", "Turquoise"],
    "Festivals": ["Christmas", "Diwali", "Eid", "Halloween", "Holi", "New Year",
                  "Thanksgiving", "Easter", "Hanukkah", "Chinese New Year", "Ramadan",
                  "Pongal", "Navratri", "Oktoberfest", "Carnival", "Independence Day",
                  "Valentine's Day", "St. Patrick's Day", "Ganesh Chaturthi", "Baisakhi", "Onam"],
    "Tools": ["Hammer", "Screwdriver", "Wrench", "Drill", "Saw", "Pliers",
              "Tape Measure", "Level", "Chisel", "Axe", "Shovel", "Ladder",
              "Sandpaper", "Crowbar", "Nail Gun", "Soldering Iron", "Flashlight",
              "Utility Knife", "Clamp", "Trowel", "Mallet"],
    "Plants": ["Rose", "Tulip", "Sunflower", "Cactus", "Bamboo", "Fern", "Oak Tree",
               "Pine Tree", "Maple Tree", "Lavender", "Mint", "Basil", "Aloe Vera",
               "Orchid", "Daisy", "Palm Tree", "Lotus", "Jasmine", "Hibiscus", "Ivy", "Moss"],
    "Games": ["Chess", "Ludo", "Monopoly", "Uno", "Poker", "Minecraft", "Fortnite",
              "PUBG", "Call of Duty", "FIFA", "GTA", "Among Us", "Roblox", "Valorant",
              "Mario", "Zelda", "Tetris", "Scrabble", "Carrom", "Snakes & Ladders", "Clash Royale"],
}

# ─── History ────────────────────────────────────────────────────────────────────
def save_game_history(data):
    file_path = "imposter_history.json"
    history = []
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                history = json.load(f)
        except Exception:
            pass
    history.append({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), **data})
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4)
    except Exception as e:
        print(f"Error saving history: {e}")


# ─── Main App Class ─────────────────────────────────────────────────────────────
class ImposterGame:
    # Colour palette
    BG      = "#0B0C10"
    CARD    = "#1F2833"
    TEAL    = "#45A29E"
    CYAN    = "#66FCF1"
    RED     = "#E84545"
    TEXT    = "#C5C6C7"
    WHITE   = "#ffffff"

    def __init__(self, page: ft.Page):
        self.page = page
        self.game_state = {
            "num_players": 3,
            "num_imposters": 1,
            "player_names": [],
            "roles": [],
            "current_player_index": 0,
            "selected_category": "",
            "selected_item": "",
        }
        self._setup_styles()

    # ── Styles ────────────────────────────────────────────────────────────────
    def _setup_styles(self):
        self.BTN_PRIMARY = ft.ButtonStyle(
            color=self.WHITE, bgcolor=self.TEAL,
            shape=ft.RoundedRectangleBorder(radius=10), padding=20,
        )
        self.BTN_DANGER = ft.ButtonStyle(
            color=self.WHITE, bgcolor=self.RED,
            shape=ft.RoundedRectangleBorder(radius=10), padding=20,
        )
        self.BTN_SECONDARY = ft.ButtonStyle(
            color=self.CYAN, bgcolor="transparent",
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(2, self.CYAN), padding=20,
        )

    # ── Navigation helper ──────────────────────────────────────────────────────
    def _go(self, content: ft.Control):
        """Replace the current view with new content. Uses ft.View so Flutter
        always gets a complete, fresh render tree — no grey-screen issues."""
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                route="/",
                bgcolor=self.BG,
                padding=ft.Padding.symmetric(horizontal=20, vertical=30),
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        [content],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll=ft.ScrollMode.AUTO,
                        expand=True,
                    )
                ],
            )
        )
        self.page.update()

    # ── Shared widgets ─────────────────────────────────────────────────────────
    def _card(self, *children, width=None):
        return ft.Container(
            content=ft.Column(list(children),
                              horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                              spacing=16),
            bgcolor=self.CARD,
            padding=30,
            border_radius=15,
            border=ft.Border.all(1, self.TEAL),
            width=width,
        )

    def _heading(self, text, size=30):
        return ft.Text(text, size=size, color=self.CYAN,
                       text_align=ft.TextAlign.CENTER,
                       weight=ft.FontWeight.BOLD)

    def _sub(self, text, color=None):
        return ft.Text(text, color=color or self.TEXT,
                       text_align=ft.TextAlign.CENTER)

    def _gap(self, h=20):
        return ft.Container(height=h)

    # ── Screen 1 – Setup ───────────────────────────────────────────────────────
    def show_setup_view(self):
        players_dd = ft.Dropdown(
            label="Total Players",
            options=[ft.DropdownOption(str(i)) for i in range(3, 16)],
            value="3", width=300, border_radius=10, border_color=self.TEAL,
        )
        imposters_dd = ft.Dropdown(
            label="Total Imposters",
            options=[ft.DropdownOption(str(i)) for i in range(1, 6)],
            value="1", width=300, border_radius=10, border_color=self.TEAL,
        )

        def on_start(e):
            n_players  = int(players_dd.value)
            n_imposters = int(imposters_dd.value)
            if n_imposters >= n_players:
                self.page.open(ft.SnackBar(
                    ft.Text("Imposters must be fewer than total players!", color=self.WHITE),
                    bgcolor=self.RED))
                return
            self.game_state["num_players"]  = n_players
            self.game_state["num_imposters"] = n_imposters
            self._go(self.show_names_view())

        return ft.Column([
            self._heading("IMPOSTER", size=50),
            self._sub("The Ultimate Party Game"),
            self._gap(30),
            self._card(
                ft.Text("GAME SETTINGS", size=18, color=self.WHITE,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER),
                players_dd,
                imposters_dd,
            ),
            self._gap(20),
            ft.Button("START GAME", on_click=on_start, width=300, style=self.BTN_PRIMARY),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=8)

    # ── Screen 2 – Player Names ────────────────────────────────────────────────
    def show_names_view(self):
        fields = [
            ft.TextField(label=f"Player {i+1}", value=f"Player {i+1}", width=300,
                         border_radius=8, border_color=self.TEAL, bgcolor=self.CARD)
            for i in range(self.game_state["num_players"])
        ]

        def on_next(e):
            names = [f.value.strip() for f in fields]
            if any(not n for n in names):
                self.page.open(ft.SnackBar(
                    ft.Text("Please fill in all player names!", color=self.WHITE),
                    bgcolor=self.RED))
                return
            self.game_state["player_names"] = names
            self._go(self.show_categories_view())

        return ft.Column([
            self._heading("WHO IS PLAYING?"),
            self._sub("Enter player names below"),
            self._gap(),
            ft.Column(fields, height=340, scroll=ft.ScrollMode.AUTO,
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            self._gap(),
            ft.Button("NEXT: CHOOSE CATEGORY", on_click=on_next, width=300, style=self.BTN_PRIMARY),
            ft.Button("BACK", on_click=lambda e: self._go(self.show_setup_view()),
                      width=300, style=self.BTN_SECONDARY),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=6)

    # ── Screen 3 – Categories ──────────────────────────────────────────────────
    def show_categories_view(self):
        def on_pick(cat):
            item = random.choice(CATEGORIES[cat])
            players = self.game_state["player_names"][:]
            random.shuffle(players)
            imposters = set(players[:self.game_state["num_imposters"]])
            roles = [
                {"name": p, "is_imposter": p in imposters,
                 "item": None if p in imposters else item}
                for p in self.game_state["player_names"]
            ]
            self.game_state.update({
                "selected_category": cat,
                "selected_item": item,
                "roles": roles,
                "current_player_index": 0,
            })
            save_game_history({"category": cat, "item": item,
                               "imposters": list(imposters),
                               "players": self.game_state["player_names"]})
            self._go(self.show_pass_device_view())

        buttons = [
            ft.Container(
                content=ft.Text(cat, weight=ft.FontWeight.BOLD, color=self.WHITE,
                                text_align=ft.TextAlign.CENTER),
                width=140, height=60, bgcolor=self.CARD, border_radius=10,
                border=ft.Border.all(2, self.TEAL), ink=True,
                on_click=lambda e, c=cat: on_pick(c),
            )
            for cat in CATEGORIES
        ]

        grid = ft.Row(buttons, wrap=True, alignment=ft.MainAxisAlignment.CENTER)

        return ft.Column([
            self._heading("SELECT CATEGORY"),
            ft.Text("Only ONE person should pick — others look away!",
                    color=self.RED, weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER),
            self._gap(),
            ft.Container(content=grid, height=420),
            self._gap(8),
            ft.Button("BACK TO NAMES",
                      on_click=lambda e: self._go(self.show_names_view()),
                      width=300, style=self.BTN_SECONDARY),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=8)

    # ── Screen 4 – Pass Device ─────────────────────────────────────────────────
    def show_pass_device_view(self):
        roles = self.game_state["roles"]
        idx   = self.game_state["current_player_index"]

        # All players done → go to discussion screen
        if idx >= len(roles):
            return self.show_discussion_view()

        player_name = roles[idx]["name"]

        def on_show(e):
            self._go(self.show_role_view(roles[idx]))

        return ft.Column([
            ft.Icon(ft.Icons.MOBILE_SCREEN_SHARE, size=100, color=self.CYAN),
            ft.Text("PASS DEVICE TO:", size=20, color=self.TEXT,
                    weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Text(player_name, size=45, color=self.WHITE,
                    weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            self._gap(40),
            ft.Container(
                content=ft.Text("Make sure nobody else is looking!",
                                color=self.RED, weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER),
                bgcolor=self.CARD, padding=15, border_radius=8,
            ),
            self._gap(20),
            ft.Button("SHOW MY ROLE", on_click=on_show, width=300, style=self.BTN_PRIMARY),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10)

    # ── Screen 5 – Role Reveal ─────────────────────────────────────────────────
    def show_role_view(self, role_data):
        def on_hide(e):
            self.game_state["current_player_index"] += 1
            self._go(self.show_pass_device_view())

        if role_data["is_imposter"]:
            badge = ft.Column([
                ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=self.RED, size=80),
                ft.Text("YOU ARE THE", size=20, color=self.TEXT,
                        weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text("IMPOSTER", size=50, color=self.RED,
                        weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text("Blend in. Act normal. Do not get caught.",
                        size=15, color=self.WHITE, text_align=ft.TextAlign.CENTER),
                self._gap(10),
                ft.Text("CATEGORY:", size=13, color=self.TEXT,
                        text_align=ft.TextAlign.CENTER),
                ft.Text(self.game_state["selected_category"], size=22,
                        color=self.WHITE, weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER),
                self._gap(6),
                ft.Container(
                    content=ft.Image(
                        src=f"https://loremflickr.com/320/240/{self.game_state['selected_category']},abstract,collage/all",
                        width=250, height=180, fit=ft.BoxFit.COVER,
                        border_radius=10,
                    ),
                    border=ft.Border.all(2, self.RED),
                    border_radius=12,
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8)
        else:
                # Create refined search tags
                search_tags = f"{role_data['item']},{self.game_state['selected_category']}".replace(" ", "")
                if self.game_state["selected_category"] == "Countries":
                    search_tags += ",flag,map"

                badge = ft.Column([
                    ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINE, color=self.TEAL, size=80),
                    ft.Text("YOU ARE NOT THE IMPOSTER", size=16, color=self.TEAL,
                            weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    self._gap(10),
                    ft.Text("CATEGORY:", size=13, color=self.TEXT,
                            text_align=ft.TextAlign.CENTER),
                    ft.Text(self.game_state["selected_category"], size=22,
                            color=self.WHITE, weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER),
                    self._gap(6),
                    ft.Text("SECRET ITEM:", size=13, color=self.TEXT,
                            text_align=ft.TextAlign.CENTER),
                    ft.Text(role_data["item"], size=34, color=self.CYAN,
                            weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    self._gap(10),
                    ft.Container(
                        content=ft.Image(
                            src=f"https://loremflickr.com/320/240/{search_tags}/all",
                            width=250, height=180, fit=ft.BoxFit.COVER,
                            border_radius=10,
                        ),
                        border=ft.Border.all(2, self.TEAL),
                        border_radius=12,
                    )
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4)

        return ft.Column([
            ft.Container(
                content=ft.Text(f"{role_data['name'].upper()}'S ROLE",
                                size=18, color=self.WHITE, weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER),
                bgcolor=self.CARD, padding=15, border_radius=10, width=350,
                alignment=ft.alignment.Alignment(0, 0),
            ),
            self._gap(24),
            badge,
            self._gap(50),
            ft.Button("HIDE ROLE & NEXT", on_click=on_hide, width=300, style=self.BTN_SECONDARY),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=6)

    # ── Screen 6 – Discussion ──────────────────────────────────────────────────
    def show_discussion_view(self):
        def on_reveal(e):
            self._go(self.show_reveal_view())

        return ft.Column([
            ft.Icon(ft.Icons.RECORD_VOICE_OVER, size=100, color=self.CYAN),
            ft.Text("ROLES DISTRIBUTED", size=20, color=self.TEXT,
                    weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Text("START DISCUSSING!", size=35, color=self.WHITE,
                    weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            self._gap(30),
            ft.Text("Look around. Who is lying?", color=self.RED,
                    italic=True, text_align=ft.TextAlign.CENTER),
            self._gap(30),
            ft.Button("REVEAL IMPOSTER(S)", on_click=on_reveal, width=300, style=self.BTN_DANGER),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=8)

    # ── Screen 7 – Reveal ─────────────────────────────────────────────────────
    def show_reveal_view(self):
        imposters = [r["name"] for r in self.game_state["roles"] if r["is_imposter"]]

        return ft.Column([
            ft.Text("THE IMPOSTER(S) WERE:", size=18, color=self.TEXT,
                    weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Text(", ".join(imposters), size=42, color=self.RED,
                    weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            self._gap(20),
            self._card(
                ft.Text("THE SECRET ITEM WAS:", size=14, color=self.TEXT,
                        text_align=ft.TextAlign.CENTER),
                ft.Text(self.game_state["selected_item"], size=34, color=self.CYAN,
                        weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                width=340,
            ),
            self._gap(40),
            ft.Button("QUICK PLAY (SAME PLAYERS)", 
                      on_click=lambda e: self._go(self.show_categories_view()), 
                      width=300, style=self.BTN_PRIMARY),
            ft.Button("NEW GAME (CHANGE PLAYERS)", 
                      on_click=lambda e: self._go(self.show_setup_view()), 
                      width=300, style=self.BTN_SECONDARY),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=8)


# ─── Entry Point ────────────────────────────────────────────────────────────────
def main(page: ft.Page):
    page.title = "IMPOSTER - The Party Game"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0B0C10"

    try:
        page.window.width  = 480
        page.window.height = 820
        page.window.resizable = True
    except Exception:
        pass

    game = ImposterGame(page)
    game._go(game.show_setup_view())   # _go() populates page.views + page.update()


if __name__ == "__main__":
    ft.run(main)
