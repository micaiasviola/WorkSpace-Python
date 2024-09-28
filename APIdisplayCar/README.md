# DisplayCar

### Descrição
DisplayCar é uma interface gráfica desenvolvida em Python, que permite aos usuários consultar modelos de carros com base em uma seleção manual de marcas. Os nomes das marcas e modelos são inseridos manualmente, oferecendo uma maneira simples de exibir as opções disponíveis.

---

# APIDisplayCar

### Descrição
APIDisplayCar expande a funcionalidade do DisplayCar ao integrar a [CarQueryAPI](https://www.carqueryapi.com/). Em vez de inserir manualmente os modelos, a aplicação faz uma requisição à API para obter os modelos de carros com base nas marcas especificadas no código. O usuário seleciona a marca desejada, e a API retorna os modelos correspondentes automaticamente.

---

# Criando o Executável

### Passos para construir o executável:
1. **Instalar o PyInstaller**  
   Para criar um executável a partir do código Python, primeiro você deve instalar o PyInstaller:
   ```bash
   pip install pyinstaller
2. **Executar Build**
    ```bash
    pyinstaller --onefile --windowed --icon=nome_do_icone.ico --add-data "nome_do_icone.ico;." nome_do_arquivo.py
    
    -- windowed: Remove o terminal (útil para aplicações com interface gráfica).
    -- icon: Define o ícone do executável.
    -- add-data: Inclui o ícone ou outros arquivos necessários para o funcionamento da aplicação.