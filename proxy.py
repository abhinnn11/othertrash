from mitmproxy import http

# We capture every HLS request and save it locally
def response(flow: http.HTTPFlow):

    url = flow.request.pretty_url

    # capture playlists
    if ".m3u8" in url:
        with open("/tmp/live.m3u8","wb") as f:
            f.write(flow.response.content)

    # capture video segments
    if ".ts" in url or ".m4s" in url:
        with open("/tmp/live.ts","ab") as f:
            f.write(flow.response.content)
