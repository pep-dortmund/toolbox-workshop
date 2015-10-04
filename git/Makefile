include ../common/common.mk
include ../common/document.mk

build/git.pdf: $(addprefix build/figures/, github.png bitbucket.png gitlab.png)

build/figures/github.png: | build/figures
	wget https://github-media-downloads.s3.amazonaws.com/GitHub-Logos.zip -O build/figures/GitHub-Logos.zip --no-use-server-timestamps
	cd build/figures && unzip GitHub-Logos.zip
	cp build/figures/GitHub-Logos/GitHub_Logo.png $@

build/figures/bitbucket.png: | build/figures
	wget http://www.atlassian.com/dms/wac/images/press/Atlassian-logos/logoBitBucketPNG.png -O $@ --no-use-server-timestamps

build/figures/gitlab.png: | build/figures
	wget https://gitlab.com/gitlab-com/gitlab-artwork/raw/master/wordmark/wm_no_bg.png -O $@ --no-use-server-timestamps
