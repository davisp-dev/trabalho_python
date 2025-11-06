# 🚀 BMAD Quick Start - Comece em 5 Minutos

## O que é BMAD?

**BMAD** = Breakthrough Method for Agile AI Driven Development

É uma metodologia que melhora a colaboração humano-IA através de:
- 🤝 **Collaboration** - Você + Claude trabalhando juntos
- ⚙️ **Optimization** - Processos comprovados
- 🤔 **Reflection** - Perguntas estratégicas
- 🎯 **Engine** - Fluxo estruturado

---

## Os 3 Tracks de Desenvolvimento

### 🏃 Track 1: Quick Flow (Rápido)
**Quando usar:** Bug simples, ajuste CSS, label errado
**Tempo:** < 30 minutos
**Documentação:** Nenhuma formal (só o commit)
**Comando:** `QUICK_FIX: [descrição]`

**Exemplo:**
```
QUICK_FIX: Corrigir alinhamento do botão no mobile
```

---

### 🏗️ Track 2: BMad Method (Padrão)
**Quando usar:** Nova feature, melhoria, análise adicional
**Tempo:** 1-4 horas
**Documentação:** PRD, Arquitetura, UX
**Comando:** `BMAD: [descrição detalhada]`

**Fluxo:**
```
1. Análise (entender contexto)
2. Planejamento (definir escopo)
3. Solução (design + arquitetura)
4. Implementação (código + testes)
```

**Exemplo:**
```
BMAD: Adicionar filtros interativos aos dashboards
- Permitir filtrar por data range
- Permitir filtrar por bairro
- Persistir seleção no localStorage
```

---

### 🏢 Track 3: Enterprise (Complexo)
**Quando usar:** Grande funcionalidade, mudança arquitetural
**Tempo:** 4+ horas
**Documentação:** PRD + Arquitetura + UX + Segurança + DevOps + Testes
**Comando:** `ENTERPRISE: [visão estratégica]`

**Exemplo:**
```
ENTERPRISE: Implementar pipeline de atualização automática de dados
- Sincronizar com API NYC daily
- Rodar análises automatically
- Notificar via email quando insights críticos surgem
```

---

## 4 Fases de Desenvolvimento

```
┌─────────────────────────────────────────────┐
│ FASE 1: ANÁLISE (5-15 min)                  │
│ - Entender contexto                         │
│ - Explorar codebase                         │
│ - Listar dependências                       │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ FASE 2: PLANEJAMENTO (10-30 min)            │
│ - Definir objetivo SMART                    │
│ - Listar requisitos                         │
│ - Identificar riscos                        │
│ - Criar BMAD Plan (tarefas)                │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ FASE 3: SOLUÇÃO (20-60 min)                 │
│ - Design UX/mockups                         │
│ - Arquitetura técnica                       │
│ - PRD com user stories                      │
│ (Skip se Quick Flow)                        │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ FASE 4: IMPLEMENTAÇÃO (iterativa)           │
│ - Código em pequenos passos                 │
│ - Testes a cada passo                       │
│ - Documentação                              │
│ - Commit & feedback loop                    │
└─────────────────────────────────────────────┘
```

---

## 5 Passos para Começar

### Passo 1: Defina Sua Tarefa

**Formato sugerido:**
```
Eu quero [AÇÃO] porque [RAZÃO] para [BENEFÍCIO]
```

**Exemplos:**
- "Eu quero adicionar filtros porque usuários precisam de análises customizadas para tomar melhores decisões"
- "Eu quero corrigir o CSS porque o layout fica ruim no mobile para que governador veja bem apresentação"

---

### Passo 2: Escolha o Track

**Quick Flow se:**
- ✅ É um bug simples
- ✅ É um ajuste visual (CSS, label)
- ✅ Leva < 30 minutos
- ✅ Não afeta arquitetura

**BMad Method se:**
- ✅ É uma nova feature
- ✅ É uma melhoria significativa
- ✅ Afeta múltiplos arquivos
- ✅ Leva 1-4 horas

**Enterprise se:**
- ✅ É uma mudança arquitetural
- ✅ Envolve segurança/performance crítica
- ✅ Afeta múltiplos sistemas
- ✅ Leva 4+ horas

---

### Passo 3: Use o Comando Certo

**Para Quick Flow:**
```
QUICK_FIX: Corrigir alinhamento do header no mobile
```

**Para BMad Method:**
```
BMAD: Adicionar filtros interativos aos dashboards
- Filtrar por data range
- Filtrar por bairro
- Salvar preferências
```

**Para Enterprise:**
```
ENTERPRISE: Implementar CI/CD com GitHub Actions
- Auto-rodar testes no push
- Auto-deploy em staging
- Notificar em slack
```

---

### Passo 4: Claude Propõe BMAD Plan

Claude irá criar um plano estruturado com:
- ✅ Análise do contexto
- ✅ Planejamento de tarefas
- ✅ Solução (design + arquitetura)
- ✅ Implementação (código)

---

### Passo 5: Aprove, Execute, Valide

**Você:**
1. Lê o BMAD Plan
2. Aprova ou sugere ajustes
3. Valida o resultado final
4. Aprova merge para main

**Claude:**
1. Implementa iterativamente
2. Mostra progresso com TodoWrite
3. Testa cada passo
4. Prepara commit com boa descrição

---

## 📝 Exemplo: Tarefa Completa com BMAD

### Você Pede:
```
BMAD: Adicionar filtro por bairro nos dashboards
```

### Claude Responde:

**FASE 1: ANÁLISE**
- ✅ 4 dashboards HTML encontrados
- ✅ Chart.js usado para gráficos
- ✅ Dados em JavaScript arrays
- ✅ localStorage disponível

**FASE 2: PLANEJAMENTO**
- Tarefa 1: Adicionar UI de filtro
- Tarefa 2: Implementar lógica de filtro
- Tarefa 3: Persistir escolha
- Tarefa 4: Testar em todos dashboards
- Timeline: 2 horas
- Riscos: Compatibilidade IE (baixa prioridade)

**FASE 3: SOLUÇÃO**
- Mockup do filtro (dropdown + checkboxes)
- Fluxo de dados (UI → filter logic → chart update)
- Tecnologia: HTML select + JavaScript vanilla

**FASE 4: IMPLEMENTAÇÃO**
```
[ ] Tarefa 1: Adicionar UI
[ ] Tarefa 2: Lógica de filtro
[ ] Tarefa 3: Persistência
[ ] Tarefa 4: Testes
[ ] Tarefa 5: Documentação
[ ] Commit & Push
```

### Você Aprova:
```
Tudo certo! Faz assim mesmo.
```

### Claude Executa:
```
1. Implementa Tarefa 1
2. Mostra resultado
3. "Tarefa 1 completa! Seguindo para Tarefa 2..."
4. Repete até todas tarefas
5. Faz commit descritivo
6. Mostra resultado final
```

### Você Valida:
```
Perfeito! Funcionou como esperado.
Commit pronto para merge.
```

---

## 🎯 Comandos Rápidos

### Para Iniciar Trabalho

```
QUICK_FIX: [descrição curta]
→ Rápido, direto, sem planejamento formal

BMAD: [descrição detalhada com contexto]
→ Planejamento completo + implementação

ENTERPRISE: [visão de negócio + requisitos]
→ Planejamento enterprise + segurança + devops
```

### Durante o Trabalho

```
ANALISAR: [componente/arquivo]
→ Entender contexto antes de mexer

REFLETIR: [questão estratégica]
→ Discussão estratégica antes de implementar

HELP: [tema]
→ Ajuda com metodologia BMAD
```

### Para Controle

```
STATUS:
→ Mostrar status do BMAD Plan atual

PRÓXIMO:
→ Qual é a próxima tarefa?

REVISAR:
→ Code review do que foi feito
```

---

## 📊 Checklist Diário

Use isto para manter foco:

- [ ] **De Manhã:**
  - [ ] Defini objetivo do dia?
  - [ ] Escolhi o track?
  - [ ] Comuniquei tarefa?

- [ ] **Durante o Dia:**
  - [ ] Sigo o BMAD Plan?
  - [ ] Documento decisões?
  - [ ] Teste cada tarefa?

- [ ] **Ao Final:**
  - [ ] Todas tarefas completadas?
  - [ ] Documentação atualizada?
  - [ ] Commit descritivo feito?
  - [ ] Preparado para code review?

---

## 💡 Dicas Práticas

### ✅ Boas Práticas BMAD

1. **Seja específico**
   - ❌ "Melhorar dashboard"
   - ✅ "Reduzir tempo de carregamento de 3s para <1s"

2. **Documente decisões**
   - ✅ "Escolhemos X porque Y"

3. **Use checklists**
   - ✅ Facilita rastreamento
   - ✅ Mostra progresso

4. **Faça commits frequentes**
   - ✅ Pequenos passos = menos risco

5. **Solicite feedback cedo**
   - ✅ Evita retrabalho

### ❌ Erros Comuns

1. **Pular planejamento**
   - ❌ Gasta mais tempo depois
   - ✅ 10 min planejamento = 30 min economia

2. **Fazer tudo de uma vez**
   - ❌ Difícil testar e debugar
   - ✅ Break em tarefas pequenas

3. **Esquecer documentação**
   - ❌ Ninguém entende depois
   - ✅ Documente enquanto implementa

4. **Commit com descrição vaga**
   - ❌ "Fix bug" (qual bug?)
   - ✅ "Fix bug de filtro que não salvava seleção"

---

## 🎓 Próximos Passos

### Agora que sabe BMAD:

1. **Defina sua primeira tarefa:**
   ```
   BMAD: [Sua tarefa aqui]
   ```

2. **Deixe Claude propor um plano**

3. **Aprove e execute iterativamente**

4. **Valide resultado final**

5. **Commit e push**

---

## 📚 Recursos Adicionais

- **Documentação Completa:** `BMAD_METHODOLOGY.md`
- **Templates Prontos:** `BMAD_TEMPLATES.md`
- **BMAD Oficial:** https://github.com/bmad-code-org/BMAD-METHOD

---

## 🚀 Comece Agora!

Qual é sua primeira tarefa com BMAD?

**Exemplos:**
1. `QUICK_FIX: Corrigir espaçamento do footer`
2. `BMAD: Adicionar busca por colisão ID nos dashboards`
3. `ENTERPRISE: Implementar pipeline de dados automático`

**Comunique comigo! 🎯**
