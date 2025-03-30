# Usa a imagem oficial do PostgreSQL versão 15 com Alpine Linux
FROM postgres:15-alpine

# Define as variáveis de ambiente para configuração do banco de dados
ENV POSTGRES_DB=ans_db
ENV POSTGRES_INITDB_ARGS="--encoding=UTF8" 

# Configura as credenciais do PostgreSQL
# Devido ao projeto ser um teste, sem credenciais sensiveis, não utilizei arquivos .env
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=test_password

# Define o diretório de trabalho onde os scripts de inicialização serão copiados
WORKDIR /docker-entrypoint-initdb.d/

# Copia o esquema do banco de dados para o diretório de inicialização
COPY schema.sql /docker-entrypoint-initdb.d/

# Copia os arquivos de dados adicionais para inicialização
COPY data/ /docker-entrypoint-initdb.d/data/

# Ajusta permissões para garantir que o usuário postgres tenha acesso adequado aos arquivos
RUN chown -R postgres:postgres /docker-entrypoint-initdb.d && \
    chmod -R 750 /docker-entrypoint-initdb.d 

# Expõe a porta padrão do PostgreSQL (5432) para conexões externas
EXPOSE 5432

# Define um comando de verificação de saúde do container, que roda a cada 30 segundos
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s \
            CMD pg_isready -U $POSTGRES_USER -d $POSTGRES_DB || exit 1
