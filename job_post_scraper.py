"""_summary_"""

import json
from linkedin_search import search_linkedin


def main():
    """_summary_"""
    # import search terms file
    search_terms_file = open("search_terms.json")
    search_terms_json = json.load(search_terms_file)
    linkedin_queries = search_terms_json["linkedin"]["search_terms"]

    # search for each term
    for query in linkedin_queries:
        print(search_linkedin(query))


if __name__ == "__main__":
    main()
