# Docker Setup - Caramelo Project

## Como usar o Docker para desenvolvimento

### Pré-requisitos
- Docker
- Docker Compose

### Passos para rodar o projeto

1. **Clone o repositório e navegue até a pasta**
   ```bash
   git clone <url-do-repo>
   cd caramelo
   ```

2. **Prepare os dados (se necessário)**
   - Crie uma pasta `data` na raiz do projeto:
     ```bash
     mkdir data
     ```
   - Coloque o arquivo `data.zip` dentro da pasta `data/`

3. **Construa e inicie o container**
   ```bash
   docker-compose up --build
   ```

4. **Acesse o Jupyter**
   - Abra o navegador e vá para: `http://localhost:8888`
   - O Jupyter vai abrir sem necessidade de token

5. **Para parar o container**
   ```bash
   docker-compose down
   ```

### Estrutura dos volumes
- `.:/app` - Todo o projeto é montado no container
- `./data:/app/data` - Pasta de dados
- `./notebooks:/app/notebooks` - Pasta para notebooks adicionais

### Notas importantes
- O notebook foi adaptado para usar caminhos Docker (`/app/data/`)
- Os dados são persistidos localmente através dos volumes
- O container é reiniciado automaticamente se parar

### Solução de problemas
- Se der erro de permissão, rode: `sudo docker-compose up --build`
- Se precisar instalar novos pacotes Python, adicione no `requirements.txt` e rebuilde o container
