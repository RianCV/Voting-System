# 🗳️ Election System Using Python

Final project for the Data-Oriented Programming course at PUCRS, involving the development of a voting system in Python.
Received the highest grade in the class.

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
