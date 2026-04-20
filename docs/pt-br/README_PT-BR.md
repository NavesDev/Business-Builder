# Business Builder

[![Licenca: MIT](https://img.shields.io/badge/Licenca-MIT-green.svg)](../../LICENSE)
![Idioma Canonico: EN](https://img.shields.io/badge/Canonico-EN-blue)
![Traducao PT--BR](https://img.shields.io/badge/Traducao-PT--BR-orange)

Business Builder e um plugin de IA e um framework orientado por documentacao para criacao de negocios digitais com padroes operacionais claros em estrategia, produto, monetizacao, growth, governanca e handoff para desenvolvimento.

## Sumario
- [Por que este projeto existe](#por-que-este-projeto-existe)
- [O que esta incluido](#o-que-esta-incluido)
- [Mapa da documentacao](#mapa-da-documentacao)
- [Fluxo recomendado de uso](#fluxo-recomendado-de-uso)
- [Protocolo de testes de skills](#protocolo-de-testes-de-skills)
- [Comandos de setup e validacao](#comandos-de-setup-e-validacao)
- [Politica de idioma canonico](#politica-de-idioma-canonico)
- [Contribuicao](#contribuicao)
- [Governanca e legal](#governanca-e-legal)

## Por que este projeto existe
Muitos projetos de negocio digital falham porque decisoes estrategicas e artefatos de implementacao ficam desconectados.  
O Business Builder oferece um modelo operacional estruturado que conecta objetivos de negocio a saidas acionaveis (requisitos, regras de negocio, criterios de aceite, metricas e controles de risco).

## O que esta incluido
- Workspace de plugin de IA com skills orientadas por papeis para criacao de negocios
- Framework ponta a ponta de negocio (8 pilares)
- Biblioteca expandida de modelos de faturamento com criterios de selecao
- Guia de contrato deterministico para skills
- Padrao de handoff para desenvolvimento (RF/RNF/BR/CA)
- Base de compliance para Brasil (LGPD, contratos, tributario/fiscal, PI)

## Mapa da documentacao
- Framework principal: [`../../BUSINESS_DOCUMENTAION.md`](../../BUSINESS_DOCUMENTAION.md)
- Framework em idioma alternativo: [`BUSINESS_DOCUMENTAION_PT-BR.md`](./BUSINESS_DOCUMENTAION_PT-BR.md)
- README canonico em ingles: [`../../README.md`](../../README.md)
- Workspace superpowers: [`../superpowers/`](../superpowers/)
- Skills: [`../../skills/`](../../skills/)

## Fluxo recomendado de uso
1. Rode `init` para iniciar `business-builder/`, capturar o estado do negocio e encaminhar validacao ao `product-owner`.
2. Leia o documento de framework de negocio.
3. Escolha o pilar alvo (estrategia, produto, monetizacao, growth etc.).
4. Extraia decisoes, KPIs, gates e riscos.
5. Produza artefatos de handoff (RF/RNF/BR/CA).
6. Execute e monitore metricas/gatilhos de risco continuamente.

## Protocolo de testes de skills
Use artefatos de validacao co-localizados em cada skill:
- `skills/<skill-name>/validation/pressure-scenarios.md`
- `skills/<skill-name>/validation/test-log.md`

`pressure-scenarios.md` define cenarios realistas de pressao decisoria (prazo, autoridade, ambiguidade etc.) com opcoes forcadas (A/B/C) e prompt "Choose one and justify.".

`test-log.md` guarda evidencia auditavel para:
- falhas RED sem a skill
- comportamento GREEN com a skill carregada
- iteracoes REFACTOR quando surgem novos loopholes

Ciclo de execucao:
1. RED: rode os cenarios sem a skill e capture racionalizacoes literalmente.
2. GREEN: rode os mesmos cenarios com a skill e valide o comportamento esperado.
3. REFACTOR: adicione contra-regras para novas racionalizacoes e rode novamente.

Checks rapidos:
```bash
# Validar estrutura dos cenarios
grep -nE "IMPORTANT: This is a real scenario|Choose one and justify" skills/<skill-name>/validation/pressure-scenarios.md

# Validar secoes RED/GREEN/REFACTOR do log
grep -nE "## RED Baseline|## GREEN Verification|## REFACTOR Iterations" skills/<skill-name>/validation/test-log.md
```

## Comandos de setup e validacao
```bash
git clone https://github.com/NavesDev/Business-Builder.git
cd BusinessBuilder

# Verificar arquivos principais
ls -la README.md BUSINESS_DOCUMENTAION.md docs/pt-br/README_PT-BR.md docs/pt-br/BUSINESS_DOCUMENTAION_PT-BR.md

# Verificar estrutura dos READMEs
grep -nE "^## " README.md docs/pt-br/README_PT-BR.md

# Verificar secoes de politica canonica/traducao
grep -nE "Canonical language policy|Politica de idioma canonico" README.md docs/pt-br/README_PT-BR.md
```

## Politica de idioma canonico
- `README.md` e o README canonico (ingles).
- `docs/pt-br/README_PT-BR.md` e a traducao em portugues.
- Fluxo de atualizacao: alterar EN primeiro e sincronizar PT-BR no mesmo ciclo.

## Contribuicao
1. Crie uma branch: `git checkout -b docs/<tema-curto>`.
2. Mantenha alteracoes focadas e com escopo claro.
3. Preserve a paridade EN/PT-BR ao atualizar README.
4. Abra um PR descrevendo o que mudou e o que foi sincronizado.

## Governanca e legal
- Changelog: [`../../CHANGELOG.MD`](../../CHANGELOG.MD)
- Codigo de Conduta: [`../../CODE_OF_CONDUCT.MD`](../../CODE_OF_CONDUCT.MD)
- Licenca: [`../../LICENSE`](../../LICENSE)
