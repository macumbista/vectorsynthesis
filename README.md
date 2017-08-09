

::::::::::VECTOR SYNTHESIS LIBRARY ::::::::::

The Vector Synthesis library allows the creation and manipulation of 2D and 3D vector shapes, Lissajous figures, and scan processed image and video inputs using audio signals sent directly to oscilloscopes, hacked CRT monitors, Vectrex game consoles, ILDA laser displays, or oscilloscope emulation softwares using the Pure Data programming environment. 

Audio waveforms control the vertical and horizontal movements as well as the brightness of a single beam of light, tracing shapes, points and curves with a direct relationship between sound and image.

The technique is based on the well-known principle of Lissajous figures, which are a mathematical representation of complex harmonic motion. Originally displayed by reflecting light between mirrors attached to a pair of vibrating tuning forks, we are most used to seeing them on the screen of an oscilloscope, where they can be produced using pairs of electronic oscillators tuned to specific ratios. 

There is a wealth of such experiments from the 1950s onward by major figure such as Mary Ellen Bute, John Whitney, Larry Cuba, Manfred Mohr, Nam June Paik, Ben Laposky, Bill Etra, and Steina & Woody Vasulka, which were all highly inspiration to the development of this library.

You can see a demo video of the scan processing and 3D rotation functions here:

	https://www.facebook.com/macumbista/videos/795648800609817/

And you can see a two hour video presentation of this library here: 
	
	https://www.facebook.com/macumbista/posts/791705604337470
 

*REQUIREMENTS*

——SOFTWARE
	
	Pure Data 32 bit, version 0.45 or newer
	Gem 0.93.3 (OPTIONAL, used in scan processor only. Installed via deken, Pd’s externals manager)
	
	NOTE: Gem does not run on 64 bit Pure Data, and Pd-Extended is too old for some features of this library.
	
——HARDWARE

	DC-coupled audio interface with minimum 3 output channels (5 recommended)
	
	Oscilloscope with X/Y/Z inputs (all DC-coupled)
	—or—
	Vectrex game console modified for X/Y/Z input (all DC-coupled)
	—or—
	Vector monitor with X/Y/Z inputs (all DC-coupled)
	—or—
	Oscilloscope software with X/Y/Z inputs such as Hansi Raber's "Oscilloscope!" app
	(Note: "Oscilloscope!" currently lacks brightness input)
	plus audio loopback application such as SoundFlower or Virtual Audio Cable
	
	
	NOTE: the Z axis should control the brightness of the beam, not 3D depth
	
	Current development is on a MacBookPro/OSX 10.12.6
	One target platform would be the BELA board with the Heavy compiler
	Scan processing with a webcam on the Raspberry Pi is also being investigated


*GENERAL NOTES*


	Audio Interface Output 1 : Horizontal
	Audio Interface Output 2 : Vertical
	Audio Interface Output 3 : Brightness
	Audio Interface Output 4 : Audio Left (Horizontal * Brightness, w/ multiplexing system patches)
	Audio Interface Output 5 : Audio Right (Vertical * Brightness, w/ multiplexing system patches)

	Higher sampling rate = higher resolution/fewer errors in the vector shapes
	Tested at 44.1K, 96K, 192K

	Stereo output is also usable, however there will be no brightness control.
	
	An AC-coupled soundcard or display will show noticeable distortions in the shape
	and screen location of the vector shapes (they will always appear in the center).

	DC-coupling is also necessary for brightness control.

	Brightness control is essential for multiplexing, scan processing, and a
	number of other interesting visual effects, however you can still use this 
	library for many things without it.





*LIST OF OBJECTS*

—-NATIVE PD OBJECTS of NOTE

	[phasor~] : sawtooth ramp generator which goes from value 0 to value 1
	[wrap~] : remainder of a division operation, used here to generate phase-locked harmonics of [phasor~].
		Adding an offset before [wrap~] changes the phase, and inserting a multiplication before [wrap~]
		changes the harmonic, since the object "wraps" any incoming signal over 1 back to 
		phase = 0 degrees.
	[cos~] : transforms the signal from [phasor~] to a cosine wave. Adding an offset before [cos~] 
		changes the phase, and inserting a multiplication before [cos~] changes the harmonic, since the 
		objects "wraps" any incoming signal over 1 back to phase = 0 degrees.

—-FUNCTION GENERATORS

	[V-operator]: function generator with variable waveshaping, scaling, and uni- and bi-polar outputs
	
——2D SHAPE GENERATORS

	[V-basic-lissajous] : create a simple Lissajous figure
	[V-lissagen] : create a Lissajous figure with wave shaping and scaling options
	[V-circle] : create a circle
	[V-triangle] : create a triangle
	[V-diamond] : create a diamond/square
	[V-poly-2D] : to do
	[V-raster] : to do

—-2D VECTOR TRANSFORMATIONS

	[V-scale-2D] : scale (resize) a 2D vector shape
	[V-translate-2D] : translate (move) a 2D vector shape
	[V-rotate-2D] : rotate a 2D vector shape
	[V-shear-2D] : to do
	[V-mirror-2D] : to do

—-3D SHAPE GENERATORS (require [V-rotate-3D] to project onto 2D vector space)
	
	[V-sphere] : create a 3D sphere of triangular faces
	[V-pyramid] : create a 3D pyramid with square base
	[V-cube] : create a 3D cube
	[V-tetrahedron] : create a 3D tetrahedron
	[V-octahedron] : create a 3D octahedron
	[V-dodecahedron] : create a 3D dodecahedron
	[V-icosahedron] : create a 3D icosahedron

—-3D VECTOR TRANSFORMATIONS

	[V-scale-3D] : to do
	[V-translate-3D] : to do
	[V-rotate-3D] : project shapes to 3D and rotate
	[V-shear-3D] : to do
	[V-mirror-3D] : to do
	[V-perspective-3D] : to do
	[V-lighting-3D] : to do

—-UTILITIES

	[V-seeme~] : plot a signal onto a visual array
	[V-tabreadlin~] : read a table with linear interpolation (for reading 3D objects)
	[V-waveselect] : preset waveshapes for [V-operator]
	[V-gamma] : apply gamma correction to the brightness signal
	[V-invert-unipolar] : invert a signal with a (0 - 1) range
	[V-invert-bipolar] : invert a signal with a (-1 - 1) range
	[V-crossfade] : morph between two 2D vector shapes
	[V-clip] : to do


—-MULTIPLEXING (see V-multiplex-help.pd for details)

	[V-masterclock] : sets multiplexing frequency and number of multiplexed channels
	[V-output] : collects multiplexed channels and sends them to the audio interface
	[V-multiplex] : assigns a vector shape to one multiplexing channel
	[V-brightness-crossfade] : crossfades the brightness of two multiplexed channels

—-SCAN PROCESSING (requires GEM external library!)

	[V-scanprocessor] : scan a camera input, image, or video and apply it to a raster

—-ILDA LASER DISPLAY OUTPUT

	[V-ilda] : to do


*ACKNOWLEDGEMENTS*


The author also wishes to thank the following people and institutions for their support of the project:

	Aalto University Media Lab (Helsinki FI)
	Marianne Decoster-Taivalkoski/CMT Sibelius Academy (Helsinki FI)
	Jason and Debora Bernagozzi/Signal Culture (Owego NY USA)
	Borut Savski/Cirkulacija2 (Ljubljana SI)
	Lars Larsen/LZX Industries (Portland OR USA)
	Spektrum (Berlin DE)
	Andy Farnell
	Ivan Marusic Klif
	Dave Jones
	Nathan Thompson
	Roland Lioni/Akira’s Rebirth
	Lee Montgomery 


Derek Holzer
Berlin July 2017
http://macumbista.net
macumbista@gmail.com
















# vectorsynthesis
