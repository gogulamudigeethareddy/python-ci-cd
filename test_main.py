from main import print_hello_world  # Import the specific function


def test_hello_world(capfd):
    print_hello_world()  # Call the function directly
    captured = capfd.readouterr()
    assert captured.out.strip() == "Hello world"
