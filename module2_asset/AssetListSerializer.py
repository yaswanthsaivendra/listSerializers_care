from rest_framework import serializers

class AssetListSerializer(serializers.ModelSerializer):
    facility = serializers.SerializerMethodField()
    asset_class = serializers.CharField(source='get_asset_class_display')
    asset_type = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Asset
        fields = ('facility', 'asset_class', 'asset_type', 'status', 'location')

    def get_facility(self, obj):
        return obj.current_location.facility.name if obj.current_location.facility else None

    def get_asset_type(self, obj):
        return obj.get_asset_type_display()

    def get_status(self, obj):
        return obj.get_status_display()

    def get_location(self, obj):
        return obj.current_location.name if obj.current_location else None
