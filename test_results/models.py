from django.db import models

# Create your models here.


class TestResults(models.Model):
    """Used to add new class instance entries to test results sql table

    This Model .... An instance of the class is made and added to test resuls sql database table anytime a public or private user clicks the "See Results" button after completing a test.
    """

    # each entry instance added to sql table will have below values: 

    is_private = models.BooleanField()
    # add_to_public_leaderboard = models.BooleanField()

    # test_id = models.CharField(max_length=50)
    username_tag = models.CharField(max_length=20)
    test_date_time_taken = models.DateTimeField()

    test_typing_speed_kps = models.IntegerField()
    test_typing_speed_kph = models.IntegerField()
    test_typing_speed_cpm = models.IntegerField()
    test_typing_speed_wpm = models.IntegerField()
    test_typing_accuracy = models.FloatField()
    test_words_completed = models.IntegerField()
    test_time_completed_in = models.IntegerField()
    
    basic_test_option = models.CharField()
    
    custom_test_bool = models.BooleanField()

    test_type = models.CharField()
    test_time_limit = models.IntegerField()
    test_word_count = models.IntegerField()
    test_custom_time_bool = models.BooleanField()
    test_custom_time = models.IntegerField()
    test_custom_text_bool = models.BooleanField()
    # test_custom_text = models.CharField(max_length=25)
    test_modifiers = models.JSONField()
    test_specialization_field = models.CharField()
    test_insertion_point_style = models.CharField()
    test_show_insertion_point = models.BooleanField()
    test_show_stats = models.BooleanField()
    test_show_timer = models.BooleanField()
    test_show_word_count = models.BooleanField()

