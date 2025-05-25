from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from documents.models import Document
from .services import AIService

class QuestionAnswerView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    ai_service = AIService()

    def post(self, request, *args, **kwargs):
        document_id = request.data.get('document_id')
        question = request.data.get('question')

        if not document_id or not question:
            return Response(
                {'error': 'Both document_id and question are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            document = Document.objects.get(id=document_id, user=request.user)
        except Document.DoesNotExist:
            return Response(
                {'error': 'Document not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        answer = self.ai_service.answer_question(question, document.content)
        return Response({'answer': answer}) 