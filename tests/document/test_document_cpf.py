"""
Testes para a classe CPF do app360-toolkit.
"""

import sys
import os
from pathlib import Path

# Adicionar o diretório src ao Python path
project_root = Path(__file__).parent.parent.parent
src_path = project_root / 'src'
sys.path.insert(0, str(src_path))

from app360_toolkit.document import CPF

class TestDocumentCPF:
    """Classe de testes para CPF."""
    
    def __init__(self):
        """Inicializar testes."""
        self.test_data = [
            '111.444.777-35',
            '111 444 777 35', 
            '11144477735',
            '111-444-777.35',
            11144477735,
            'af1g1r1hg4as44jk7y7r7e3w5ww',
            None,
            '',
            '11111111111',
            ' ',
        ]
    
    def test_cleaner_cpf(self):
        """Testa limpeza e validação de CPF."""
        print('--- Test for cleaner CPF ---')
        
        for element in self.test_data:
            try:
                # CORRETO: Instanciar a classe CPF para cada teste
                test_cpf = CPF()  # ← Criar instância
                test_cpf.set(element)  # ← Definir valor
                
                # CORRETO: Usar métodos que existem
                print(f'✅ Original: {element} -> Limpo: {test_cpf.get} -> Formatado: {test_cpf.formatted}')
                
            except ValueError as e:
                print(f'❌ Erro com {element}: {e}')
            except Exception as e:
                print(f'❌ Erro inesperado com {element}: {e}')
        
        print()
    
    def test_cpf_constructor(self):
        """Testa construtor da classe CPF."""
        print('--- Test CPF Constructor ---')
        
        for element in self.test_data:
            try:
                # Testar construtor direto
                test_cpf = CPF(element)  # ← Passar valor no construtor
                print(f'✅ Constructor: {element} -> {test_cpf}')
                
            except ValueError as e:
                print(f'❌ Constructor erro com {element}: {e}')
            except Exception as e:
                print(f'❌ Constructor erro inesperado com {element}: {e}')
        
        print()
    
    def test_cpf_methods(self):
        """Testa métodos específicos da classe CPF."""
        print('--- Test CPF Methods ---')
        
        # Testar com CPF válido
        try:
            valid_cpf = "11144477735"  # CPF válido para teste
            cpf = CPF(valid_cpf)
            
            print(f"CPF de teste: {valid_cpf}")
            print(f"✅ Formatado: {cpf.formatted}")
            print(f"✅ Vazio?: {cpf.is_empty}")
            print(f"✅ Type: {cpf.document}")
            print(f"✅ String: {str(cpf)}")
            print(f"✅ Repr: {repr(cpf)}")
            
        except Exception as e:
            print(f"❌ Erro nos métodos: {e}")
        
        print()
    
    def test_cpf_validation(self):
        """Testa validação específica de CPFs."""
        print('--- Test CPF Validation ---')
        
        # CPFs para teste de validação
        validation_tests = [
            ('11144477735', True),   # CPF válido
            ('111.444.777-35', True), # CPF válido formatado
            ('11111111111', False),  # CPF inválido (todos iguais)
            ('123.456.789-00', False), # CPF inválido
            ('12345678901', False),  # CPF inválido
            (' ', False),  # CPF inválido
            (None, False),  # CPF inválido
            ('', False),  # CPF inválido
        ]
        
        for cpf_value, expected in validation_tests:
            try:
                cpf = CPF()
                is_valid = cpf.validate(cpf_value)
                status = "✅" if is_valid == expected else "❌"
                print(f"{status} {cpf_value}: válido={is_valid} (esperado={expected})")
                
            except ValueError as e:
                # Se esperávamos inválido e deu erro, está correto
                if not expected:
                    print(f"✅ {cpf_value}: erro esperado - {e}")
                else:
                    print(f"❌ {cpf_value}: erro inesperado - {e}")
            except Exception as e:
                print(f"❌ {cpf_value}: erro inesperado - {e}")
        
        print()
    
    def run_all_tests(self):
        """Executa todos os testes."""
        print("="*50)
        print("EXECUTANDO TODOS OS TESTES DE CPF")
        print("="*50)
        
        self.test_cleaner_cpf()
        self.test_cpf_constructor()
        self.test_cpf_methods()
        self.test_cpf_validation()
        
        print("="*50)
        print("TESTES CONCLUÍDOS")
        print("="*50)


def test_imports():
    """Testa diferentes formas de import."""
    print("--- Test Imports ---")
    
    try:
        from app360_toolkit.processors.document import CPF as CPF1
        print("✅ Import explícito: from app360_toolkit.processors.document import CPF")
    except ImportError as e:
        print(f"❌ Erro import explícito: {e}")
    
    try:
        from app360_toolkit.document import CPF as CPF2
        print("✅ Import virtual: from app360_toolkit.document import CPF")
    except ImportError as e:
        print(f"❌ Erro import virtual: {e}")
    
    try:
        from app360_toolkit import CPF as CPF3
        print("✅ Import direto: from app360_toolkit import CPF")
    except ImportError as e:
        print(f"❌ Erro import direto: {e}")
    
    print()


if __name__ == '__main__':
    # Testar imports primeiro
    test_imports()
    
    # Executar testes da classe
    test_runner = TestDocumentCPF()
    test_runner.run_all_tests()