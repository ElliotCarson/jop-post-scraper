"""Module to search linkedin jobs and return results"""


from urllib import parse as urlp


def search_linkedin(query: list[dict]) -> str:
    """_summary_

    Args:
        query (list[dict]): _description_

    Returns:
        str: _description_
    """

    LINKEDIN_SEARCH_BASE_URL_STR = "https://www.linkedin.com/jobs/search/"

    # split up the query terms
    keywords = query["keywords"]  # list[str]
    locations = query["locations"]  # list[dict]
    job_type_filters = query["job_type"]  # dict, multi-select filter
    # TODO: update this to be dynamic for additional single-select filters
    date_posted_filters = query["date_posted"]  # dict

    # -JOB TYPE FILTERS- #
    # create url param string for job type filters
    unencoded_job_type_str = ""
    for job_type_filter in job_type_filters:
        if job_type_filter["active"]:
            if unencoded_job_type_str != "":
                unencoded_job_type_str += ","
            unencoded_job_type_str += job_type_filter["url_param"]
    # encode for URL
    job_type_filter_str = "&f_JT="
    job_type_filter_str += urlp.quote_plus(unencoded_job_type_str)

    # -WORK TYPE FILTERS-
    # create a single that combines all work type filters (remote, etc.)
    # on-site=1, hybrid = 3, remote = 2
    for idx, location in enumerate(locations):
        unencoded_location_WT_str = ""
        if location["on-site"]:
            unencoded_location_WT_str += "1"
        if location["remote"]:
            if unencoded_location_WT_str != "":
                unencoded_location_WT_str += ","
            unencoded_location_WT_str += "2"
        if location["hybrid"]:
            if unencoded_location_WT_str != "":
                unencoded_location_WT_str += ","
            unencoded_location_WT_str += "3"
        location_WT_str = "&f_WT=" + urlp.quote_plus(unencoded_location_WT_str)
        locations[idx]["WT_str"] = location_WT_str

    search_urls = []
    # Create list of search pages based on params
    # Search each term
    for keyword in keywords:
        # encode string to avoid URL parse issues
        encoded_keyword = urlp.quote_plus(keyword)
        keyword_param = f"&keywords={encoded_keyword}"

        # In each location
        for location in locations:
            location_geoId_str = location["geoId"]
            location_url_param_str = f"?geoId={location_geoId_str}"
            location_param = location_url_param_str
            location_param += location["WT_str"]

            # With each filter
            # TODO: make this one conditional on filters existing
            for date_posted_filter in date_posted_filters:
                filter_param = ""
                if date_posted_filter["val"] != "hidden":
                    date_url_param_str = "&f_TPR=" + date_posted_filter["val"]
                    filter_param = date_url_param_str
                # add website to list
                search_urls.append(LINKEDIN_SEARCH_BASE_URL_STR
                                   + keyword_param + location_param
                                   + filter_param)

    return search_urls
