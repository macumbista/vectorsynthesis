The wkt_parse.py was authored by Lee Mongomery for the Vector Synthesis Pure Data library.

This script helps you to convert SVG artwork drawn in Inkscape, Illustrator, etc in the WKT file format (“Well Known Text” is normally used to embed line artwork in GPS maps, for example), and then parse the data from the WKT file into two text files. Each text file will hold either the X or Y axis points representing the 2D shape, normalized between values of -1 and 1.

This script requires Python to be installed on your machine, and your ability to use the Terminal to run it.

STEP ONE: PREPARING THE ARTWORK

In your SVG editor, create a drawing. Shapes with closed boundaries work best, such as fonts. More complex drawings, or drawings with open areas, may not display properly. Fonts will need to be converted to a path (select letter, then “Path—>Stroke to Path” menu in Inkscape). Geometric shapes created from their respective menus probably do not need to be converted to paths. Center your artwork before saving the SVG (select all, then “Align and Distribute” menu in Inkscape to center horizontally and vertically).

STEP TWO: CONVERT TO WKT

Open your SVG file in a text editor, select all the text found there and copy it. Then upload your SVG content for conversion on this website:

https://mygeodata.cloud/converter/svg-to-wkt

You will have a CSV (comma separated values) file with WKT inside. Open the file and look for strings within “ “ (quote marks), for example:


POLYGON ((101.119367 5.827172,87.753843 20.859209,102.413776 35.505808,72.61227 33.075881,52.112446 45.376343,47.05522 28.836075,19.722122 21.797664,46.392965 14.005137,50.005269 -2.652438,71.558681 9.06149,101.119367 5.827172))

Copy paste each string into it’s own textfile and save with the file extension .wkt

The online converter will break complex forms into a number of polygons. Each will have to be used separately to be drawn accurately. 

STEP TWO-POINT-FIVE: ADVANCED FIGURES

You could also experiment with the following format, by making a GEOMETRYCOLLECTION out of the individual POLYGON results according to the following pattern, however such collections are usually too complex to be drawn accurately:

GEOMETRYCOLLECTION(POLYGON((354.5 -428.5,256.3 -409.2,184.7 -479.1,172.7 -379.7,84.1 -333.2,174.9 -291.2,191.7 -192.5,259.8 -265.9,358.8 -251.4,310.1 -338.8,354.5 -428.5)),POLYGON((395.3 -525.7,256.1 -479.1,138.8 -567.5,140 -420.7,19.7 -336.4,159.7 -292.2,202.7 -151.8,288 -271.3,434.8 -268.8,347.5 -386.8,395.3 -525.7)),POLYGON((277 -517.2,218.1 -429.5,112.4 -428.3,177.6 -345.1,146.1 -244.3,245.3 -280.6,331.5 -219.4,327.6 -325.1,412.4 -388.1,310.8 -417.1,277 -517.2)))

STEP THREE: CREATE THE TABLES

Open a Terminal window on your computer and navigate to the directory where the “wkt_parse.py” resides. Type:

python wkt_parse.py

in your Terminal and follow the on-screen prompt to locate the file with your WKT data. The script will separate the points from the WKT file into two text files. These text files will appear as follows:

1488_xpoints.txt
1488_ypoints.txt

Where “1488” is the number of points in the file, and “xpoints” or “ypoints” indicates to which axis these points belong. You may then open these two textfiles in the “VS-object_2d-help.pd” patch and see them on your oscilloscope display.