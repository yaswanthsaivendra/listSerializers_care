from rest_framework import serializers

class BedListSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)
    facilityId = serializers.SerializerMethodField()
    locationId = serializers.SerializerMethodField()
    name = serializers.CharField()
    description = serializers.CharField(default="")
    bedType = serializers.IntegerField(source="bed_type")

    def get_facilityId(self, obj):
        return str(obj.facility.external_id)

    def get_locationId(self, obj):
        return str(obj.location.external_id)

    class Meta:
        model = Bed
        fields = ('id', 'facilityId', 'name',
        'description', 'bedType', 'locationId'
        )
