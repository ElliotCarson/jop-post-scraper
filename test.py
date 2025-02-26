"""test module"""
import urllib.parse


def test_url_encoding():
    """_summary_
    """
    expected_string = "F%2CC"
    safe_string = urllib.parse.quote_plus("F,C")
    # expect "F%2CC"
    print(safe_string)
    if safe_string == expected_string:
        print("String encoded correctly!")
    else:
        print("Error!")


def main():
    """_summary_
    """
    test_url_encoding()


main()
