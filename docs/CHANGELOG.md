# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

---

## v[0.1.0] - 2025-09-25

### Adicionado

> Implementação inicial do módulo Document
> Implementação da classe `CPF` e `CNPJ` com validação e formatação
> Validação de dígitos verificadores para CPF e CNPJ
> Formatação automática de documentos
> Sistema de limpeza de caracteres especiais

### Funcionalidades

- ✅ Validação de CPF e CNPJ
- ✅ Formatação de CPF (XXX.XXX.XXX-XX)
- ✅ Formatação de CNPJ (XXX.XXX.XXX/XXXX-XX)
- ✅ Limpeza automática de caracteres não numéricos
- ✅ Verificação de dígitos verificadores
- ✅ Detecção de CPFs e CNPJs com dígitos repetidos

---

---

## Convenções de Versionamento

- **MAJOR**: Mudanças incompatíveis na API
- **MINOR**: Funcionalidades adicionadas de forma compatível
- **PATCH**: Correções de bugs compatíveis

## Tipos de Mudanças

- **Adicionado** para novas funcionalidades
- **Alterado** para mudanças em funcionalidades existentes
- **Descontinuado** para funcionalidades que serão removidas
- **Removido** para funcionalidades removidas
- **Corrigido** para correções de bugs
- **Segurança** para vulnerabilidades corrigidas
