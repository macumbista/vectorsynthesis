READ ME FOR THE VECTOR SYNTHESIS PARSER

This Python script assembles the lines and vertices of a 3D OBJ file into three tables which can be used by the Pure Data Vector Synthesis library to render 3D shapes as audio signals sent to an XY oscilloscope or other vector display.

PREPROCESSING:

1) You will need to import your OBJ file into Hansi Raber’s Oscilloscope application:
https://github.com/kritzikratzi/Oscilloscope

2) Save the file you have imported the OBJ file into and open it in a text editor. 

3) Locate the sections of the file labelled “lines” and “vertices” as shown below, and copy those blocks of text into the “lines_vertices.py” file as shown below.

4) Run the script as shown below. It will generate three text files as well as tell you the total number of vertices in the shape.

5) Load the contents of “xvert.txt”, “yvert.txt” and “zvert.txt” into the appropriate tables in the Pd patch you wish to use. Remember to adjust the table size to accomodate the total number of vertices, as well as the multiplier for the [phasor~] which reads them. See “V-cube-help.pd” for example, to see a patch which uses these kind of tables.

FORMAT OF LINES_VERTICES

Lines and Vertices are processed from a single file in the same directory as the script.

The script assumes a file named "lines_vertices.py"

formating of "lines_vertices.py" is as follows:

"lines":[{0 1}{1 2}{2 6}{6 2}{2 7}{7 1}{1 6}{6 5}{5 3}{3 5}{5 6}{6 10}{10 3}{3 8}{8 3}{3 9}{9 2}{2 9}{9 3}{3 10}{10 5}{5 10}{10 6}{6 11}{11 1}{1 7}{7 2}{2 10}{10 9}{9 8}{8 4}{4 3}{3 4}{4 5}{5 11}{11 4}{4 8}{8 7}{7 8}{8 9}{9 10}{10 2}{2 1}{1 11}{11 5}{5 4}{4 11}{11 6}{6 1}{1 0}{0 4}{4 0}{0 7}{7 9}{9 7}{7 0}{0 8}{8 0}{0 11}{11 0}]

"vertices":[{0,-0.525731,0.850651}{0.850651,0,0.525731}{0.850651,0,-0.525731}{-0.850651,0,-0.525731}{-0.850651,0,0.525731}{-0.525731,0.850651,0}{0.525731,0.850651,0}{0.525731,-0.850651,0}{-0.525731,-0.850651,0}{0,-0.525731,-0.850651}{0,0.525731,-0.850651}{0,0.525731,0.850651}]


n.b.  no extraneous spaces or characters.

the script deletes unnecessary characters and changes others to format this data into list variables that python can work with.

RUNNING THE SCRIPT

to run the script:

1 Navigate to the script directory.
2 type "python vs_line_parse.py"
3 this script was written in python 2.7 not sure if it will work under python 3.0
