# Implementações simples para automações simples!

O projeto tem como objetivo facilitar a criação de automações simples em python, principalmente para os iniciantes na linguagem, encapsulando várias funcionalidades de bibliotecas mais complexas (como selenium e MIME) em funções simples de serem utilizadas

## Instalação

Certifique-se de instalar todas as bibliotecas necessárias (requirements.txt)

## Modo de usar

### Link

Classe base para iniciarmos uma automação no navegador, recebe como parâmetro:
**url**: string da url desejada
**driver**: string 'Chrome' ou 'Firefox' para indicar o driver a ser utilizado
**sleep**: integer para definir o tempo de espera entre cada ação

#### Importando a biblioteca:

```python
from app.link import Link
```

#### Criando uma instância:

```python
link_instance = Link(
        url='google.com',
        driver='Chrome',
        sleep=1
    )
```

#### Abrindo o link:

```python
link_instance.openLink()
```

#### Interagindo com elementos da página:

```python
// Clica em um elemento pelo seu xpath
link_instance.click_element(element_xpath)

// Preenche um campo de texto com o texto especificado
link_instance.send_keys(element_xpath)

// Limpa um campo de texto
link_instance.clear_field(element_xpath)

// Maximiza a tela do navegador
link_instance.maximize()

// Muda o foco do navegador para o alerta e aceita o mesmo
link_instance.accept_alert()

// Move o cursor para o elemento baseado em seu xpath
link_instance.move_to(element_xpath)

// Clica com o botão direito no elemento baseado em seu xpath
link_instance.right_click(element_xpath)

// Aguarda o elemento se tornar clicável (por 60 segundos)
link_instance.wait_element_clickable(element_xpath)

// Clica com o botão esquerdo no elemento baseado em seu xpath
link_instance.click_element(element_xpath)

// Digita o texto indicado no elemento baseado em seu xpath
link_instance.send_keys(element_xpath, text)

// Limpa o campo de texto
link_instance.clear_field(element_xpath)

// Pressiona a tecla indicada no teclado
link_instance.press_key('enter')

// Alternativa para limpar o campo de texto com o teclado
link_instance.clear_text(element_xpath)

// Digita o texto indicado no elemento baseado em seu name
link_instance.send_keys_by_name(element_name, text)

// Troca para a janela aberta baseada no seu index
link_instance.switch_window(index)

// Troca o foco do navegador para um iframe
link_instance.switch_to_frame(xpath)

// Verifica se o elemento (xpath) existe, retorna True ou False
link_instance.element_exists(xpath)

// Tira um print da tela do navegador e salva no caminho passado
link_instance.take_screenshot(path)
```

---

### Email

Classe base para enviar email usando autenticação SMTP, recebe como parâmetro:
**smtp_server**: string do servidor smtp
**smtp_port**: integer da porta do servidor smtp
**smtp_username**: string do username para autenticação
**smtp_password**: string com a senha para autenticação
**subject**: string com o assunto do email
**email_body**: string com o conteúdo do corpo do email (em HTML ou string)
**html_body**: boolean, False como padrão, deverá ser mudado para True caso passe um body em html no parâmetro 'email_body'
**receivers**: list de string com todos os endereços que irão receber o email
**attachments**: list de string com todos os caminhos para arquivos que serão enviados como anexo
**cco**: list de string contendo todos os endereços que irão receber o email como cópia oculta

#### Importando a biblioteca:

```python
from app.email import Email
```

#### Criando uma instância:
```python
email = Email(
    smtp_server='smtp.office365.com',
    smtp_port=587,
    smtp_username='teste@teste.com.br',
    smtp_password='password',
    subject='Teste',
    email_body='Email de teste',
    receivers=['receiver1@teste.com.br', 'receiver2@teste.com.br']
)
```

#### Enviando o email:
```python
email.send()
```

***Author***: https://github.com/fanecovsf  
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

