# 🐍 Scripts Python - Análise de Segurança Viária NYC

## 📋 Visão Geral

Este diretório contém **4 scripts Python** que reproduzem toda a análise de dados de colisões veiculares de NYC realizada na apresentação ao Governador.

**Dados Analisados:**
- 2.216.469 colisões
- 726.530 pessoas feridas
- 3.509 pessoas mortas
- Período: 2013-2025 (13 anos)

---

## 🚀 Como Usar

### **Prerequisitos**
```bash
pip install pandas numpy
```

### **Opção 1: Executar Análise Completa (Recomendado)**
```bash
python3 EXECUTAR_ANALISE_COMPLETA.py
```

Isto executará os 3 módulos sequencialmente em ~2-3 minutos.

### **Opção 2: Executar Módulos Individualmente**

#### Módulo 1: Análise Principal
```bash
python3 01_analise_principal.py
```
**Conteúdo:**
- Indicadores-chave (KPIs)
- Distribuição por bairro
- Análise de vítimas
- Padrões temporais (hora/mês)
- Fatores contribuintes
- Tendência anual (2012-2025)
- Tipos de veículos

#### Módulo 2: Análise Avançada
```bash
python3 02_analise_avancada.py
```
**Conteúdo:**
- Severidade por número de veículos
- Análise bairro x vulnerabilidade
- Horários críticos por bairro
- Causas vs grupos vulneráveis
- Identificação de ruas críticas (high-risk locations)
- 7 recomendações estratégicas detalhadas

#### Módulo 3: Análise Econômica
```bash
python3 03_analise_economica.py
```
**Conteúdo:**
- Custos totais ($75.9B em 13 anos)
- Orçamento de investimento ($350M/ano)
- Análise de ROI (11x-24x)
- Cenários (conservador vs agressivo)
- Custo da inação
- Payback period (< 1 mês)

### **Opção 3: Preparar Dados (Se necessário)**
```bash
python3 00_fix_columns.py
```

Isto cria um arquivo limpo: `Motor_Vehicle_Collisions_LIMPO.csv`

---

## 📂 Estrutura dos Arquivos

| Arquivo | Tamanho | Descrição |
|---------|---------|-----------|
| `00_fix_columns.py` | 1 KB | Correção de colunas com problema de encoding |
| `01_analise_principal.py` | 13 KB | Análise geral e indicadores-chave |
| `02_analise_avancada.py` | 18 KB | Análise profunda e recomendações |
| `03_analise_economica.py` | 16 KB | Análise financeira e ROI |
| `EXECUTAR_ANALISE_COMPLETA.py` | 22 KB | Script master que executa tudo |
| `Motor_Vehicle_Collisions_LIMPO.csv` | 800 MB | Dados limpos (gerado automaticamente) |

---

## 📊 Saída Esperada

Ao executar qualquer script, você verá:

```
==========================================================================================
ANÁLISE GERAL - INDICADORES-CHAVE
==========================================================================================

📊 VOLUME GERAL (2013-2025)
  • Total de Colisões: 2,216,469
  • Total de Feridos: 726,530
  • Total de Mortos: 3,509
  • Média Diária: 456 colisões
  ...
```

A saída é **estruturada** com seções claras separadas por linhas de `=`.

---

## 🎯 Principais Funções por Módulo

### **Módulo 1: `01_analise_principal.py`**

```python
carregar_dados(caminho_csv)          # Carrega e prepara dados
analise_geral(df)                    # KPIs principais
analise_por_bairro(df)               # Distribuição geográfica
analise_vitimas(df)                  # Análise de vítimas
analise_temporal(df)                 # Padrões por hora/mês
analise_causas(df)                   # Fatores contribuintes
analise_tendencia_anual(df)          # Evolução 2012-2025
analise_veiculos(df)                 # Tipos de veículos
```

### **Módulo 2: `02_analise_avancada.py`**

```python
analise_severidade_multiplos_veiculos(df)    # Colisões por # de veículos
analise_bairro_vulnerabilidade(df)           # Grupos vulneráveis por bairro
analise_horarios_criticos_bairro(df)         # Horas críticas por bairro
analise_causas_versus_vulneraveis(df)        # Causas que afetam cada grupo
analise_ruas_criticas(df)                    # High-risk locations
gerar_recomendacoes(df)                      # 7 recomendações estratégicas
```

### **Módulo 3: `03_analise_economica.py`**

```python
analise_custos_totais(df)            # Custos: vidas, saúde, propriedade
orçamento_investimento()              # Investimento recomendado
analise_roi(custos, investimento, df) # ROI em 2 cenários
resumo_executivo_financeiro(...)      # Resumo executivo
```

---

## 💡 Exemplos de Uso Prático

### **Exemplo 1: Extrair apenas KPIs**
```python
import pandas as pd
from analise_principal import carregar_dados, analise_geral

df = carregar_dados('Motor_Vehicle_Collisions_LIMPO.csv')
kpis = analise_geral(df)

print(f"Total de colisões: {kpis['total_colisoes']:,}")
print(f"Total de feridos: {kpis['total_feridos']:,}")
print(f"Total de mortos: {kpis['total_mortos']:,}")
```

### **Exemplo 2: Análise de severidade por bairro**
```python
from analise_principal import carregar_dados, analise_por_bairro

df = carregar_dados('Motor_Vehicle_Collisions_LIMPO.csv')
bairros = analise_por_bairro(df)

for bairro, colisoes in bairros.items():
    print(f"{bairro}: {colisoes:,} colisões")
```

### **Exemplo 3: Calcular ROI**
```python
from analise_economica import analise_custos_totais, analise_roi, orçamento_investimento

df = carregar_dados('Motor_Vehicle_Collisions_LIMPO.csv')
custos = analise_custos_totais(df)
investimento = orçamento_investimento()
roi = analise_roi(custos, investimento, df)

print(f"ROI Conservador: {roi['conservador']['roi_multiplo']:.2f}x")
print(f"ROI Agressivo: {roi['agressivo']['roi_multiplo']:.2f}x")
```

---

## 🔍 Principais Descobertas

Ao executar os scripts, você encontrará:

### **Top 5 Insights**

1. **Desatenção ao Volante = 31.1%** (Principal causa)
   - 552.838 acidentes
   - Recomendação: Aumentar fiscalização

2. **Pedestres 5x Mais Vulneráveis** (CRÍTICO)
   - Taxa mortalidade 1.30% vs 0.27% de motoristas
   - Recomendação: Ciclovias protegidas

3. **Brooklyn = 26.4% Severidade** (Maior concentração)
   - 492.489 colisões = 22.2% do total
   - Recomendação: Task Force dedicado

4. **Período 14h-18h = 27% de Colisões**
   - Pico: 16h-17h (158.146 colisões)
   - Recomendação: Reforço policial

5. **Paradoxo 2020-2025** (Paradoxal)
   - Colisões ↓ 46%, Mortalidade ↑ 103%
   - Hipótese: Maior velocidade em vias descongestas

### **Análise Econômica**
- Custo total: $75.9B em 13 anos
- Investimento recomendado: $350M/ano
- ROI esperado: 11x-24x
- Payback: < 1 mês
- Vidas salvas/ano: 68-268

---

## 📈 Estrutura dos Dados

O DataFrame após carregar tem as seguintes colunas principais:

```python
df.columns = [
    'CRASH DATE',                    # Data do acidente
    'CRASH TIME',                    # Hora do acidente
    'BOROUGH',                       # Bairro (Brooklyn, Queens, etc)
    'LATITUDE', 'LONGITUDE',         # Coordenadas geográficas
    'NUMBER OF PERSONS INJURED',     # Total de feridos
    'NUMBER OF PERSONS KILLED',      # Total de mortos
    'NUMBER OF PEDESTRIANS INJURED', # Pedestres feridos
    'NUMBER OF PEDESTRIANS KILLED',  # Pedestres mortos
    'NUMBER OF CYCLIST INJURED',     # Ciclistas feridos
    'NUMBER OF CYCLIST KILLED',      # Ciclistas mortos
    'NUMBER OF MOTORIST INJURED',    # Motoristas feridos
    'NUMBER OF MOTORIST KILLED',     # Motoristas mortos
    'CONTRIBUTING FACTOR VEHICLE 1', # Fator contribuinte primário
    'VEHICLE TYPE CODE 1',           # Tipo de veículo
    ...
]
```

---

## 🛠️ Troubleshooting

### **Erro: "FileNotFoundError"**
Certifique-se de que o arquivo CSV está no diretório correto:
```bash
ls -la Motor_Vehicle_Collisions_LIMPO.csv
```

### **Erro: "KeyError: 'CRASH DATE'"**
Execute o script de correção:
```bash
python3 00_fix_columns.py
```

### **Erro: "ModuleNotFoundError: pandas"**
Instale as dependências:
```bash
pip install pandas numpy
```

### **Execução Lenta**
Isto é normal para 2.2M registros. Primeira execução pode levar 2-3 minutos.
Resultados serão armazenados em memória para rapidez.

---

## 🎁 Dados de Saída

Você pode capturar os resultados em variáveis Python:

```python
import pandas as pd
from analise_principal import *

df = carregar_dados('Motor_Vehicle_Collisions_LIMPO.csv')
kpis = analise_geral(df)
bairros = analise_por_bairro(df)
vitimas = analise_vitimas(df)

# Agora você tem:
print(kpis['total_colisoes'])           # 2.216.469
print(bairros['BROOKLYN'])              # 492.489
print(vitimas['pedestres'])             # 133.610
```

---

## 📚 Documentação Adicional

Veja também:
- `INDEX_DASHBOARDS.html` - Dashboards visuais interativos
- `DASHBOARD_2_VULNERABILIDADE_RECOMENDACOES.html` - Análise detalhada
- `DASHBOARD_3_IMPACTO_ECONOMICO.html` - Justificativa financeira
- `README_DASHBOARDS.md` - Guia de apresentação

---

## 👨‍💻 Como Estender

Você pode criar suas próprias análises usando as funções fornecidas:

```python
import pandas as pd
from analise_principal import carregar_dados

df = carregar_dados('Motor_Vehicle_Collisions_LIMPO.csv')

# Sua análise customizada
brooklyn = df[df['BOROUGH'] == 'BROOKLYN']
print(f"Acidentes em Brooklyn: {len(brooklyn):,}")

# Filtrar por ano
ano_2024 = df[df['ANO'] == 2024]
print(f"Acidentes em 2024: {len(ano_2024):,}")

# Analisar causa específica
desatencao = df[df['CONTRIBUTING FACTOR VEHICLE 1'].str.contains('Inattention', na=False)]
print(f"Acidentes por desatenção: {len(desatencao):,}")
```

---

## ✅ Checklist de Uso

- [ ] Verifiquei que pandas e numpy estão instalados
- [ ] Coloquei o arquivo CSV no diretório correto
- [ ] Executei `00_fix_columns.py` para preparar dados
- [ ] Testei `EXECUTAR_ANALISE_COMPLETA.py`
- [ ] Explorei os 3 módulos individualmente
- [ ] Capturei os dados em variáveis Python para análise customizada
- [ ] Consultei os dashboards HTML para visualizações

---

## 📞 Suporte

Se encontrar problemas:

1. Verifique que o arquivo CSV existe e tem 2.216.469 linhas
2. Certifique-se de que pandas/numpy estão instalados
3. Execute `00_fix_columns.py` se houver erros de coluna
4. Tente executar um módulo por vez para identificar o problema

---

**Versão:** 1.0
**Data:** 2025-10-30
**Python:** 3.8+
**Dependências:** pandas, numpy

🚗 Análise Completa de Segurança Viária NYC em Python
