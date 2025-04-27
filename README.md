# Conecta CRM - README

## Sobre o Projeto

Conecta CRM é um aplicativo de networking desenvolvido para o evento "Conecta CRM" que ocorrerá em 17 de maio no Hotel Bourbon Fortaleza. O aplicativo permite que donos de agências, gestores de tráfego e empresários se conectem para fomentar parcerias e contratações de serviços.

## Tecnologias Utilizadas

- **Frontend**: React.js com Tailwind CSS
- **Backend**: Supabase (autenticação, banco de dados PostgreSQL, armazenamento)
- **Implantação**: Vercel/Netlify (recomendado)

## Funcionalidades

1. **Autenticação**
   - Login e cadastro de usuários
   - Perfis personalizados por tipo (Agência, Gestor de Tráfego, Empresa)

2. **Perfil do Usuário**
   - Edição de informações pessoais
   - Listagem de serviços oferecidos
   - Descrição do que está buscando no evento

3. **Descoberta**
   - Visualização de outros participantes
   - Filtro por tipo de perfil
   - Sistema de "Conectar" ou "Ignorar"

4. **Conexões**
   - Gerenciamento de solicitações de conexão
   - Aceitação ou recusa de conexões

5. **Chat**
   - Conversas em tempo real entre usuários conectados
   - Lista de conversas ativas

## Estrutura do Projeto

```
conecta-crm-app/
├── public/
│   └── images/
│       └── logo.png
├── src/
│   ├── components/
│   │   └── Navbar.js
│   ├── pages/
│   │   ├── Login.js
│   │   ├── Register.js
│   │   ├── Profile.js
│   │   ├── Discover.js
│   │   ├── Connections.js
│   │   ├── Chat.js
│   │   └── ChatList.js
│   ├── App.js
│   ├── AuthContext.js
│   ├── index.css
│   └── supabaseClient.js
├── supabase/
│   ├── migrations/
│   │   └── 0001_initial.sql
│   └── README.md
├── mockups/
│   ├── login.png
│   ├── cadastro.png
│   ├── perfil.png
│   ├── descoberta.png
│   ├── conexoes.png
│   ├── chat.png
│   └── lista_chat.png
├── .env.example
├── DEPLOYMENT.md
└── README.md
```

## Instalação e Execução Local

1. Clone o repositório
2. Instale as dependências:
   ```
   pnpm install
   ```
3. Configure o arquivo `.env.local` com suas credenciais do Supabase
4. Execute o aplicativo em modo de desenvolvimento:
   ```
   pnpm run dev
   ```

## Implantação

Consulte o arquivo [DEPLOYMENT.md](./DEPLOYMENT.md) para instruções detalhadas sobre como implantar o aplicativo em produção.

## Configuração do Supabase

Consulte o arquivo [supabase/README.md](./supabase/README.md) para instruções detalhadas sobre como configurar o projeto Supabase.

## Identidade Visual

- **Cores Principais**: 
  - Azul Marinho: #0F2C5C
  - Laranja: #FF6B35

- **Logo**: Símbolo de conexão/link dentro de um círculo sobre fundo azul marinho

## Licença

Este projeto é proprietário e foi desenvolvido exclusivamente para o evento Conecta CRM.

## Contato

Para suporte ou dúvidas, entre em contato com a equipe do Conecta CRM.
