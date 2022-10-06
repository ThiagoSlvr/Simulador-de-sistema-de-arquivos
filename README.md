Simulador de Sistema de Arquivos.

Um sistema de arquivos baseado em i-nodes. O seu disco rígido virtual possui 128MB e cada bloco possui 4KB.
O sistema de arquivos é persistente, o que significa que se o processo do sistema de arquivos for encerrado, o conteúdo é mantido e carregado na próxima vez que o processo for iniciado.


O que entregar? código do sistema de arquivos e documentação de uso. No caso de trabalhos feitos em grupo, apenas um aluno precisa entregar.

Operações sobre arquivos:

    - Criar arquivo (touch arquivo)
    - Remover arquivo (rm arquivo)
    - Escrever no arquivo (echo "conteudo legal" >> arquivo)
    - Ler arquivo (cat arquivo)
    - Copiar arquivo (cp arquivo1 arquivo2)
    - Renomear arquivo (mv arquivo1 arquivo2)

Operações sobre diretórios:

    - Criar diretório (mkdir diretorio)
    - Remover diretório (rmdir diretorio) - só funciona se diretório estiver vazio
    - Trocar de diretório (cd diretorio)
        * Não esquecer dos arquivos especiais . e .. 
    - Renomear diretorio (mv diretorio1 diretorio2)