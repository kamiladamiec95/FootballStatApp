import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('/src/')
import src.menu as menu


def test_show_menu(capsys):
    menu.show_menu()
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    expected = (
            "1. Import event files\n"
            "2. Import team files\n"
            "3. Add leagues from config\n"
            "4. Add league manually\n"
            "5. Settings\n"
            "6. Quit\n"
            )
    assert out.startswith(expected)


def test_show_sub_menu(capsys):
    menu.show_sub_menu()
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    expected = (
                "1. Change event files path\n"
                "2. Change team files path\n"
                "3. Show files path\n"
                "4. Back"
                )
    assert out.startswith(expected)

