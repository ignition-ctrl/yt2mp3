#!/usr/bin/env python
# -*- coding: utf-8 -*-
import youtube-dl
import os
import sys
import download


if __name__ == "__main__":
    download.download_thumbnail(sys.argv[1], sys.argv[2])