

::::::::::VECTOR SYNTHESIS LIBRARY ::::::::::

The Vector Synthesis library allows the creation and manipulation of 2D and 3D vector shapes, Lissajous figures, and scan processed image and video inputs using audio signals sent directly to oscilloscopes, Vectrex game consoles, ILDA laser displays, or oscilloscope emulation softwares using the Pure Data programming environment. 

Audio waveforms control the vertical and horizontal movements as well as the brightness of a single beam of light, tracing shapes, points and curves with a direct relationship between sound and image.

The technique is based on the well-known principle of Lissajous figures, which are a mathematical representation of complex harmonic motion. Originally displayed by reflecting light between mirrors attached to a pair of vibrating tuning forks, we are most used to seeing them on the screen of an oscilloscope, where they can be produced using pairs of electronic oscillators tuned to specific ratios. 

There is a wealth of such experiments from the 1950s onward by major figure such as Mary Ellen Bute, John Whitney, Larry Cuba, Manfred Mohr, Nam June Paik, Ben Laposky, Bill Etra, and Steina & Woody Vasulka, which were all highly inspiration to the development of this library.

Tutorials, announcements, and testing here: [Vector Synthesis group] (https://www.facebook.com/groups/vectorsynthesis/)

	

Demo videos here:

	[https://vimeo.com/macumbista] (https://vimeo.com/macumbista)

 If this library has been useful, please consider making a donation towards the development:
 
 [![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=SPHWJSJWH92GG&source=url)
 
 Or consider ordering a copy of the Vector Synthesis book:
 
 	[http://www.lulu.com/shop/derek-holzer/vector-synthesis-a-media-archaeological-investigation-into-sound-modulated-light/paperback/product-24379956.html] (http://www.lulu.com/shop/derek-holzer/vector-synthesis-a-media-archaeological-investigation-into-sound-modulated-light/paperback/product-24379956.html)
 

*REQUIREMENTS*

——SOFTWARE
	
	Pure Data "Vanilla", version 0.49 or newer. 
	Gem 0.93.3 (OPTIONAL, used in scan processor only. Installed via deken, Pd’s externals manager)
	
	NOTE: Pd-Extended is too old for some features of this library.
	
——HARDWARE
	
	RECOMMENDED
	
	DC-coupled audio interface 
	Minimum 3 output channels (horizontal, vertical, brightness)
	5 output channels recommended if seperate stereo audio channels are desired
	High sampling rate also recommended (192 kHz if possible)
	
	Oscilloscope with X/Y/Z inputs (all DC-coupled)
	—or—
	Vectrex game console modified for X/Y/Z input (all DC-coupled)
	—or—
	Vector monitor with X/Y/Z inputs (all DC-coupled)
	—or—
	Oscilloscope software with X/Y/Z inputs such as Hansi Raber's "Oscilloscope!" app
	https://github.com/kritzikratzi/Oscilloscope/releases/tag/1.0.9
	(Hold SHIFT key when selecting input for third channel brightness control)
	plus audio loopback application such as SoundFlower or Virtual Audio Cable
	
	NOTE: the Z axis should control the brightness of the beam, not 3D depth
	
	MINIMUM
	
	You can try using this library with only a two channel soundcard and a more common X/Y oscilloscope. You will not have control over the brightness, and I have found that built-in laptop audio outputs in particular introduce a lot of visual noise into the oscilloscope image.
	
	You can find an excellent overview of how DC COUPLING and SAMPLING RATE affect the oscilloscope image here:
	
	https://www.youtube.com/watch?v=piZPIMYfq0c



*GENERAL NOTES*

	Start with the first files in the library, they are the tutorials:
	
		000.A.VECTOR_GENERATORS.pd
		000.B.2D_VECTORS.pd
		000.C.3D_VECTORS.pd
		000.D.VECTOR_MODIFIERS.pd
		000.G.VECTOR_MULTIPLEXING.pd
		000.I.PRESET_SYSTEM.pd
		
	The files with "gui" in their name are a designed to be patched together much like a modular synth.
	The files with "help" in their name are also very good examples to start with to learn more code. 
	The files without "help" in their name are the abstractions themselves, without any controls.
	The files with ".txt" extension are backup data for the various 3D shapes.

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

	[V-operator]: function generator with variable waveshaping, scaling, phase, and uni- and bi-polar outputs
	
——2D SHAPE GENERATORS

	[VS-basic-lissajous] : create a simple Lissajous figure
	[VS-sine-circle] : create a circle
	[VS-triangle] : create a triangle
	[VS-diamond] : create a diamond/square
	[VS-poly] : create an n-sided polygon
	[VS-raster] : create a horizontal, vertical, or grid raster
	[VS-object_2d] : read X and Y points from a textfile and draw them
	[VS-syntheshape] : complex oscilloscope art generator based on Mitchell Waite's 1974 "Syntheshape"

—-VECTOR TRANSFORMATIONS

	[VS-scale] : scale (resize) a 2D or 3D vector shape
	[VS-translate] : translate (move) a 2D or 3D vector shape
	[VS-rotate] : rotate a 2D or 3D vector shape
	[VS-projector] : project 3D shapes into 2D vector space with perspective and shadow
	[VS-morph] : morph between two 2D vector shapes
	[VS-decimate] : reduce the number of points used to draw a vector shape, with or without smoothing
	
—-3D SHAPE GENERATORS
	
	[VS-sphere] : create a 3D sphere of triangular faces
	[VS-pyramid] : create a 3D pyramid with square base
	[VS-cube] : create a 3D cube
	[VS-tetrahedron] : create a 3D tetrahedron
	[VS-octahedron] : create a 3D octahedron
	[VS-dodecahedron] : create a 3D dodecahedron
	[VS-icosahedron] : create a 3D icosahedron
	[VS-hand] : create a 3D hand shape

—-UTILITIES

	[VS-seeme] : plot three signals (X, Y, and brightness, for example) onto visual arrays
	[VS-tabreadlin~] : read a table with linear interpolation (for reading 3D objects)
	[VS-waveselect] : preset waveshapes for [VS-operator]
	[VS-gamma] : apply gamma correction to the brightness signal
	[VS-invert-unipolar] : invert a signal with a (0 - 1) range
	[VS-invert-bipolar] : invert a signal with a (-1 - 1) range
	[VS-blanking] : control the brightness of an object in relation to the phase of its signal
	[VS-tri2ramp] : transform an input triangle wave (from an analog synth for example) to a ramp
	[VS-gemhead-master] : simple controls for Gem portion of scan processing patches
	[VS-sig2float] : method for reading an audio signal as a samplerate stream of floats



—-MULTIPLEXING (see V-multiplex-help.pd for details)

	[VS-masterclock] : sets multiplexing frequency and number of multiplexed channels
	[VS-output] : collects multiplexed channels and sends them to the audio interface
	[VS-multiplex] : assigns a vector shape to one multiplexing channel
	[VS-brightness-crossfade] : crossfades the brightness of two multiplexed channels

—-SCAN PROCESSING (requires GEM external library!)

	[VS-scanprocessor] : scan a camera input, image, or video with a raster or other vectors

—-ILDA LASER DISPLAY OUTPUT

	[VS-ilda] : output to an ILDA laser display projector


*ACKNOWLEDGEMENTS*


I would like to thank the following people and institutions for their support and encouragement of the project: 

	Antti Ikonen/Aalto University Media Lab (Helsinki FI)
	Marianne Decoster-Taivalkoski/Centre for Music & Technology of the Sibelius Academy (Helsinki FI)
	Jason and Debora Bernagozzi/Signal Culture (Owego NY USA)
	Borut Savski/Cirkulacija2 (Ljubljana SI)
	Lars Larsen/LZX Industries (Portland OR USA)
	Gisle Frøysland/Piksel (Bergen NO)
	Alfredo Ciannameo and Lieke Ploeger/Spektrum (Berlin DE)
	Svetlana Maras/Radio Belgrade Electronic Studio (Belgrade SRB)
	Tapio “Tassu” Takala/Aalto University Department of Computer Science (Helsinki FI)
	Joseph Hyde/Seeing Sound/Bath Spa University (Bath UK)
	Jeff Chippewa & Nicolas Bernier/Canadian Electroacoustic Community (Montreal CA)
	Kari Yli-Annala/AAVE Festival (Helsinki FI)
	Andy Farnell
	Ivan Marušić Klif
	Dave Jones
	Nathan Thompson
	Roland Lioni/Akira’s Rebirth
	Hansi Raber
	Jerobeam Fenderson
	Lee Montgomery
	Andrew Duff
	Marco Donnarumma
	Robert Henke
	Chris King
	and finally the Video Circuits online community, without whom I never would have started down this crazy road


Derek Holzer
Helsinki June 2019
http://macumbista.net
macumbista AT THE DOMAIN gmail DOT com
















# vectorsynthesis
