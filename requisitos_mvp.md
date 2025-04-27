# Análise de Requisitos Revisada - MVP Aplicativo Conecta CRM

## Identidade Visual
- **Azul Marinho**: #0F2C5C - Cor predominante
- **Laranja**: #FF6B35 - Cor de destaque
- **Logo**: Símbolo de conexão/link dentro de um círculo sobre fundo azul marinho

## Requisitos Funcionais Essenciais para MVP

1. **Login e Cadastro Simplificado**
   - Autenticação por email/senha
   - Formulário de cadastro minimalista

2. **Perfil do Usuário Básico**
   - Seleção de tipo: Agência, Gestor de Tráfego ou Empresa
   - Campo para nome/empresa
   - Lista simplificada de serviços oferecidos
   - Descrição curta do que está buscando

3. **Descoberta Simplificada**
   - Lista básica de outros participantes
   - Filtro simples por tipo de usuário
   - Cards minimalistas com informações essenciais
   - Botões para "Conectar" ou "Ignorar"

4. **Conexões**
   - Lista de conexões realizadas
   - Status básico (pendente/aceita)

5. **Chat Básico**
   - Interface simples de mensagens
   - Apenas texto, sem recursos avançados

## Tecnologias para MVP de Baixo Custo

### Frontend
- **Framework**: React.js (create-react-app)
- **Estilização**: Tailwind CSS (zero configuração adicional)
- **Hospedagem**: Netlify/Vercel (plano gratuito)

### Backend
- **Supabase** (plano gratuito)
  - Autenticação pronta
  - Banco de dados PostgreSQL
  - Armazenamento de arquivos
  - Realtime subscriptions para chat

### Otimizações
- Carregamento lazy de componentes
- Imagens otimizadas
- Bundle minificado

## Priorização para Desenvolvimento Rápido
1. Configuração do projeto e integração com Supabase
2. Implementação do sistema de autenticação
3. Criação de perfis básicos
4. Sistema de descoberta e conexões
5. Chat básico
6. Testes e ajustes finais

## Estimativa de Tempo
- Configuração inicial: 1 dia
- Autenticação e perfis: 2 dias
- Descoberta e conexões: 2 dias
- Chat básico: 2 dias
- Testes e ajustes: 1 dia
- **Total**: 8 dias (pronto antes do evento em 17 de maio)

## Recursos Descartados para o MVP
- Agenda do evento
- Sistema avançado de matchmaking
- Gamificação
- Integração com redes sociais
- Analytics complexos
- Recursos offline avançados
