from django.db import models

# Create your models here.


class TestResults(models.Model):
    """Used to add new class instance entries to test results sql table

    This Model .... An instance of the class is made and added to test results sql database table anytime a public or private user clicks the "See Results" button after completing a test.
    """

    # each entry instance added to sql table will have below values: 

    is_private_test = models.BooleanField(null=True, blank=False)
    # add_to_public_leaderboard = models.BooleanField()
    # test_id = models.CharField(max_length=50)
    is_private_user = models.BooleanField(null=True, blank=False)
    username_tag = models.CharField(max_length=20, null=True, blank=True)
    test_date_time_taken = models.DateTimeField(null=False, blank=False)

    test_typing_speed_kps = models.IntegerField(null=True, blank=True)
    test_typing_speed_kph = models.IntegerField(null=True, blank=True)
    test_typing_speed_cpm = models.IntegerField(null=True, blank=True)
    test_typing_speed_wpm = models.IntegerField(null=False, blank=False)
    test_typing_accuracy = models.FloatField(null=False, blank=False)
    test_overall_score = models.FloatField(null=True, blank=True)

    test_words_completed = models.IntegerField(null=False, blank=False)
    test_time_completed_in = models.IntegerField(null=False, blank=False)
    
    basic_test_option = models.CharField(null=True, blank=True)
    
    custom_test_bool = models.BooleanField(null=False, blank=False)

    test_type = models.CharField(null=False, blank=False)
    test_time_limit = models.IntegerField(null=True, blank=True)
    test_word_count = models.IntegerField(null=True, blank=True)
    test_custom_time_bool = models.BooleanField(null=False, blank=False)
    test_custom_time = models.IntegerField(null=True, blank=True)
    test_custom_text_bool = models.BooleanField(null=False, blank=False)
    # test_custom_text = models.CharField(max_length=25)
    test_modifiers = models.JSONField(null=True, blank=True)
    test_specialization_field = models.CharField(null=True, blank=True)
    test_insertion_point_style = models.CharField(null=False, blank=False)
    test_show_insertion_point = models.BooleanField(null=False, blank=False)
    test_show_stats = models.BooleanField(null=False, blank=False)
    test_show_timer = models.BooleanField(null=False, blank=False)
    test_show_word_count = models.BooleanField(null=False, blank=False)

