# Perguntas
## 1) Você acha que este código está estruturado, legível e escalável? Se não, o que você mudaria?
 - Eu coloque a conexão com o banco de dados em outro arquivo. Afinal cada "classe" deveria ter a sua responsabilidade.
 - Coloquei uns logs para a gente saber o que está acontecendo. Poderia adicionar mais, mas ai vai de cada um.
 - print não funciona
 - Tinha umas coisas que não faziam nada
 - Separei o comando bash em uma variável

## 2) Quanto a conteinerização, liste as brechas de segurança que você identificou neste código? Como você as resolveria?
 1. Colocar usuário e senha no código -> Usar variável de ambiente ou arquivo de configuração.
 2. Fazer ssh -> Usar um volume compartilhado ou um endpoint, mas um volume compartilhado (para esse problema) seria mais adequado.

## 3) Na produção, o ambiente do cliente conta com um Cluster Kubernetes local. Como portar a orquestração dos containers do docker-compose para o kubernetes?
 - Coloquei os manifestos do Kubernetes necessários para o endpoint "animals" funcionar. 
 - Teria que fazer umas modificações para o "times" funcionar também.