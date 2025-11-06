# 📋 BMAD Templates - Modelos Prontos para Usar

## Template 1: BMAD Plan Completo (BMad Method Track)

```markdown
# [TÍTULO DA TAREFA]

## 🔍 FASE 1: ANÁLISE

### Contexto do Negócio
**O que:** [Descrição do que precisa ser feito]
**Por que:** [Razão/Valor de negócio]
**Para quem:** [Stakeholder/Usuário]
**Impacto:** [Como mede sucesso?]

### Exploração Técnica
**Arquivos afetados:**
- [ ] [arquivo 1]
- [ ] [arquivo 2]

**Dependências:**
- [ ] [dependência 1]
- [ ] [dependência 2]

**Arquitetura atual:**
[Descrever como funciona agora]

---

## 📋 FASE 2: PLANEJAMENTO

### Objetivo SMART
[Específico, Mensurável, Atingível, Relevante, Temporal]

### Escopo Definido
**Incluído ✅:**
- [ ] Requisito 1
- [ ] Requisito 2

**Excluído ❌:**
- [ ] Requisito fora do escopo 1
- [ ] Requisito fora do escopo 2

### Timeline & Esforço
- **Tempo estimado:** [X horas]
- **Complexidade:** [Baixa / Média / Alta]
- **Track:** [Quick Flow / BMad Method / Enterprise]

### Riscos & Mitigações
| Risco | Prob. | Impacto | Mitigação |
|-------|--------|---------|-----------|
| [Risco 1] | Alta | Alto | [Mitigação] |
| [Risco 2] | Média | Médio | [Mitigação] |

### Dependências Externas
- [ ] [Dep 1] - Status: [✅ OK / ⏳ Pendente]
- [ ] [Dep 2] - Status: [✅ OK / ⏳ Pendente]

---

## 🎨 FASE 3: SOLUÇÃO

### PRD - Product Requirements Document

**User Stories:**
```
Como [usuário],
quero [funcionalidade],
para que [benefício].

Critérios de aceitação:
- [ ] Critério 1
- [ ] Critério 2
- [ ] Critério 3
```

**Requisitos Funcionais:**
1. [RF1] - [Descrição]
2. [RF2] - [Descrição]

**Requisitos Não-Funcionais:**
1. [RNF1] - [Descrição] (Performance, Segurança, etc.)
2. [RNF2] - [Descrição]

### Arquitetura & Design

**Diagrama de Componentes:**
```
[Incluir diagrama ASCII ou descrição]
```

**Fluxo de Dados:**
```
Input → [Processamento] → Output
```

**Decisões Arquiteturais:**
1. **Decision 1:** [Opção A] vs [Opção B]
   - Escolhida: [Opção A] porque [razão]
   - Trade-off: [Benefício] vs [Custo]

### UX/Design

**Wireframe:**
```
[Descrição visual ou ASCII art]
```

**Considerações de UX:**
- [ ] Acessibilidade (WCAG)
- [ ] Responsividade (Mobile/Desktop)
- [ ] Consistência com design atual
- [ ] Performance percebida

---

## 🛠️ FASE 4: IMPLEMENTAÇÃO

### Breakdown de Tarefas
```
[ ] Tarefa 1: [Descrição]
    - Sub-tarefa 1.1
    - Sub-tarefa 1.2

[ ] Tarefa 2: [Descrição]
    - Sub-tarefa 2.1

[ ] Testes
    - [ ] Teste unitário
    - [ ] Teste integração
    - [ ] Teste aceitação

[ ] Documentação
    - [ ] README atualizado
    - [ ] Código comentado
    - [ ] Changelog

[ ] Deploy/Git
    - [ ] Commit com mensagem clara
    - [ ] Code review
    - [ ] Merge para main
```

### Critérios de Aceitação Técnica
- [ ] Feature implementada conforme PRD
- [ ] Testes passam (100% cobertura no novo código)
- [ ] Documentação atualizada
- [ ] Sem warnings/erros no build
- [ ] Performance aceitável
- [ ] Git commit com descrição clara

### Verificação Final
- [ ] Funciona em ambiente local
- [ ] Funciona em ambiente staging
- [ ] Testes passam
- [ ] Documentação está clara
- [ ] Code review aprovado
- [ ] Pronto para produção

---

## 📊 Métricas de Sucesso

**Métrica 1:** [O que medir?]
- Baseline: [Valor anterior]
- Target: [Objetivo]
- Resultado: [Será preenchido após implementação]

**Métrica 2:** [O que medir?]
- Baseline: [Valor anterior]
- Target: [Objetivo]
- Resultado: [Será preenchido após implementação]

---

## 📝 Notas e Decisões

[Registrar decisões tomadas durante o processo]

---

## 🚀 Status da Tarefa

**Atual:** [Análise / Planejamento / Solução / Implementação / Completa]
**Data Criação:** [Data]
**Última Atualização:** [Data]
**Estimado Conclusão:** [Data]
```

---

## Template 2: Quick Flow (Bug Fix Rápido)

```markdown
# [BUG TITLE]

## 📍 Problema
**Descrição:** [O que está quebrado?]
**Severidade:** [Crítica / Alta / Média / Baixa]
**Impacto:** [Quantos usuários?]
**Sistema Afetado:** [Qual arquivo/módulo?]

## 🔍 Causa Raiz
[Por que ocorre?]

## ✅ Solução
**Arquivo(s):**
- [ ] [arquivo 1]
- [ ] [arquivo 2]

**Mudança:**
[Descrição técnica da mudança]

## 🧪 Verificação
- [ ] Bug foi reproduzido
- [ ] Solução implementada
- [ ] Bug não ocorre mais
- [ ] Sem regressões

## 🔄 Prevenção
[Como evitar no futuro?]

## 📦 Deploy
- [ ] Commit feito
- [ ] Merged para main
- [ ] Pronto para produção
```

---

## Template 3: Enterprise Track (Grande Funcionalidade)

```markdown
# [GRANDE FUNCIONALIDADE]

## 🏢 Visão Estratégica

### Justificativa de Negócio
**Problema:** [Qual problema resolve?]
**Oportunidade:** [Qual valor cria?]
**ROI Estimado:** [Se aplicável]
**Timeline Crítica:** [Há deadline?]

### Stakeholders
- [ ] [Stakeholder 1] - [Função/Expectativa]
- [ ] [Stakeholder 2] - [Função/Expectativa]

---

## 📋 ANÁLISE & PLANEJAMENTO
[Use template completo acima]

---

## 🔐 Considerações de Segurança
- [ ] OWASP Top 10 verificado
- [ ] Autenticação/Autorização
- [ ] Validação de entrada
- [ ] Proteção de dados sensíveis
- [ ] Auditoria/Logging

## 🚀 Considerações de DevOps
- [ ] CI/CD pipeline
- [ ] Ambiente de teste
- [ ] Monitoramento
- [ ] Rollback plan
- [ ] Documentação de Deploy

## 🧪 Estratégia de Testes
- [ ] Testes unitários (>80% cobertura)
- [ ] Testes integração
- [ ] Testes e2e
- [ ] Performance testing
- [ ] Load testing

---

## 📊 Métricas & Monitoramento
[Define observabilidade pós-deploy]

---

## 🎯 Go-Live Checklist
- [ ] Code review aprovado
- [ ] Testes passam 100%
- [ ] Documentação completa
- [ ] Monitoring ativo
- [ ] Rollback plan preparado
- [ ] Comunicação stakeholders
- [ ] Backup feito
```

---

## Template 4: Sprint Review (Retrospectiva BMAD)

```markdown
# 📊 Sprint Review & Retrospective

## 🎯 Objetivos Planejados
- [ ] Objetivo 1: [Completado / Em Progresso / Não iniciado]
- [ ] Objetivo 2: [Completado / Em Progresso / Não iniciado]

## ✅ Completado
- [Tarefa 1] - [Tempo: X horas]
- [Tarefa 2] - [Tempo: Y horas]

## ⏳ Em Progresso
- [Tarefa 3] - [Status: % completado]

## ❌ Não Iniciado
- [Tarefa 4] - [Razão: bloqueado / prioridade mudou]

---

## 📈 Métricas
| Métrica | Target | Resultado | Variação |
|---------|--------|-----------|----------|
| Tarefas completadas | 5 | 4 | -20% |
| Bugs encontrados | < 3 | 2 | ✅ OK |
| Cobertura testes | >80% | 85% | ✅ OK |

---

## 🔍 Reflexão - O que Aprendemos?

### O que funcionou bem? 🟢
1. [Feedback positivo 1]
2. [Feedback positivo 2]

### O que não funcionou? 🔴
1. [Desafio 1] - Solução: [Ajuste]
2. [Desafio 2] - Solução: [Ajuste]

### Como melhorar? 🚀
1. [Melhoria 1] para próxima iteração
2. [Melhoria 2] para próxima iteração

---

## 📋 Ação Items para Próxima Iteração
- [ ] [Ação 1] - Owner: [Você/Claude]
- [ ] [Ação 2] - Owner: [Você/Claude]

## 📅 Próxima Sprint
**Data:** [Data]
**Foco:** [Área de foco]
**Objetivos:** [Listar]
```

---

## 🎓 Como Usar os Templates

### Situação 1: Nova Feature
→ Use **Template 1: BMAD Plan Completo**

### Situação 2: Bug Simples
→ Use **Template 2: Quick Flow**

### Situação 3: Grande Mudança
→ Use **Template 3: Enterprise Track**

### Situação 4: Fim de Sprint
→ Use **Template 4: Sprint Review**

---

## 💡 Dicas de Preenchimento

✅ **Seja Específico:**
- Não: "Melhorar performance"
- Sim: "Reduzir tempo de carregamento do dashboard de 3s para <1s"

✅ **Use Checklists:**
- Mais fácil de rastrear
- Mostra progresso
- Evita esquecer tarefas

✅ **Documente Decisões:**
- "Escolhemos X porque Y"
- Facilita revisão posterior
- Ensina futuros desenvolvedores

✅ **Atualize Regularmente:**
- Pelo menos 1x por dia
- Reflete realidade do projeto
- Ajuda na comunicação

---

## 🚀 Próximo Passo

Escolha uma das opções:

1. **QUICK_FIX:** Tem um bug simples para consertar?
2. **BMAD:** Quer adicionar uma nova feature?
3. **ENTERPRISE:** Tem uma grande mudança planejada?
4. **REFLETIR:** Quer discutir estratégia antes de implementar?

**Qual delas você escolhe para começar?**
