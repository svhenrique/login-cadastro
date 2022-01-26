from django.template.defaultfilters import filesizeformat
from django.core.exceptions import ValidationError

allowed_formats = "'.gif', '.jpg', '.jpeg', '.png'"

max_size = 5*1000000  # byte format

def byte_to_mb(byte_file):
    to_kB = to_MB = 1024
    return byte_file//(to_kB*to_MB)

mensagens_erros = {
    'max_size': f"A imagem não pode ser maior que {byte_to_mb(max_size)} MB.",
    'content_type': f"Apenas arquivos no formato {allowed_formats} são suportados"
}

def validate_file_format(archive):
    file_format = archive.name.split('.')[-1]
    if file_format not in allowed_formats:
        raise ValidationError(mensagens_erros['content_type'])
    return archive

def validate_file_size(archive):
    file_size = archive.size
    if file_size > max_size:
        raise ValidationError(mensagens_erros['max_size'])
    return archive