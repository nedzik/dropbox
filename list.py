#!/usr/bin/env python

import sys
import os
import dropbox.files

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print "Usage: {} <absolute-path-to-dropbox-folder>".format(sys.argv[0].split('/')[-1])
        sys.exit(1)

    oauth2_access_token = os.getenv('DROPBOX_OAUTH_TOKEN')
    if not oauth2_access_token:
        print "Error: Could not get Dropbox access token"
        sys.exit(1)

    dbx = dropbox.Dropbox(oauth2_access_token)
    print "\n".join([x.name for x in dbx.files_list_folder('' if sys.argv[1] == '/' else sys.argv[1]).entries])
