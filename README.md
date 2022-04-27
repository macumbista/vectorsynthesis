

*::::::::::VECTOR SYNTHESIS LIBRARY ::::::::::*

[![](https://github.com/macumbista/vectorsynthesis/blob/master/divisions_still.png)](https://vimeo.com/344599871 "Vector Synthesis: Divisions of a Circle by Macumbista on Vimeo")

*Click through image for ""Vector Synthesis: Divisions of a Circle" by Macumbista on Vimeo*

The Vector Synthesis library allows the creation and manipulation of 2D and 3D vector shapes, Lissajous figures, and scan processed image and video inputs using audio signals sent directly to oscilloscopes, Vectrex game consoles, ILDA laser displays, or oscilloscope emulation softwares using the Pure Data programming environment. 

Audio waveforms control the vertical and horizontal movements as well as the brightness of a single beam of light, tracing shapes, points and curves with a direct relationship between sound and image.

The technique is based on the well-known principle of Lissajous figures, which are a mathematical representation of complex harmonic motion. Originally displayed by reflecting light between mirrors attached to a pair of vibrating tuning forks, we are most used to seeing them on the screen of an oscilloscope, where they can be produced using pairs of electronic oscillators tuned to specific ratios. 

There is a wealth of such experiments from the 1950s onward by major figure such as Mary Ellen Bute, John Whitney, Larry Cuba, Manfred Mohr, Nam June Paik, Ben Laposky, Bill Etra, Gary Hill, and Steina & Woody Vasulka, which were all highly inspiration to the development of this library.

Tutorials, announcements, and testing here: 

https://www.facebook.com/groups/vectorsynthesis/

Demo videos here: 

https://vimeo.com/macumbista

 If this library has been useful, please consider making a donation towards the development:
 
 [![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=SPHWJSJWH92GG&source=url)
 
 Or you can support my research by ordering a copy of the Vector Synthesis book: 
 
 http://www.lulu.com/shop/derek-holzer/vector-synthesis-a-media-archaeological-investigation-into-sound-modulated-light/paperback/product-24379956.html
 
 You can also take a workshop from me. My workshops are annouced on the Facebook group above or on my website: 
 
 http://macumbista.net 
 

*REQUIREMENTS*

——SOFTWARE
	
	Pure Data "Vanilla", version 0.49 or newer: 

https://puredata.info/downloads/pure-data

	Gem 0.93.3 (OPTIONAL, used in scan processor only). 
	Gem is installed via deken, Pd’s externals manager (Menu bar: Help-->Find Externals)
	
	NOTE: Pd-Extended is too old for some features of this library. Do not rely on it.
	Purr-Data is also not explicitely supported.
	
——AUDIO INTERFACE
	
	DC-coupled audio interface: 

https://www.sweetwater.com/sweetcare/articles/which-audio-interfaces-are-dc-coupled/#dc-coupled-interfaces
	
	Minimum 3 output channels (horizontal, vertical, brightness)
	5 output channels recommended if seperate stereo audio channels are desired
	6 balanced audio outputs recommended for ILDA laser control 
	8 balanced audio outputs recommended for ILDA plus seperate stereo audio
	High sampling rate also recommended (192 kHz if possible)
	Tested with MOTU UltraLite mk3 USB2 audio interface (Ten DC coupled, balanced outputs)
	
——DISPLAYS
	
	Oscilloscope or vector monitor (not vectorscope!) with X/Y/Z inputs (all DC-coupled):

https://web.archive.org/web/20190825120849/http://vectorvgapro.com/XY_Displays.html
	
	—or—
	
	Vectrex game console modified for X/Y/Z input (all DC-coupled) according to these instructions:

http://users.sussex.ac.uk/~ad207/adweb/assets/vectrexminijackinputmod2014.pdf

	I also recommend modifying the Vectrex to disable the so-called "spot killer", which is 
	a safety feature designed to prevent burning a spot in the phosphor of the Cathode Ray 
	Tube of your Vectrex. Unfortunately, this spot killer is quite conservative and tends to 
	shut down your image if the frequency and/or amplitude of the XY signals are too small. 
	Disabling the spot killer is simply a matter of bridging two pins of a transistor on the 
	CRT driver board, as shown in the following image:

https://github.com/macumbista/vectorsynthesis/blob/master/spot%20killer%20mod.JPG

	Instead of the solder bridge shown, I recommend using a switch rated for at least 110V. 
	In such case, *enable* the spot killer (switch open) when powering up and powering down 
	the Vectrex as well as for normal game play, and *disable* (switch closed) the spot killer 
	when using the Vectrex for audio-driven graphics. 
	
	NOTE: no matter how careful you are, there is still a good chance you will make a small 
	mark in the phosphor. You have been warned.
	
	—or—
	
	ILDA laser display with the following adapter from your minimum 6 channel, DC coupled 
	audio interface with balanced outputs (recommended: MOTU UltraLite) and the following 
	DIY adapter box: 

https://github.com/ffd8/dac_ilda 
	
	—or—
	
	Oscilloscope software with X/Y/Z inputs such as Hansi Raber's "Oscilloscope!" app

https://github.com/kritzikratzi/Oscilloscope/releases/tag/1.0.9
	
	(Hold SHIFT key when selecting input for third channel brightness control)
	plus audio loopback application such as SoundFlower, BlackHole or Virtual Audio Cable. 
	Please see SOFTWARE-OSCILLOSCOPE-TUTORIAL-MAC.pdf for MacOS and 
	SOFTWARE-OSCILLOSCOPE-TUTORIAL-WIN.pdf for Windows for further details on setup.
	
	NOTE: the Z axis should control the brightness of the beam, not 3D depth
	

*GENERAL NOTES*

	Start with the first files in the library, they are the tutorials:
	
	000.A.VECTOR_GENERATORS.pd
	000.A1.VECTOR_GENERATORS-ILDA.pd
	000.B.2D_VECTORS.pd
	000.B1.2D_VECTORS-ILDA.pd
	000.C.3D_VECTORS.pd
	000.C1.3D_VECTORS-ILDA.pd
	000.D.VECTOR_MODIFIERS.pd
	000.D1.VECTOR_MODIFIERS-ILDA.pd
	000.G.VECTOR_MULTIPLEXING.pd
	000.G1.VECTOR_MULTIPLEXING-ILDA.pd
	000.H.ILDA_OUTPUT.pd
	000.I.PRESET_SYSTEM.pd
	000.I1.PRESET_SYSTEM-ILDA.pd
	
	All the ILDA patches require 000.H.ILDA_OUTPUT.pd to be open and an ILDA laser to be connected. 
		
	The files with "gui" in their name are designed to be patched together much like a modular synth.
	The files with "help" in their name are good examples to start with to learn more code. 
	The files without "gui" or "help" in their name are the abstractions themselves, without any controls.
	The files with a ".txt" extension are backup data for the various 3D shapes.
	
	
	For control of an oscilloscope, the following channels are used (where Audio Left and Right can be reassigned):

	Audio Interface Output 1 : Horizontal
	Audio Interface Output 2 : Vertical
	Audio Interface Output 3 : Brightness
	Audio Interface Output 4 : Audio Left (Horizontal * Brightness)
	Audio Interface Output 5 : Audio Right (Vertical * Brightness)
	
	For ILDA laser control, the channel assignement looks like this (where Audio Left and Right can be reassigned):
	
	Audio Interface Output 1 : Horizontal
	Audio Interface Output 2 : Vertical
	Audio Interface Output 3 : Brightness (normally not used, kept for compatibility)
	Audio Interface Output 4 : Red
	Audio Interface Output 5 : Green
	Audio Interface Output 6 : Blue
	Audio Interface Output 7 : Audio Left (Horizontal * Brightness)
	Audio Interface Output 8 : Audio Right (Vertical * Brightness)

	Higher sampling rate = higher resolution/fewer errors in the vector shapes
	Tested at 44.1kHz, 48kHz, 96kHz, 192kHz


*USING NON-RECOMMENDED HARDWARE*

	A stereo audio output is also usable, as well as a more common X/Y oscilloscope display,
	however there will be no brightness control.
	
	Normal laptop headphone audio outputs generate a lot of noise which is visible in the image.
	One interesting note is that all Apple iPhone and iPad headphone outputs are DC coupled.
	
	An AC-coupled soundcard or display will show noticeable distortions in the shape, 
	and the vector shapes will always appear in the center of the screen.

	DC-coupling is also necessary for brightness control.

	Brightness control is essential for multiplexing, scan processing of videos and photos, 
	and a number of other interesting visual effects, however you can still use this 
	library for many things without it.
	
	DC COUPLING and SAMPLING RATE both affect the oscilloscope image. 
	
	Without DC COUPLING, your image will always try to stay centered on the screen.
	If the shape you are drawing is irregularly sized, this can cause a lot of unwanted motion.
	
	And the lower your SAMPLING RATE is (44.1 or 48 kHz instead of 96 or 192 kHz), the more
	difficult it will be to draw shapes with sharp corners. You will see rounded corners and 
	often overshoots due to aliasing errors at these lower sampling rates.
	
[![](http://img.youtube.com/vi/piZPIMYfq0c/0.jpg)](http://www.youtube.com/watch?v=piZPIMYfq0c "Oscilloscope Music Tutorial 2: Setup (Compression, DC-coupling, Sampling Rate, Aliasing by Jerobeam Fenderson)")


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
	Carsten Stabenow & Gesine Pagels
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
	and finally the Video Circuits online community, without whom I never would have started down 
	this crazy road


	Derek Holzer
	UPDATED Stockholm March 2021
	http://macumbista.net
	macumbista AT THE DOMAIN gmail DOT com
















# vectorsynthesis
