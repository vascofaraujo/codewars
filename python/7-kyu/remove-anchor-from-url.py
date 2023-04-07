def remove_url_anchor(url):
    # TODO: complete
    anchor_index = url.find("#")
    if anchor_index != -1:
        url = url[0:anchor_index]
    return url
