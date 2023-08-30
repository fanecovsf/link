# Biblioteca "Link" baseada em Selenium

A biblioteca **Link** é uma classe Python que encapsula funcionalidades relacionadas ao controle automatizado de navegadores web, utilizando a biblioteca Selenium. Ela fornece métodos para abrir links, interagir com elementos da página, aguardar condições específicas e realizar ações diversas em um navegador web.

## Instalação

Certifique-se de ter a biblioteca Selenium instalada. Se não estiver instalada, você pode instalá-la usando o seguinte comando:

```
pip install selenium
```

## Uso Básico

1. Importando a biblioteca:

```python
from link import Link
```

2. Criando uma instância:

```python
// Crie uma instância da classe "Link" passando o link desejado e o tipo de driver (Chrome ou Firefox).
// O modo headless (opcional) define se o navegador será executado em modo headless (sem interface gráfica).
linkInstance = Link(link="https://www.example.com", driver="Chrome", headless=true);
```

3. Abrindo o link:

```python
// Abre o link no navegador configurado.
linkInstance.openLink()
```

4. Interagindo com elementos da página:

```python
// Espera até que um elemento seja clicável e então clica nele.
linkInstance.clickElement(elementXpath="//button[@id='submit-button']")

// Preenche um campo de texto com o texto especificado.
linkInstance.sendKeys(elementXpath="//input[@name='username']", text="my_username")

// Limpa um campo de texto.
linkInstance.clearField(elementXpath="//input[@name='password']")

// Obtém o valor de um elemento (por exemplo, um campo de texto).
value = linkInstance.getValue(elementXpath="//input[@name='email']")
```

5. Realizando ações do teclado:

```python
// Pressiona a tecla Enter.
linkInstance.pressEnter()

// Pressiona a tecla Tab.
linkInstance.pressTab()

// Pressiona a tecla Down.
linkInstance.pressDown()

// Pressiona a tecla Up.
linkInstance.pressUp()
```

6. Trabalhando com janelas e frames:

```python
// Alterna para uma janela específica pelo índice.
linkInstance.switchWindow(index=1)

// Alterna para um frame especificado pelo seletor CSS.
linkInstance.switchSelector(cssSelector=".frame-class")

// Alterna para um frame especificado pelo XPath.
linkInstance.switchFrameXpath(xpath="//iframe[@id='frame-id']")
```

7. Outras ações:

```python
// Maximiza a janela do navegador.
linkInstance.maximize();

// Espera até que um elemento seja visível e clicável e então clica nele.
linkInstance.clickElement(elementXpath="//a[@class='link']")

// Fecha a instância do navegador.
linkInstance.quitSite()

// Verifica se o elemento existe (True ou False).
linkInstance.elementExist(xpath)
```

## Considerações Finais

A biblioteca **Link** simplifica a automação de tarefas em navegadores web, permitindo a interação com elementos de páginas, espera por condições específicas e execução de ações de teclado. Ela é uma ferramenta útil para testes automatizados, raspagem de dados e outras atividades que envolvam a interação com páginas da web por meio de um navegador automatizado.

