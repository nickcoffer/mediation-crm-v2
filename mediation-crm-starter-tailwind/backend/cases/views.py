from rest_framework import viewsets, permissions, status
from .models import Case, Party, Session
from .serializers import CaseSerializer, PartySerializer, SessionSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import update_session_auth_hash

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all().order_by("-created_at")
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated]

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all().order_by("-created_at")
    serializer_class = PartySerializer
    permission_classes = [permissions.IsAuthenticated]

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by("-created_at")
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def login_view(request):
    return Response({"detail": "Use /api/auth/jwt/create/ with email + password"})

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def change_password(request):
    user = request.user
    old_password = request.data.get("old_password")
    new_password = request.data.get("new_password")
    
    if not old_password or not new_password:
        return Response(
            {"detail": "Both old and new password are required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if not user.check_password(old_password):
        return Response(
            {"detail": "Current password is incorrect"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user.set_password(new_password)
    user.save()
    update_session_auth_hash(request, user)
    
    return Response({"detail": "Password changed successfully"})
