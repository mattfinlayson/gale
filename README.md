gale
=============

A little python blogging engine based heavily on toto and inspired by yaki
***

introduction
=============

    git clone git://github.com/savagegus/gale.git myblog
    cd myblog
    python gale.py
***

philosophy
=============

Simple as I could make it, but not any simpler. Tornado provides the serves the content, data storage is on the file system, templating is done through tornado. There is no database.

how it works
=============

tornado is the only moving part, it has an index handler and an article handler at the moment, with more to come. articles are stored on the filesystem (in my case revisioned by dropbox) and there is a very basic ArticleProvider that slurps it all up and passes it to tornado.

articles are stored as text files, following toto's format. metadata is embedded in a yaml format.

individual articles are accessed through pretty url's like /articles/2011/1/1/blogging-with-gale

thanks
=============
To [tornado]("http://www.tornadoweb.org/") for the heavy lifting.
To [Alexis Sellier]("http://cloudhead.io") for [toto]("https://github.com/cloudhead/toto") and all the ideas the theme gale uses
To [Rui Carmo]("http://the.taoofmac.com") for [yaki]("http://code.google.com/p/yaki/") and the ideas that gale steals from it.

used
=============
[thepatternlibrary]("http://thepatternlibrary.com/")
