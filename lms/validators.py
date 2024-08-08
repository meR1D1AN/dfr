from rest_framework import serializers


class YouTubeValidators:
    def __init__(self, field):
        self.field = field

    def __call__(self, attrs):
        url = attrs.get(self.field)
        if (
            url
            and not url.startswith("https://www.youtube.com/")
            and not url.startswith("https://youtube.com/")
        ):
            raise serializers.ValidationError(
                {self.field: "Можно добавлять ссылки только с youtube"}
            )
