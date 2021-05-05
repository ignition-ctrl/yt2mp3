#!/usr/bin/env python
# -*- coding: utf-8 -*-
import youtube-dl
import os
import sys
from downloadimg import download_thumbnail


if __name__ == "__main__":
    downloadimg.download_thumbnail(sys.argv[1], sys.argv[2])
