import random

MINA = -1

class CampoMinado:
    def __init__(self, tamanho):
        self.LINHAS, self.COLUNAS = tamanho
        self.nr_minas = random.randint(1, int(self.LINHAS * self.COLUNAS * .5))
        
        self.inicializar_tabuleiro()
        self.preencher_minas_adjacentes()
    
    def inicializar_tabuleiro(self):
        self.tabuleiro = [[0]*self.COLUNAS for _ in range(self.LINHAS)]
        
        # Colocação de Minas
        minas_adicionadas = 0
        while minas_adicionadas < self.nr_minas:
            linha = random.randint(0, self.LINHAS-1)
            coluna = random.randint(0, self.COLUNAS-1)
            
            if self.tabuleiro[linha][coluna] != MINA:
                self.tabuleiro[linha][coluna] = MINA
                minas_adicionadas += 1
            
        print(f"Tabuleiro ({self.LINHAS}x{self.COLUNAS}) com {self.nr_minas} minas inicializado.")
    
    def preencher_minas_adjacentes(self):
        vizinhos = (
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        )
        for i in range(self.LINHAS):
            for j in range(self.COLUNAS):
                # Ingora Campos Minados
                if self.tabuleiro[i][j] == MINA:
                    continue
                # Conta Minas Adjacentes
                for di, dj in vizinhos:
                    vi, vj = i + di, j + dj
                    
                    # Ignora Cantos do Tabuleiro
                    if vi < 0 or vj < 0 or vi >= self.LINHAS or vj >= self.COLUNAS:
                        continue
                    
                    # Contar
                    if self.tabuleiro[vi][vj] == MINA:
                        self.tabuleiro[i][j] += 1
        
    def revelar(self, i, j):
        if self.tabuleiro[i][j] == MINA:
            return None
        
        return self.tabuleiro[i][j]


        