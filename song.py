MULTIPLIER_MIN = 1
MULTIPLIER_MAX = 5
HIT_SCORE = 10
NOTE_STREAK = 5

class Song:
    def __init__(self, name, speed, spacing, difficulty):
        self.songName = name
        self.songChart = name + ".txt"
        self.songMP3 = name + ".mp3"
        self.chartSpeed = speed
        self.chartSpacing = spacing
        self.difficulty = difficulty
        self.score = 0
        self.notesHit = 0
        self.multiplier = MULTIPLIER_MIN
        self.totalNotesHit = 0
        self.totalNotesMissed = 0

    # Get name of song
    def getName(self):
        return self.songName

    # Get file name for chart
    def getChart(self):
        return self.songChart
    
    # Get mp3 file for song
    def getMP3(self):
        return self.songMP3
    
    # Determines the speed of the chart
    def getChartSpeed(self):
        return self.chartSpeed
    
    # Determines the spacing of notes in the chart
    def getChartSpacing(self):
        return self.chartSpacing
    
    # Increment the score and adjust multiplier if necessary
    def noteHit(self):
        self.score = self.score + (HIT_SCORE * self.multiplier)
        self.notesHit = self.notesHit + 1
        self.totalNotesHit = self.totalNotesHit + 1

        if self.notesHit >= NOTE_STREAK * self.multiplier and self.multiplier < MULTIPLIER_MAX:
            self.notesHit = 0
            self.multiplier = self.multiplier + 1

    # Reset multiplier and dock points
    def noteMiss(self):
        self.totalNotesMissed = self.totalNotesMissed + 1
        if self.score < 0:
            self.score = 0
        self.notesHit = 0
        self.multiplier = MULTIPLIER_MIN

    # Set everything back to default values
    def reset(self):
        self.score = 0
        self.notesHit = 0
        self.multiplier = MULTIPLIER_MIN
        self.totalNotesHit = 0
        self.totalNotesMissed = 0

    # Returns the current score
    def getScore(self):
        return str(self.score)
    
    # Returns the current mutliplier
    def getMultiplier(self):
        return str(self.multiplier)

    # Returns the difficulty of the song
    def getDifficulty(self):
        return self.difficulty
    
    # Returns the number of notes hit and missed in the song
    def getSummary(self):
        return (str(self.totalNotesHit), str(self.totalNotesMissed))  