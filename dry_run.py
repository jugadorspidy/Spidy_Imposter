import flet as ft
from main import ImposterGame, CATEGORIES
from unittest.mock import MagicMock

def dry_run_test():
    print("--- STARTING DRY RUN VALIDATION ---")
    
    # Mocking flet Page
    mock_page = MagicMock(spec=ft.Page)
    mock_page.controls = []
    mock_page.window = MagicMock()
    mock_page.fonts = {}
    
    try:
        print("1. Initializing game class...")
        game = ImposterGame(mock_page)
        
        print("2. Testing Setup View...")
        setup_view = game.show_setup_view()
        assert setup_view is not None
        
        print("3. Testing Names View...")
        game.game_state["num_players"] = 4
        names_view = game.show_names_view()
        assert names_view is not None
        
        print("4. Testing Categories View...")
        categories_view = game.show_categories_view()
        assert categories_view is not None
        
        print("5. Testing Pass Device View...")
        # Mocking game state for role viewing
        game.game_state["player_names"] = ["P1", "P2", "P3"]
        game.game_state["num_imposters"] = 1
        game.game_state["selected_category"] = "Sports"
        game.game_state["selected_item"] = "Football"
        game.game_state["roles"] = [
            {"name": "P1", "is_imposter": False, "item": "Football"},
            {"name": "P2", "is_imposter": True, "item": None},
            {"name": "P3", "is_imposter": False, "item": "Football"}
        ]
        game.game_state["current_player_index"] = 0
        
        pass_view = game.show_pass_device_view()
        assert pass_view is not None
        
        print("6. Testing Role View (Normal User)...")
        role_view_normal = game.show_role_view(game.game_state["roles"][0])
        assert role_view_normal is not None
        
        print("7. Testing Role View (Imposter)...")
        role_view_imposter = game.show_role_view(game.game_state["roles"][1])
        assert role_view_imposter is not None
        
        print("8. Testing Discussion View...")
        disc_view = game.show_discussion_view()
        assert disc_view is not None
        
        print("9. Testing Reveal View...")
        reveal_view = game.show_reveal_view()
        assert reveal_view is not None
        
        print("\n--- DRY RUN SUCCESSFUL: ALL VIEWS VALIDATED ---")
        return True
        
    except Exception as e:
        print(f"\n!!! DRY RUN FAILED: {str(e)} !!!")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = dry_run_test()
    if not success:
        exit(1)
