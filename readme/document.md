# Document Module --> CPF

## 📋 Módulo de Processamento de Documentos

> Este módulo fornece uma arquitetura robusta e extensível para validação, formatação e manipulação de documentos brasileiros.

---

## 🏗️ Funcionalidades

> CPF</br>
> CNPJ

_**obs.:** Os métodos e Propriedades abaixo são úteis para todas as funcionalidades listadas acima._

## Inicialização

```python
    from app360_toolkit.document import CPF
    cpf = CPF() # CPF vazio
    # ou
    cpf = CPF('12345678901') # CPF com valor inicial
```

---

## 📋 Métodos Disponíveis

### set (method)

> Define o valor do CPF, validando automaticamente com base no tamanho, padrão e dígitos verificadores

**Parâmetros:**

doc_number (str): Número do CPF a ser definido

**Comportamento:**

- Remove automaticamente caracteres especiais
- Valida o formato e dígitos verificadores
- Armazena apenas se válido

```python
    cpf.set('12345678901') # Apenas números
    cpf.set('123.456.789-01') # Formatado
    cpf.set('123 456 789 01') # Com espaços
    # ⚠️ Nota: Lança ValueError se o CPF for inválido.
```

### validate (method)

> Valida o valor do CPF de forma simplificada e direta, retornando True ou False

**Parâmetros:**

doc_number (str): Número do CPF a ser validado

**Retorno:**

bool: True se válido, False se inválido

```python
    is_valid = cpf.validate('12345678901') # True/False
    is_valid = cpf.validate('123.456.789-01') # True/False
    is_valid = cpf.validate('11111111111') # False (dígitos iguais)
```

**Validações realizadas:**

✅ Verificação de comprimento (11 dígitos)
✅ Detecção de dígitos repetidos
✅ Cálculo de dígitos verificadores
✅ Limpeza automática de caracteres especiais

---

## 🔧 Propriedades

### get (property)

> Resgata o valor limpo (apenas números) do CPF armazenado

**Retorno:**

str: CPF sem formatação (apenas dígitos)

```python
    cpf = CPF('123.456.789-01')
    number = cpf.get # '12345678901'
```

### formatted (property)

> Formata o valor do CPF dentro da convenção brasileira (XXX.XXX.XXX-XX)

**Retorno:**

str: CPF formatado ou string vazia se não houver valor

```python
    cpf = CPF('12345678901')
    formatted_number = cpf.formatted # '123.456.789-01'
```

### is_empty (property)

> Verifica se existe valor armazenado na instância

**Retorno:**

bool: True se vazio, False se contém valor

```python
    cpf = CPF()
    is_empty = cpf.is_empty # True

    cpf.set('12345678901')
    is_empty = cpf.is_empty # False
```

### document (property)

> Retorna o tipo do documento da classe atual

**Retorno:**

str: Nome da classe do documento

```python
    cpf = CPF()
    document_type = cpf.document # 'CPF'
```

---

## 🎯 Exemplos Práticos

### Validação Básica

```python
    from app360_toolkit.document import CPF

    # Criar e validar
    cpf = CPF()
    cpf.set('123.456.789-01')
    cpf.fotmatted
    #ou
    cpf = CPF('123.456.789-01')
    cpf.fotmatted
    # ou Valida somente
    cpf = CPF()
    is_valid = cpf.validate('123.456.789-01')
```

### A classe aceita diferentes tipos de entrada

cpf = CPF(12345678901) # int
cpf = CPF('12345678901') # str
cpf = CPF('123.456.789-01') # str formatado

docs.python.org</br>
⚠️ Importante: Esta implementação valida apenas o formato e algoritmo do CPF. Para verificar se um CPF está ativo na Receita Federal, consulte os serviços oficiais.
