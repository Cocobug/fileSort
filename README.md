fileSort
========

Sorting files according to some rules

> Compyg Copyright (C) 2011 Cocobug
> is distributed in the hope that it will be useful, but
> WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

MANUAL
========
usage: fileSort.py [-h] [-v] [-f] config [config ...]

Read a config file and apply it's rules

positional arguments:
  config         a config file to apply

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  be verbose
  -f, --force    overwrite destination data

Configure
----------
### How to configure ###

#### Syntax ####
Rules are stored in config files (ini style).
[/Folder/To/Be/Sorted]
> The section is the folder in witch the rules will take place

The rules are formated this way
> attribute.operator(value)
> * The Attribute is the field according to whom the value is gonna be analysed (Aka: Name, size ...)
> * The Operator is the analyser pattern so to speak (Aka: is, contains ...)
> * The Value is the seeked value.

Then comes the Action part
> Next to the equal sign, is put the action type marker.
> * ':' means Copy to destination
> * '!' means Delete the file
> * Left void means move to destination

Then comes the destination part
> The destination can either be relative to the current folder './', inherited from your main folder '~', or absolute '/'

### Actions ###

* Move
* Copy
* Remove

> Yet to be implemented
* Archive

### Operator ###

* is
* is_not
* contains
* contains_not
* starts
* ends
* more
* less

> Yet to be implemented
* Recognition of custom patterns with AND, OR, NOT


### Attribute ###

* Name : The name of the file (Case insensitive)
* Type : The type of the file (Case insensitive). See mimetypes for more details.
* Size : The size of the file (Octal)
* Extention (or ext): The extention of the file (with the '.' dot)
* Date : The date of creation of the file

### Mimetypes ###
* Type audio
> * audio/mp4: MP4 audio
> * audio/mpeg: MP3 or other MPEG audio
> * audio/ogg: Ogg Vorbis, Speex, Flac and other audio
> * audio/vorbis: Vorbis encoded audio
> * audio/vnd.wave: WAV audio

* Type image
> * image/gif: GIF image
> * image/jpeg: JPEG JFIF image; Defined in RFC 2045 and RFC 2046
> * image/png: Portable Network Graphics; Registered,[9] Defined in RFC 2083
> * image/tiff: Tag Image File Format (only for Baseline TIFF); Defined in RFC 3302

* Type model (For 3D models)
> * model/iges: IGS files, IGES files
> * model/mesh: MSH files, MESH files
> * model/vrml: WRL files, VRML files
> * model/x3d: X3D ISO standard for representing 3D computer graphics

* Type text (For human-readable text and source code)
> * text/css: Cascading Style Sheets
> * text/csv: Comma-separated values
> * text/html: HTML
> * text/javascript (Obsolete): JavaScript
> * text/plain: Textual data
> * text/vcard: vCard (contact information)
> * text/xml: Extensible Markup Language3

* Type video (For video)
> * video/mpeg: MPEG-1 video with multiplexed audio
> * video/mp4: MP4 video
> * video/ogg: Ogg Theora or other video (with audio)
> * video/quicktime: QuickTime video
> * video/webm: WebM Matroska-based open media format
> * video/x-matroska: Matroska open media format
> * video/x-ms-wmv: Windows Media Video
> * video/x-flv: Flash video (FLV files)

* Type application: (For Multipurpose files)
> * application/json: JavaScript Object Notation JSON
> * application/javascript: ECMAScript/JavaScript
> * application/ogg: Ogg, a multimedia bitstream container format
> * application/pdf: Portable Document Format
> * application/postscript: PostScript
> * application/zip: ZIP archive files
> * application/x-gzip: Gzip
> * application/x-dvi: device-independent document in DVI format
> * application/x-latex: LaTeX files
> * application/x-font-ttf: TrueType Font No registered MIME type, but this is the most commonly used
> * application/x-shockwave-flash: Adobe Flash files for example with the extension .swf
> * application/x-stuffit: StuffIt archive files
> * application/x-rar-compressed: RAR archive files
> * application/x-tar: Tarball files
> * application/x-javascript: Javascript (also ?)
> * application/x-deb: deb (file format), a software package format used by the Debian project
> * audio/x-aac: .aac audio files
> * audio/x-caf: Apple's CAF audio files
> * image/x-xcf: GIMP image file

Credits to [Wikipedia](http://en.wikipedia.org)'s Article on [Internet media types](http://en.wikipedia.org/wiki/Internet_media_type)

TODO
========

Urgent
--------

Important
---------
* Clever recognitions (Aka: $date$, $rand$)
* Multiple section analysis (Aka: [A B C])

Alpha-Test
---------
* Regular expression understanding
* Recurtion in sub-folders
* Series of rules (AND, OR)

Cosmetic
---------
* For python 2.6 users: Argparse inexistent, shutils inexistant (Arrr)

Done (In theory)
--------
> * Complete path Errors
> * Malformed config file on '.' seeking
> * Do the the destination more cleverly
