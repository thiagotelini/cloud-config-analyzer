# ☁️ Cloud Config Analyzer  
Analisador de configurações inseguras em ambientes Cloud usando IA

O **Cloud Config Analyzer** é um projeto acadêmico que utiliza **Python + Machine Learning** para identificar configurações inseguras em buckets de cloud (simulados à semelhança do Google Cloud Storage).  
A ideia surgiu a partir de um incidente real envolvendo configurações incorretas em buckets da CIEE.

O sistema é capaz de classificar buckets como:

- ✅ **secure** — sem vulnerabilidades detectadas  
- ⚠️ **attention** — não exposto, mas com pontos de melhoria (ex: criptografia desativada)  
- ❌ **insecure** — expostos publicamente ou com ACLs indevidas  

O projeto inclui:
✔ Relatório HTML profissional  
✔ Mock de dados + treinamento do modelo  
✔ Adaptador para converter JSON real de buckets para o formato de entrada da IA  

---

## 🎯 Objetivo do Projeto

- Demonstrar como falhas de configuração em ambientes cloud podem ser detectadas automaticamente.  
- Criar um pipeline simples de Machine Learning capaz de identificar riscos.  
- Oferecer uma ferramenta educacional para análise de segurança de buckets.  
- Simular o funcionamento de uma solução real de "Cloud Security Posture Management" (CSPM).

---

## 🧠 Como funciona

### 1. Gerador de dataset mockado  
Cria configurações aleatórias de buckets com combinações de:
- public_read  
- encryption  
- acl_all_users  

Cada linha recebe a classificação automática “secure”, “attention” ou “insecure”.

### 2. Treinamento do modelo  
O dataset é usado para treinar um **RandomForestClassifier**, que aprende padrões dessas configurações.

### 3. Adaptador JSON → Features  
JSONs reais de buckets são convertidos para:

```json
{
  "bucket_name": "...",
  "public_read": 0,
  "encryption": 1,
  "acl_all_users": 0
}
```

### 4. Classificação  
O modelo prediz a classe de segurança de cada bucket.

### 5. Saída  
- Tabela colorida no terminal  
- Relatório estruturado em HTML  

---

## 🛠 Tecnologias utilizadas

- **Python 3.14**
- **scikit-learn** — Machine Learning (RandomForest)
- **pandas** — Manipulação de dados
- **json** — Manipulação de configs
- **HTML/CSS** — Relatório estruturado

---

## 📁 Estrutura de pastas

```bash
cloud-config-analyzer/
│
├── analyzer/
│   ├── data_mocks/                    # JSONs de exemplo (secure, insecure, attention)
│   ├── json_configurations_adapter.py # Adaptador que lê configs reais
│   └── configurations_analyzer.py     # Lógica de predição do modelo
│
├── model/
│   ├── configs_dataset.csv            # Dataset gerado durante execução
│   ├── data_set_generator.py          # Gerador de dataset para treinamento
│   └── train_model.py                 # Treinamento do modelo
│
├── utils/
│   ├── display_response.py            # Tabela e saída colorida no terminal
│   ├── html_report_generator.py       # Gerador de relatório em html
│   └── log_colors.py                  # Tabela de cores
│
├── runner.py                          # Arquivo principal para executar o fluxo completo
│
├── requirements.txt                   # Dependências do projeto
└── README.md                          # Este arquivo
```

---

## ▶️ Como executar o projeto

### 1. Criar o ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Windows (Git Bash):**
```bash
source venv/Scripts/activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

---

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Executar o projeto completo

```bash
python runner.py
```

Fluxo executado:

1. Geração do dataset  
2. Treinamento do modelo  
3. Carregamento dos JSONs de teste  
4. Predições  
5. Exibição no terminal  
6. Geração do relatório HTML (`report.html`)

---

## 📊 Exemplo de saída no terminal

```
RESULTADO DA ANÁLISE
+------------------------------+------------------+
| Bucket Name                  | Classificação    |
+------------------------------+------------------+
| secure-bucket                | ✓ Seguro         |
| prod-public                  | ✗ Inseguro       |
| no-kms-bucket                | ⚠ Atenção        |
+------------------------------+------------------+
```

---

## 🧾 Relatório HTML

O projeto gera automaticamente o arquivo:

```
report.html
```

Abra no navegador para visualizar uma análise completa e formatada.

---

## 📄 Autor

Thiago Telini - RA: 25000552
