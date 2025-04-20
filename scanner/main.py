# scanner.py

def scan_contracts(limit=10):
    print(f"\u23f3 Escaneando os {limit} contratos mais antigos simulados...")
    dummy_data = []
    for i in range(limit):
        dummy_data.append({
            "address": f"0xDummyContract{i}",
            "last_tx": 0,
            "activity_score": 0,
        })
    return dummy_data


# classify.py

def classify_data(data):
    results = []
    for item in data:
        if item['last_tx'] == 0:
            classification = 'Reintegrável'
        else:
            classification = 'Ativo'
        results.append({
            "address": item["address"],
            "class": classification
        })
    return results


# config.py

ETHERSCAN_API_KEY = "sua_api_key_aqui"
NETWORK = "mainnet"


# utils.py

def format_address(address):
    return address.lower()


# requirements.txt

web3
requests
pandas


# README.md

# 🧪 Scanner Vetorialético AGro

Este é um protótipo em Python para identificar contratos e carteiras inativas na blockchain como parte da criptoarqueologia energética vetorial.

## Como usar

```bash
pip install -r requirements.txt
python main.py
```

## Módulos
- `scanner.py`: simula contratos antigos
- `classify.py`: classifica contratos como ativos ou reintegráveis
- `main.py`: orquestra execução
- `utils.py`: funções auxiliares
