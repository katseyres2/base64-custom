myList = {
	"A": "00000",
	"B": "00001", 
	"C": "00010",
	"D": "00011",
	"E": "00100",
	"F": "00101",
	"G": "00110",
	"H": "00111",
	"I": "01000",
	"J": "01001",
	"K": "01010",
	"L": "01011",
	"M": "01100",
	"N": "01101",
	"O": "01110",
	"P": "01111",
	"Q": "10000",
	"R": "10001",
	"S": "10010",
	"T": "10011",
	"U": "10100",
	"V": "10101",
	"W": "10110",
	"X": "10111",
	"Y": "11000",
	"Z": "11001",
	"a": "11010",
	"b": "11011",
	"c": "11100",
	"d": "11101",
	"e": "11110",
	"f": "11111",
}

message = "KREEGTaOPNRDIcbFGYaFeMLTLcaHOMbTGBWWKXbJNZXGSdDd"
quintuplets = []
quintupletsJoined = ""
decoded = ""

for letter in message:
	quintuplets.append(myList[letter])
	quintupletsJoined += myList[letter]

for idx in range(0, len(quintupletsJoined), 8):
	print(quintupletsJoined[idx:idx+8])
