from PyQt5 import  uic,QtWidgets


#função desparada pelo botão no formulario
def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    
    if formulario.radioButton.isChecked() :
        print("Categoria Informatica selecionada")
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Alimentos selecionada")
    else :
        print("Categoria Eletronicos selecionada")

    print("Código:",linha1)
    print("Descricao:",linha2)
    print("Preco",linha3)
    

#objeto que cria a aplicação e carrega o arquivo
app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui") #carrega o arquivo do qtdesign
formulario.pushButton.clicked.connect(funcao_principal) #botão para executar a função

formulario.show()
app.exec()


