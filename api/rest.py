from rest_framework import routers, serializers, viewsets

from .models import Book

router = routers.DefaultRouter()

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = [
			'id',
			'user',
			'url',
			'title',
			'author',
			'page',
			'status',
		]
class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
	def get_queryset(self):
		return Book.objects.filter(user = self.request.user)
router.register('books', BookViewSet)
