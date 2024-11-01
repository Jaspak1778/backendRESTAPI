# main/api_views.py
#REST Api näkymä funktiot
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post, Comment, Like, User
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        # Palauttaa vain kirjautuneen käyttäjän querysetin
        return User.objects.filter(id=self.request.user.id)

#Käyttäjä tiedot
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile_view(request):
    """
    Palauttaa kirjautuneen käyttäjän profiilitiedot.
    """
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)    


@api_view(['POST'])
def login_view(request):
    """
    Ohje.
    Käyttäjän kirjautuminen.
    Kirjoita käyttäjätunnus ja salasana POST-pyyntöön JSON-muodossa ja merkkijonot string tyyppinä. 
    Esim:

    {
    "username": "Käyttäjä",
    "password": "salasana"
    }
    
    """
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)