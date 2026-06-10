FROM python:3.11

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . ./

# Instala as dependências especificadas no arquivo requirements.txt
RUN pip install -r requirements.txt

# Expõe a porta 8080, que é a porta padrão em que o Flask é executado
ENV PORT=8080
EXPOSE 8080

# Comando a ser executado quando o contêiner for iniciado
CMD python app.py
