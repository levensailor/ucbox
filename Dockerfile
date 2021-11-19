FROM netboxcommunity/netbox:latest-ldap

COPY ./ucbox_plugin /source/ucbox_plugin/ucbox_plugin/
COPY ./setup.py /source/ucbox_plugin/
COPY ./MANIFEST.in /source/ucbox_plugin/
COPY ./README.md /source/ucbox_plugin/
RUN pip3 install --no-cache-dir /source/ucbox_plugin/
