# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:28:10 2022

@author: matan shemesh nimetz
"""

import winsound
class exInstrument(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)
        
class Instrument():
	"""This super class manage the basic instrument data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		self._brand = input("Enter the new instrument's brand : ")
		self._model = input("Enter the new instrument's model : ")
		self._color = input("Enter the new instrument's color : ")
		self._weight = float(input("Enter the new instrument's weight (in KG) : "))
		self._year = int(input("Enter the new instrument's year (from 1900-2022) : "))
		if (self._year<1900 or self._year>2022):
		 raise exInstrument("the year is invalid")
		self._price = float(input("Enter the new instrument's price (in shekel) : "))
		if (self._price<0):
		 raise exInstrument("the price can't be a negative number")
		self._CatalogNumber = input("Enter the new instrument's catalog number (can contain letters and numbers) : ")
#this function strings all the data into a string value and returns it
	def GetInstrument(self):
		s ="Instrument's data : \n"
		s = s +	"Brand : "+" "+self._brand+"\n"
		s = s +	"Model : "+" "+self._model+"\n"
		s = s +	"Color : "+" "+self._color+"\n"
		s = s +	"Weight : "+" "+str(self._weight)+" "+ "KG\n"
		s = s +	"Year : "+" "+str(self._year)+"\n"
		s = s +	"Price : "+" "+str(self._price) +" "+ "shekel\n"
		s = s +	"Catalog number : "+" "+self._CatalogNumber+"\n"
		return s
#this is a repr use for getting a basic information
	def __repr__(self):
		return "Instrument's brand: "+self._brand + "," +" "+ "Instrument's price: " +str(self._price)
#this is a str use for getting a basic information
	def __str__(self):
		return "Instrument's brand: "+self._brand + "," +" "+ "Instrument's catalog number: " +str(self._CatalogNumber)


        
class exStringed(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Stringed(Instrument):
	"""This instument sub class manage the basic stringed instrument data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Stringed,self).__init__()
		self._NumOfStrings = int(input("Enter Number of strings : "))
		if(self._NumOfStrings < 0 or self._NumOfStrings > 12):
			raise exStringed("the number of stirngs is invalid")
#this function strings all the data into a string value and returns it
	def GetStringed(self):
		s =Instrument.GetInstrument(self)
		s = s +"Number of strings : "+" "+str(self._NumOfStrings)+"\n"
		return s
#this repr returns a basic information
	def __repr__(self):
		return Instrument.__repr__(self)+ "," +" " +"Number of strings:"+" "+str(self._NumOfStrings)
#this  str returns a basic information
	def __str__(self):
		return Instrument.__str__(self)+ "," +" " +"Number of strings:"+" "+str(self._NumOfStrings)

        
class exBow(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Bow(Stringed):
	"""This class manage the bow instrument data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Bow,self).__init__()
		tiny="1/4"
		small="1/2"
		medium="3/4"
		large="4/4"
		self._size = input("Enter size (1/4, 1/2, 3/4, 4/4) : ")
		if((self._size.casefold()).__eq__(tiny.casefold())):
			pass
		elif ((self._size.casefold()).__eq__(small.casefold())):
			pass
		elif ((self._size.casefold()).__eq__(medium.casefold())):
			pass
		elif ((self._size.casefold()).__eq__(large.casefold())):
			pass
		else:
			raise exBow("the size is invalid")
#this function strings all the data into a string value and returns it
	def GetBow(self):
		s =Stringed.GetStringed(self)
		s = s +"The size is : "+" "+self._size+"\n"
		return s
#this  repr returns a basic information
	def __repr__(self):
		return Stringed.__repr__(self)+ "," +" " +"The size is:"+" "+self._size
##this  str returns a basic information
	def __str__(self):
		return Stringed.__str__(self)+ "," +" " +"The size is:"+" "+self._size
        
class exViolin(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Violin(Bow):
	"""This bow sub class manage the violin data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Violin,self).__init__()
		type1="wood"
		type2="plastic"
		self._ChinRestType = input("Enter chin rest type (Plastic or Wood) : ")
		if((self._ChinRestType.casefold()).__eq__(type1.casefold())):
			pass
		elif ((self._ChinRestType.casefold()).__eq__(type2.casefold())):
			pass
		else:
			raise exViolin("the chin rest type you entered is invalid")
		print("Violin was constructed!")
#this function strings all the data into a string value and returns it
	def GetViolin(self):
		s ="*****************************************:\n"
		s = s +"Violin: \n"
		s = s +Bow.GetBow(self)
		s = s +"The chin type is : "+" " +self._ChinRestType+"\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("Violin", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		  return self.GetViolin()
#this is an str returns a basic information
	def __str__(self):
		return Bow.__str__(self)+ "," +" " +"Chin rest type:"+" "+str(self._ChinRestType)
        

class exCello(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Cello(Bow):
	"""This bow sub class manage the cello data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Cello,self).__init__()
		tailtype1="wood"
		tailtype2="plastic"
		tailtype3="metal"
		self._TailPieceType = input("Enter tail piece type (Plastic ,Wood or metal) : ")
		if((self._TailPieceType.casefold()).__eq__(tailtype1.casefold())):
			pass
		elif ((self._TailPieceType.casefold()).__eq__(tailtype2.casefold())):
			pass
		elif ((self._TailPieceType.casefold()).__eq__(tailtype3.casefold())):
			pass
		else:
			raise exCello("the tail piece type you entered is invalid")
		print("Cello was constructed!")
#this function strings all the data into a string value and returns it
	def GetCello(self):
		s ="*****************************************:\n"
		s = s +"Cello: \n"
		s = s +Bow.GetBow(self)
		s = s +"The tail piece type is : "+" " +self._TailPieceType+"\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("Cello", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		return self.GetCello()
#this str returns a basic information
	def __str__(self):
		return Bow.__str__(self)+ "," +" " +"Tail piece type:"+" "+self._TailPieceType
        

class exViola(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Viola(Bow):
	"""This bow sub class manage the viola data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Viola,self).__init__()
		self._BodyLength = int(input("Enter Body length (from 30 to 46 cm) : "))
		if(self._BodyLength < 30 or self._BodyLength > 46):
			raise exViola("the body-length is invalid")
		print("Viola was constructed!")
#this function strings all the data into a string value and returns it
	def GetViola(self):
		s ="*****************************************:\n"
		s = s +"Viola: \n"
		s = s +Bow.GetBow(self)
		s = s +"The body length is : "+" " +str(self._BodyLength) +" " +"cm\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("Viola", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		return self.GetViola()
#this str returns a basic information
	def __str__(self):
		return Bow.__str__(self)+ "," +" " +"Body length:"+" "+str(self._BodyLength)+" "+"cm"
        
class exContrabass(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Contrabass(Bow):
	"""This bow sub class manage the contrabass data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Contrabass,self).__init__()
		bowtype1="french"
		bowtype2="german"
		self._BowType = input("Enter the bow type (french or german) : ")
		if((self._BowType.casefold()).__eq__(bowtype1.casefold())):
			pass
		elif ((self._BowType.casefold()).__eq__(bowtype2.casefold())):
			pass
		else:
			raise exContrabass("the chin rest type you entered is invalid")
		print("Contrabass was constructed!")
#this function strings all the data into a string value and returns it
	def GetContrabass(self):
		s ="*****************************************:\n"
		s = s +"Contrabass: \n"
		s = s +Bow.GetBow(self)
		s = s +"The bow type is : "+" " +self._BowType+"\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("Contrabass", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		return self.GetContrabass()
#this str returns a basic information
	def __str__(self):
		return Bow.__str__(self)+ "," +" " +"Bow type:"+" "+self._BowType
        
class exGuitar(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Guitar(Stringed):
	"""This stringed sub class manage the basic guitar data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Guitar,self).__init__()
		wood1="alder"
		wood2="mahogany"
		wood3="cedar"
		wood4="ash"
		self._TypeOfWood = input("Enter type of wood (alder, mahogany, cedar or ash) : ")
		if((self._TypeOfWood.casefold()).__eq__(wood1.casefold())):
			pass
		elif ((self._TypeOfWood.casefold()).__eq__(wood2.casefold())):
			pass
		elif ((self._TypeOfWood.casefold()).__eq__(wood3.casefold())):
			pass
		elif ((self._TypeOfWood.casefold()).__eq__(wood4.casefold())):
			pass
		else:
			raise exGuitar("the type of wood is invalid")
#this function strings all the data into a string value and returns it
	def GetGuitar(self):
		s =Stringed.GetStringed(self)
		s = s +"The wood type is : "+" "+self._TypeOfWood+"\n"
		return s
#this repr returns a basic information
	def __repr__(self):
		return Stringed.__repr__(self)+ "," +" " +"Wood type:"+" "+str(self._TypeOfWood)
#this str returns a basic information
	def __str__(self):
		return Stringed.__str__(self)+ "," +" " +"Wood type:"+" "+str(self._TypeOfWood)
        
class exBass(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Bass(Guitar):
	"""This guitar sub class manage the bass guitar data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Bass,self).__init__()
		neckwood1="maple"
		neckwood2="rosewood"
		self._TypeOfNeckWood = input("Enter type of neck wood (maple or rosewood) : ")
		if((self._TypeOfNeckWood.casefold()).__eq__(neckwood1.casefold())):
			pass
		elif ((self._TypeOfNeckWood.casefold()).__eq__(neckwood2.casefold())):
			pass
		else:
			raise exBass("the type of neck wood is invalid")
		print("Bass-Guitar was constructed!")
#this function strings all the data into a string value and returns it
	def GetBass(self):
		s ="*****************************************:\n"
		s = s +"Bass Guitar:\n"
		s = s +Guitar.GetGuitar(self)
		s = s +"The neck wood type is : "+" " +self._TypeOfNeckWood+"\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("BassGuitar", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		return self.GetBass()
#this str returns a basic information
	def __str__(self):
		return Guitar.__str__(self)+ "," +" " +"Neck wood type:"+" "+self._TypeOfNeckWood
        
class exAccustic(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Accustic(Guitar):
	"""This guitar sub class manage the accustic guitar data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Accustic,self).__init__()
		t="true"
		f="false"
		self._IsElectric = input("Is this accustic electric? (enter true or false): ")
		if((self._IsElectric.casefold()).__eq__(t.casefold())):
			self._IsElectric=True
		elif ((self._IsElectric.casefold()).__eq__(f.casefold())):
			self._IsElectric=False
		else:
			raise exAccustic("the answer is invalid")
		print("Accustic-Guitar was constructed!")
#this function strings all the data into a string value and returns it
	def GetAccustic(self):
		s ="*****************************************:\n"
		s = s +"Accustic Guitar:\n"
		s = s +Guitar.GetGuitar(self)
		s = s +"This accustic guitar is electric: "+" " +str(self._IsElectric)+"\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("AccusticGuitar", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		return self.GetAccustic()
#this str returns a basic information
	def __str__(self):
		return Guitar.__str__(self)+ "," +" " +"is electric:"+" "+str(self._IsElectric)
        
class exClassic(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Classic(Guitar):
	"""This guitar sub class manage the classic guitar data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Classic,self).__init__()
		self._SizeHole = int(input("Enter the size of the guitar hole (from 40 to 60 cm): "))
		if(self._SizeHole < 40 or self._SizeHole > 60):
			raise exViola("the guitar-hole is invalid")
		print("Classic-Guitar was constructed!")
#this function strings all the data into a string value and returns it
	def GetClassic(self):
		s ="*****************************************:\n"
		s = s +"Classic Guitar:\n"
		s = s +Guitar.GetGuitar(self)
		s = s +"The hole size is : "+" " +str(self._SizeHole) +" " + "cm\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("ClassicGuitar", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		return self.GetClassic()
#this str returns a basic information
	def __str__(self):
		return Guitar.__str__(self)+ "," +" " +"Size of guitar hole:"+" "+str(self._SizeHole)
        
class exElectric(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Electric(Guitar):
	"""This guitar sub class manage the electric guitar data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Electric,self).__init__()
		single="single-coil"
		humb="humbucker"
		self._PickUpType = input("Enter the pick-up type (single-ciol or humbucker): ")
		if((self._PickUpType.casefold()).__eq__(single.casefold())):
			pass
		elif ((self._PickUpType.casefold()).__eq__(humb.casefold())):
			pass
		else:
			raise exElectric("the type of the pick-up is invalid")
		print("Electric-Guitar was constructed!")
#this function strings all the data into a string value and returns it
	def GetElectric(self):
		s ="*****************************************:\n"
		s = s +"Electric Guitar:\n"
		s = s +Guitar.GetGuitar(self)
		s = s +"The pick-up is : "+" " +self._PickUpType+ "\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("ElectricGuitar", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		return self.GetElectric()
#this str returns a basic information
	def __str__(self):
		return Guitar.__str__(self)+ "," +" " +"Pick-up type:"+" "+self._PickUpType

class exWind(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Wind(Instrument):
	"""This instrument sub class manage the basic wind instrument data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Wind,self).__init__()
		material1="metal"
		material2="wood"
		self._material = (input("Enter the wind instrument's material (metal or wood) : "))
		if((self._material.casefold()).__eq__(material1.casefold())):
			pass
		elif ((self._material.casefold()).__eq__(material2.casefold())):
			pass
		else:
			raise exWind("the material is invalid")
#this function strings all the data into a string value and returns it
	def GetWind(self):
		s =Instrument.GetInstrument(self)
		s = s +"The wind instrument's material : "+" "+self._material+"\n"
		return s
#this repr returns a basic information
	def __repr__(self):
		return Instrument.__repr__(self)+ "," +" " +"Material type:"+" "+self._material
#this str returns a basic information
	def __str__(self):
		return Instrument.__str__(self)+ "," +" " +"Material type:"+" "+self._material
        
class exTrumpet(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Trumpet(Wind):
	"""This wind sub class manage the trumpet data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Trumpet,self).__init__()
		Tr="true"
		Fa="false"
		self._HasMute = input("Is this trumpet has mute mode? (enter true or false): ")
		if((self._HasMute.casefold()).__eq__(Tr.casefold())):
			self._HasMute=True
		elif ((self._HasMute.casefold()).__eq__(Fa.casefold())):
			self._HasMute=False
		else:
			raise exTrumpet("the answer is invalid")
		print("Trumpet was constructed!")
#this function strings all the data into a string value and returns it
	def GetTrumpet(self):
		s ="*****************************************:\n"
		s = s +"Trumpet:\n"
		s = s +Wind.GetWind(self)
		s = s +"This trumpet has a mute mode : "+" " +str(self._HasMute)+"\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("Trumpet", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		return self.GetTrumpet()
#this str returns a basic information
	def __str__(self):
		return Wind.__str__(self)+ "," +" " +"has mute mode:"+" "+str(self._HasMute)
        
class exSaxophone(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Saxophone(Wind):
	"""This wind sub class manage the saxophone data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Saxophone,self).__init__()
		s="soprano"
		a="alto"
		t="tenor"
		b="baritone"
		self._Range = input("Enter the range (soprano, alto, tenor or baritone  ): ")
		if((self._Range.casefold()).__eq__(s.casefold())):
			pass
		elif ((self._Range.casefold()).__eq__(a.casefold())):
			pass
		elif ((self._Range.casefold()).__eq__(t.casefold())):
			pass
		elif ((self._Range.casefold()).__eq__(b.casefold())):
			pass
		else:
			raise exSaxophone("the range is invalid")
		print("Saxophone was constructed!")
#this function strings all the data into a string value and returns it
	def GetSaxophone(self):
		s ="*****************************************:\n"
		s = s +"Saxophone:\n"
		s = s +Wind.GetWind(self)
		s = s +"The range is : "+" " +self._Range+"\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("Saxophone", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		return self.GetSaxophone()
#this str returns a basic information
	def __str__(self):
		return Wind.__str__(self)+ "," +" " +"Range:"+" "+self._Range
        
class exFlute(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Flute(Wind):
	"""This wind sub class manage the flute data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Flute,self).__init__()
		S="silver"
		G="gold"
		self._MouthPieceCover = input("Enter the mouth piece cover (silver or gold): ")
		if((self._MouthPieceCover.casefold()).__eq__(S.casefold())):
			pass
		elif ((self._MouthPieceCover.casefold()).__eq__(G.casefold())):
			pass
		else:
			raise exFlute("the cover is invalid")
		print("Flute was constructed!")
#this function strings all the data into a string value and returns it
	def GetFlute(self):
		s ="*****************************************:\n"
		s = s +"Flute:\n"
		s = s +Wind.GetWind(self)
		s = s +"The mouth piece cover is : "+" "+ self._MouthPieceCover+"\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("Flute", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		return self.GetFlute()
#this str returns a basic information
	def __str__(self):
		return Wind.__str__(self)+ "," +" " +"Mouth piece cover:"+" "+self._MouthPieceCover

class exKeyboard(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Keyboard(Instrument):
	"""This instrument sub class manage the basic wind instrument data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Keyboard,self).__init__()
		self._NumOfKeys = int(input("Enter Number of keys (from 70 to 97) : "))
		if(self._NumOfKeys < 70 or self._NumOfKeys > 97):
			raise exKeyboard("the number of keys is invalid")
#this function strings all the data into a string value and returns it
	def GetKeyboard(self):
		s =Instrument.GetInstrument(self)
		s = s +"Number of keys : "+" "+str(self._NumOfKeys)+"\n"
		return s
#this repr returns a basic information
	def __repr__(self):
		return Instrument.__repr__(self)+ "," +" " +"Number of keys:"+" "+str(self._NumOfKeys)
#this str returns a basic information
	def __str__(self):
		return Instrument.__str__(self)+ "," +" " +"Number of keys:"+" "+str(self._NumOfKeys)
        
class exOrgan(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Organ(Keyboard):
	"""This keyboard sub class manage the organ data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Organ,self).__init__()
		self._NumOfEffects = int(input("Enter Number of sound effects (from 88 to 10,000) : "))
		if(self._NumOfEffects < 88 or self._NumOfEffects > 10000):
			raise exOrgan("the number of sound effects is invalid")
		print("Organ was constructed!")
#this function strings all the data into a string value and returns it
	def GetOrgan(self):
		s ="*****************************************:\n"
		s = s +"Organ:\n"
		s = s +Keyboard.GetKeyboard(self)
		s = s +"Number of effects : "+" "+str(self._NumOfEffects)+"\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("Organ", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		 return self.GetOrgan()
#this str returns a basic information
	def __str__(self):
		return Keyboard.__str__(self)+ "," +" " +"Number of effects:"+" "+str(self._NumOfEffects)
        
class exPiano(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Piano(Keyboard):
	"""This keyboard sub class manage the piano data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Piano,self).__init__()
		T="true"
		F="false"
		self._IsGrand = input("Is this piano grand? (enter true or false): ")
		if((self._IsGrand.casefold()).__eq__(T.casefold())):
			self._IsGrand=True
		elif ((self._IsGrand.casefold()).__eq__(F.casefold())):
			self._IsGrand=False
		else:
			raise exPiano("the answer is invalid")
		print("Piano was constructed!")
#this function strings all the data into a string value and returns it
	def GetPiano(self):
		s ="*****************************************:\n"
		s = s +"Piano:\n"
		s = s +Keyboard.GetKeyboard(self)
		s = s +"This piano is a grand piano :" +" "+str(self._IsGrand)+"\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("Piano", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		 return self.GetPiano()
#this str returns a basic information
	def __str__(self):
		return Keyboard.__str__(self)+ "," +" " +"is it a grand piano:"+" "+str(self._IsGrand)

class exPercussion(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Percussion(Instrument):
	"""This instrument sub class manage the basic percussion instrument data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Percussion,self).__init__()
		self._NumOfSticks = int(input("Enter Number of sticks (1 or 2) : "))
		if(self._NumOfSticks < 1 or self._NumOfSticks > 2):
			raise exPercussion("the number of sticks is invalid")
#this function strings all the data into a string value and returns it
	def GetPercussion(self):
		s =Instrument.GetInstrument(self)
		s = s +"Number of sticks : "+" "+str(self._NumOfSticks)+"\n"
		return s
#this repr returns a basic information
	def __repr__(self):
		return Instrument.__repr__(self)+ "," +" " +"Number of sticks:"+" "+str(self._NumOfSticks)
#this str returns a basic information
	def __str__(self):
		return Instrument.__str__(self)+ "," +" " +"Number of sticks:"+" "+str(self._NumOfSticks)
        
class exDrums(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)
class Drums(Percussion):
	"""This percussion sub class manage the drums data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Drums,self).__init__()
		self._DrumheadWidth = int(input("Enter the drumhead width (from 9-12 inch) : "))
		if(self._DrumheadWidth < 9 or self._DrumheadWidth > 12):
			raise exDrums("the drumhead range is invalid")
		print("Drums were constructed!")
#this function strings all the data into a string value and returns it
	def GetDrums(self):
		s ="*****************************************:\n"
		s = s +"Drums: \n"
		s = s +Percussion.GetPercussion(self)
		s = s +"The drumhead width is : "+" "+str(self._DrumheadWidth)+" "+ "inch\n"
		s = s +"*****************************************:\n"
		return s
#this function activates a wav file, the instrument sound
	def Play(self):
		winsound.PlaySound("Drums", winsound.SND_FILENAME)
#this repr use for returning the information above
	def __repr__(self):
		return self.GetDrums()
#this str returns a basic information
	def __str__(self):
		return Percussion.__str__(self)+ "," +" " +"The drumhead range:"+" "+str(self._DrumheadWidth)+" "+"inch"

class exHandling(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Handling():
	"""This super class manage the basic instrument handling data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		self._Cost = float(input("Enter the handling cost (in shekel) : "))
		if(self._Cost <=0 ):
			raise exHandling("the number is invalid, you cant handle for free")
#this function print the handling cost
	def printHandling(self):
		print("The handling cost is : ",self._Cost ,"shekel")
#this repr returns the handling cost
	def __repr__(self):
		return "The cost is:"+" "+str(self._Cost)+" "+"shekel"
#this str returns the handling cost
	def __str__(self):
		return "The cost is:"+" "+str(self._Cost)+" "+"shekel"
    
class exSetup(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Setup(Handling):
	"""This handling sub class manage the setup data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Setup,self).__init__()
		self._ActionHeight = float(input("Enter the action height to setup (from 1 to 2.7 mm) : "))
		if(self._ActionHeight < 1 or self._ActionHeight>2.7):
			raise exSetup("the height is invalid")
#this function print the setup data
	def printSetup(self):
		print("*************************")
		print("Setup information: ")
		Handling.printHandling(self)
		print("The setted up action height is : ",self._ActionHeight ,"mm")
		print("*************************")
#this repr returns the basic handling information
	def __repr__(self):
		return Handling.__repr__(self)+ "," +" " +"Setted up action height :"+" "+str(self._ActionHeight)+" "+"mm"
#this str returns the basic handling information
	def __str__(self):
		return Handling.__repr__(self)+ "," +" " +"Setted up action height :"+" "+str(self._ActionHeight)+" "+"mm"
    
class exChangeStrings(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class ChangeStrings(Handling):
	"""This handling sub class manage the string changing data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(ChangeStrings,self).__init__()
		self._NumOfChangeStrings = int(input("Enter the number of string to change (from 1 to 12) : "))
		if(self._NumOfChangeStrings < 1 or self._NumOfChangeStrings>12):
			raise exChangeStrings("the number of strings is invalid")
#this function print the string changing data
	def printChangeStrings(self):
		print("*************************")
		print("Changing strings information: ")
		Handling.printHandling(self)
		print("The number of strings that were changed: ",self._NumOfChangeStrings)
		print("*************************")
#this repr returns the basic handling information
	def __repr__(self):
		return Handling.__repr__(self)+ "," +" " +"The number of changed strings:"+" "+str(self._NumOfChangeStrings)
#this str returns the basic handling information
	def __str__(self):
		return Handling.__repr__(self)+ "," +" " +"The number of changed strings:"+" "+str(self._NumOfChangeStrings)
    
class exRepair(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class Repair(Handling):
	"""This handling sub class manage the repairing data and methonds"""
#this is a constructor thats gets all the information from the user
	def __init__(self):
		super(Repair,self).__init__()
		self._Length = float(input("Enter the repairing time (in hour) : "))
		if(self._Length <=0):
			raise exRepair("the number is invalid")
#this function print the reparing data
	def printRepair(self):
		print("*************************")
		print("Repairing information: ")
		Handling.printHandling(self)
		print("The repairing took: ",self._Length,"-","hr")
		print("*************************")
#this repr returns the basic handling information
	def __repr__(self):
		return Handling.__repr__(self)+ "," +" " +"Repairing time:"+" "+str(self._Length)+" "+"hr"
#this str returns the basic handling information
	def __str__(self):
		return Handling.__repr__(self)+ "," +" " +"Repairing time:"+" "+str(self._Length)+" "+"hr"

class exMusicStore(Exception):
	"""This class manage the exception handling"""
#this is the constructor
	def __init__(self,str):
		self._desc=str
#this function prints the exception message
	def printException(self):
		print(self._desc)

class MusicStore():
	"""This music store class (container class) manage all music store data and methonds"""
#this is a constructor thats has the container data members
	def __init__(self,n="Music-Center"):
		self._name=n
		self._AllInstruments=[]
		self._CashFlow=0
		self._NumOfSelles=0
#this function strings all the data into a string value and returns it
	def GetStoreData(self):
		s = "======================================================================================\n"
		s = s +	"The business name is: " + self._name + "\n"
		s = s + "--------------------------------\n\n"
		s = s + "Amount of instruments:\n"
		s = s + "~~~~~~~~~~~~~~~~~~~~~~\n\n"
		if(len(self._AllInstruments)==0):
			s = s + "The store doesn't have any instruments!\n"
		s = s + "There are" +" "+ str(len(self._AllInstruments)) +" "+ "instruments in the store.\n"
		s = s + "------------------------------\n"
		if (self._CashFlow<=0):
			s = s + "The store dosen't have any money!\n"
		else:
			s = s + "The cash-flow of the store is: " +" "+ str(self._CashFlow) +" "+ "shekel.\n"
		s = s + "------------------------------\n"
		s = s + str(self._NumOfSelles) +" "+ "sales were made in the store.\n"
		s = s + "------------------------------\n"
		if(len(self._AllInstruments)==0):
			s = s + "There are no instruments information to print!\n"
		else:
			s = s + "Instrument list:\n"
			s = s + "~~~~~~~~~~~~~~~~~\n\n"
			s = s + str(self._AllInstruments).strip('[]')
		return s
#this function prints all the store data to the screen
	def PrintStoreData(self):
		print(self.GetStoreData())
#this repr returns all store data
	def __repr__(self):
		return repr(self.GetStoreData())
#this function inserts a new instrument to the list
	def insert(self,I):
		self._AllInstruments.append(I)
		print("an instrument was inserted succesfully!")
#this function Sort all the instruments in ascending order based on price
	def ascendingOrderPrice(self):
		self._AllInstruments.sort(key=lambda x: x._price)
#this function Sort all the instruments in descending order based on price
	def descendingOrderPrice(self):
		self._AllInstruments.sort(key=lambda x: x._price, reverse=True)
#this function Sort all the instruments in ascending order based on year
	def ascendingOrderYear(self):
		self._AllInstruments.sort(key=lambda y: y._year)
#this function Sort all the instruments in descending order based on year
	def descendingOrderYear(self):
		self._AllInstruments.sort(key=lambda y: y._year, reverse=True)
#this function delets an object(instrument) from the list
	def __delitem__(self,index):
		del self._AllInstruments[index]
#this function updating an instruments price
	def __setitem__(self,I,price):
		I._price=price
		print("The price was updated succesfully!")
#this function prints out a basic information of an instrument and his position in the list
	def __getitem__(self,index):
		print("This instrument is in ",str(index),"position in the instrument list of the store")
#this str returns the cash0flow details
	def __str__(self):
		return "The cash-flow stands on: "+" "+str(self._CashFlow)+" "+"shekel"
		print("")
#this function activates a sale by selected precent using map
	def sale(self,precent):
		def disc(self):
			self._price-=(self._price*precent)/100
		for i in map(disc, self._AllInstruments):
			print("")
		print("The products now are"+" "+str(precent)+"%  off")
#this function uses the handle class and his sub-classes, and activate the classes methods only is the instrument is a guitar object
	def handle(self):
		found=True
		print("Please select the handling type for your guitar: ")
		print("1) Setup")
		print("2) Change your strings")
		print("3) Repair")
		n=int(input("Please enter your choice: "))
		if(n==1):
			h=Setup()
			h.printSetup()
			self._CashFlow+=h._Cost
		elif(n==2):
			h=ChangeStrings()
			h.printChangeStrings()
			self._CashFlow+=h._Cost
		elif(n==3):
			h=Repair()
			h.printRepair()
			self._CashFlow+=h._Cost
		else:
			print("Wrong choice, please try again")
			print("")
			found=False
#this function saves all the store data to a text file
	def SaveToFile(self):
			T=open(input("Please enter the destination  file name (.txt): "), "w")
			print(self.GetStoreData(), file=T)
			T.close()

#this function activates the main menu
	def Menu(self):
		while(True):
			print("======================================================================================")
			print("Welcome to the",self._name)
			print("############################")
			print("")
			print("Main menu:")
			print("**********")
			print("1) Insert a new instrument to the system")
			print("2) Print all store data")
			print("3) Print store cash-flow")
			print("4) Print all the instruments in the store")
			print("5) Sort all the instruments in ascending order based on price")
			print("6) Sort all the instruments in descending order based on price")
			print("7) Sort all the instruments in ascending order based on year")
			print("8) Sort all the instruments in descending order based on year")
			print("9) Get the stock of an instrument category")
			print("10) Sell an instrument (based on catalog number)")
			print("11) Get an instrument's basic information and location in the list (based on catalog number)")
			print("12) Play an instrument (based on catalog number)")
			print("13) Make a disscount off all instrument's price in store")
			print("14) Edit an existing instrument's price (based on catalog number)")
			print("15) Handle a guitar from a client (this store support guitars only)")
			print("16) Jam session")
			print("17) Save all store data to a file")
			print("18) Exit")
			print("======================================================================================")
			print("")
			choice=int(input("Please enter your choice: "))
			print("")
			if(choice==1):
				found=True
				print("Please select the instrument catagory: ")
				print("***************************************")
				print("1) Percussion")
				print("2) Keyboard")
				print("3) Stringed")
				print("4) Wind")
				print("")
				subchoice1=int(input("Please enter your choice: "))
				print("")
				if(subchoice1==1):
					print("Please select the instrument:")
					print("1) Drums")
					print("")
					percussionchoice=int(input("Please select the instrument: "))
					if(percussionchoice==1):
						x=Drums()
					else:
						print("wrong choice, please try again!")
						print("")
						found=False
				elif(subchoice1==2):
					print("Please select the instrument:")
					print("1) Organ")
					print("2) Piano")
					print("")
					keyboardchoice=int(input("Please enter your choice: "))
					print("")
					if(keyboardchoice==1):
						x=Organ()
					elif(keyboardchoice==2):
						x=Piano()
					else:
						print("wrong choice, please try again!")
						print("")
						found=False
				elif(subchoice1==3):
					print("Please select the sub category:")
					print("1) Bow")
					print("2) Guitar")
					print("")
					stringedchoice=int(input("Please enter your choice: "))
					print("")
					if(stringedchoice==1):
						print("Please select the instrument:")
						print("1) Violin")
						print("2) Cello")
						print("3) Viola")
						print("4) Contrabass")
						print("")
						bowchoice=int(input("Please enter your choice: "))
						print("")
						if(bowchoice==1):
							x=Violin()
						elif(bowchoice==2):
							x=Cello()
						elif(bowchoice==3):
							x=Viola()
						elif(bowchoice==4):
							x=Contrabass()
						else:
							print("Wrong choice, please try again!")
							print("")
							found=False
					elif(stringedchoice==2):
						print("Please select the instrument:")
						print("1) Bass")
						print("2) Accustic")
						print("3) Classic")
						print("4) Electric")
						print("")
						guitarchoice=int(input("Please enter your choice: "))
						print("")
						if(guitarchoice==1):
							x=Bass()
						elif(guitarchoice==2):
							x=Accustic()
						elif(guitarchoice==3):
							x=Classic()
						elif(guitarchoice==4):
							x=Electric()
						else:
							print("Wrong choice, please try again!")
							print("")
							found=False
					else:
						print("Wrong choice, please try again!")
						print("")
						found=False
				elif(subchoice1==4):
					print("Please select the instrument:")
					print("1) Trumpet")
					print("2) Saxophone")
					print("3) Flute")
					print("")
					windchoice=int(input("Please enter your choice: "))
					print("")
					if(windchoice==1):
						x=Trumpet()
					elif(windchoice==2):
						x=Saxophone()
					elif(windchoice==3):
						x=Flute()
					else:
						print("wrong choice, please try again!")
						print("")
						found=False
				else:
					print("Wrong choice, please try again!")
					print("")
					found=False
				if found is True:
					self.insert(x)
			elif(choice==2):
				self.PrintStoreData()
			elif(choice==3):
				 print(self.__str__())
			elif(choice==4):
				if(len(self._AllInstruments)==0):
					print("There are no instruments in the store!")
					print("")
				else:
					print (str(self._AllInstruments).strip('[]'))
					print("")
			elif(choice==5):
				if(len(self._AllInstruments)==0):
					print("Can't sort because there are no instruments in the store!")
				else:
					self.ascendingOrderPrice()
					print("Done! print all the instruments again to see results.")
					print("")
			elif(choice==6):
				if(len(self._AllInstruments)==0):
					print("Can't sort because there are no instruments in the store!")
				else:
					self.descendingOrderPrice()
					print("Done! print all the instruments again to see results.")
					print("")
			elif(choice==7):
				if(len(self._AllInstruments)==0):
					print("Can't sort because there are no instruments in the store!")
				else:
					self.ascendingOrderYear()
					print("Done! print all the instruments again to see results.")
					print("")
			elif(choice==8):
				if(len(self._AllInstruments)==0):
					print("Can't sort because there are no instruments in the store!")
				else:
					self.descendingOrderYear()
					print("Done! print all the instruments again to see results.")
					print("")
			elif(choice==9):
				print("Please select the instrument catagory: ")
				print("***************************************")
				print("1) Percussion")
				print("2) Keyboard")
				print("3) Stringed")
				print("4) Wind")
				print("")
				subchoice9=int(input("Please enter your choice: "))
				print("")
				if(subchoice9==1):
					filtered1 = filter(lambda x: isinstance(x, Percussion), self._AllInstruments)
					print("There are",len(list(filtered1)),"percussion instruments in the store.")
					print("")
				elif(subchoice9==2):
					filtered2 = filter(lambda x: isinstance(x, Keyboard), self._AllInstruments)
					print("There are",len(list(filtered2)),"keyboard instruments in the store.")
					print("")
				elif(subchoice9==3):
					filtered3 = filter(lambda x: isinstance(x, Stringed), self._AllInstruments)
					print("There are",len(list(filtered3)),"stringed instruments in the store.")
					print("")
				elif(subchoice9==4):
					filtered4 = filter(lambda x: isinstance(x, Wind), self._AllInstruments)
					print("There are",len(list(filtered4)),"wind instruments in the store.")
					print("")
				else:
					print("Wrong choice, please try again!")
			elif(choice==10):
				i=input("Please enter the instrument's catalog number: ")
				found=False
				for instrument in self._AllInstruments:
					if(instrument._CatalogNumber==i):
						x=self._AllInstruments.index(instrument)
						self._CashFlow+=instrument._price
						self._NumOfSelles+=1
						self.__delitem__(x)
						print("Sold!")
						found=True
				if not found:
					print("This catalog number doesn't exit, please try again!")
			elif(choice==11):
				i=input("Please enter the instrument's catalog number: ")
				found=False
				for instrument in self._AllInstruments:
					if(instrument._CatalogNumber==i):
						x=self._AllInstruments.index(instrument)
						print("Basic information:")
						print("------------------")
						print(str(instrument))
						print("")
						print("Location details:")
						print("------------------")
						self.__getitem__(x)
						print("")
						found=True
				if not found:
						print("This catalog number doesn't exit, please try again!")
			elif(choice==12):
				i=input("Please enter the instrument's catalog number: ")
				found=False
				for instrument in self._AllInstruments:
					if(instrument._CatalogNumber==i):
						instrument.Play()
						print("Very nice playing!")
						found=True
				if not found:
						print("This catalog number doesn't exit, please try again!")
			elif(choice==13):
				p=float(input("Please enter the disscount number (in %): "))
				self.sale(p)
			elif(choice==14):
				i=input("Please enter the instrument's catalog number: ")
				v=float(input("Please enter the new price: "))
				found=False
				for instrument in self._AllInstruments:
					if(instrument._CatalogNumber==i):
						self.__setitem__(instrument, v)
						found=True
				if not found:
						print("This catalog number doesn't exit, please try again!")
			elif(choice==15):
				i=input("Please enter the guitar's catalog number: ")
				print("")
				found=False
				for instrument in self._AllInstruments:
					if(instrument._CatalogNumber==i):
						if(not isinstance(instrument, Guitar)):
							print("This is not a guitar, please try again!")
						else:
							self.handle()
						found=True
				if not found:
						print("Instrument doesn't exist!")
			elif(choice==16):
				if(len(self._AllInstruments)<3):
					print("For a jam session, we need at least 3 instruments to play with!")
				else:
					print("Please select the instrument catagory: ")
					print("***************************************")
					print("1) Blues")
					print("2) Classic")
					print("3) Funk")
					print("4) Jazz")
					print("5) Reggae")
					print("6) Rock")
					print("")
					subchoice15=int(input("Please enter your choice: "))
					print("")
					if(subchoice15==1):
						winsound.PlaySound("Blues", winsound.SND_FILENAME)
						print("Great playing!")
					elif(subchoice15==2):
						winsound.PlaySound("Classic", winsound.SND_FILENAME)
						print("Great playing!")
					elif(subchoice15==3):
						winsound.PlaySound("Funk", winsound.SND_FILENAME)
						print("Great playing!")
					elif(subchoice15==4):
						winsound.PlaySound("Jazz", winsound.SND_FILENAME)
						print("Great playing!")
					elif(subchoice15==5):
						winsound.PlaySound("Reggae", winsound.SND_FILENAME)
						print("Great playing!")
					elif(subchoice15==6):
						winsound.PlaySound("Rock", winsound.SND_FILENAME)
						print("Great playing!")
					else:
						print("Wrong choice, please try again!")
			elif(choice==17):
				self.SaveToFile()
				print("Store data was writen to the file!")
			elif(choice==18):
				print("Goodbye! see you again!")
				return
			else:
				print("Wrong choice, please try again!")
				print("")





#v=Violin()
s=MusicStore()
s.Menu()
#s.Menu()
#o1=Organ()
#L=[]
#b=Bass()
#L.append(v)
#L.append(b)
#T=open(input("Please enter the destination  file name: "), "w")
#for word in L:
#    print(print(L), file=T)
#T.close()
#print(L.index(b))
#L.sort(key=lambda x: x._price, reverse=True)
#print(L)
#t=Trumpet()
#c=Contrabass()
#s=Saxophone()
#e=Electric()
#d=Drums()
#v=Viola()
#c=Cello()
#C=Contrabass()
#h=Repair()


