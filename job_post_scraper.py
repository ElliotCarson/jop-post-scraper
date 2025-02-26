"""_summary_"""

import json
from linkedin.linkedin_url_generator import search_linkedin
from linkedin.linkedin_scraper import scrape_linkedin_page


def main():
    """_summary_"""
    # import search terms file
    search_terms_file = open("search_terms.json", encoding="utf-8")
    search_terms_json = json.load(search_terms_file)
    linkedin_queries = search_terms_json["linkedin"]

    # search for each term
    linkedin_urls = search_linkedin(linkedin_queries)
    # print(len(linkedin_urls))

    # scrape the webpages
    job_list = []
    for url in linkedin_urls:
        job_list += scrape_linkedin_page(url)
    print(len(job_list))


if __name__ == "__main__":
    main()
