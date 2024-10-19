import PySimpleGUI as sg
from jogo import CampoMinado, MINA
sg.theme('Light Gray 3')

class Tela:
    def __init__(self):
        self.LINHAS, self.COLUNAS = self.perguntar_tamaho()  
        self.tabuleiro = CampoMinado((self.LINHAS, self.COLUNAS))   
        self.jogando = True
        self.botoes = self.gerar_botoes()

        self.layout = [
            [sg.Text("Clique em um campo para revelar!")],
            *self.botoes,
            [sg.Stretch(), sg.Button("Reiniciar", key="Reiniciar"), sg.Stretch()]
        ]
        self.window = sg.Window('Campo Minado', self.layout, finalize=True)
        
        self.reiniciar()

    def perguntar_tamaho(self):
        entrada = sg.popup_get_text("Escreva o tamanho do tabuleiro (ex. 10x10)", "Campo Minado")
        entrada = entrada.lower().strip().split('x')
        return int(entrada[0]), int(entrada[1])
    
    def reiniciar(self):
        # Novo Tabuleiro
        self.tabuleiro = CampoMinado((self.LINHAS, self.COLUNAS))   
        self.jogando = True
        # Limpar Botões
        for i in range(self.LINHAS):
            for j in range(self.COLUNAS):
                if self.window[f"{i},{j}"]:
                    self.window[f"{i},{j}"].update("")
                    normal_color = self.window["Reiniciar"].ButtonColor
                    self.window[f"{i},{j}"].update(button_color = normal_color)
        
        
    
    def gerar_botoes(self):
        botoes = []
        
        for i in range(self.tabuleiro.LINHAS):
            linha = []
            for j in range(self.tabuleiro.COLUNAS):
                btn = sg.Button(size=(4, 2), key=f"{i},{j}", pad=(0,0))
                linha.append(btn)
            botoes.append(linha)
                
        return botoes
    def revelar_tudo(self):
        for i in range(self.LINHAS):
            for j in range(self.COLUNAS):
                if self.window[f"{i},{j}"]:
                    if self.tabuleiro.tabuleiro[i][j] == MINA:
                        self.window[f"{i},{j}"].update("*")
                        self.window[f"{i},{j}"].update(button_color = ('white','red'))
                    else:
                        self.window[f"{i},{j}"].update(self.tabuleiro.tabuleiro[i][j])
        
        
        
    def mostrar(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break
            
            if event == "Reiniciar":
                self.reiniciar()
                     
            if not self.jogando:
                continue
            
            posicao = event.split(',')
            if len(posicao) == 2:
                i = int(posicao[0])
                j = int(posicao[1])
                
                resultado = self.tabuleiro.revelar(i, j)
                if resultado is not None:
                    # Revelar
                    self.window[event].update(resultado)
                    self.window[event].update(button_color = ('white','green'))
                else:
                    # Terminar o Jogo
                    self.revelar_tudo()
                    self.jogando = False
                    sg.popup_timed("O Jogo Terminou!", text_color='red',auto_close_duration=3)
                
    
        self.window.close()
        
if __name__ == '__main__':
    tela = Tela()
    tela.mostrar()