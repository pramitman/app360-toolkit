"""
CNPJ (Cadastro Nacional de Pessoa Jurídica) processor.

Brazilian corporate taxpayer registry document validation and formatting.
"""

from ...factories.document_factory import DocumentFactory

class CNPJ(DocumentFactory):
    
    def _format(self) -> str:
        doc_number=self._doc_number
        formatted = f'{doc_number[:2]}.{doc_number[2:5]}.{doc_number[5:8]}/{doc_number[8:12]}-{doc_number[12:]}'
        return formatted
    
    def _clean(self, doc_number:str) -> str:
        return ''.join(char for char in doc_number if char.isdigit())
    
    def _is_valid(self, doc_number:str) -> bool:
        # document lenght == 14
        if len(doc_number) != 14:
            self._error(f'CNPJ deve ter 14 digitos. Encontrados: {len(doc_number)}')
        
        # repeated numbers
        if doc_number == doc_number[0]*14:
            self._error('CNPJ inválido: todos os dígitos são iguais')

        # check digit
        list_calc=[5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        first_digit = self._calculate_digit(doc_number,list_calc,12)
        if first_digit != int(doc_number[12]):
            self._error('CNPJ inválido: dígito verificador incorreto')

        list_calc=[6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        second_digit = self._calculate_digit(doc_number, list_calc, 13)
        if second_digit != int(doc_number[13]):
            self._error('CNPJ inválido: dígito verificador incorreto')
        
        return True
    
    def _calculate_digit(self, doc_number:str, weight_list, range_calc) -> int:
        sum_calc=sum(int(doc_number[i])* weight_list[i] for i in range(range_calc))
        rest_calc=sum_calc % 11
        digit=0 if rest_calc<2 else 11-rest_calc
        return digit