
from rest_framework import serializers

from .models import  WatchList, StreamPlatform, Review ,UNWatchList

class WatchListSerializers(serializers.ModelSerializer):
    #link = serializers.HyperlinkedIdentityField(view_name = 'movie_details')
    class Meta:
        model = WatchList
        fields = "__all__"
        #["title", "storyline", "platform", "active", "created" ]
        
    
class StreamPlatformSerializers(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name = 'stream_details')
    #watchlist = WatchListSerializers(many = True, read_only = True)
    # watchlist = serializers.HyperlinkedRelatedField(many= True, read_only = True, view_name ="stream_details")
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        #["id","name","about", "website"]
        
        
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationsError("Name is two short")     
    #     return value
    
    def validate_name(self, value):
        if len(value) <= 3 :
            raise serializers.ValidationError(" name is two short")
        return value
    
    def validate_about(self, value):
        if len(value) <= 10:
            raise serializers.ValidationError("About Section is too Short ")
        return value
    
    def validate(self, data):
        if data['name'] == data['about']:
            raise serializers.ValidationError("NAME and ABOUT MUST be different")
        return data
    
    
class ReviewSerializers(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only = True)
    watchlist = serializers.StringRelatedField(read_only= True)
    class Meta:
        model = Review
        fields = "__all__"
        #execlude = ('watchlist',)
    

class UNWatchListSerializers(serializers.ModelSerializer):
    class Meta:
        model = UNWatchList
        fields = "__all__"
        
#=====================================================================================================================================================        

# class WatchListSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     storyline = serializers.CharField(max_length=255)
#     #platform = serializers.ForeignKey(StreamPlatform, on_delete = models.CASCADE)
#     active = serializers.BooleanField(default =True)
#     created = serializers.DateTimeField()
    
#     def create(self, validated_data):
#         """
#         Create and return  anew instance , gicven the value
#         """
#         return WatchList.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         update and return an existeing 'snipt' instance, given th value
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.storyline= validated_data.get('storyline', instance.storyline)
#         instance.active= vaildated_data.get('active', instance.active)
#         instance.created = vaildated_data.get('created', instance.created)
#         instance.save()
#         return instance
    

# class StreamPlatformSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length =50)
#     about = serializers.CharField(max_length=255)
#     website= serializers.URLField(max_length= 255)
    
#     def create(self, validated_data):
#         """
#         Create and return  anew instance , gicven the value
#         """
#         return StreamPlatform.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         update and return an existeing 'snipt' instance, given th value
#         """
        
#         instance.name = validated_data.get('name', instance.name)
#         instance.about= validated_data.get('about', instance.about)
#         instance.website = validated_data.get('website', instance.website)
#         instance.save()
#         return instance
    