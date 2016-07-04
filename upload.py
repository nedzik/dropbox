#!/usr/bin/env python

import sys
import os
import dropbox.files

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print "Usage: {} <local-file> <absolute-path-to-dropbox-folder>".format(sys.argv[0].split('/')[-1])
        sys.exit(1)

    file_to_upload = open(sys.argv[1])
    dropbox_path = sys.argv[2] + '/' + sys.argv[1].split('/')[-1]

    oauth2_access_token = os.getenv('DROPBOX_OAUTH_TOKEN')
    if not oauth2_access_token:
        print "Error: Could not get Dropbox access token"
        sys.exit(1)

    dbx = dropbox.Dropbox(oauth2_access_token)
    dbx.files_upload(file_to_upload, dropbox_path, mode=dropbox.files.WriteMode.overwrite)
