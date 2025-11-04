"""
SCRIPT DE CORREÇÃO - Fix Coluna de Data
========================================

Corrige o nome da coluna CRASH DATE que está com problema de encoding
"""

import pandas as pd

# Carregar com encoding específico
df = pd.read_csv('/Users/davisouza/Documents/Trabalho Facul Python /Motor_Vehicle_Collisions_-_Crashes.csv',
                  low_memory=False, encoding='utf-8')

# Renomear colunas problemáticas
df.columns = df.columns.str.strip()  # Remove espaços
print("Colunas originais:")
print(list(df.columns))

# Verificar e corrigir se necessário
if 'çaCRASH DATE' in df.columns:
    df.rename(columns={'çaCRASH DATE': 'CRASH DATE'}, inplace=True)
    print("\n✓ Coluna 'çaCRASH DATE' renomeada para 'CRASH DATE'")

# Salvar com colunas corrigidas
df.to_csv('/Users/davisouza/Documents/Trabalho Facul Python /Motor_Vehicle_Collisions_LIMPO.csv', index=False)
print("✓ Arquivo limpo salvo: Motor_Vehicle_Collisions_LIMPO.csv")

print("\nNovas colunas:")
print(list(df.columns))
print(f"\nTotal de linhas: {len(df):,}")
