# SISTEMA DE ELEIÇÃO VIA ARQUIVOS TXT

## MANUAL DE USO DO PROGRAMA ELEIÇÃO

1. Estar dentro da pasta **Atividade_Eleicao**
2. Colocar, na pasta **entrada**, os seguintes arquivos:
    * *"entrada/eleicaoRS.txt"* ou qualquer nome, contendo partidos, pessoas e candidatos a serem adicionados ( cada um com seu respectivo cabeçalho)
    * Arquivos de urnas com as votaçoes. Ex: *"entrada/urna1.txt"*, *"entrada/urna2.txt"* .. *"entrada/urnaN.txt"*
3. No terminal, executar python app.py com o arquivo da eleicao e depois o das urnas. Ex:
  'python app.py *"entrada/eleicaoRS.txt"* *"entrada/urna1.txt"* *"entrada/urna2.txt"* 
4. Ver os arquivos txt de saída (boletim, contabilizçao e erros) na pasta **saida**

# 🗳️ Election System Using TXT Files

## 📘 User Guide – Election Program

### 📥 Input Files
Place the following files inside the `entrada` (input) folder
(There are already existing files in the folders for testing):

- **Election configuration file** (e.g., `entrada/eleicaoRS.txt`)  
  This file must include:
  - Political parties  
  - People  
  - Candidates  
  > ⚠️ Each section must be preceded by its appropriate header.

- **Voting files** (e.g., `entrada/urna1.txt`, `entrada/urna2.txt`, ..., `entrada/urnaN.txt`)  
  Each file represents the votes from a voting machine.

### ▶️ Running the Program
Use the terminal to run the program with the following command:

```bash
python app.py entrada/eleicaoRS.txt entrada/urna1.txt entrada/urna2.txt entrada/urna3.txt entrada/urna4.txt entrada/urna5.txt entrada/urna6.txt entrada/urna7.txt
```
### 📤 Output Files 
After execution, the following TXT files will be generated inside the `saida` (output) folder:
 - *boletimUrna.txt*
 - *contabilizacao.txt*
 - *erros_log.txt*
