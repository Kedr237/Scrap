from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from notes.api.v1.serializers import NoteSerializer
from notes.models import Note

User = get_user_model()


class TestNoteSerializer(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='TestNoteSerializer',
            password='TestNoteSerializer',
            email='TestNoteSerializer@test.com',
        )

    def test_valid_serializer(self):
        note_1 = Note.objects.create(
            owner=self.user,
            title='Note TestNoteSerializer 1',
            content='Content',
        )
        note_2 = Note.objects.create(
            owner=self.user,
            title='Note TestNoteSerializer 2',
            content='Content',
        )
        tz = timezone.get_current_timezone()
        data = NoteSerializer([note_1, note_2], many=True).data
        expected_data = [
            {
                'id': note_1.id,
                'owner': self.user.id,
                'title': 'Note TestNoteSerializer 1',
                'content': 'Content',
                'image': None,
                'created': note_1.created.astimezone(tz).isoformat(),
                'modified': note_1.modified.astimezone(tz).isoformat(),
            },
            {
                'id': note_2.id,
                'owner': self.user.id,
                'title': 'Note TestNoteSerializer 2',
                'content': 'Content',
                'image': None,
                'created': note_2.created.astimezone(tz).isoformat(),
                'modified': note_2.modified.astimezone(tz).isoformat(),
            },
        ]
        self.assertEqual(data, expected_data)
