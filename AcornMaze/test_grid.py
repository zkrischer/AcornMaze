from grid import grid_to_string
from player import Player
from game_parser import read_lines
from game import Game
from moves import walking_to_fire_test
from moves import walking_to_teleporter_test
from moves import walking_to_water_test
from moves import putting_out_fire_test
from moves import walking_off_grid



def test_grid():
    # Forms the Grid
    game=Game('board_hard.txt',Player())
    grid = game.grid
    
    # Tests initial formation of grid
    test = f"*A*************\n*       2 *   *\n* *** ** **** *\n* *  W*   1   *\n* ***** ***** *\n*  2 *   ** *F*\n* ** ***  F   *\n* 1********F  *\n*************Y*\n\nYou have {game.player.num_water_buckets} water buckets."
    assert game.string == test
    assert grid == game.grid

    # Test for when you walk into a wall.
    game.gameMove('a')
    test = f"*A*************\n*       2 *   *\n* *** ** **** *\n* *  W*   1   *\n* ***** ***** *\n*  2 *   ** *F*\n* ** ***  F   *\n* 1********F  *\n*************Y*\n\nYou have {game.player.num_water_buckets} water buckets.\n\nYou walked into a wall. Oof!"
    assert game.string == test

    # Test for dying in fire.
    game = Game("board_hard.txt",Player())
    walking_to_fire_test(game)
    test = f"*X*************\n*       2 *   *\n* *** ** **** *\n* *  W*   1   *\n* ***** ***** *\n*  2 *   ** *F*\n* ** ***  A   *\n* 1********F  *\n*************Y*\n\nYou have {game.player.num_water_buckets} water buckets.\n\n\nYou step into the fires and watch your dreams disappear :(."
    assert game.string == test

    # Test for picking up a water bucket
    game = Game('board_hard.txt',Player())
    walking_to_water_test(game)
    test = f"*X*************\n*       2 *   *\n* *** ** **** *\n* *  A*   1   *\n* ***** ***** *\n*  2 *   ** *F*\n* ** ***  F   *\n* 1********F  *\n*************Y*\n\nYou have {game.player.num_water_buckets} water bucket.\n\nThank the Honourable Furious Forest, you've found a bucket of water!"
    assert game.string == test

    # Test for putting out a fire
    putting_out_fire_test(game)
    test = f"*X*************\n*       2 *   *\n* *** ** **** *\n* *   *   1   *\n* ***** ***** *\n*  2 *   ** *F*\n* ** ***  A   *\n* 1********F  *\n*************Y*\n\nYou have {game.player.num_water_buckets} water buckets.\n\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!"
    assert game.string == test

    # Tests for teleporter functions
    game = Game('board_hard.txt',Player())
    
    # Basic Functionality
    walking_to_teleporter_test(game)
    test = test = f"*X*************\n*       2 *   *\n* *** ** **** *\n* *  W*   1   *\n* ***** ***** *\n*  A *   ** *F*\n* ** ***  F   *\n* 1********F  *\n*************Y*\n\nYou have {game.player.num_water_buckets} water buckets.\n\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time."
    assert game.string == test

    # Pressing e on a teleporter
    game.gameMove('e')
    test = f"*X*************\n*       A *   *\n* *** ** **** *\n* *  W*   1   *\n* ***** ***** *\n*  2 *   ** *F*\n* ** ***  F   *\n* 1********F  *\n*************Y*\n\nYou have {game.player.num_water_buckets} water buckets.\n\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time."
    assert game.string == test

    # Walking onto a wall whilst on a teleporter
    game.gameMove('w')
    test = f"*X*************\n*       A *   *\n* *** ** **** *\n* *  W*   1   *\n* ***** ***** *\n*  2 *   ** *F*\n* ** ***  F   *\n* 1********F  *\n*************Y*\n\nYou have {game.player.num_water_buckets} water buckets.\n\nYou walked into a wall. Oof!"
    assert game.string == test

    # Test for walking out of the grid
    game = Game('extra_storage.txt',Player())
    walking_off_grid(game)
    test = f"*X*************\n*       2 *    \n* *** ** **** *\n* *  W*   1   A\n* ***** ***** *\n*  2 *   ** *F*\n* ** ***  F   *\n* 1********F  *\n*************Y*\n\nYou have 0 water buckets.\n\nYou walked into a wall. Oof!"
    assert game.string == test




def run_tests():
    test_grid()

run_tests()

