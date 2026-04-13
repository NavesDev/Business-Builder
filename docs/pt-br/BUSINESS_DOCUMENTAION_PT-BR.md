# BUSINESS DOCUMENTAION

## 1) Objetivo, escopo e principios de uso
Este documento define um **padrao operacional completo** para criacao de negocios digitais no Brasil.  
Ele foi desenhado para servir a dois usos:

1. **Operacao do negocio** (estrategia, produto, crescimento, financeira, compliance).
2. **Conversao em skills de IA** (cada pilar pode virar uma skill especialista).

### Regras mestras do padrao
- Toda decisao precisa de: **dono + metrica + criterio de saida**.
- Nenhuma iniciativa entra em execucao sem hipotese e criterio de sucesso.
- Nenhum desenvolvimento comeca sem requisito funcional, regra de negocio e criterio de aceite.
- Nenhum crescimento escala sem unit economics dentro dos limites da secao 1.1.
- Nenhuma entrega avanca com risco juridico/fiscal critico aberto.

### 1.1 Dicionario operacional e limites padrao (hibrido)
Os limites abaixo sao **valores recomendados iniciais**.  
Cada skill deve sobrescrever os valores quando o contexto exigir (segmento, ticket, ciclo de venda e maturidade).

| Termo ambiguo no texto | Definicao operacional obrigatoria | Valor padrao recomendado |
|---|---|---|
| Unit economics saudavel | LTV/CAC >= limite e Payback CAC <= limite e Margem de contribuicao >= limite | LTV/CAC >= 3; Payback <= 12 meses; Margem >= 40% |
| Limite definido | Threshold explicito por KPI no input da skill | Nunca usar sem numero/percentual |
| Minimo aprovado | Conjunto minimo de artefatos obrigatorios por gate | Campos obrigatorios preenchidos + aprovados |
| Validado | Evidencia registrada + metrica observada | 2 ciclos de medicao consecutivos |
| Priorizado | Ordenacao formal (RICE/MoSCoW) com dono e prazo | Backlog com ranking + justificativa |
| Queda de conversao relevante | Variacao percentual vs media movel recente | Queda > 15% vs media de 4 semanas |
| Churn alto | Churn acima do teto mensal por segmento | B2C > 5%/mes; B2B > 3%/mes |
| Pacote compliance minimo aprovado | Kit legal/fiscal/LGPD completo | Termos + politica + base legal + obrigacoes fiscais |

**Regra de execucao para skills:** qualquer gate com "limite", "minimo", "validado" ou "priorizado" deve apontar para valor objetivo.

---

## 2) Metodo universal: da ideia a execucao
| Fase | Objetivo | Entrega obrigatoria | Gate de saida (nao avanca sem isso) | Dono primario |
|---|---|---|---|---|
| 0. Fundacao estrategica | Definir problema, ICP e proposta de valor | Tese de negocio validada | ICP + dor priorizada + proposta unica documentada | Founder/CEO |
| 1. Desenho da oferta | Definir produto/servico e pacote comercial | Oferta principal + roadmap MVP | Escopo MVP e criterios de qualidade aprovados | Product Owner |
| 2. Monetizacao | Definir modelo de faturamento e pricing | Estrategia de receita | Modelo principal e politica comercial formalizados | CEO + Financeiro |
| 3. Go-to-market | Estruturar aquisicao e vendas | Plano de canais e funil | Meta de CAC por canal e plano de experimentacao | Growth Lead |
| 4. Conversao e retencao | Melhorar ativacao, conversao e LTV | Jornada de ativacao e CRM | Onboarding definido + metas de conversao/retencao | PO + CRM/CS |
| 5. Operacao e governanca | Garantir entrega com qualidade | Playbooks, SLAs e ritos | Donos, handoffs e ritual de gestao ativos | Operacoes |
| 6. Escala sustentavel | Crescer com controle financeiro e legal | Plano de escala | Margem, caixa e compliance dentro dos limites | Lideranca + CFO + Juridico |

---

## 3) Arquitetura dos 8 pilares (mapa mestre)
| Pilar | Pergunta central | Saida obrigatoria |
|---|---|---|
| 1. Estrategia e Posicionamento | Que problema resolvemos e para quem? | Documento de tese + ICP + posicionamento |
| 2. Oferta e Produto | O que entregamos e como isso gera valor? | Blueprint de oferta + escopo MVP + backlog |
| 3. Receita e Monetizacao | Como capturamos valor de forma previsivel? | Estrategia de faturamento + pricing + politicas |
| 4. Aquisicao e Growth | Como geramos demanda de forma repetivel? | Plano de canais + funil + plano de testes |
| 5. Conversao e Retencao | Como melhoramos ativacao, recorrencia e LTV? | Jornada de cliente + plano CRM/CS |
| 6. Operacao e Gestao | Como executamos sem perder qualidade? | SOPs + SLAs + governanca de execucao |
| 7. Financas e Unit Economics | O negocio para em pe financeiramente? | DRE gerencial + cenarios + unit economics |
| 8. Compliance e Governanca | O negocio esta legalmente protegido? | Mapa LGPD + contratos + trilha fiscal |

---

## 4) Catalogo de cargos e responsabilidades (base para skills)
| Cargo | Missao | Principais decisoes | Entregaveis minimos |
|---|---|---|---|
| Founder/CEO | Direcionar estrategia e alocacao de recursos | Nicho, tese, priorizacao macro, risco | Plano estrategico, metas trimestrais |
| **Product Owner (PO)** | Traduzir objetivos de negocio em produto executavel | Escopo MVP, prioridade de backlog, criterio de aceite | Backlog priorizado, historias, aceite |
| Product Manager | Gerir ciclo de descoberta e evolucao de produto | Trade-off de impacto vs esforco | Roadmap, metricas de produto |
| UX/UI Designer | Garantir clareza de jornada e usabilidade | Fluxos, arquitetura de informacao, padrao visual | Fluxos, wireframes, prototipos |
| Tech Lead | Garantir viabilidade tecnica e qualidade | Arquitetura tecnica, NFRs, divida tecnica | Especificacao tecnica, padroes |
| Growth Lead | Construir maquina de aquisicao previsivel | Mix de canais, budget, experimento | Plano de growth, dashboard de canais |
| CRM/Retention Lead | Elevar ativacao e reduzir churn | Jornadas de CRM, segmentacao, gatilhos | Fluxos de ciclo de vida, playbooks |
| Sales Lead/Closer | Converter oportunidades em receita | Processo comercial, qualificacao, script | Pipeline, playbook de vendas |
| Head de Operacoes | Escalar entrega com consistencia | Processos, SLAs, automacoes, handoffs | SOPs, matriz de responsabilidades |
| CFO/Financeiro | Garantir saude economica | Pricing final, reinvestimento, caixa, risco | DRE, fluxo de caixa, plano financeiro |
| Juridico | Cobrir risco contratual e regulatorio | Termos, contratos, enquadramentos | Pacote contratual e pareceres |
| DPO/Privacidade | Governar dados pessoais e LGPD | Base legal, retencao, resposta a incidentes | Inventario de dados e politica LGPD |

> Regra: um mesmo profissional pode acumular papeis no inicio, mas as **responsabilidades** continuam obrigatorias.

---

## 5) Playbook detalhado por pilar

## Pilar 1 - Estrategia e Posicionamento
### Objetivo
Definir com precisao o problema, publico prioritario e diferencial competitivo.

### Entradas obrigatorias
- Hipotese inicial de nicho.
- Evidencias qualitativas (entrevistas, comunidades, feedback de mercado).
- Analise de concorrencia direta/indireta.

### Decisoes criticas
- ICP principal e ICP secundario.
- Promessa central de valor (em 1 frase objetiva).
- Tese de diferenciacao (preco, velocidade, especializacao, experiencia, tecnologia).

### Regras de negocio
- **RN-E1:** Nenhuma oferta vai ao mercado sem ICP definido.
- **RN-E2:** Toda promessa comercial precisa de evidencia operacional.
- **RN-E3:** Posicionamento deve caber em mensagem de 30 segundos.

### KPIs minimos
- Taxa de entrevistas concluidas por ciclo.
- Taxa de resposta positiva da proposta de valor.
- Share de objeções recorrentes (para refinamento da tese).

### Cargos e responsabilidades
- Founder/CEO: dono da tese e da priorizacao.
- Estrategia/PM: consolida insights e hipoteses.
- Growth: valida narrativa em canais reais.

### Gate de saida
Documento estrategico aprovado com ICP, proposta de valor, diferenciais e metricas de validacao.

---

## Pilar 2 - Oferta e Produto
### Objetivo
Transformar a tese de valor em oferta clara, escopo executavel e experiencia consistente.

### Entradas obrigatorias
- Documento estrategico (pilar 1).
- Restricoes de equipe, prazo e tecnologia.
- Requisitos legais/comerciais da oferta.

### Decisoes criticas
- Escopo do MVP e fronteira de nao-escopo.
- Nivel de servico (manual, semi-automatizado, automatizado).
- Jornada principal de compra e uso.

### Regras de negocio
- **RN-P1:** Todo item de backlog precisa mapear para objetivo de negocio.
- **RN-P2:** Historia sem criterio de aceite nao entra em desenvolvimento.
- **RN-P3:** Mudanca de escopo exige reavaliacao de prazo, custo e risco.

### Checklist operacional
- Definir oferta principal, opcional e premium.
- Estruturar onboarding, entrega de valor inicial e suporte.
- Criar backlog por epicos, historias e criterios de aceite.
- Definir Definition of Ready (DoR) e Definition of Done (DoD).

### KPIs minimos
- Tempo ate primeiro valor (TTFV).
- Taxa de ativacao.
- Taxa de conclusao de jornada principal.

### Cargos e responsabilidades
- **PO:** define escopo, prioriza backlog, valida aceite.
- UX/UI: desenha fluxos, remove friccao e garante clareza.
- Tech Lead: valida viabilidade tecnica e NFRs.

### Gate de saida
Escopo MVP aprovado, backlog priorizado e aceite definido por item critico.

---

## Pilar 3 - Receita e Monetizacao
### Objetivo
Definir como o negocio captura valor, sustenta caixa e cresce com margem.

### Entradas obrigatorias
- Custo de entrega por cliente.
- Percepcao de valor do ICP.
- Benchmark de mercado.

### Decisoes criticas
- Modelo principal de faturamento.
- Politica de preco, desconto, upgrade e cancelamento.
- Estrategia de captura de receita recorrente vs transacional.

### Regras de negocio
- **RN-M1:** Nenhuma oferta sem politica de preco e reembolso formal.
- **RN-M2:** Desconto fora da politica exige aprovacao do dono financeiro.
- **RN-M3:** Todo plano deve ter margem minima definida.

### KPIs minimos
- MRR/ARR ou Receita Mensal (conforme modelo).
- Ticket medio.
- Margem de contribuicao.
- Taxa de upgrade/downgrade.

### Cargos e responsabilidades
- CEO: define direcionamento de captura de valor.
- Financeiro: valida margem e impacto no caixa.
- Growth/Vendas: testa elasticidade e conversao por faixa de preco.

### Gate de saida
Modelo de receita principal validado, politica comercial publicada e metas financeiras definidas.

---

## Pilar 4 - Aquisicao e Growth
### Objetivo
Criar aquisicao previsivel com controle de CAC e qualidade de leads.

### Entradas obrigatorias
- ICP validado.
- Oferta e pricing formalizados.
- Posicionamento e mensagens-chave.

### Decisoes criticas
- Canais principais (organico, pago, parceria, outbound, comunidade).
- Orcamento e limite de CAC por canal.
- Cadencia de experimentos e criterios de corte/escala.

### Regras de negocio
- **RN-G1:** Campanha sem hipotese e metrica alvo nao entra no ar.
- **RN-G2:** Canal com CAC acima do limite por 2 ciclos entra em revisao.
- **RN-G3:** Toda nova campanha precisa de rastreabilidade de atribuicao.

### KPIs minimos
- CAC por canal.
- Taxa de conversao por etapa do funil.
- Custo por lead qualificado (CPLQ).
- Payback de aquisicao.

### Cargos e responsabilidades
- Growth Lead: dono de estrategia de canais e experimentos.
- Mídia/Performance: execucao de campanhas e criativos.
- Conteudo/SEO: aquisicao organica de medio/longo prazo.

### Gate de saida
Funil operacional com metas por etapa e plano ativo de otimizacao semanal.

---

## Pilar 5 - Conversao e Retencao
### Objetivo
Aumentar conversao, diminuir churn e elevar valor do cliente no ciclo de vida.

### Entradas obrigatorias
- Dados de funil, onboarding e uso.
- Motivos de perda/cancelamento.
- Segmentacao de base.

### Decisoes criticas
- Estrategia de onboarding por perfil.
- Jornadas de CRM (ativacao, engajamento, recuperacao).
- Politica de atendimento e sucesso do cliente.

### Regras de negocio
- **RN-R1:** Todo cliente novo entra em trilha de onboarding estruturada.
- **RN-R2:** Queda de retencao acima do limite dispara plano de acao.
- **RN-R3:** Motivos de churn devem ser classificados e revisados mensalmente.

### KPIs minimos
- Taxa de ativacao.
- Conversao de trial para pago (obrigatorio para modelos trial/freemium; nos demais usar conversao proposta->compra, conforme secao 9.1).
- Churn de receita e de clientes.
- LTV e NPS/CSAT.

### Cargos e responsabilidades
- CRM/Retention: dono das jornadas e segmentacao.
- CS: operacao de suporte e reducao de churn.
- Produto: ajustes de friccao com base em comportamento real.

### Gate de saida
Jornada completa de ciclo de vida operante, com metas de ativacao e retencao.

---

## Pilar 6 - Operacao e Gestao
### Objetivo
Padronizar execucao para ganhar qualidade, previsibilidade e escala.

### Entradas obrigatorias
- Mapa de processos da cadeia de valor.
- Definicao de papeis e handoffs.
- Historico de incidentes e gargalos.

### Decisoes criticas
- Quais processos padronizar primeiro.
- Quais SLAs sao inegociaveis.
- Quais etapas exigem automacao.

### Regras de negocio
- **RN-O1:** Processo critico precisa de SOP e dono.
- **RN-O2:** SLA estourado recorrente gera plano de melhoria obrigatorio.
- **RN-O3:** Handoff entre areas deve ter entrada/saida explicita.

### KPIs minimos
- Cumprimento de SLA.
- Lead time operacional.
- Taxa de retrabalho.
- Taxa de incidentes.

### Cargos e responsabilidades
- Operacoes: dono de SOP, qualidade e melhoria continua.
- PMO/Coordenacao: cadencia e governanca de execucao.
- Tech/Automacao: ganhos de eficiencia com sistemas.

### Gate de saida
Processos criticos padronizados, SLAs monitorados e governanca ativa.

---

## Pilar 7 - Financas e Unit Economics
### Objetivo
Garantir sustentabilidade financeira e suporte para escalar sem destruir caixa.

### Entradas obrigatorias
- Receita por linha de negocio.
- Custos fixos, variaveis e de aquisicao.
- Historico de inadimplencia e cancelamento.

### Decisoes criticas
- Margem minima por oferta.
- Limite de investimento em aquisicao.
- Politica de reinvestimento e reserva de caixa.

### Regras de negocio
- **RN-F1:** Oferta com margem de contribuicao abaixo do limite entra em ajuste.
- **RN-F2:** Aquisicao acima de payback maximo definido exige revisao.
- **RN-F3:** Decisao de escala depende de caixa projetado e risco controlado.

### KPIs minimos e formulas
- Margem de contribuicao = Receita - custos variaveis.
- LTV (estimado) = Ticket medio mensal x margem bruta x vida media (meses).
- Payback CAC = CAC / margem de contribuicao mensal por cliente.
- Runway de caixa (meses).

### Cargos e responsabilidades
- CFO/Financeiro: dono de caixa, margem e cenarios.
- Founder/CEO: decide alocacao macro com base nos cenarios.
- Growth/Comercial: ajusta aquisicao conforme limites financeiros.

### Gate de saida
Modelo financeiro com cenarios (base, otimista, critico) e limites de risco definidos.

---

## Pilar 8 - Compliance e Governanca
### Objetivo
Garantir conformidade legal, fiscal e de dados para proteger o negocio.

### Entradas obrigatorias
- Fluxos de dados e contratos vigentes.
- Modelo de receita e operacao fiscal.
- Canais de venda e relacionamento com consumidor.

### Decisoes criticas
- Bases legais LGPD por fluxo.
- Estrutura contratual por tipo de relacao.
- Regime tributario e obrigacoes acessorias.

### Regras de negocio
- **RN-C1:** Nenhum dado pessoal sem finalidade e base legal definida.
- **RN-C2:** Toda relacao comercial relevante precisa de contrato formal.
- **RN-C3:** Lancamento sem cobertura fiscal/tributaria e bloqueado.

### KPIs minimos
- Percentual de fluxos com base legal mapeada.
- Tempo medio de resposta a solicitacao de titular.
- Incidentes juridicos/fiscais por periodo.

### Cargos e responsabilidades
- Juridico: dono de contratos, termos e pareceres.
- DPO: dono de governanca LGPD.
- Financeiro/Fiscal: dono de conformidade tributaria.

### Gate de saida
Pacote legal/fiscal/LGPD minimo aprovado e monitorado.

---

## 6) Biblioteca expandida de modelos de faturamento
| Modelo | Como fatura | Quando usar | Metrica principal | Risco critico |
|---|---|---|---|---|
| Assinatura mensal | Mensalidade recorrente | Valor continuo e uso frequente | MRR e churn | Churn alto |
| Assinatura anual | Pagamento anual | Produto maduro e previsivel | ARR e renovacao | Alto desconto antecipado |
| Freemium -> Pago | Plano gratis + upsell | Base ampla e produto com rede/uso | Conversao free->paid | Baixa conversao |
| Trial -> Pago | Periodo de teste | Produto com valor percebido rapido | Conversao de trial | Trial sem ativacao |
| Compra unica | Pagamento pontual | Entrega fechada e objetiva | Ticket medio | Receita imprevisivel |
| Licenca por usuario (seat) | Valor por assento ativo | SaaS B2B com equipes | ARPA | Subutilizacao de seats |
| Uso/consumo (usage-based) | Por volume de uso | APIs, processamento, dados | Receita por unidade | Volatilidade de consumo |
| Tiers (Good/Better/Best) | Faixas de plano | Segmentos com maturidades diferentes | Mix de planos | Canibalizacao entre planos |
| Bundle de ofertas | Pacote de produtos/servicos | Cross-sell e aumento de ticket | Attach rate | Complexidade de entrega |
| Taxa de implementacao + mensalidade | Setup + recorrencia | Servico consultivo com produto recorrente | Payback e MRR | Dependencia de servico |
| Agencia/retainer | Mensalidade por servico continuo | Operacao de marketing/ops recorrente | Retencao de contrato | Gargalo operacional |
| Projeto fechado (fixed fee) | Valor por escopo fechado | Entregas personalizadas | Margem por projeto | Escopo estourar |
| Comissao de marketplace | % sobre transacao | Intermediacao de oferta/demanda | GMV e take rate | Fraude e dependencia de volume |
| Afiliacao/revenda | Comissao por venda | Distribuicao por parceiros | Receita por afiliado | Qualidade de canal |
| Publicidade/patrocinio | Venda de audiencia | Midia/comunidade com trafego | eCPM e ocupacao | Dependencia de audiencia |
| White-label/OEM | Licenciamento para terceiros | Solucao replicavel para parceiros | Receita B2B por contrato | Suporte complexo |

### Regra de selecao de modelo (ordem obrigatoria)
1. Verificar **natureza do valor** (continuo vs pontual).
2. Verificar **capacidade operacional** (escala manual vs automatizada).
3. Validar **unit economics** por modelo candidato.
4. Definir modelo principal e secundario (backup de receita).
5. Formalizar politica comercial (preco, desconto, cancelamento, reembolso).

---

## 7) Estrategias de design do projeto/produto
### 7.1 Descoberta (Discovery)
- Entrevistas com ICP, analise de objeções e mapeamento de jobs-to-be-done.
- Definir problema prioritario em termos mensuraveis.
- Validar risco de desejabilidade antes de construir.

### 7.2 Definicao de escopo
- Escopo MVP: somente o que prova valor e gera sinal de negocio.
- Nao-escopo explicito para evitar inflacao de backlog.
- Priorizacao por RICE (Reach, Impact, Confidence, Effort) ou MoSCoW.

### 7.3 Design de experiencia
- Mapear jornada completa: descoberta -> decisao -> onboarding -> uso -> renovacao.
- Definir momentos de valor percebido.
- Reduzir friccao nas etapas de cadastro, pagamento e ativacao.

### 7.4 Arquitetura de experimentacao
- Cada experimento precisa de hipotese, variavel, publico, prazo e metrica.
- Padrao de decisao: escalar, iterar ou matar experimento.
- Repositorio unico de aprendizados para nao repetir erro.

---

## 8) Padrao de requisitos e regras de negocio para desenvolvimento
Esta e a etapa final obrigatoria para o time de produto/engenharia.

### 8.1 Estrutura minima do pacote de handoff tecnico
- Mapa de capacidades de negocio por pilar.
- Requisitos funcionais (RF) por fluxo.
- Requisitos nao funcionais (RNF) por dominio tecnico.
- Regras de negocio (BR) formalizadas.
- Criterios de aceite (CA) por historia.
- Dependencias, riscos e premissas.

### 8.2 Template de requisito funcional (RF)
```text
ID: RF-###
Titulo:
Objetivo de negocio:
Ator principal:
Fluxo principal:
Fluxos alternativos/excecoes:
Entradas obrigatorias:
Saidas esperadas:
Eventos de auditoria:
Regras de negocio relacionadas: BR-###
```

### 8.3 Template de regra de negocio (BR)
```text
ID: BR-###
Descricao: Se [condicao], entao [acao], exceto quando [excecao].
Origem: Pilar X
Justificativa de negocio:
Impacto em receita/custo/risco:
```

### 8.4 Template de criterio de aceite (CA)
```text
ID: CA-###
Cenario (Given):
Acao (When):
Resultado (Then):
Metrica observavel:
```

### 8.5 Requisitos nao funcionais obrigatorios (RNF)
- Seguranca (auth, autorizacao, trilha de auditoria).
- Performance (tempo maximo por operacao critica).
- Disponibilidade (SLA tecnico por modulo).
- Observabilidade (logs, metricas, alertas).
- Confiabilidade (tratamento de falhas e idempotencia).
- Privacidade (minimizacao e retencao de dados).

### 8.6 Definition of Ready (DoR) e Definition of Done (DoD)
**DoR minimo:** historia com contexto, BR vinculada, aceite definido e dependencias mapeadas.  
**DoD minimo:** implementado, validado nos criterios de aceite, monitoravel e documentado.

---

## 9) Compliance Brasil (bloco obrigatorio)
### LGPD
- Inventario de dados pessoais (coleta, uso, armazenamento, descarte).
- Base legal por finalidade.
- Processo para direitos do titular (acesso, correcao, exclusao, portabilidade).
- Politica de retencao e resposta a incidente.

### Contratos e consumidor
- Termos de uso, politica de privacidade e politica comercial.
- Contratos com fornecedores, parceiros e afiliados.
- Adequacao ao CDC para ofertas, cancelamento e publicidade.

### Tributario/fiscal
- Enquadramento tributario por modelo de negocio (com orientacao contabil).
- Emissao fiscal por tipo de operacao.
- Rotina de conciliacao financeira e fiscal.

### Propriedade intelectual
- Titularidade de marca, software, conteudo e base de conhecimento.
- Contratos de cessao/licenciamento obrigatorios quando houver criacao de software, conteudo ou marca por terceiros.

---

## 9.1 Matriz de aplicabilidade de KPIs (obrigatoria para skills)
Para eliminar "quando aplicavel", cada skill deve marcar KPI como **obrigatorio** ou **substituto obrigatorio**.

| KPI primario | Obrigatorio quando | Substituto obrigatorio quando nao se aplica |
|---|---|---|
| MRR/ARR | Modelo recorrente (assinatura, retainer, licenca recorrente) | Receita mensal total + margem de contribuicao |
| Conversao trial->pago | Modelo com trial ou freemium | Conversao proposta->compra |
| Churn de receita/clientes | Receita recorrente | Taxa de recompra ou taxa de renovacao |
| NPS | Base com volume minimo de respostas no ciclo | CSAT padronizado por interacao |
| Payback CAC | Canais pagos ou investimento comercial relevante | Custo de aquisicao por canal + ciclo de fechamento |

**Regra:** nenhuma skill pode retornar KPI como "N/A". Se o KPI primario nao se aplica, o substituto vira obrigatorio.

---

## 10) Matriz de riscos e controles com gatilhos de acao
| Risco | Gatilho objetivo | Acao imediata | Dono |
|---|---|---|---|
| CAC fora de controle | CAC > `CAC_MAXIMO` por 2 ciclos consecutivos | Congelar escala no canal e revisar oferta/criativo | Growth |
| Conversao baixa | Queda de conversao > `QUEDA_CONVERSAO_MAXIMA` | Revisar jornada e propostas de valor por etapa | PO + Growth |
| Churn alto | Churn mensal > `CHURN_MAXIMO_SEGMENTO` | Acionar plano de retencao e entrevistas de cancelamento | CRM/CS |
| Margem comprimida | Margem de contribuicao < `MARGEM_MINIMA` | Revisar preco, custo e mix de oferta | Financeiro |
| Risco LGPD | Incidente ou solicitacao sem resposta no prazo | Acionar protocolo DPO e comunicacao juridica | DPO/Juridico |
| Gargalo operacional | SLA estourado de forma recorrente | Revisar processo, capacidade e automacao | Operacoes |

---

## 11) Cadencia de gestao (rituais obrigatorios)
- **Diario (operacao):** fila critica, incidentes, gargalos.
- **Semanal (performance):** funil, receita, churn, principais experimentos.
- **Quinzenal (produto):** revisao de backlog, escopo e aprendizados.
- **Mensal (executivo):** DRE gerencial, caixa, riscos e decisoes de alocacao.
- **Trimestral (estrategico):** reposicionamento, novos bets e encerramento de linhas.

---

## 12) Roadmap de maturidade e gates
| Nivel | Estado | Evidencias obrigatorias |
|---|---|---|
| Nivel 0 - Hipotese | Problema e publico em validacao | ICP e tese em teste |
| Nivel 1 - Fundacao | Oferta funcional e primeiras vendas | MVP com valor entregue e funil inicial |
| Nivel 2 - Tracao | Aquisicao e operacao previsiveis | Canais com CAC controlado e retencao ativa |
| Nivel 3 - Escala | Crescimento com margem e governanca | Unit economics dentro dos limites da secao 1.1 + compliance robusto |
| Nivel 4 - Otimizacao | Expansao disciplinada | Portfolio de receita e processos maduros |

---

## 13) Blueprint para converter este padrao em skills de IA
### 13.1 Skills recomendadas (minimo)
| Skill | Objetivo | Entrada obrigatoria | Saida padrao |
|---|---|---|---|
| skill-estrategia-posicionamento | Definir ICP e tese de valor | Nicho, dores, sinais de mercado | Tese validada + ICP priorizado |
| skill-oferta-produto | Montar oferta e backlog MVP | Tese estrategica + restricoes | Escopo MVP + backlog + aceite |
| skill-receita-monetizacao | Definir faturamento e pricing | Custo, valor percebido, benchmark | Modelo principal + politica comercial |
| skill-aquisicao-growth | Estruturar canais e funil | ICP + oferta + budget | Plano de canais + metas de CAC |
| skill-conversao-retencao | Melhorar ativacao e LTV | Dados de funil e churn | Plano CRM/CS + metas de retencao |
| skill-operacao-gestao | Padronizar execucao | Processos atuais e SLAs | SOPs + handoffs + governanca |
| skill-financas-unit-economics | Garantir sustentabilidade | Receita, custos, caixa | Modelo financeiro + limites |
| skill-compliance-governanca | Cobrir legal/fiscal/LGPD | Fluxos de dados e contratos | Pacote de compliance minimo |
| skill-handoff-dev | Traduzir negocio para engenharia | Saidas dos 8 pilares | RF/RNF/BR/CA priorizados |

### 13.2 Contrato deterministico por skill (obrigatorio)
Cada skill deve seguir o mesmo contrato em Markdown para manter consistencia.

#### Bloco A - Entrada obrigatoria da skill
| Campo | Obrigatorio | Exemplo |
|---|---|---|
| skill_id | Sim | `skill-aquisicao-growth` |
| segmento | Sim | `B2B`, `B2C` ou `Hibrido` |
| modelo_receita | Sim | `Assinatura mensal` |
| fase_maturidade | Sim | `Nivel 1`, `Nivel 2` |
| thresholds | Sim | `CAC_MAXIMO`, `MARGEM_MINIMA`, `CHURN_MAXIMO_SEGMENTO` |

#### Bloco B - Saida obrigatoria da skill
| Secao | Conteudo minimo obrigatorio |
|---|---|
| Status final | `aprovado`, `ajustes_obrigatorios` ou `reprovado_gate` |
| Diagnostico resumido | 3 a 5 linhas com contexto e principal conclusao |
| Decisoes tomadas | Lista com IDs (`DEC-001`, `DEC-002`), decisao e justificativa |
| Checklist executado | Lista com IDs (`CHK-*`) e status (`ok`, `pendente`, `bloqueado`) |
| KPIs e limites | KPI, valor atual, meta, limite e unidade |
| Riscos | IDs (`RSK-*`), nivel, mitigacao e dono |
| Gates | IDs (`GATE-*`) com resultado (`pass` ou `fail`) e acao corretiva |
| Proximo pacote de acao | Acao, dono e prazo |

#### Bloco C - Regras deterministicas de status
1. Se qualquer gate tiver resultado `fail`, status final = `reprovado_gate`.
2. Se nenhum gate falhar e houver checklist com `pendente`/`bloqueado`, status = `ajustes_obrigatorios`.
3. Se todos os gates passarem e checklist estiver sem pendencias, status = `aprovado`.
4. Toda skill deve manter IDs estaveis (`DEC-*`, `CHK-*`, `RSK-*`, `GATE-*`) para rastreabilidade.

---

## 14) Checklist final de prontidao para desenvolvimento
Antes de acionar time tecnico, confirmar:
- [ ] Escopo MVP aprovado pelo PO e lideranca.
- [ ] RF, RNF, BR e CA completos e sem ambiguidade.
- [ ] Dependencias externas identificadas.
- [ ] Riscos criticos com plano de mitigacao.
- [ ] Requisitos de compliance incorporados no backlog.
- [ ] KPI de negocio vinculado a cada entrega prioritaria.

> Se qualquer item acima estiver pendente, o projeto **nao entra em desenvolvimento**.
