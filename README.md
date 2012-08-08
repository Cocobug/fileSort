fileSort
========

Sorting files according to some rules

> Compyg Copyright (C) 2011 Cocobug
> is distributed in the hope that it will be useful, but
> WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

MANUAL
========

Configure
----------
### How to configure ###
> Yet to be added
* Everything

### Actions ###

* Move
* Copy
* Remove

> Yet to be implemented
* Archive

### Patterns ###

* is
* is_not
* contains
* contains_not
* starts
* ends
* more
* less

> Yet to be implemented
* Recognition of custom patterns with AND OR NOT


### Known Fields ###

* Name : The name of the file (Case insensitive)
* Type : The type of the file (Case insensitive). See mimetypes for more details.
* Size : The size of the file (Octal)
* Extention (or ext): The extention of the file (with the '.' dot)

> Yet to be implemented
* Date : The date of creation of the file

### Mimetypes ###
* Type audio
> audio/mp4: MP4 audio
> audio/mpeg: MP3 or other MPEG audio
> audio/ogg: Ogg Vorbis, Speex, Flac and other audio
> audio/vorbis: Vorbis encoded audio
> audio/vnd.wave: WAV audio

* Type image
> image/gif: GIF image
> image/jpeg: JPEG JFIF image; Defined in RFC 2045 and RFC 2046
> image/png: Portable Network Graphics; Registered,[9] Defined in RFC 2083
> image/tiff: Tag Image File Format (only for Baseline TIFF); Defined in RFC 3302

* Type model (For 3D models)
> model/iges: IGS files, IGES files
> model/mesh: MSH files, MESH files
> model/vrml: WRL files, VRML files
> model/x3d: X3D ISO standard for representing 3D computer graphics

* Type text (For human-readable text and source code)
text/css: Cascading Style Sheets
text/csv: Comma-separated values
text/html: HTML
text/javascript (Obsolete): JavaScript
text/plain: Textual data
text/vcard: vCard (contact information)
text/xml: Extensible Markup Language3

* Type video (For video)
video/mpeg: MPEG-1 video with multiplexed audio
video/mp4: MP4 video
video/ogg: Ogg Theora or other video (with audio)
video/quicktime: QuickTime video
video/webm: WebM Matroska-based open media format
video/x-matroska: Matroska open media format
video/x-ms-wmv: Windows Media Video
video/x-flv: Flash video (FLV files)

* Type application: (For Multipurpose files)
> application/json: JavaScript Object Notation JSON
> application/javascript: ECMAScript/JavaScript
> application/ogg: Ogg, a multimedia bitstream container format
> application/pdf: Portable Document Format
> application/postscript: PostScript
> application/zip: ZIP archive files
> application/x-gzip: Gzip
> application/x-dvi: device-independent document in DVI format
> application/x-latex: LaTeX files
> application/x-font-ttf: TrueType Font No registered MIME type, but this is the most commonly used
> application/x-shockwave-flash: Adobe Flash files for example with the extension .swf
> application/x-stuffit: StuffIt archive files
> application/x-rar-compressed: RAR archive files
> application/x-tar: Tarball files
> application/x-javascript: Javascript (also ?)
> application/x-deb: deb (file format), a software package format used by the Debian project
> audio/x-aac: .aac audio files
> audio/x-caf: Apple's CAF audio files
> image/x-xcf: GIMP image file

Credits to [Wikipedia](http://en.wikipedia.org)'s Article on [Internet media types](http://en.wikipedia.org/wiki/Internet_media_type)

TODO
========

Urgent
--------


Important
---------
* Series of rules (AND, OR)
* Clever recognitions (Aka: $date$, $rand$)

Alpha-Test
---------
* Regular expression understanding
* Recurtion in sub-folders

Cosmetic
---------
* For python 2.6 users: Argparse inexistent, shutils inexistant (Arrr)

* Add the help to Manual
* Give some details on how to conf in Manual

Done (In theory)
--------
> * Complete path Errors
> * Malformed config file on '.' seeking
> * Do the the destination more cleverly
