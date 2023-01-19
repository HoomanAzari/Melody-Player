import musicalbeeps

class Note:
    """ A class to represent a note.

    Instance:
    *duration = float
    *pitch = str
    *octave = int
    *accidental = str
    """
    
    OCTAVE_MIN = 1      #Class Attribute
    OCTAVE_MAX = 7      #Class Attribute
    
    def __init__(self, duration, pitch, octave = 1, acc_value = 'natural'):
        ''' (float, str, int, str) -> NoneType
        Creates an object of type Note
        
        >>> note = Note(2.0, "B", 4, "natural")
        >>> note.pitch
        'B'
        
        >>> note = Note(2.0, "X", 4, "natural")
        Traceback (most recent call last):
        AssertionError: Wrong input
        
        >>> note = Note(2.0, "B", 25, "natural")
        Traceback (most recent call last):
        AssertionError: Wrong input
        '''
        
        allowed_pitch = ["A", "B", "C", "D", "E", "F", "G", "R"]
        allowed_value = ["sharp", "flat", "natural"]
         
        if type(duration) != float and type(duration) != int or duration <= 0.0:
            raise AssertionError("Wrong input")
        if type(pitch) != str or pitch not in allowed_pitch or len(pitch)!=1 :
            raise AssertionError("Wrong input")
        if type(octave) != int or octave not in range(Note.OCTAVE_MIN, Note.OCTAVE_MAX + 1):
            raise AssertionError("Wrong input")
        if type(acc_value) != str or acc_value.lower() not in allowed_value:  
            raise AssertionError("Wrong input") 
            
        acc_value = acc_value.lower()   
        self.duration = float(duration)
        self.pitch = pitch
        self.octave = octave
        self.accidental = acc_value
    
    
    def __str__(self):
        ''' () -> str
        Returns the note string
        
        >>> note = Note(2.0, "B", 4, "natural")
        >>> print(note)
        2.0 B 4 natural
        
        >>> note = Note(2.0, "B", 4, "sharp")
        >>> print(note)
        2.0 B 4 sharp
        
        >>> note = Note(8.0, "B", 4, "natural")
        >>> print(note)
        8.0 B 4 natural
        '''
        
        note_string = (str(self.duration) + " " + self.pitch + " " +      
    str(self.octave) + " " + self.accidental)
        return note_string
    
    
    def play(self, play_obj): 
        ''' (player) -> none
        '''

        if self.pitch == "R":
            note_string = 'pause'
            
        elif self.accidental == "sharp":
            note_string = self.pitch + str(self.octave) + '#'
            
        elif self.accidental == 'flat':
            note_string = self.pitch + str(self.octave) + 'b'
            
        else:
            note_string = self.pitch + str(self.octave)
             
        play_obj.play_note(note_string, self.duration)
        
        
   
    