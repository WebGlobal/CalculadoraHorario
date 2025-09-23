# CalculadoraHorario
Calculadora para Horário Saída

Status: UNDEFINED

# Calculadora Horário

Calculádora simples para cálculo do horário de saída, para até 3 intervalos de tempo.

## Uso Local

### Execução 

Para executar a chamada via Linux

```
$ python3 main.py -hi1 09:00 -hf1 12:00 -hi2 13:00 -hf2 14:00 -hi3 15:00 -hf3 19:30
```
onde:

- '-hora_ini1' | '-hi1' Indica o primeiro horário de entrada;
- '-hora_fim1' | '-hf1' Indica o primeiro horário de saída;
- '-hora_ini2' | '-hi2' Indica o segundo horário de entrada;   
- '-hora_fim2' | '-hf2' Indica o segundo horário de saída;
- '-hora_ini3' | '-hi3' Indica o terceiro horário de entrada;    
- '-hora_fim3' | '-hf3' Indica o terceiro horário de saída;

Observações: 
- Apenas o parâmetro '-hora_ini1' | '-hi1' é obrigatório, os outros são opcionais. 
- Se não for fornecido nenhum outro parâmetro de intervalo, será considerado 1h de almoço.
