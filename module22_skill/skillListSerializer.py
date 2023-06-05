class SkillSerializer(ModelSerializer):
    id = UUIDField(source="external_id", read_only=True)

    class Meta:
        model = Skill
        fields = ("id", "name")