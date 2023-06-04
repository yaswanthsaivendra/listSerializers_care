from rest_framework import serializers

class AssetTransactionListSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='external_id', read_only=True)
    from_location_name = serializers.CharField(source='from_location.name', read_only=True)
    to_location_name = serializers.CharField(source='to_location.name', read_only=True)
    performed_by_first_name = serializers.CharField(source='performed_by.first_name', read_only=True)
    performed_by_last_name = serializers.CharField(source='performed_by.last_name', read_only=True)
    modified_date = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = AssetTransaction
        fields = (
            'id',
            'from_location_name',
            'to_location_name',
            'performed_by_first_name',
            'performed_by_last_name',
            'modified_date'
        )
