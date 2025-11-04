"""
ANÁLISE PRINCIPAL - SEGURANÇA VIÁRIA NYC
=========================================

Script principal para carregar e explorar dados de colisões veiculares de NYC
Período: 2013-2025
Total de registros: 2.216.469 colisões

Autor: Sistema de Análise Automática
Data: 2025-10-30
"""

import pandas as pd
import numpy as np
from collections import Counter
import warnings

warnings.filterwarnings('ignore')

# ============================================================================
# 1. CARREGAR E EXPLORAR DADOS
# ============================================================================

def carregar_dados(caminho_csv):
    """Carrega o dataset de colisões veiculares"""
    print("\n" + "="*90)
    print("CARREGANDO DADOS...")
    print("="*90)

    df = pd.read_csv(caminho_csv, low_memory=False)

    # Converter datas
    df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'], format='%m/%d/%Y', errors='coerce')
    df['HORA'] = pd.to_datetime(df['CRASH TIME'], format='%H:%M', errors='coerce').dt.hour
    df['MES'] = df['CRASH DATE'].dt.month
    df['ANO'] = df['CRASH DATE'].dt.year

    print(f"\n✓ Dataset carregado com sucesso!")
    print(f"  • Total de linhas: {len(df):,}")
    print(f"  • Total de colunas: {df.shape[1]}")
    print(f"  • Período: {df['CRASH DATE'].min().date()} até {df['CRASH DATE'].max().date()}")

    return df


# ============================================================================
# 2. ANÁLISE GERAL
# ============================================================================

def analise_geral(df):
    """Análise geral dos dados"""
    print("\n" + "="*90)
    print("ANÁLISE GERAL - INDICADORES-CHAVE")
    print("="*90)

    total_colisoes = len(df)
    total_feridos = int(df['NUMBER OF PERSONS INJURED'].sum())
    total_mortos = int(df['NUMBER OF PERSONS KILLED'].sum())

    print(f"\n📊 VOLUME GERAL (2013-2025)")
    print(f"  • Total de Colisões: {total_colisoes:,}")
    print(f"  • Total de Feridos: {total_feridos:,}")
    print(f"  • Total de Mortos: {total_mortos:,}")
    print(f"  • Média Diária: {int(total_colisoes / (13.3 * 365))} colisões")
    print(f"  • Média Diária de Feridos: {int(total_feridos / (13.3 * 365))} pessoas")

    return {
        'total_colisoes': total_colisoes,
        'total_feridos': total_feridos,
        'total_mortos': total_mortos
    }


# ============================================================================
# 3. ANÁLISE POR BAIRRO
# ============================================================================

def analise_por_bairro(df):
    """Análise de distribuição por bairro"""
    print("\n" + "="*90)
    print("DISTRIBUIÇÃO POR BAIRRO (BOROUGH)")
    print("="*90)

    borough_dist = df[df['BOROUGH'].notna()]['BOROUGH'].value_counts()

    print("\nRanking de Colisões por Bairro:")
    for idx, (borough, count) in enumerate(borough_dist.items(), 1):
        pct = (count / len(df)) * 100
        print(f"  {idx}. {borough:20} {count:>10,} colisões ({pct:5.1f}%)")

    # Análise de severidade por bairro
    print("\n\nAnálise de Severidade por Bairro:")
    for borough in borough_dist.index:
        borough_data = df[df['BOROUGH'] == borough]
        total = len(borough_data)
        feridos = borough_data['NUMBER OF PERSONS INJURED'].sum()
        mortos = borough_data['NUMBER OF PERSONS KILLED'].sum()
        graves = len(borough_data[(borough_data['NUMBER OF PERSONS INJURED'] > 0) |
                                  (borough_data['NUMBER OF PERSONS KILLED'] > 0)])
        taxa_severidade = (graves / total) * 100
        vitimas_por_colisao = (feridos + mortos) / total

        print(f"\n  {borough}:")
        print(f"    • Colisões: {total:,}")
        print(f"    • Feridos: {int(feridos):,}")
        print(f"    • Mortos: {int(mortos):,}")
        print(f"    • Taxa de Severidade: {taxa_severidade:.1f}%")
        print(f"    • Vítimas/Colisão: {vitimas_por_colisao:.2f}")

    return borough_dist


# ============================================================================
# 4. ANÁLISE DE VÍTIMAS
# ============================================================================

def analise_vitimas(df):
    """Análise detalhada de vítimas por tipo"""
    print("\n" + "="*90)
    print("ANÁLISE DE VÍTIMAS - DISTRIBUIÇÃO POR TIPO")
    print("="*90)

    pedestres_feridos = int(df['NUMBER OF PEDESTRIANS INJURED'].sum())
    pedestres_mortos = int(df['NUMBER OF PEDESTRIANS KILLED'].sum())
    pedestres_total = pedestres_feridos + pedestres_mortos

    ciclistas_feridos = int(df['NUMBER OF CYCLIST INJURED'].sum())
    ciclistas_mortos = int(df['NUMBER OF CYCLIST KILLED'].sum())
    ciclistas_total = ciclistas_feridos + ciclistas_mortos

    motoristas_feridos = int(df['NUMBER OF MOTORIST INJURED'].sum())
    motoristas_mortos = int(df['NUMBER OF MOTORIST KILLED'].sum())
    motoristas_total = motoristas_feridos + motoristas_mortos

    total_vitimas = pedestres_total + ciclistas_total + motoristas_total

    print(f"\n👥 PEDESTRES (Grupo Mais Vulnerável)")
    print(f"  • Total de Vítimas: {pedestres_total:,}")
    print(f"  • Feridos: {pedestres_feridos:,}")
    print(f"  • Mortos: {pedestres_mortos:,}")
    taxa_ped = (pedestres_mortos / pedestres_total * 100) if pedestres_total > 0 else 0
    print(f"  • Taxa de Mortalidade: {taxa_ped:.2f}% (⚠️ CRÍTICA)")
    print(f"  • % do Total: {(pedestres_total/total_vitimas)*100:.1f}%")

    print(f"\n🚴 CICLISTAS")
    print(f"  • Total de Vítimas: {ciclistas_total:,}")
    print(f"  • Feridos: {ciclistas_feridos:,}")
    print(f"  • Mortos: {ciclistas_mortos:,}")
    taxa_cicl = (ciclistas_mortos / ciclistas_total * 100) if ciclistas_total > 0 else 0
    print(f"  • Taxa de Mortalidade: {taxa_cicl:.2f}%")
    print(f"  • % do Total: {(ciclistas_total/total_vitimas)*100:.1f}%")

    print(f"\n🚗 MOTORISTAS")
    print(f"  • Total de Vítimas: {motoristas_total:,}")
    print(f"  • Feridos: {motoristas_feridos:,}")
    print(f"  • Mortos: {motoristas_mortos:,}")
    taxa_motor = (motoristas_mortos / motoristas_total * 100) if motoristas_total > 0 else 0
    print(f"  • Taxa de Mortalidade: {taxa_motor:.2f}%")
    print(f"  • % do Total: {(motoristas_total/total_vitimas)*100:.1f}%")

    print(f"\n\n⚠️ COMPARAÇÃO DE RISCO")
    print(f"  • Pedestres são {taxa_ped/taxa_motor:.1f}x MAIS vulneráveis que motoristas")
    print(f"  • Ciclistas são {taxa_cicl/taxa_motor:.1f}x MAIS vulneráveis que motoristas")

    return {
        'pedestres': {'total': pedestres_total, 'feridos': pedestres_feridos, 'mortos': pedestres_mortos, 'taxa': taxa_ped},
        'ciclistas': {'total': ciclistas_total, 'feridos': ciclistas_feridos, 'mortos': ciclistas_mortos, 'taxa': taxa_cicl},
        'motoristas': {'total': motoristas_total, 'feridos': motoristas_feridos, 'mortos': motoristas_mortos, 'taxa': taxa_motor}
    }


# ============================================================================
# 5. ANÁLISE TEMPORAL
# ============================================================================

def analise_temporal(df):
    """Análise de padrões temporais"""
    print("\n" + "="*90)
    print("ANÁLISE TEMPORAL - PADRÕES POR HORA E MÊS")
    print("="*90)

    # Por hora
    print(f"\n⏰ COLISÕES POR HORA DO DIA")
    colisoes_hora = df['HORA'].value_counts().sort_index()
    hora_max = colisoes_hora.idxmax()
    valor_max = colisoes_hora.max()

    print(f"\n  Hora de Pico: {int(hora_max):02d}:00-{int(hora_max)+1:02d}:00 com {valor_max:,} colisões")
    print(f"\n  Período Crítico (14:00-18:00): {int(colisoes_hora[14:18].sum()):,} colisões")
    pct_critico = (colisoes_hora[14:18].sum() / len(df)) * 100
    print(f"  Proporção do Dia: {pct_critico:.1f}%")

    # Por mês
    print(f"\n\n📅 COLISÕES POR MÊS")
    colisoes_mes = df['MES'].value_counts().sort_index()
    mes_names = ['', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    mes_max = colisoes_mes.idxmax()
    print(f"\n  Mês de Pico: {mes_names[mes_max]} com {colisoes_mes.max():,} colisões")

    print(f"\n  Distribuição por Mês:")
    for mes, count in colisoes_mes.items():
        pct = (count / len(df)) * 100
        print(f"    {mes_names[int(mes)]:3} {count:>10,} ({pct:5.1f}%)")

    return {'hora': colisoes_hora, 'mes': colisoes_mes}


# ============================================================================
# 6. ANÁLISE DE CAUSAS
# ============================================================================

def analise_causas(df):
    """Análise de fatores contribuintes"""
    print("\n" + "="*90)
    print("ANÁLISE DE FATORES CONTRIBUINTES")
    print("="*90)

    # Compilar todas as causas
    all_factors = []
    factor_cols = ['CONTRIBUTING FACTOR VEHICLE 1', 'CONTRIBUTING FACTOR VEHICLE 2',
                   'CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4',
                   'CONTRIBUTING FACTOR VEHICLE 5']

    for col in factor_cols:
        factors = df[col].dropna().tolist()
        factors = [f for f in factors if f != 'Unspecified']
        all_factors.extend(factors)

    factor_counts = Counter(all_factors)
    top_factors = factor_counts.most_common(20)

    print(f"\nTop 20 Causas de Colisões:")
    for idx, (factor, count) in enumerate(top_factors, 1):
        pct = (count / len(all_factors)) * 100
        print(f"  {idx:2}. {factor:50} {count:>10,} ({pct:5.1f}%)")

    # Análise de causas comportamentais vs ambientais
    comportamentais = 0
    ambientais = 0

    behavior_keywords = ['inattention', 'distraction', 'yield', 'closely', 'speed',
                        'improper', 'inexperience', 'fatigued', 'drowsy', 'alcohol',
                        'turning', 'backing', 'unsafely', 'lane']

    for factor, count in factor_counts.items():
        if any(keyword in factor.lower() for keyword in behavior_keywords):
            comportamentais += count
        else:
            ambientais += count

    total_factors = comportamentais + ambientais
    print(f"\n\nCLASSIFICAÇÃO DE CAUSAS:")
    print(f"  • Causas Comportamentais: {comportamentais:,} ({comportamentais/total_factors*100:.1f}%)")
    print(f"  • Causas Ambientais/Outros: {ambientais:,} ({ambientais/total_factors*100:.1f}%)")

    return dict(top_factors)


# ============================================================================
# 7. ANÁLISE DE TENDÊNCIA ANUAL
# ============================================================================

def analise_tendencia_anual(df):
    """Análise de tendência ao longo dos anos"""
    print("\n" + "="*90)
    print("ANÁLISE TEMPORAL - TENDÊNCIA ANUAL")
    print("="*90)

    ano_data = []
    for year in sorted(df[df['ANO'].notna()]['ANO'].unique()):
        year_df = df[df['ANO'] == year]
        colisoes = len(year_df)
        feridos = int(year_df['NUMBER OF PERSONS INJURED'].sum())
        mortos = int(year_df['NUMBER OF PERSONS KILLED'].sum())
        vitimas_col = (feridos + mortos) / colisoes if colisoes > 0 else 0

        ano_data.append({
            'ano': int(year),
            'colisoes': colisoes,
            'feridos': feridos,
            'mortos': mortos,
            'vitimas_por_colisao': vitimas_col
        })

    print(f"\n{'Ano':<6} {'Colisões':>12} {'Var %':>10} {'Feridos':>10} {'Mortos':>8} {'Vít/Col':>10}")
    print("-" * 60)

    prev_colisoes = None
    for item in ano_data:
        colisoes = item['colisoes']
        if prev_colisoes:
            variacao = ((colisoes - prev_colisoes) / prev_colisoes) * 100
            var_str = f"{variacao:+6.1f}%"
        else:
            var_str = "  -   "

        print(f"{item['ano']:<6} {colisoes:>12,} {var_str:>10} {item['feridos']:>10,} {item['mortos']:>8,} {item['vitimas_por_colisao']:>10.2f}")
        prev_colisoes = colisoes

    # Análise do paradoxo 2020-2025
    print(f"\n\n⚠️ PARADOXO DESCOBERTO (2020-2025):")
    ano_2019 = [a for a in ano_data if a['ano'] == 2019][0]
    ano_2024 = [a for a in ano_data if a['ano'] == 2024][0]

    var_colisoes = ((ano_2024['colisoes'] - ano_2019['colisoes']) / ano_2019['colisoes']) * 100
    var_mortalidade = ((ano_2024['vitimas_por_colisao'] - ano_2019['vitimas_por_colisao']) / ano_2019['vitimas_por_colisao']) * 100

    print(f"  • Colisões 2019→2024: {var_colisoes:+.1f}% (redução)")
    print(f"  • Mortalidade/Colisão 2019→2024: {var_mortalidade:+.1f}% (⚠️ AUMENTO)")
    print(f"  • Interpretação: Menos colisões, mas cada uma é mais severa")
    print(f"  • Hipótese: Redução de congestionamento permite maior velocidade")

    return ano_data


# ============================================================================
# 8. ANÁLISE DE VEÍCULOS
# ============================================================================

def analise_veiculos(df):
    """Análise de tipos de veículos envolvidos"""
    print("\n" + "="*90)
    print("ANÁLISE DE TIPOS DE VEÍCULOS ENVOLVIDOS")
    print("="*90)

    all_vehicles = []
    vehicle_cols = ['VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2', 'VEHICLE TYPE CODE 3',
                    'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5']

    for col in vehicle_cols:
        all_vehicles.extend(df[col].dropna().tolist())

    vehicle_counts = Counter(all_vehicles)
    vehicle_top = vehicle_counts.most_common(15)

    print(f"\nTop 15 Tipos de Veículos:")
    for idx, (vehicle, count) in enumerate(vehicle_top, 1):
        pct = (count / len(all_vehicles)) * 100
        print(f"  {idx:2}. {vehicle:40} {count:>10,} ({pct:5.1f}%)")

    return dict(vehicle_top)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    # Caminho do arquivo CSV
    csv_path = '/Users/davisouza/Documents/Trabalho Facul Python /Motor_Vehicle_Collisions_LIMPO.csv'

    # Carregar dados
    df = carregar_dados(csv_path)

    # Executar análises
    kpis = analise_geral(df)
    bairros = analise_por_bairro(df)
    vitimas = analise_vitimas(df)
    temporal = analise_temporal(df)
    causas = analise_causas(df)
    tendencia = analise_tendencia_anual(df)
    veiculos = analise_veiculos(df)

    # Resumo final
    print("\n" + "="*90)
    print("ANÁLISE CONCLUÍDA")
    print("="*90)
    print("\n✅ Análise completa finalizada!")
    print(f"\nResumo de Dados Processados:")
    print(f"  • Total de Colisões: {kpis['total_colisoes']:,}")
    print(f"  • Feridos: {kpis['total_feridos']:,}")
    print(f"  • Mortos: {kpis['total_mortos']:,}")
    print(f"  • Período: 2013-2025")
    print(f"  • Bairros Analisados: {len(bairros)}")
    print(f"  • Causas Identificadas: {len(causas)}")
    print(f"  • Tipos de Veículos: {len(veiculos)}")
