# bot-whats

Esse é um projeto teste de apenas retornar o texto de um audio enviado pelo whats via api.

O serviço recebe a URL de um áudio (`.ogg`), baixa o arquivo e usa a API do OpenAI (Whisper) para transcrever o conteúdo em texto.

## Requisitos

- Python 3.12
- Uma chave de API da OpenAI

## Configuração

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Defina a variável de ambiente com sua chave da OpenAI:

   ```bash
   export OPENAI_API_KEY=sua-chave-aqui
   ```

## Executando localmente

```bash
python app.py
```

A aplicação sobe em `http://localhost:5000`.

Também é possível rodar via Docker:

```bash
docker build -t bot-whats .
docker run -p 5000:5000 -e OPENAI_API_KEY=sua-chave-aqui bot-whats
```

## Uso da API

### `POST /convert`

Recebe a URL de um áudio e retorna a transcrição em texto.

**Request:**

```bash
curl -X POST http://localhost:5000/convert \
  -H "Content-Type: application/json" \
  -d '{"url": "https://exemplo.com/audio.ogg"}'
```

**Response:**

```json
{
  "message": "texto transcrito do áudio",
  "output_file": "audios/input_audio.ogg"
}
```
