"""_summary_"""
import urllib.request


def scrape_linkedin_page(url: str) -> list:
    """_summary_

    Args:
        url (str): _description_

    Returns:
        list: _description_
    """
    print(url)
    page = urllib.request.urlopen(url)
    print(page.read())
    return (url[40])
