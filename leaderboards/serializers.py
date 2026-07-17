# import serializers from the REST framework
from rest_framework import serializers

# import the test results data model
from test_results.models import TestResults

# serializer class for converting viewsets responses to and from JSON between it and models.py
class LeaderboardSerializer(serializers.ModelSerializer):
    
    # have to declare rank as an "explicit field on the serializer class" otherwise the serializer will try looking for rank in the database and error
    rank = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = TestResults
        fields = ("id",
                  "rank",
                  "username_tag",
                  "test_typing_speed_kps",
                  "test_typing_speed_kph",
                  "test_typing_speed_cpm",
                  "test_typing_speed_wpm",
                  "test_typing_accuracy",
                  "test_overall_score"
                  )