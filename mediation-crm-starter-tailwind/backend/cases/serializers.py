from rest_framework import serializers
from .models import Case, Party, Session

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

class CaseSerializer(serializers.ModelSerializer):
    parties = PartySerializer(many=True, read_only=True)
    sessions = SessionSerializer(many=True, read_only=True)
    amount_outstanding = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Case
        fields = [
            "id", "reference", "title", "status", "notes",
            "party1_name", "party1_email", "party1_phone",
            "party2_name", "party2_email", "party2_phone",
            "enquiry_date", "voucher_used", "internal_notes",
            "amount_owed", "amount_paid", "amount_outstanding", "payment_notes",
            "created_at", "updated_at", "parties", "sessions"
        ]