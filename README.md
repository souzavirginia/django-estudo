# django-estudo
Aplicação Django para consultar animais e filtrar por nome ou raça.

## Executar localmente

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

A lista de animais fica em `/animais/`. Cadastre tipos, raças e animais pelo
admin em `/admin/` antes de testar os filtros. A listagem de tipos e raças fica
em `/animais/tipos/`.
