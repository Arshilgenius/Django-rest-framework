from rest_framework import serializers
from .models import Profile,Ques,Scrib,Tag

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'

class QuesSerializer(serializers.ModelSerializer):

    vote_from = serializers.ListField(child=serializers.IntegerField()) #list of strings

    def to_representation(self, instance: Ques): #get request
        instance.vote_from = [int(i) for i in instance.vote_from.split(',')] #gets value from db and changes to array 
        return super(QuesSerializer, self).to_representation(instance) #returns the changed value

    def to_internal_value(self, data): #post request
        ret = super(QuesSerializer, self).to_internal_value(data) #first takes data 
        if ret['vote_from']: 
            ret['vote_from'] = ','.join(str(i) for i in ret['vote_from']) #then changes data inside

        return ret #then pushes data inside



    class Meta:
        model = Ques
        fields ='__all__'


class ScribSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrib
        fields ='__all__'

class TagSerializer(serializers.ModelSerializer):



    vote_from = serializers.ListField(child=serializers.IntegerField()) #list of strings

    def to_representation(self, instance: Tag): #get request
        instance.vote_from = [int(i) for i in instance.vote_from.split(',')] #gets value from db and changes to array 
        return super(TagSerializer, self).to_representation(instance) #returns the changed value

    def to_internal_value(self, data): #post request
        ret = super(TagSerializer, self).to_internal_value(data) #first takes data 
        if ret['vote_from']: 
            ret['vote_from'] = ','.join(str(i) for i in ret['vote_from']) #then changes data inside

        return ret #then pushes data inside




    class Meta:
        model = Tag
        fields ='__all__'
