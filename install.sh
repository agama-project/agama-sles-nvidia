#!/bin/bash
set -eu
# Install all provided files either into the build root or to the current system,
# this script is used by agama-sles-nvidia.spec.

# The caller (RPM .spec) is expected to set these environment variables:
# SRCDIR=.
# DESTDIR=%{buildroot}
# datadir=%{_datadir}

if [ "${1-}" = --system ]; then
    SRCDIR=.
    DESTDIR=""
    datadir=/usr/share
fi

# install regular file, with mode 644 (not an executable with mode 755)
install6() {
    install -m 0644 "$@"
}

install6 -D -t "${DESTDIR}${datadir}"/agama/products.d "${SRCDIR}"/products.d/*.yaml
install6 -D -t "${DESTDIR}${datadir}"/agama/web_ui/assets/appearance "${SRCDIR}"/branding/*.css
install6 -D -t "${DESTDIR}${datadir}"/agama/web_ui/assets/appearance/fonts "${SRCDIR}"/branding/*.woff2
