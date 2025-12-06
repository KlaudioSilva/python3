#conversão de tipos, coersão
#type convertion, typecasting, coertion
#é o ato de converter um tipo em outro
#tipos imutáveis e primitivos:
#str, int, float, bool
#print('1' + 1)      #vai receber a mensagem: 'TypeError: can only concatenate str (not "int") to str'
print('a' + 'b')
print('------------------------------------------')

print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))        #uma string vazia é false, mas uma string com um espaço é true
print(str(11) + 'b')    #converte o '11' para string e assim concatena com a letra 'b'