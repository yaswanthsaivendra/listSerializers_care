class AssetBedListSerializer(ModelSerializer):
    id = UUIDField(source="external_id", read_only=True)
    asset = UUIDField(source="asset.external_id", read_only=True)
    bed = UUIDField(source="bed.external_id", read_only=True)

    class Meta:
        model = AssetBed
        exclude = ("deleted", "external_id", "meta")
