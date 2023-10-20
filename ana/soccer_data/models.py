from django.db import models

# Define the Team model (soccer_data/models.py)
class Team(models.Model):
    name = models.CharField(max_length=100)  # The name of the team
    founded_year = models.PositiveIntegerField()  # The year the team was founded
    city = models.CharField(max_length=100)  # The city the team is based in

    def __str__(self):
        return self.name  # Returns the name of the team when the object is printed

# Define the Player model (soccer_data/models.py)
class Player(models.Model):
    first_name = models.CharField(max_length=100)  # The first name of the player
    last_name = models.CharField(max_length=100)  # The last name of the player
    position = models.CharField(max_length=50)  # The position of the player on the field
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # Foreign key to the Team model, indicating which team the player belongs to

    def __str__(self):
        return f'{self.first_name} {self.last_name}'  # Returns the full name of the player when the object is printed

# Define the Match model (soccer_data/models.py)
class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)  # Foreign key to the Team model for the home team
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)  # Foreign key to the Team model for the away team
    home_team_score = models.PositiveIntegerField()  # The score of the home team
    away_team_score = models.PositiveIntegerField()  # The score of the away team
    date = models.DateField()  # The date the match was played

    def __str__(self):
        return f'{self.home_team} vs {self.away_team} on {self.date}'  # Returns a string representation of the match when the object is printed
