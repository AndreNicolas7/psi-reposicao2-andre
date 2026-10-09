# README Explicativo
## André Nícolas de oliveira Santos

## Justificativa breve respondendo:

1. Por que as rotas de leituras ficaram em `leituras.py` e não em `app.py`?
As rotas de leituras ficaram em `leituras.py` porque o Flask usa blueprints para separar responsabilidades: `app.py` é o ponto de montagem da aplicação, enquanto o blueprint de leituras concentra o CRUD e a lógica do domínio relacionado a leitura, isso deixa a aplicação organizada, reutilizável e facilita a proteção das rotas por autenticação.

2. Como a aplicação identifica o usuário logado usando `session`? 
Gravando `session["usuario_id"]` e `session["usuario_nome"]` após o login em `auth.py`, em seguida as rotas privadas verificam essa sessão em `seguranca.py` antes de permitir acesso.

3. Como `sefuranca.py`, `leituras.py` e `database.py` impedem o acesso a leituras de outro usuário?
 Os 3 impedem acesso a leituras de outro usuário porque todas as consultas de leitura usam o `usuario_id` do usuário autenticado, `exigir_login()` bloqueia acessos anônimos e, em `database.py`, as funções como `listar_leituras`, `buscar_leitura`, `atualizar_leitura`, `alternar_concluida` e `excluir_leitura` filtram por `usuario_id`, além de `leituras.py` validar o dono antes de editar, concluir ou excluir qualquer registro.