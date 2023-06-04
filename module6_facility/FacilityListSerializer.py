
class FacilityBasicInfoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)
    local_body_object = LocalBodySerializer(source="local_body", read_only=True)
    facility_type = serializers.SerializerMethodField()
    read_cover_image_url = serializers.CharField(read_only=True)
    features = serializers.MultipleChoiceField(choices=FEATURE_CHOICES)
    patient_count = serializers.SerializerMethodField()
    bed_count = serializers.SerializerMethodField()
    phone_number = serializers.CharField(read_only=True)

    def get_bed_count(self, facility):
        return Bed.objects.filter(facility=facility).count()

    def get_patient_count(self, facility):
        return PatientRegistration.objects.filter(
            facility=facility, is_active=True
        ).count()

    def get_facility_type(self, facility):
        return {
            "id": facility.facility_type,
            "name": facility.get_facility_type_display(),
        }

    class Meta:
        model = Facility
        fields = (
            "id",
            "name",
            "local_body_object",
            "facility_type",
            "read_cover_image_url",
            "features",
            "patient_count",
            "bed_count",
            "phone_number",
        )