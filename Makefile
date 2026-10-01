PYTHON = python3

.PHONY: help run-server run-client clean

help:
	@echo "Comandos disponíveis:"
	@echo "  make run-server  - Inicia o processo do servidor TCP"
	@echo "  make run-client  - Inicia o processo do cliente TCP"
	@echo "  make clean       - Remove caches e arquivos temporários do Python"

run-server:
	@echo "[*] Iniciando o servidor TCP..."
	$(PYTHON) servidor/main.py

run-client:
	@echo "[*] Iniciando o cliente TCP..."
	$(PYTHON) cliente/main.py

clean:
	@echo "[*] Limpando caches do Python..."
	rm -rf servidor/__pycache__ cliente/__pycache__ __pycache__
	rm -f *.pyc servidor/*.pyc cliente/*.pyc