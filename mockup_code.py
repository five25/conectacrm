import os
from PIL import Image, ImageDraw, ImageFont
import math

# Cores da identidade visual
AZUL_MARINHO = (15, 44, 92)  # #0F2C5C
LARANJA = (255, 107, 53)     # #FF6B35
BRANCO = (255, 255, 255)
CINZA_CLARO = (240, 240, 240)
CINZA_ESCURO = (100, 100, 100)

# Dimensões das telas
LARGURA = 360
ALTURA = 640

def criar_diretorio(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

def desenhar_barra_superior(draw, texto="Conecta CRM"):
    # Fundo da barra
    draw.rectangle([(0, 0), (LARGURA, 60)], fill=AZUL_MARINHO)
    
    # Logo simplificado (círculo com ícone de conexão)
    draw.ellipse([(15, 15), (45, 45)], outline=BRANCO, width=2)
    draw.line([(22, 30), (38, 30)], fill=BRANCO, width=2)
    draw.line([(25, 25), (35, 35)], fill=BRANCO, width=2)
    draw.line([(25, 35), (35, 25)], fill=BRANCO, width=2)
    
    # Texto do título
    fonte = ImageFont.truetype("DejaVuSans-Bold.ttf", 18)
    draw.text((60, 20), texto, fill=BRANCO, font=fonte)

def desenhar_botao(draw, x, y, largura, altura, texto, cor_fundo=LARANJA, cor_texto=BRANCO, raio=10):
    # Desenhar retângulo arredondado
    draw.rounded_rectangle([(x, y), (x + largura, y + altura)], radius=raio, fill=cor_fundo)
    
    # Texto do botão
    fonte = ImageFont.truetype("DejaVuSans.ttf", 14)
    text_width = fonte.getlength(texto)
    text_x = x + (largura - text_width) / 2
    text_y = y + (altura - 14) / 2
    draw.text((text_x, text_y), texto, fill=cor_texto, font=fonte)

def desenhar_campo_texto(draw, x, y, largura, altura, placeholder="", valor="", raio=5):
    # Fundo do campo
    draw.rounded_rectangle([(x, y), (x + largura, y + altura)], radius=raio, fill=BRANCO, outline=CINZA_CLARO)
    
    # Texto
    fonte = ImageFont.truetype("DejaVuSans.ttf", 14)
    texto = valor if valor else placeholder
    cor = CINZA_ESCURO if valor else CINZA_CLARO
    draw.text((x + 10, y + (altura - 14) / 2), texto, fill=cor, font=fonte)

def desenhar_card_usuario(draw, x, y, largura, altura, nome, tipo, servicos, busca):
    # Fundo do card
    draw.rounded_rectangle([(x, y), (x + largura, y + altura)], radius=10, fill=BRANCO, outline=CINZA_CLARO)
    
    # Avatar placeholder
    draw.ellipse([(x + 15, y + 15), (x + 65, y + 65)], fill=CINZA_CLARO)
    
    # Informações do usuário
    fonte_nome = ImageFont.truetype("DejaVuSans-Bold.ttf", 16)
    fonte_info = ImageFont.truetype("DejaVuSans.ttf", 12)
    
    draw.text((x + 80, y + 15), nome, fill=AZUL_MARINHO, font=fonte_nome)
    draw.text((x + 80, y + 40), tipo, fill=CINZA_ESCURO, font=fonte_info)
    draw.text((x + 15, y + 80), f"Oferece: {servicos}", fill=CINZA_ESCURO, font=fonte_info)
    draw.text((x + 15, y + 100), f"Busca: {busca}", fill=CINZA_ESCURO, font=fonte_info)
    
    # Botões
    desenhar_botao(draw, x + 15, y + altura - 40, (largura - 45) / 2, 30, "Ignorar", CINZA_CLARO, CINZA_ESCURO)
    desenhar_botao(draw, x + largura/2 + 15, y + altura - 40, (largura - 45) / 2, 30, "Conectar")

def desenhar_mensagem_chat(draw, x, y, largura, texto, enviada=True):
    # Calcular altura baseada no texto
    fonte = ImageFont.truetype("DejaVuSans.ttf", 14)
    linhas = math.ceil(fonte.getlength(texto) / (largura - 20))
    altura = max(40, 20 + linhas * 20)
    
    # Determinar posição e cor baseado em quem enviou
    if enviada:
        pos_x = LARGURA - largura - x
        cor = LARANJA
    else:
        pos_x = x
        cor = CINZA_CLARO
    
    # Desenhar balão
    draw.rounded_rectangle([(pos_x, y), (pos_x + largura, y + altura)], radius=10, fill=cor)
    
    # Texto da mensagem
    cor_texto = BRANCO if enviada else CINZA_ESCURO
    draw.text((pos_x + 10, y + 10), texto, fill=cor_texto, font=fonte)
    
    return altura

def criar_tela_login():
    img = Image.new('RGB', (LARGURA, ALTURA), BRANCO)
    draw = ImageDraw.Draw(img)
    
    # Barra superior
    desenhar_barra_superior(draw, "Conecta CRM")
    
    # Logo grande
    draw.ellipse([(LARGURA/2 - 50, 120), (LARGURA/2 + 50, 220)], fill=AZUL_MARINHO)
    draw.line([(LARGURA/2 - 25, 170), (LARGURA/2 + 25, 170)], fill=BRANCO, width=4)
    draw.line([(LARGURA/2 - 20, 155), (LARGURA/2 + 20, 185)], fill=BRANCO, width=4)
    draw.line([(LARGURA/2 - 20, 185), (LARGURA/2 + 20, 155)], fill=BRANCO, width=4)
    
    # Título
    fonte_titulo = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
    draw.text((LARGURA/2 - 100, 250), "Bem-vindo ao", fill=AZUL_MARINHO, font=fonte_titulo)
    draw.text((LARGURA/2 - 80, 280), "Conecta CRM", fill=LARANJA, font=fonte_titulo)
    
    # Campos de login
    desenhar_campo_texto(draw, 40, 350, LARGURA - 80, 50, "Email")
    desenhar_campo_texto(draw, 40, 420, LARGURA - 80, 50, "Senha")
    
    # Botão de login
    desenhar_botao(draw, 40, 500, LARGURA - 80, 50, "ENTRAR")
    
    # Link para cadastro
    fonte_link = ImageFont.truetype("DejaVuSans.ttf", 14)
    draw.text((LARGURA/2 - 100, 570), "Não tem conta?", fill=CINZA_ESCURO, font=fonte_link)
    draw.text((LARGURA/2 + 20, 570), "Cadastre-se", fill=LARANJA, font=fonte_link)
    draw.line([(LARGURA/2 + 20, 588), (LARGURA/2 + 100, 588)], fill=LARANJA, width=1)
    
    return img

def criar_tela_cadastro():
    img = Image.new('RGB', (LARGURA, ALTURA), BRANCO)
    draw = ImageDraw.Draw(img)
    
    # Barra superior
    desenhar_barra_superior(draw, "Cadastro")
    
    # Campos de cadastro
    fonte_label = ImageFont.truetype("DejaVuSans-Bold.ttf", 14)
    draw.text((40, 80), "Informações Básicas", fill=AZUL_MARINHO, font=fonte_label)
    
    desenhar_campo_texto(draw, 40, 110, LARGURA - 80, 50, "Nome/Empresa")
    desenhar_campo_texto(draw, 40, 180, LARGURA - 80, 50, "Email")
    desenhar_campo_texto(draw, 40, 250, LARGURA - 80, 50, "Senha")
    
    draw.text((40, 320), "Tipo de Perfil", fill=AZUL_MARINHO, font=fonte_label)
    
    # Opções de tipo de perfil
    opcoes = ["Agência", "Gestor de Tráfego", "Empresa"]
    for i, opcao in enumerate(opcoes):
        y = 350 + i * 60
        draw.rounded_rectangle([(40, y), (LARGURA - 40, y + 50)], radius=5, fill=BRANCO, outline=CINZA_CLARO)
        draw.ellipse([(50, y + 15), (70, y + 35)], outline=CINZA_ESCURO, width=2)
        if i == 0:  # Primeira opção selecionada
            draw.ellipse([(53, y + 18), (67, y + 32)], fill=LARANJA)
        
        fonte = ImageFont.truetype("DejaVuSans.ttf", 14)
        draw.text((80, y + 18), opcao, fill=CINZA_ESCURO, font=fonte)
    
    # Botão de cadastro
    desenhar_botao(draw, 40, 560, LARGURA - 80, 50, "CADASTRAR")
    
    return img

def criar_tela_perfil():
    img = Image.new('RGB', (LARGURA, ALTURA), BRANCO)
    draw = ImageDraw.Draw(img)
    
    # Barra superior
    desenhar_barra_superior(draw, "Meu Perfil")
    
    # Avatar e informações básicas
    draw.ellipse([(LARGURA/2 - 50, 80), (LARGURA/2 + 50, 180)], fill=CINZA_CLARO)
    
    fonte_nome = ImageFont.truetype("DejaVuSans-Bold.ttf", 18)
    fonte_info = ImageFont.truetype("DejaVuSans.ttf", 14)
    
    draw.text((LARGURA/2 - 80, 200), "João da Silva", fill=AZUL_MARINHO, font=fonte_nome)
    draw.text((LARGURA/2 - 60, 230), "Gestor de Tráfego", fill=CINZA_ESCURO, font=fonte_info)
    
    # Seções do perfil
    fonte_secao = ImageFont.truetype("DejaVuSans-Bold.ttf", 16)
    
    draw.text((40, 280), "Serviços Oferecidos:", fill=AZUL_MARINHO, font=fonte_secao)
    draw.rounded_rectangle([(40, 310), (LARGURA - 40, 380)], radius=5, fill=BRANCO, outline=CINZA_CLARO)
    draw.text((50, 320), "• Facebook Ads\n• Google Ads\n• Estratégia de Funil", fill=CINZA_ESCURO, font=fonte_info)
    
    draw.text((40, 400), "Buscando:", fill=AZUL_MARINHO, font=fonte_secao)
    draw.rounded_rectangle([(40, 430), (LARGURA - 40, 500)], radius=5, fill=BRANCO, outline=CINZA_CLARO)
    draw.text((50, 440), "Parcerias com agências para\ngerenciamento de tráfego pago\npara clientes de grande porte.", fill=CINZA_ESCURO, font=fonte_info)
    
    # Botão de editar
    desenhar_botao(draw, 40, 530, LARGURA - 80, 50, "EDITAR PERFIL")
    
    # Barra de navegação inferior
    draw.rectangle([(0, ALTURA - 60), (LARGURA, ALTURA)], fill=BRANCO, outline=CINZA_CLARO)
    icones = ["Perfil", "Descobrir", "Conexões", "Chat"]
    for i, icone in enumerate(icones):
        x = LARGURA * (i + 0.5) / len(icones)
        y = ALTURA - 40
        cor = LARANJA if i == 0 else CINZA_ESCURO
        fonte_icone = ImageFont.truetype("DejaVuSans.ttf", 12)
        text_width = fonte_icone.getlength(icone)
        draw.text((x - text_width/2, y), icone, fill=cor, font=fonte_icone)
    
    return img

def criar_tela_descoberta():
    img = Image.new('RGB', (LARGURA, ALTURA), BRANCO)
    draw = ImageDraw.Draw(img)
    
    # Barra superior
    desenhar_barra_superior(draw, "Descobrir")
    
    # Filtros
    draw.rounded_rectangle([(40, 70), (LARGURA - 40, 110)], radius=5, fill=BRANCO, outline=CINZA_CLARO)
    fonte_filtro = ImageFont.truetype("DejaVuSans.ttf", 14)
    draw.text((50, 82), "Filtrar por: Todos", fill=CINZA_ESCURO, font=fonte_filtro)
    draw.polygon([(LARGURA - 60, 85), (LARGURA - 50, 95), (LARGURA - 70, 95)], fill=CINZA_ESCURO)
    
    # Cards de usuários
    desenhar_card_usuario(draw, 20, 130, LARGURA - 40, 180, 
                         "Maria Oliveira", "Agência", 
                         "Marketing Digital, SEO, Redes Sociais", 
                         "Clientes para gestão de tráfego")
    
    desenhar_card_usuario(draw, 20, 330, LARGURA - 40, 180, 
                         "Empresa XYZ", "Empresa", 
                         "Produtos de Tecnologia", 
                         "Agência para gestão de marketing")
    
    # Barra de navegação inferior
    draw.rectangle([(0, ALTURA - 60), (LARGURA, ALTURA)], fill=BRANCO, outline=CINZA_CLARO)
    icones = ["Perfil", "Descobrir", "Conexões", "Chat"]
    for i, icone in enumerate(icones):
        x = LARGURA * (i + 0.5) / len(icones)
        y = ALTURA - 40
        cor = LARANJA if i == 1 else CINZA_ESCURO
        fonte_icone = ImageFont.truetype("DejaVuSans.ttf", 12)
        text_width = fonte_icone.getlength(icone)
        draw.text((x - text_width/2, y), icone, fill=cor, font=fonte_icone)
    
    return img

def criar_tela_conexoes():
    img = Image.new('RGB', (LARGURA, ALTURA), BRANCO)
    draw = ImageDraw.Draw(img)
    
    # Barra superior
    desenhar_barra_superior(draw, "Minhas Conexões")
    
    # Lista de conexões
    fonte_titulo = ImageFont.truetype("DejaVuSans-Bold.ttf", 16)
    fonte_subtitulo = ImageFont.truetype("DejaVuSans.ttf", 14)
    
    # Conexões aceitas
    draw.text((20, 80), "Conexões Aceitas (2)", fill=AZUL_MARINHO, font=fonte_titulo)
    
    # Conexão 1
    draw.rounded_rectangle([(20, 110), (LARGURA - 20, 170)], radius=10, fill=BRANCO, outline=CINZA_CLARO)
    draw.ellipse([(35, 125), (75, 165)], fill=CINZA_CLARO)
    draw.text((90, 125), "Maria Oliveira", fill=AZUL_MARINHO, font=fonte_subtitulo)
    draw.text((90, 145), "Agência", fill=CINZA_ESCURO, font=fonte_subtitulo)
    desenhar_botao(draw, LARGURA - 100, 135, 70, 30, "Chat", LARANJA)
    
    # Conexão 2
    draw.rounded_rectangle([(20, 180), (LARGURA - 20, 240)], radius=10, fill=BRANCO, outline=CINZA_CLARO)
    draw.ellipse([(35, 195), (75, 235)], fill=CINZA_CLARO)
    draw.text((90, 195), "Carlos Mendes", fill=AZUL_MARINHO, font=fonte_subtitulo)
    draw.text((90, 215), "Gestor de Tráfego", fill=CINZA_ESCURO, font=fonte_subtitulo)
    desenhar_botao(draw, LARGURA - 100, 205, 70, 30, "Chat", LARANJA)
    
    # Conexões pendentes
    draw.text((20, 270), "Conexões Pendentes (1)", fill=AZUL_MARINHO, font=fonte_titulo)
    
    # Conexão pendente
    draw.rounded_rectangle([(20, 300), (LARGURA - 20, 360)], radius=10, fill=BRANCO, outline=CINZA_CLARO)
    draw.ellipse([(35, 315), (75, 355)], fill=CINZA_CLARO)
    draw.text((90, 315), "Empresa XYZ", fill=AZUL_MARINHO, font=fonte_subtitulo)
    draw.text((90, 335), "Empresa", fill=CINZA_ESCURO, font=fonte_subtitulo)
    desenhar_botao(draw, LARGURA - 180, 325, 70, 30, "Recusar", CINZA_CLARO, CINZA_ESCURO)
    desenhar_botao(draw, LARGURA - 100, 325, 70, 30, "Aceitar", LARANJA)
    
    # Barra de navegação inferior
    draw.rectangle([(0, ALTURA - 60), (LARGURA, ALTURA)], fill=BRANCO, outline=CINZA_CLARO)
    icones = ["Perfil", "Descobrir", "Conexões", "Chat"]
    for i, icone in enumerate(icones):
        x = LARGURA * (i + 0.5) / len(icones)
        y = ALTURA - 40
        cor = LARANJA if i == 2 else CINZA_ESCURO
        fonte_icone = ImageFont.truetype("DejaVuSans.ttf", 12)
        text_width = fonte_icone.getlength(icone)
        draw.text((x - text_width/2, y), icone, fill=cor, font=fonte_icone)
    
    return img

def criar_tela_chat():
    img = Image.new('RGB', (LARGURA, ALTURA), BRANCO)
    draw = ImageDraw.Draw(img)
    
    # Barra superior
    desenhar_barra_superior(draw, "Chat - Maria Oliveira")
    
    # Área de mensagens
    draw.rectangle([(0, 60), (LARGURA, ALTURA - 70)], fill=CINZA_CLARO, width=0)
    
    # Mensagens
    altura1 = desenhar_mensagem_chat(draw, 10, 80, 240, "Olá! Vi seu perfil e gostaria de conversar sobre uma possível parceria.", False)
    altura2 = desenhar_mensagem_chat(draw, 10, 80 + altura1 + 10, 240, "Temos clientes que precisam de gestão de tráfego.", False)
    
    altura3 = desenhar_mensagem_chat(draw, 10, 80 + altura1 + altura2 + 30, 240, "Oi Maria! Claro, podemos conversar. Quais tipos de clientes vocês atendem?")
    
    altura4 = desenhar_mensagem_chat(draw, 10, 80 + altura1 + altura2 + altura3 + 50, 240, "Principalmente e-commerces e SaaS. Podemos nos encontrar no evento?", False)
    
    # Área de digitação
    draw.rectangle([(0, ALTURA - 70), (LARGURA, ALTURA - 60)], fill=CINZA_CLARO)
    draw.rounded_rectangle([(10, ALTURA - 50), (LARGURA - 70, ALTURA - 10)], radius=20, fill=BRANCO, outline=CINZA_CLARO)
    fonte_placeholder = ImageFont.truetype("DejaVuSans.ttf", 14)
    draw.text((20, ALTURA - 40), "Digite sua mensagem...", fill=CINZA_CLARO, font=fonte_placeholder)
    
    # Botão de enviar
    draw.ellipse([(LARGURA - 60, ALTURA - 50), (LARGURA - 10, ALTURA - 10)], fill=LARANJA)
    # Ícone de enviar (seta)
    draw.polygon([(LARGURA - 45, ALTURA - 35), (LARGURA - 25, ALTURA - 30), (LARGURA - 35, ALTURA - 20)], fill=BRANCO)
    draw.line([(LARGURA - 45, ALTURA - 35), (LARGURA - 25, ALTURA - 30), (LARGURA - 35, ALTURA - 20)], fill=BRANCO, width=2)
    
    # Barra de navegação inferior
    draw.rectangle([(0, ALTURA - 60), (LARGURA, ALTURA)], fill=BRANCO, outline=CINZA_CLARO)
    icones = ["Perfil", "Descobrir", "Conexões", "Chat"]
    for i, icone in enumerate(icones):
        x = LARGURA * (i + 0.5) / len(icones)
        y = ALTURA - 40
        cor = LARANJA if i == 3 else CINZA_ESCURO
        fonte_icone = ImageFont.truetype("DejaVuSans.ttf", 12)
        text_width = fonte_icone.getlength(icone)
        draw.text((x - text_width/2, y), icone, fill=cor, font=fonte_icone)
    
    return img

def criar_tela_lista_chat():
    img = Image.new('RGB', (LARGURA, ALTURA), BRANCO)
    draw = ImageDraw.Draw(img)
    
    # Barra superior
    desenhar_barra_superior(draw, "Conversas")
    
    # Lista de conversas
    fonte_nome = ImageFont.truetype("DejaVuSans-Bold.ttf", 16)
    fonte_msg = ImageFont.truetype("DejaVuSans.ttf", 14)
    fonte_hora = ImageFont.truetype("DejaVuSans.ttf", 12)
    
    # Conversa 1
    draw.line([(0, 130), (LARGURA, 130)], fill=CINZA_CLARO, width=1)
    draw.ellipse([(20, 70), (80, 130)], fill=CINZA_CLARO)
    draw.text((90, 75), "Maria Oliveira", fill=AZUL_MARINHO, font=fonte_nome)
    draw.text((90, 100), "Podemos nos encontrar no evento?", fill=CINZA_ESCURO, font=fonte_msg)
    draw.text((LARGURA - 70, 75), "10:30", fill=CINZA_ESCURO, font=fonte_hora)
    
    # Conversa 2
    draw.line([(0, 200), (LARGURA, 200)], fill=CINZA_CLARO, width=1)
    draw.ellipse([(20, 140), (80, 200)], fill=CINZA_CLARO)
    draw.text((90, 145), "Carlos Mendes", fill=AZUL_MARINHO, font=fonte_nome)
    draw.text((90, 170), "Obrigado pela conexão!", fill=CINZA_ESCURO, font=fonte_msg)
    draw.text((LARGURA - 70, 145), "Ontem", fill=CINZA_ESCURO, font=fonte_hora)
    
    # Barra de navegação inferior
    draw.rectangle([(0, ALTURA - 60), (LARGURA, ALTURA)], fill=BRANCO, outline=CINZA_CLARO)
    icones = ["Perfil", "Descobrir", "Conexões", "Chat"]
    for i, icone in enumerate(icones):
        x = LARGURA * (i + 0.5) / len(icones)
        y = ALTURA - 40
        cor = LARANJA if i == 3 else CINZA_ESCURO
        fonte_icone = ImageFont.truetype("DejaVuSans.ttf", 12)
        text_width = fonte_icone.getlength(icone)
        draw.text((x - text_width/2, y), icone, fill=cor, font=fonte_icone)
    
    return img

def main():
    diretorio_mockups = "/home/ubuntu/conecta-crm-app/mockups"
    criar_diretorio(diretorio_mockups)
    
    # Criar e salvar as telas
    telas = {
        "login": criar_tela_login(),
        "cadastro": criar_tela_cadastro(),
        "perfil": criar_tela_perfil(),
        "descoberta": criar_tela_descoberta(),
        "conexoes": criar_tela_conexoes(),
        "chat": criar_tela_chat(),
        "lista_chat": criar_tela_lista_chat()
    }
    
    for nome, img in telas.items():
        img.save(f"{diretorio_mockups}/{nome}.png")
    
    print(f"Mockups criados com sucesso em {diretorio_mockups}")

if __name__ == "__main__":
    main()
