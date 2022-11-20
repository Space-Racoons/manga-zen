# Documento de visão

# Equipe e Definições dos papeis

Membro | Papel | Email
------ | ----- | -----
Felipe | Programador | ------------
Guilherme | Programador | -------------
Renildo | Programador | renildorabi22@gmail.com

## Matriz de Competências 

Membro | Competência 
------ | -----------
Guilherme | Desenvolvedor Python(Django), JavaScript.
Felipe | Desenvolvedor Python(Django), Golang, C.
Renildo | Desenvolvedor Python(Django), JavaScript.


# Descrição do projeto

O projeto se trata de um leitor de mangá online. Tendo como principal função permitir que o leitor possa escolher
o idioma é que se deseja ler. Além da função de "My collection", onde o usuário poderá adicionar todos os seus mangá favoritos.


# Perfis dos usuários

O sistema poderá ser usado por três tipos de usuário.

* Usuário Admin: Esse usuário tem a permissão de deletar comentários e usuários que por alguma razão forem contra as regras do site/sistema.

* Usuário normal: Esse usuário poderá adicionar comentário nos mangás e nos capítulos. Também terá o direito de criar a sua coleção com os seus mangá favoritos.

* Usuário visitante: Esse usuário se trata do usuário que não tem uma conta no sistema. Ele poderá somente ler os mangás disponiveis no site. Caso queira comentar e criar sua coleção de mangás, terá que fazer um cadastro no sistema.

Requisito| Descrição   | Ator |
---------| ----------- | ---------- |
RF001 - Adicionar comentário | O usuário poderá adicionar um comentário á um mangá ou capítulo. | Usuário normal e Usuário Admin
RF002 - Editar comentário | O usuário poderá editar o seu comentário em um mangá ou capítulo. | Usuário normal e Usuário Admin
RF003 - Visualizar comentário | O usuário poderá ver os comentários do mangá ou capítulo. | Usuário normal, Usuário Admin e Usuário visitante
RF004 - Deletar comentário | O usuário poderá deleter o seu comentário em um mangá ou capítulo. | Usuário normal e Usuário Admin 
RF005 - Visualizar mangá | O usuário poderá vizualizar o mangá e as suas informações.| Usuário normal, Usuário Admin e Usuário visitante
RF006 - Ler capítulo | O usuário poderá ler os capítulos do mangá. | Usuário normal, Usuário Admin e Usuário visitante