# import serializers from the REST framework
from rest_framework import serializers

# import the test results data model
from .models import TestResults

# create a serializer class
class TestResultsSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = TestResults
        fields = ("id",
                  "is_private_test",
                  "is_private_user",
                  "username_tag",
                  "test_date_time_taken",
                  "test_typing_speed_kps",
                  "test_typing_speed_kph",
                  "test_typing_speed_cpm",
                  "test_typing_speed_wpm",
                  "test_typing_accuracy",
                  "test_words_completed",
                  "test_time_completed_in",
                  "basic_test_option",
                  "custom_test_bool",
                  "test_type",
                  "test_time_limit",
                  "test_word_count",
                  "test_custom_time_bool",
                  "test_custom_time",
                  "test_custom_text_bool",
                  "test_modifiers",
                  "test_specialization_field",
                  "test_insertion_point_style",
                  "test_show_insertion_point",
                  "test_show_stats",
                  "test_show_timer",
                  "test_show_word_count"
                  )