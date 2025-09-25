"""
Testes para a classe CNPJ do app360-toolkit.
"""

import sys
import os
from pathlib import Path

# Adicionar o diretório src ao Python path
project_root = Path(__file__).parent.parent.parent
src_path = project_root / 'src'
sys.path.insert(0, str(src_path))

from app360_toolkit.document import CNPJ

class TestDocumentCNPJ:
    """Classe de testes para CNPJ."""
    
    def __init__(self):
        """Inicializar testes."""
        self.test_data = [
            '17.317.186/0001-00',
            '17 317 186 0001 00', 
            '17317186000100',
            '17-317-186x0001y00',
            17317186000100,
            'a1d7f3r1t7g1h8y6u0kj0k0i1k0l0l',
            None,
            '',
            '11111111111111',
            ' ',
        ]
    
    def test_cleaner_cnpj(self):
        """Testa limpeza e validação de CNPJ."""
        print('--- Test for cleaner CNPJ ---')
        
        for element in self.test_data:
            try:
                # CORRETO: Instanciar a classe CNPJ para cada teste
                test_cnpj = CNPJ()  # ← Criar instância
                test_cnpj.set(element)  # ← Definir valor
                
                # CORRETO: Usar métodos que existem
                print(f'✅ Original: {element} -> Limpo: {test_cnpj.get} -> Formatado: {test_cnpj.formatted}')
                
            except ValueError as e:
                print(f'❌ Erro com {element}: {e}')
            except Exception as e:
                print(f'❌ Erro inesperado com {element}: {e}')
        
        print()
    
    def test_cnpj_constructor(self):
        """Testa construtor da classe CNPJ."""
        print('--- Test CNPJ Constructor ---')
        
        for element in self.test_data:
            try:
                # Testar construtor direto
                test_cnpj = CNPJ(element)  # ← Passar valor no construtor
                print(f'✅ Constructor: {element} -> {test_cnpj}')
                
            except ValueError as e:
                print(f'❌ Constructor erro com {element}: {e}')
            except Exception as e:
                print(f'❌ Constructor erro inesperado com {element}: {e}')
        
        print()
    
    def test_cnpj_methods(self):
        """Testa métodos específicos da classe CNPJ."""
        print('--- Test CNPJ Methods ---')
        
        # Testar com CNPJ válido
        try:
            valid_cnpj = "17317186000100"  # CNPJ válido para teste
            cnpj = CNPJ(valid_cnpj)
            
            print(f"CNPJ de teste: {valid_cnpj}")
            print(f"✅ Formatado: {cnpj.formatted}")
            print(f"✅ Vazio?: {cnpj.is_empty}")
            print(f"✅ Type: {cnpj.document}")
            print(f"✅ String: {str(cnpj)}")
            print(f"✅ Repr: {repr(cnpj)}")
            
        except Exception as e:
            print(f"❌ Erro nos métodos: {e}")
        
        print()
    
    def test_cnpj_validation(self):
        """Testa validação específica de CNPJs."""
        print('--- Test CNPJ Validation ---')
        
        # CNPJs para teste de validação
        validation_tests = [
            ('17317186000100', True),   # CNPJ válido
            ('17.317.186/0001-00', True), # CNPJ válido formatado
            ('11111111111111', False),  # CNPJ inválido (todos iguais)
            ('17317186000101', False), # CNPJ inválido
            (' ', False),  # CNPJ inválido
            (None, False),  # CNPJ inválido
            ('', False),  # CNPJ inválido
        ]
        
        for cnpj_value, expected in validation_tests:
            try:
                cnpj = CNPJ()
                is_valid = cnpj.validate(cnpj_value)
                status = "✅" if is_valid == expected else "❌"
                print(f"{status} {cnpj_value}: válido={is_valid} (esperado={expected})")
                
            except ValueError as e:
                # Se esperávamos inválido e deu erro, está correto
                if not expected:
                    print(f"✅ {cnpj_value}: erro esperado - {e}")
                else:
                    print(f"❌ {cnpj_value}: erro inesperado - {e}")
            except Exception as e:
                print(f"❌ {cnpj_value}: erro inesperado - {e}")
        
        print()
    
    def run_all_tests(self):
        """Executa todos os testes."""
        print("="*50)
        print("EXECUTANDO TODOS OS TESTES DE CNPJ")
        print("="*50)
        
        self.test_cleaner_cnpj()
        self.test_cnpj_constructor()
        self.test_cnpj_methods()
        self.test_cnpj_validation()
        
        print("="*50)
        print("TESTES CONCLUÍDOS")
        print("="*50)


def test_imports():
    """Testa diferentes formas de import."""
    print("--- Test Imports ---")
    
    try:
        from app360_toolkit.processors.document import CNPJ as CNPJ1
        print("✅ Import explícito: from app360_toolkit.processors.document import CNPJ")
    except ImportError as e:
        print(f"❌ Erro import explícito: {e}")
    
    try:
        from app360_toolkit.document import CNPJ as CNPJ2
        print("✅ Import virtual: from app360_toolkit.document import CNPJ")
    except ImportError as e:
        print(f"❌ Erro import virtual: {e}")
    
    try:
        from app360_toolkit import CNPJ as CNPJ3
        print("✅ Import direto: from app360_toolkit import CNPJ")
    except ImportError as e:
        print(f"❌ Erro import direto: {e}")
    
    print()


if __name__ == '__main__':
    # Testar imports primeiro
    test_imports()
    
    # Executar testes da classe
    test_runner = TestDocumentCNPJ()
    test_runner.run_all_tests()