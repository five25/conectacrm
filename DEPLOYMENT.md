# Conecta CRM - Instruções de Implantação

Este documento contém instruções para implantar o aplicativo Conecta CRM.

## Pré-requisitos

1. Conta no Supabase (https://supabase.com/)
2. Conta em um serviço de hospedagem como Vercel, Netlify ou similar

## Configuração do Supabase

1. Crie um novo projeto no Supabase
2. No Editor SQL do Supabase, execute o script SQL contido em `supabase/migrations/0001_initial.sql`
3. Verifique se as tabelas `profiles`, `connections` e `messages` foram criadas corretamente
4. Vá para Configurações > API e copie a URL do projeto e a chave anônima

## Configuração do Ambiente

1. Crie um arquivo `.env.local` na raiz do projeto com base no arquivo `.env.example`
2. Preencha as variáveis de ambiente com os valores do seu projeto Supabase:
   ```
   REACT_APP_SUPABASE_URL=sua-url-do-supabase
   REACT_APP_SUPABASE_ANON_KEY=sua-chave-anonima-do-supabase
   ```

## Construção do Aplicativo

1. Instale as dependências:
   ```
   pnpm install
   ```

2. Construa o aplicativo para produção:
   ```
   pnpm run build
   ```

3. O resultado da construção estará na pasta `build`

## Implantação

### Opção 1: Vercel (Recomendado)

1. Conecte seu repositório GitHub ao Vercel
2. Configure as variáveis de ambiente no painel do Vercel
3. Implante o aplicativo

### Opção 2: Netlify

1. Conecte seu repositório GitHub ao Netlify
2. Configure as variáveis de ambiente no painel do Netlify
3. Implante o aplicativo

### Opção 3: Hospedagem Estática

1. Faça upload da pasta `build` para qualquer serviço de hospedagem estática
2. Configure o redirecionamento para que todas as rotas apontem para `index.html`

## Testes Pós-Implantação

1. Verifique se o login e o registro estão funcionando corretamente
2. Teste a criação e edição de perfis
3. Teste a descoberta de outros usuários
4. Teste a criação de conexões
5. Teste o envio e recebimento de mensagens

## Suporte

Para suporte ou dúvidas, entre em contato com a equipe do Conecta CRM.
