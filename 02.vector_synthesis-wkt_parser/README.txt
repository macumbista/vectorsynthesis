The wkt_parse.py was authored by Lee Mongomery for the Vector Synthesis Pure Data library.

This script helps you to convert SVG artwork drawn in Inkscape, Illustrator, etc in the WKT file format (“Well Known Text” is normally used to embed line artwork in GPS maps, for example), and then parse the data from the WKT file into two text files. Each text file will hold either the X or Y axis points representing the 2D shape, normalized between values of -1 and 1.

This script requires Python to be installed on your machine, and your ability to use the Terminal to run it.

STEP ONE: PREPARING THE ARTWORK

In your SVG editor, create a drawing. Shapes with closed boundaries work best, such as fonts. More complex drawings, or drawings with open areas, may not display properly. Fonts will need to be converted to a path (select letter, then “Path—>Stroke to Path” menu in Inkscape). Geometric shapes created from their respective menus probably do not need to be converted to paths. Center your artwork before saving the SVG (select all, then “Align and Distribute” menu in Inkscape to center horizontally and vertically).

STEP TWO: CONVERT TO WKT

Open your SVG file in a text editor, select all the text found there and copy it. Then paste your SVG content into the first field on this website:

http://svg-to-wkt.linfiniti.com/

Copy the text which appears in the second field after clicking “Do It!”, and paste that into a new text document, then save that to your hard drive.

STEP THREE: CREATE THE TABLES

Open a Terminal window on your computer and navigate to the directory where the “wkt_parse.py” resides. Type:

python wkt_parse.py

in your Terminal and follow the on-screen prompt to locate the file with your WKT data. The script will separate the points from the WKT file into two text files. These text files will appear as follows:

1488_xpoints.txt
1488_ypoints.txt

Where “1488” is the number of points in the file, and “xpoints” or “ypoints” indicates to which axis these points belong. You may then open these two textfiles in the “VS-object_2d-help.pd” patch and see them on your oscilloscope display.