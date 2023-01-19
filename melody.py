import note
import musicalbeeps

class Melody:
    ''' A class to represent a melody.

    Instance:
    *filename: str
    '''
    
    def __init__(self,filename):
        ''' (str) -> NoneType
        Creates an object of class Melody
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> len(happy_birthday.notes)
        25
        >>> print(happy_birthday.notes[5])
        1.0 F 4 sharp
        
        >>> twinkle = Melody("twinkle.txt")
        >>> len(twinkle.notes)
        42
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> print(hot_cross_buns.notes[2])
        1.0 G 4 natural
    
        '''
        file = open(filename, "r")
        note_list = file.read().split("\n")
        
        self.title = note_list[0]
        self.author = note_list[1]
        
        note_list1 = []
        repeated = []
        repeated_bool = False
        
        for i in note_list[2:]:
            values = i.split()
            
            if values[1] == "R":
                note_p = values[0:2]
                repeat = values[2]
                note_string = note.Note(float(note_p[0]), note_p[1])
                note_string_copy = note.Note(float(note_p[0]), note_p[1])
            else:
                note_p = values[0:4]
                repeat = values[4]
                note_string = note.Note(float(note_p[0]), note_p[1], int(note_p[2]), note_p[3])
                note_string_copy = note.Note(float(note_p[0]), note_p[1], int(note_p[2]), note_p[3])
                
            note_list1 += [note_string]
            
            if repeat == "true":
                if repeated_bool:
                    repeated += [note_string_copy]
                    note_list1 += repeated
                    repeated = []
                    repeated_bool = False
                else:
                    repeated_bool = True
            
            if repeated_bool:
                repeated += [note_string_copy]
        
        self.notes = note_list1[:]
                    
        file.close()

        
    def play(self, play_obj):   
        ''' (player) -> none
        '''

        for element in self.notes:
            element.play(play_obj)
            
              
    def get_total_duration(self):
        """ () -> float
        Returns the total duration of a song
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.get_total_duration()
        13.0
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> hot_cross_buns.get_total_duration()
        8.0
        
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.get_total_duration()
        24.5
        """
        duration = 0.0
        for element in self.notes:
            duration += element.duration
        return float(duration)
    
    def lower_octave(self):
        """ () -> bool
        Lowers the octave of all notes by 1 and returns a boolean.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.notes[5].octave
        3
        
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.lower_octave()
        True
        >>> twinkle.notes[2].octave
        3
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> hot_cross_buns.lower_octave()
        True
        >>> hot_cross_buns.notes[8].octave
        3
        """
        for element in self.notes:
            if element.pitch != "R" and element.octave <= element.OCTAVE_MIN:
                return False 
        for element in self.notes:
            if element.pitch != "R":
                element.octave -=1
        return True
    
    def upper_octave(self):
        """ () -> bool
        Highers the octave of all notes by 1 and returns a boolean.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.upper_octave()
        True
        >>> happy_birthday.notes[5].octave
        5
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>> hot_cross_buns.upper_octave()
        True
        >>> hot_cross_buns.notes[8].octave
        5
        
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.upper_octave()
        True
        >>> twinkle.notes[2].octave
        5
        """
        for element in self.notes:
            if element.pitch != "R" and element.octave >= element.OCTAVE_MAX:
                return False
        for element in self.notes:
            if element.pitch != "R":
                element.octave +=1
        return True
    
    def change_tempo(self, temp):
        """ (float) -> NoneType
        Multiplies the duration each of note by the specified value.
        
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.change_tempo(0.5)
        >>> happy_birthday.get_total_duration()
        6.5
        
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.change_tempo(2)
        >>> twinkle.get_total_duration()
        49.0
        
        >>> twinkle = Melody("twinkle.txt")
        >>> twinkle.change_tempo('john')
        Traceback (most recent call last):
        AssertionError: Invalid input
        """
        
        if type(temp) != float and type(temp) != int or temp <= 0.0:
            raise AssertionError("Invalid input")
        
        for element in self.notes:
            element.duration *= float(temp)
            
            
            


            
