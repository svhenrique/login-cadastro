from django.template.defaultfilters import filesizeformat
from django.core.exceptions import ValidationError

allowed_formats = "'.gif', '.jpg', '.jpeg', '.png'"

max_size = 4*10000000  # byte format

mensagens_erros = {
    'max_size': f"A imagem não pode ser maior que {max_size} kB.",
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