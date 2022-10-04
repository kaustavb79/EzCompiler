from distutils.command.upload import upload
from django.core.exceptions import ValidationError
from django.db import models
import uuid

def media_uuid_generate():
    return 'M_' + str(uuid.uuid4())


def validate_upload_file(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 50.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


class CompilerAPIModel(models.Model):
    request_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    source_code_file = models.FileField(upload_to='media_file/source_code',null=True, blank=True)
    additional_file = models.FileField(upload_to='media_file/external_file',null=True, blank=True,validators=[validate_upload_file],help_text='Maximum file size allowed is 50Mb')
    code_language = models.CharField(max_length=10)
    final_response = models.CharField(null=True, blank=True,max_length=2000)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.code_language} file --- {self.request_id}"

    class Meta:
        ordering = ('-date_time',)
