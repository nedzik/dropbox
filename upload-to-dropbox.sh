#!/usr/bin/env bash 

. /usr/local/bin/virtualenvwrapper.sh

base_dir=$(dirname $0)
if [[ $(ls -l $0 | cut -c1-1) == "l" ]]; then
	base_dir=$(ls -l $0 | cut -d '>' -f2-2)
	base_dir=$(dirname ${base_dir})
fi

workon dropbox
${base_dir}/upload.py $*
deactivate
