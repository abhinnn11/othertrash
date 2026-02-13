from mitmproxy import http
import os
import time

streamfile = "/tmp/live.ts"

def response(flow: http.HTTPFlow):

    url = flow.request.pretty_url.lower()

    # detect video segments
    if ".ts" in url or ".m4s" in url:

        # create file if first segment
        if not os.path.exists(streamfile):
            print("New stream detected")
        
        with open(streamfile, "ab") as f:
            f.write(flow.response.content)
