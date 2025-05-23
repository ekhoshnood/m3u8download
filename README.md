# m3u8download
a fixed Python library to download video at m3u8 url


Disclaimer: I did not create this library, I have only made minor modifications. Original project homepage can be found here: https://pypi.org/project/m3u8downloader/.

m3u8download
============================

m3u8download is a tool to download video at a m3u8 link. `HTTP Live
Streaming (HLS)`_ is becoming popular. m3u8 playlist is used by HLS to serve
video fragments of different quality to different clients. This tool supports
HLS master playlist and media playlist. If master playlist is given, it
selects the highest resolution automatically. HLS fragment encryption is
supported. Resume from partial download is supported, just rerun the same
command to continue.

ffmpeg is used to convert the downloaded fragments into final mp4 video file.

Installation
------------

To install m3u8download, simply:

.. code-block:: bash

   $ sudo apt install -y ffmpeg
   $ pip install --user m3u8download


Quick Start
-----------

Example command line usage:

.. code-block:: bash

   downloadm3u8 -o ~/Downloads/foo.mp4 https://example.com/path/to/foo.m3u8

If ~/.local/bin is not in $PATH, you can use full path:

.. code-block:: bash

   ~/.local/bin/downloadm3u8 -o ~/Downloads/foo.mp4 https://example.com/path/to/foo.m3u8

Here is built-in command line help:

.. code-block:: bash

   usage: m3u8download [-h] [--version] [--debug] --output OUTPUT
                         [--tempdir TEMPDIR] [--concurrency N]
                         URL
   
   download video at m3u8 url
   
   positional arguments:
     URL                   the m3u8 url
   
   optional arguments:
     -h, --help            show this help message and exit
     --version             show program's version number and exit
     --debug               enable debug log
     --output OUTPUT, -o OUTPUT
                           output video filename, e.g. ~/Downloads/foo.mp4
     --tempdir TEMPDIR     temp dir, used to store .ts files before combing them
                           into mp4
     --concurrency N, -c N
                           number of fragments to download at a time

Documentation
-------------

This command line tool doesn't have extra documents.

Limitations
-------------

This tool only parses minimum m3u8 extensions for selecting media playlist
from master playlist, downloading key and fragments from media playlist. If a
m3u8 file doesn't download correctly, it's probably some new extension was
added to the HLS spec which this tool isn't aware of.

ChangeLog
---------

* v0.25.5.1
Fixing when downloading m3u8 streams with long URLs of m3u8download