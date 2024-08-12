# stage 1, construction
FROM python:alpine AS compile-image


RUN apk update && \
    apk add --no-cache gcc musl-dev libffi-dev 

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .



# stage 2
FROM python:alpine

COPY --from=compile-image /opt/venv /opt/venv

# Asegúrate de usar el entorno virtual
#es justo eso. La configuración de ENV PATH="/opt/venv/bin:$PATH" asegura que 
#cuando el sistema busca un ejecutable (como python), primero revisa el directorio 
#/opt/venv/bin antes de buscar en los otros directorios listados en PATH.
ENV PATH="/opt/venv/bin:$PATH" 

WORKDIR /app

COPY --from=compile-image /app /app

RUN adduser -D myuser && \
    chown -R myuser:myuser /app 
    
RUN apk add --no-cache curl

USER myuser

EXPOSE 8080

CMD ["python", "main.py"]
