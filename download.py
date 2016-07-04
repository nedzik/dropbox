#!/usr/bin/env python

import sys
import os
import dropbox.files

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print "Usage: {} <absolute-path-to-dropbox-file>".format(sys.argv[0].split('/')[-1])
        sys.exit(1)

    local_file = sys.argv[1].split('/')[-1]
    dropbox_file = sys.argv[1]

    oauth2_access_token = os.getenv('DROPBOX_OAUTH_TOKEN')
    if not oauth2_access_token:
        print "Error: Could not get Dropbox access token"
        sys.exit(1)

    dbx = dropbox.Dropbox(oauth2_access_token)
    dbx.files_download_to_file(local_file, dropbox_file)
