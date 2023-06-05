class UserSkillSerializer(ModelSerializer):
    id = UUIDField(source="external_id", read_only=True)
    skill = ExternalIdSerializerField(write_only=True, required=True, queryset=Skill.objects.all())
    skill_object = SkillListSerializer(source="skill", read_only=True)

    class Meta:
        model = UserSkill
        fields = ("id", "skill", "skill_object")