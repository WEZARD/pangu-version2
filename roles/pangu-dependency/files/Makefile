.PHONY: rpm clean

VERSION ?= 1.3.0
BUILD_NUMBER ?= 1
SOURCE = jnetpcap-$(VERSION).tar.gz
TOPDIR = /tmp/jnetpcap-rpm
PWD = $(shell pwd)

rpm: $(SOURCE)
	@rpmbuild -v -bb \
			--define "_sourcedir $(PWD)" \
			--define "_rpmdir $(PWD)" \
			--define "_topdir $(TOPDIR)" \
			--define "version $(VERSION)" \
			--define "build_number $(BUILD_NUMBER)" \
			jnetpcap.spec

$(SOURCE):
	@spectool \
			--define "version $(VERSION)" \
			-g jnetpcap.spec

clean:
	@rm -rf $(TOPDIR) x86_64
	@rm -f $(SOURCE)
