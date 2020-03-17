# Text-recognition

This is my attempt to write a text recognition program without using any specialized libraries for this purpose.

The aim was not to write adaptive to any font and size program but to apply supervised machine learning algorithm to 
this (600 dpi.png) specific example and master NumPy.

Steps:
1) Upload image in grayscale and get an array of arrays(lines) of "0" - black pixels; "255" - white pixels.
2) Split an array into "rows" (find starting and ending index of consecutive lines where black pixels exist)
3) Split "rows" into characters (same as the previous step)

Here supervised machine learning begins
The dictionary where we store our learning results structured as follows: {shape_of_character: [character(text), character(array)], ...}
	
4) iterate through every character, find the ones shape and compare it with keys in the dictionary
if the same key exists:
- iterate through every value in this key and
- subtract array(we are looking for) from  array(in dictionary)
- the subtraction transform values as follows: 
																	 0 - 0 -> 0 (match of black pixels)
																	255 - 255 -> 0 (match of white pixels)
																	255 - 0 -> 255 (pixels do not match)
																	0 - 255 -> 100 (pixels do not match)
																	
- calculate the control_sum of resulting array & fraction = (pixels that do not match) / (pixels that match)
	We calculate those indicators to avoid over/underfitting and choose the best result if there are multiple
- the corresponding character is found - concatenate it to the "text" variable
				
5) if the same key does not exist:
- Show character
- Ask to input the character
- Add information to the dictionary
								
To witness the learning process run "learning_example.py" and type at least 3-4 lines of text
When character is found - two or more figures appear and you can see the subtraction result of image we are looking for and those in the dictionary
				
