"""_summary_"""

import json
from linkedin_search import search_linkedin


def main():
    """_summary_"""
    # import search terms file
    search_terms_file = open("search_terms.json", encoding="utf-8")
    search_terms_json = json.load(search_terms_file)
    linkedin_queries = search_terms_json["linkedin"]

    # search for each term
    linkedin_urls = search_linkedin(linkedin_queries)
    print(len(linkedin_urls))


if __name__ == "__main__":
    main()
