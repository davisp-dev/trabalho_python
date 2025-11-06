# 🤖 BMAD Agents - Índice Completo

## Overview

Este diretório contém as configurações dos **agentes especializados** que orquestram o desenvolvimento do projeto NYC Traffic Safety Analysis usando a metodologia BMAD.

**Total de Agentes:** 8 agentes especializados
**Framework:** Breakthrough Method for Agile AI Driven Development
**Status:** Totalmente configurados para o projeto

---

## 📋 Agentes Disponíveis

### 1. 🎯 BMAD Master (core-bmad-master.customize.yaml)

**Função:** Orquestrador e diretor do framework

| Aspecto | Descrição |
|---------|-----------|
| **Role** | Orchestrator & Framework Director |
| **Responsabilidades** | Coordenar todos agentes, garantir qualidade, validar conformidade |
| **Expertise** | Metodologia BMAD, gestão de projetos, arquitetura |
| **Quando usar** | Decisões estratégicas, escalações críticas |
| **Deliverables** | Plano de projeto, validações de qualidade |

**Como usar:**
```
"Preciso de decisão estratégica sobre [topico]"
"Qual é a abordagem BMAD correta para [situação]?"
"Como coordenar [múltiplos componentes]?"
```

---

### 2. 💼 Product Manager (bmm-pm.customize.yaml)

**Função:** Estratégia de produto e valor de negócio

| Aspecto | Descrição |
|---------|-----------|
| **Role** | Product Strategy & Business Value |
| **Responsabilidades** | Definir requisitos, validar valor, priorizar backlog |
| **Expertise** | Estratégia de produto, análise de mercado, comunicação executiva |
| **Quando usar** | Definição de features, priorização, alinhamento stakeholders |
| **Deliverables** | PRD, user stories, roadmap |

**Como usar:**
```
"Qual é o próximo feature mais valioso para o governador?"
"Como comunicar o impacto desta feature?"
"Qual é a ordem certa de prioridades?"
```

---

### 3. 📊 Analyst (bmm-analyst.customize.yaml)

**Função:** Análise de dados e requisitos

| Aspecto | Descrição |
|---------|-----------|
| **Role** | Data Analysis & Requirements |
| **Responsabilidades** | Extrair insights, validar dados, documentar metodologia |
| **Expertise** | Análise estatística, Python/SQL, visualização de dados |
| **Quando usar** | Análise de dados, validação de hipóteses, geração de insights |
| **Deliverables** | Análise exploratória, relatórios, KPI specs |

**Como usar:**
```
"Quais são os insights principais dos dados de colisões?"
"Como validar esta hipótese com dados?"
"Qual é o padrão em [determinado aspecto]?"
```

---

### 4. 🏗️ Architect (bmm-architect.customize.yaml)

**Função:** Arquitetura técnica e design

| Aspecto | Descrição |
|---------|-----------|
| **Role** | Technical Architecture & Design |
| **Responsabilidades** | Desenhar arquitetura, avaliar tecnologias, documentar decisões |
| **Expertise** | Design de arquitetura, escalabilidade, performance |
| **Quando usar** | Decisões técnicas, design de sistema, trade-offs |
| **Deliverables** | Arquitetura diagram, technology stack, ADR |

**Como usar:**
```
"Como estruturar [componente] para escalar?"
"Qual tecnologia usar para [requisito]?"
"Quais são os trade-offs de [duas opções]?"
```

---

### 5. 🎨 UX Designer (bmm-ux-designer.customize.yaml)

**Função:** Experiência do usuário e design

| Aspecto | Descrição |
|---------|-----------|
| **Role** | User Experience & Design |
| **Responsabilidades** | Desenhar interfaces, validar usabilidade, garantir acessibilidade |
| **Expertise** | UX design, interaction design, accessibility (WCAG) |
| **Quando usar** | Design de interfaces, mockups, usabilidade |
| **Deliverables** | Wireframes, mockups, design system, accessibility specs |

**Como usar:**
```
"Como desenhar filtro para melhor experiência?"
"Como melhorar usabilidade desta tela?"
"Este design está acessível?"
```

---

### 6. 💻 Developer (bmm-dev.customize.yaml)

**Função:** Implementação e codificação

| Aspecto | Descrição |
|---------|-----------|
| **Role** | Implementation & Coding |
| **Responsabilidades** | Implementar design, escrever código limpo, otimizar |
| **Expertise** | Python, JavaScript, HTML/CSS, best practices |
| **Quando usar** | Implementação de features, code review, debugging |
| **Deliverables** | Código funcional, testes, documentação |

**Como usar:**
```
"Como implementar [feature] conforme spec?"
"Por que este código está lento?"
"Qual é a melhor prática para [padrão]?"
```

---

### 7. 🧪 Test Architect (bmm-tea.customize.yaml)

**Função:** Qualidade e arquitetura de testes

| Aspecto | Descrição |
|---------|-----------|
| **Role** | Quality Assurance & Testing Strategy |
| **Responsabilidades** | Desenhar estratégia de testes, validar qualidade, rastrear bugs |
| **Expertise** | Testing strategies, manual/automated testing, QA |
| **Quando usar** | Estratégia de testes, validação de qualidade, bug reporting |
| **Deliverables** | Test strategy, test cases, quality metrics |

**Como usar:**
```
"Como testar [feature] completamente?"
"Quais são os edge cases de [cenário]?"
"Por que este bug não foi encontrado antes?"
```

---

### 8. 📝 Technical Writer (bmm-tech-writer.customize.yaml)

**Função:** Documentação e transfer de conhecimento

| Aspecto | Descrição |
|---------|-----------|
| **Role** | Documentation & Knowledge Transfer |
| **Responsabilidades** | Documentar código, criar guides, manter README |
| **Expertise** | Technical writing, Markdown, knowledge management |
| **Quando usar** | Documentação, guides, knowledge transfer |
| **Deliverables** | README files, code docs, user guides |

**Como usar:**
```
"Como documentar [função] claramente?"
"Qual é a melhor forma de explicar [conceito]?"
"Como estruturar este guia?"
```

---

### 9. 🎬 Scrum Master (bmm-sm.customize.yaml)

**Função:** Processo e coordenação do time

| Aspecto | Descrição |
|---------|-----------|
| **Role** | Process & Team Coordination |
| **Responsabilidades** | Facilitar sprints, remover bloqueadores, rastrear progresso |
| **Expertise** | Agile/Scrum, facilitação, gestão de conflitos |
| **Quando usar** | Planejamento de sprint, remoção de bloqueadores, ritmo |
| **Deliverables** | Sprint plan, daily updates, retrospective |

**Como usar:**
```
"Como planejar o próximo sprint?"
"Qual é o bloqueador principal agora?"
"Como melhorar nossa velocidade?"
```

---

## 🔄 Fluxo de Trabalho com Agentes

### Típico Development Flow

```
┌─────────────────────────────────────────────────────────────┐
│ 1. PM Define Feature                                        │
│    - Requisito de negócio                                   │
│    - Valor para stakeholders                                │
│    - User stories com critérios de aceitação               │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Analyst Valida com Dados                                 │
│    - Requisito faz sentido?                                 │
│    - Quais são os padrões nos dados?                        │
│    - Qual é a métrica de sucesso?                           │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Architect Desenha Solução                                │
│    - Como implementar?                                      │
│    - Quais tecnologias?                                     │
│    - Como escalar?                                          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. UX Designer Cria Mockups                                 │
│    - Como usuário interage?                                 │
│    - Interface clara e intuitiva?                           │
│    - Acessível?                                             │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Developer Implementa                                     │
│    - Código conforme spec?                                  │
│    - Limpo e testável?                                      │
│    - Performance OK?                                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 6. Test Architect Valida Qualidade                          │
│    - Todos critérios de aceitação passam?                   │
│    - Edge cases cobertos?                                   │
│    - Pronto para produção?                                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 7. Tech Writer Documenta                                    │
│    - README atualizado?                                     │
│    - Código comentado?                                      │
│    - Changelog?                                             │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 8. Scrum Master Fecha Sprint                                │
│    - Feature pronta para produção?                          │
│    - Time satisfeito?                                       │
│    - Lições aprendidas?                                     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 9. BMAD Master Valida Conformidade                          │
│    - Processo BMAD seguido?                                 │
│    - Qualidade acima de padrão?                             │
│    - Pronto para merge/release?                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 💬 Como Convocar Agentes

### Formato Geral

```
[Agent]: [Solicitação clara com contexto]

Exemplo:
PM: Qual é a próxima feature mais valiosa para adicionar?
    Contexto: Já temos filtros básicos, próxima prioridade.

Analyst: Como validar que os filtros melhoram compreensão dos dados?

Developer: Como implementar localStorage para persistir filtros?
```

### Padrão de Resposta

Cada agente responde com:
1. **Análise** - O que entendi
2. **Recomendação** - Qual é a melhor abordagem
3. **Próximos Passos** - O que fazer agora
4. **Alternativas** - Outras opções consideradas

---

## 🎯 Casos de Uso por Agente

| Situação | Agent | Pergunta |
|----------|-------|----------|
| Nova feature | PM | "Qual é o valor de negócio?" |
| Entender dados | Analyst | "Qual é o padrão nos dados?" |
| Decisão técnica | Architect | "Como estruturar isto?" |
| Interface confusa | UX Designer | "Como melhorar a usabilidade?" |
| Código lento | Developer | "Por que está lento?" |
| Quanto testar | Test Architect | "Qual é a estratégia de testes?" |
| Documentação | Tech Writer | "Como documentar isto?" |
| Sprint com atrasos | Scrum Master | "Como recuperar velocidade?" |
| Decisão estratégica | BMAD Master | "Qual é a melhor abordagem?" |

---

## 📊 Status dos Agentes

| Agent | Status | Configurado | Pronto |
|-------|--------|-------------|--------|
| BMAD Master | ✅ Ativo | ✅ Sim | ✅ Sim |
| PM | ✅ Ativo | ✅ Sim | ✅ Sim |
| Analyst | ✅ Ativo | ✅ Sim | ✅ Sim |
| Architect | ✅ Ativo | ✅ Sim | ✅ Sim |
| UX Designer | ✅ Ativo | ✅ Sim | ✅ Sim |
| Developer | ✅ Ativo | ✅ Sim | ✅ Sim |
| Test Architect | ✅ Ativo | ✅ Sim | ✅ Sim |
| Technical Writer | ✅ Ativo | ✅ Sim | ✅ Sim |
| Scrum Master | ✅ Ativo | ✅ Sim | ✅ Sim |

---

## 🚀 Começar a Usar os Agentes

### 1. Defina sua necessidade
```
"Preciso [ação] porque [razão] para [benefício]"
```

### 2. Escolha o agente certo
```
Nova feature? → PM
Dados? → Analyst
Código? → Developer
Qualidade? → Test Architect
Documentação? → Tech Writer
Processo? → Scrum Master
```

### 3. Comunique claramente
```
"[Agent]: [Pergunta específica com contexto]"
```

### 4. Implemente a recomendação
```
Agente propõe → Você valida → Implementa → Próximo agente valida
```

---

## 📚 Documentação dos Agentes

Cada arquivo `.customize.yaml` contém:
- **name** - Nome do agente
- **role** - Função principal
- **description** - O que faz
- **capabilities** - Competências
- **key_responsibilities** - Responsabilidades
- **deliverables** - O que entrega
- **integration_points** - Com quem trabalha
- **context_for_ai** - Personalidade e expertise
- **collaboration_rules** - Como trabalhar
- **success_criteria** - O que é sucesso
- **[Customizações para NYC Traffic]** - Contexto específico do projeto

---

## 🔗 Próximo Passo

Você agora tem **9 agentes especializados** configurados para ajudar no desenvolvimento!

**Qual é sua próxima tarefa?**

Exemplos:
- `PM: Qual feature quer implementar primeiro?`
- `Analyst: Como validar o impacto dos filtros?`
- `Developer: Como estruturar o código para filtros?`
- `UX Designer: Como desenhar a interface de filtros?`
- `Test Architect: Como testar completamente os filtros?`

**Escolha um agente e comece!** 🚀
