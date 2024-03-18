MULTIPLIER_MIN = 1
MULTIPLIER_MAX = 5
HIT_SCORE = 10
MISS_SCORE = 50
NOTE_STREAK = 5

class Song:
    def __init__(self, name, speed, difficulty):
        self.songChart = name + ".txt"
        self.songMP3 = name + ".mp3"
        self.chartSpeed = speed
        self.difficulty = difficulty
        self.score = 0
        self.notesHit = 0
        self.multiplier = MULTIPLIER_MIN

    # Get file name for chart
    def getChart(self):
        return self.songChart
    
    # Get mp3 file for song
    def getMP3(self):
        return self.songMP3
    
    # Determines the speed of the chart
    def getChartSpeed(self):
        return self.chartSpeed
    
    # Increment the score and adjust multiplier if necessary
    def noteHit(self):
        self.score = self.score + (HIT_SCORE * self.multiplier)
        self.notesHit = self.notesHit + 1

        if self.notesHit >= NOTE_STREAK * self.multiplier and self.multiplier < MULTIPLIER_MAX:
            self.notesHit = 0
            self.multiplier = self.multiplier + 1

    # Reset multiplier and dock points
    def noteMiss(self):
        self.score = self.score - MISS_SCORE
        if self.score < 0:
            self.score = 0
        self.notesHit = 0
        self.multiplier = MULTIPLIER_MIN

    # Set everything back to default values
    def reset(self):
        self.score = 0
        self.notesHit = 0
        self.multiplier = MULTIPLIER_MIN

    def getScore(self):
        return str(self.score)
    
    def getMultiplier(self):
        return str(self.multiplier)

    def getDifficulty(self):
        return self.difficulty    